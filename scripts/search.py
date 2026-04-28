#!/usr/bin/env python3
"""
search.py - ClassIn API 文档检索脚本（支持本地 / LLM 双模式）

用法：
    python scripts/search.py "你的问题" [--top 5]
    python scripts/search.py "你的问题" --mode llm --top 4
    python scripts/search.py "你的问题" --format json

检索模式由 config.yaml 决定，默认使用 local（本地向量检索）。
可在命令行用 --mode 参数覆盖配置文件设置。

模式说明：
    local  : ChromaDB 本地向量检索，余弦相似度，无需 API Key
    llm    : 先向量检索召回候选片段，再用 LLM 重排序（更精准）
"""

import sys
import json
import argparse
import os
import pathlib

# ─── 路径配置 ───────────────────────────────────────────────────────────────
SKILL_ROOT      = pathlib.Path(__file__).parent.parent
DB_DIR          = SKILL_ROOT / ".rag_db"
CONFIG_FILE     = SKILL_ROOT / "config.yaml"
COLLECTION_NAME = "classin_api_docs"
EMBED_MODEL     = "BAAI/bge-small-zh-v1.5"
BGE_QUERY_PREFIX = "为这个句子生成表示以用于检索相关文章："

# ─── 配置加载 ────────────────────────────────────────────────────────────────

def load_config() -> dict:
    """加载 config.yaml，支持环境变量覆盖"""
    try:
        import yaml
    except ImportError:
        print("[ERROR] 缺少 PyYAML，运行：pip install pyyaml", file=sys.stderr)
        raise SystemExit(1)

    if not CONFIG_FILE.exists():
        return {"retrieval_mode": "local", "local": {"top_k": 6, "score_threshold": 0.30}, "llm": {}}

    cfg = yaml.safe_load(CONFIG_FILE.read_text(encoding="utf-8"))
    # 环境变量覆盖（方便部署时注入 API Key）
    if "llm" in cfg and "openai" in cfg["llm"]:
        key = os.environ.get("OPENAI_API_KEY", "")
        if key and not cfg["llm"]["openai"].get("api_key"):
            cfg["llm"]["openai"]["api_key"] = key
    if "llm" in cfg and "claude" in cfg["llm"]:
        key = os.environ.get("ANTHROPIC_API_KEY", "")
        if key and not cfg["llm"]["claude"].get("api_key"):
            cfg["llm"]["claude"]["api_key"] = key
    if "llm" in cfg and "dashscope" in cfg["llm"]:
        key = os.environ.get("DASHSCOPE_API_KEY", "")
        if key and not cfg["llm"]["dashscope"].get("api_key"):
            cfg["llm"]["dashscope"]["api_key"] = key
    return cfg


# ─── 向量检索（local / llm 共同部分）─────────────────────────────────────────

def vector_search(query: str, top_k: int = 10, threshold: float = 0.0):
    """
    基于 ChromaDB 的向量语义检索，返回所有高于阈值的片段。
    """
    try:
        import chromadb
        from chromadb.utils import embedding_functions
    except ImportError:
        print("[ERROR] 缺少依赖，运行：pip install -r scripts/requirements.txt", file=sys.stderr)
        raise SystemExit(1)

    if not DB_DIR.exists():
        print("[ERROR] 向量索引不存在，请先运行：python scripts/build_index.py", file=sys.stderr)
        raise SystemExit(1)

    client = chromadb.PersistentClient(path=str(DB_DIR))
    embed_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name=EMBED_MODEL, device="cpu"
    )

    try:
        collection = client.get_collection(name=COLLECTION_NAME, embedding_function=embed_fn)
    except Exception:
        print("[ERROR] 找不到索引 collection，请先运行：python scripts/build_index.py", file=sys.stderr)
        raise SystemExit(1)

    total = collection.count()
    if total == 0:
        print("[ERROR] 向量库为空，请先运行：python scripts/build_index.py", file=sys.stderr)
        raise SystemExit(1)

    results = collection.query(
        query_texts=[BGE_QUERY_PREFIX + query],
        n_results=min(top_k, total),
        include=["documents", "metadatas", "distances"],
    )

    hits = []
    for doc, meta, dist in zip(
        results["documents"][0],
        results["metadatas"][0],
        results["distances"][0],
    ):
        score = round(1.0 - dist, 4)
        if score >= threshold:
            hits.append({"text": doc, "source": meta.get("source", "unknown"),
                         "section": meta.get("section", ""), "score": score})

    hits.sort(key=lambda x: x["score"], reverse=True)
    return hits


# ─── LLM 重排序 ─────────────────────────────────────────────────────────────

def llm_rerank(query: str, candidates: list, cfg: dict) -> tuple:
    """
    使用 LLM 对候选片段进行重排序，返回 (精选片段列表, token统计字典)。
    """
    provider = cfg.get("provider", "openai")
    provider_cfg = cfg.get(provider, {})

    # 构建片段列表供 LLM 参考
    chunk_lines = []
    for i, hit in enumerate(candidates, 1):
        chunk_lines.append(f"【片段{i}】（来源：{hit['source']}，章节：{hit['section']}）\n{hit['text'][:500]}")
    chunks_text = "\n\n".join(chunk_lines)

    prompt = cfg.get("rerank", {}).get("prompt_template", "").format(
        query=query, chunks=chunks_text
    )

    empty_token = {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}

    try:
        if provider == "openai":
            result, token_info = _call_openai(prompt, provider_cfg)
        elif provider == "claude":
            result, token_info = _call_claude(prompt, provider_cfg)
        elif provider == "dashscope":
            result, token_info = _call_dashscope(prompt, provider_cfg)
        elif provider == "ollama":
            result, token_info = _call_ollama(prompt, provider_cfg)
        else:
            print(f"[ERROR] 不支持的 LLM provider: {provider}", file=sys.stderr)
            return candidates[: cfg.get("rerank", {}).get("final_top_k", 4)], empty_token
    except Exception as e:
        print(f"[WARN] LLM 调用失败，降级为向量检索结果：{e}", file=sys.stderr)
        return candidates[: cfg.get("rerank", {}).get("final_top_k", 4)], empty_token

    # 解析 LLM 返回的编号列表
    ranked = _parse_rerank_response(result, candidates)
    return ranked, token_info


def _call_openai(prompt: str, cfg: dict) -> tuple:
    import openai
    client = openai.OpenAI(
        api_key=cfg.get("api_key", ""),
        base_url=cfg.get("base_url") or None,
        timeout=cfg.get("timeout", 30),
    )
    resp = client.chat.completions.create(
        model=cfg.get("model", "gpt-4o-mini"),
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        max_tokens=200,
    )
    usage = resp.usage
    token_info = {
        "prompt_tokens": usage.prompt_tokens if hasattr(usage, 'prompt_tokens') else 0,
        "completion_tokens": usage.completion_tokens if hasattr(usage, 'completion_tokens') else 0,
        "total_tokens": usage.total_tokens if hasattr(usage, 'total_tokens') else 0,
    }
    return resp.choices[0].message.content.strip(), token_info


def _call_claude(prompt: str, cfg: dict) -> tuple:
    import anthropic
    client = anthropic.Anthropic(
        api_key=cfg.get("api_key", ""),
        base_url=cfg.get("base_url") or None,
        timeout=cfg.get("timeout", 30),
    )
    resp = client.messages.create(
        model=cfg.get("model", "claude-3-haiku-20240307"),
        max_tokens=200,
        messages=[{"role": "user", "content": prompt}],
    )
    usage = resp.usage
    token_info = {
        "prompt_tokens": usage.input_tokens if hasattr(usage, 'input_tokens') else 0,
        "completion_tokens": usage.output_tokens if hasattr(usage, 'output_tokens') else 0,
        "total_tokens": (usage.input_tokens + usage.output_tokens) if hasattr(usage, 'input_tokens') else 0,
    }
    return resp.content[0].text.strip(), token_info


def _call_dashscope(prompt: str, cfg: dict) -> tuple:
    import openai
    client = openai.OpenAI(
        api_key=cfg.get("api_key", ""),
        base_url=cfg.get("base_url", "https://dashscope.aliyuncs.com/api/v1"),
        timeout=cfg.get("timeout", 30),
    )
    resp = client.chat.completions.create(
        model=cfg.get("model", "qwen-plus"),
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        max_tokens=200,
    )
    usage = resp.usage
    token_info = {
        "prompt_tokens": usage.prompt_tokens if hasattr(usage, 'prompt_tokens') else 0,
        "completion_tokens": usage.completion_tokens if hasattr(usage, 'completion_tokens') else 0,
        "total_tokens": usage.total_tokens if hasattr(usage, 'total_tokens') else 0,
    }
    return resp.choices[0].message.content.strip(), token_info


def _call_ollama(prompt: str, cfg: dict) -> tuple:
    import openai
    client = openai.OpenAI(
        api_key=cfg.get("api_key", "ollama"),
        base_url=cfg.get("base_url", "http://localhost:11434/v1"),
        timeout=cfg.get("timeout", 120),
    )
    resp = client.chat.completions.create(
        model=cfg.get("model", "qwen2.5:7b"),
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        max_tokens=200,
    )
    usage = resp.usage
    token_info = {
        "prompt_tokens": usage.prompt_tokens if hasattr(usage, 'prompt_tokens') else 0,
        "completion_tokens": usage.completion_tokens if hasattr(usage, 'completion_tokens') else 0,
        "total_tokens": usage.total_tokens if hasattr(usage, 'total_tokens') else 0,
    }
    return resp.choices[0].message.content.strip(), token_info


def _parse_rerank_response(response: str, candidates: list) -> list:
    """解析 LLM 返回的编号字符串（如 '1, 3, 2'），返回对应片段列表"""
    import re
    numbers = re.findall(r'\d+', response)
    result = []
    for num_str in numbers:
        idx = int(num_str) - 1
        if 0 <= idx < len(candidates):
            result.append(candidates[idx])
    if not result:
        final_k = 4
        return candidates[:final_k]
    return result


# ─── 主检索入口 ─────────────────────────────────────────────────────────────

def search(query: str, mode: str = None, top_k: int = None,
           threshold: float = None) -> tuple:
    """
    统一检索入口，根据配置自动选择模式。
    返回 (hits, token_info) 元组：
      - hits: 相关片段列表
      - token_info: LLM 调用统计（local 模式为空字典）
    """
    cfg = load_config()
    mode = mode or cfg.get("retrieval_mode", "local")
    final_threshold = threshold if threshold is not None \
        else cfg.get("local", {}).get("score_threshold", 0.30)

    local_cfg   = cfg.get("local", {})
    llm_cfg     = cfg.get("llm", {})
    rerank_cfg  = llm_cfg.get("rerank", {})

    empty_token = {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}

    if mode == "local":
        k = top_k or local_cfg.get("top_k", 6)
        return vector_search(query, top_k=k, threshold=final_threshold), empty_token

    elif mode == "llm":
        candidate_count = rerank_cfg.get("candidate_count", 10)
        candidates = vector_search(query, top_k=candidate_count, threshold=0.25)
        if not candidates:
            return [], empty_token
        if rerank_cfg.get("enabled", True):
            print(f"[INFO] 使用 LLM 对 {len(candidates)} 个候选片段进行重排序...", file=sys.stderr)
            return llm_rerank(query, candidates, llm_cfg)
        else:
            return candidates[:rerank_cfg.get("final_top_k", 4)], empty_token

    else:
        print(f"[ERROR] 不支持的检索模式: {mode}，请使用 local 或 llm", file=sys.stderr)
        raise SystemExit(1)


def format_markdown(hits: list, query: str, mode: str, token_info: dict = None) -> str:
    if not hits:
        return ("> 未在 ClassIn API 文档中找到与「{}」相关的内容。\n"
                "> 请检查问题描述，或确认文档是否已建立索引。").format(query)
    mode_tag = "本地检索" if mode == "local" else "LLM 重排序"
    lines = [f"## 检索结果（{mode_tag} | 问题：{query}）\n",
             f"共找到 {len(hits)} 个相关片段：\n"]
    for i, hit in enumerate(hits, 1):
        module = hit.get("module", "")
        source = hit.get("source", "")
        section = hit.get("section", "")
        module_tag = f"【{module}】" if module else ""
        lines.append(
            f"---\n### [{i}] {module_tag} `{source}`\n"
            f"**章节**: {section}  **相关度**: {hit['score']:.2%}\n\n"
            + hit["text"] + "\n"
        )
    # 添加 token 统计信息
    if token_info and token_info.get("total_tokens", 0) > 0:
        lines.append("\n---\n")
        lines.append(f"**Token 使用统计**：")
        lines.append(f"| 项目 | 数量 |")
        lines.append(f"|------|------:|")
        lines.append(f"| 输入 Token | {token_info['prompt_tokens']:,} |")
        lines.append(f"| 输出 Token | {token_info['completion_tokens']:,} |")
        lines.append(f"| **总计** | **{token_info['total_tokens']:,}** |")
    return "\n".join(lines)


# ─── CLI ────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="ClassIn API 文档检索（双模式）")
    parser.add_argument("query", help="检索问题")
    parser.add_argument("--top", type=int, default=None, help="返回片段数量")
    parser.add_argument("--threshold", type=float, default=None, help="相关度阈值（local 模式）")
    parser.add_argument("--mode", choices=["local", "llm"], default=None, help="覆盖配置文件设置")
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown")
    args = parser.parse_args()

    hits, token_info = search(args.query, mode=args.mode, top_k=args.top, threshold=args.threshold)
    mode = args.mode or load_config().get("retrieval_mode", "local")

    if args.format == "json":
        print(json.dumps({"hits": hits, "token_info": token_info}, ensure_ascii=False, indent=2))
    else:
        print(format_markdown(hits, args.query, mode, token_info))


if __name__ == "__main__":
    main()
