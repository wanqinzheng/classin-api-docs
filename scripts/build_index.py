#!/usr/bin/env python3
"""
build_index.py - 构建 ClassIn API 文档向量索引

支持复杂嵌套目录结构，自动识别模块，按 Markdown 标题智能切片。

用法：
    python scripts/build_index.py              # 增量索引
    python scripts/build_index.py --rebuild    # 强制全量重建
    python scripts/build_index.py --stats      # 仅显示文档统计
"""

import os
import re
import json
import hashlib
import pathlib
import argparse
import sys

# ─── 路径配置 ───────────────────────────────────────────────────────────────
SKILL_ROOT       = pathlib.Path(__file__).parent.parent
REFS_DIR         = SKILL_ROOT / "references"
DB_DIR           = SKILL_ROOT / ".rag_db"
META_FILE        = DB_DIR / "meta.json"
COLLECTION_NAME  = "classin_api_docs"

CHUNK_SIZE    = 600   # 每片最大字符数
CHUNK_OVERLAP = 80    # 相邻片段重叠字符数
EMBED_MODEL   = "BAAI/bge-small-zh-v1.5"

# 排除的文件/目录
EXCLUDE_NAMES = {
    "README.md", "SUMMARY.md", "cover.jpg", "cover_small.jpg",
    "footer.jpg", "footer_small.jpg", "README.png", "API_Sequence.md",
    "introduction.md", ".DS_Store", "Thumbs.db"
}
EXCLUDE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".mp4", ".mp3", ".pdf"}


# ─── 工具函数 ────────────────────────────────────────────────────────────────

def file_hash(path: pathlib.Path) -> str:
    return hashlib.md5(path.read_bytes()).hexdigest()


def get_module_name(rel_path: pathlib.Path) -> str:
    """从相对路径提取模块名"""
    parts = rel_path.parts
    if len(parts) > 1:
        return parts[0]  # 第一级目录名作为模块名
    return "基础文档"


def get_api_name(file_path: pathlib.Path) -> str:
    """从文件名提取 API 名称"""
    name = file_path.stem  # 去掉扩展名
    # 处理特殊字符
    name = name.replace("_", " ").replace("-", " ")
    # 转换驼峰为空格分隔
    name = re.sub(r"([a-z])([A-Z])", r"\1 \2", name)
    return name.title()


def clean_markdown(text: str) -> str:
    """清理 Markdown 特殊格式，保留结构信息"""
    # 移除图片引用（保留 alt 文字）
    text = re.sub(r"!\[.*?\]\(.*?\)", "", text)
    # 移除内部链接但保留文本
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    # 规范化空白
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def split_markdown(text: str, source: str, module: str):
    """
    针对 ClassIn API 文档优化的切片策略：
    1. 按 ## 二级标题切片（接口粒度）
    2. 保留 # 一级标题作为上下文前缀
    3. 超长接口按字符数二次切割
    """
    chunks = []
    current_h1 = ""
    current_h2 = ""
    buffer = ""

    lines = text.splitlines(keepends=True)

    def flush(buf, h1, h2, module):
        content = buf.strip()
        if len(content) < 50:  # 过短片段跳过
            return
        prefix = f"# {module}\n" if module else ""
        if h1:
            prefix += f"## {h1}\n"
        if h2 and h2 != h1:
            prefix += f"### {h2}\n"
        full = (prefix + content).strip()
        # 超长则按字符数二次切割
        for i in range(0, len(full), CHUNK_SIZE - CHUNK_OVERLAP):
            piece = full[i: i + CHUNK_SIZE]
            if piece.strip():
                chunks.append({
                    "text": piece,
                    "source": source,
                    "module": module,
                    "section": h2 or h1 or get_api_name(pathlib.Path(source)),
                })

    for line in lines:
        h1_match = re.match(r"^#\s+(.+)", line)
        h2_match = re.match(r"^##\s+(.+)", line)

        if h1_match:
            flush(buffer, current_h1, current_h2, module)
            buffer = ""
            current_h1 = h1_match.group(1).strip()
            current_h2 = ""
        elif h2_match:
            # 二级标题强制切分（接口边界）
            if buffer.strip():
                flush(buffer, current_h1, current_h2, module)
            buffer = line  # 新接口从标题开始
            current_h2 = h2_match.group(1).strip()
        else:
            buffer += line

        # 缓冲区超长时提前切割
        if len(buffer) > CHUNK_SIZE * 1.5:
            flush(buffer, current_h1, current_h2, module)
            buffer = ""

    flush(buffer, current_h1, current_h2, module)
    return chunks


def scan_documents():
    """扫描 references/ 目录，返回所有有效的 Markdown 文件"""
    md_files = []
    for f in sorted(REFS_DIR.rglob("*.md")):
        # 排除文件名
        if f.name in EXCLUDE_NAMES:
            continue
        # 排除扩展名
        if f.suffix.lower() in EXCLUDE_EXTENSIONS:
            continue
        md_files.append(f)
    return md_files


def load_meta() -> dict:
    if META_FILE.exists():
        return json.loads(META_FILE.read_text(encoding="utf-8"))
    return {}


def save_meta(meta: dict):
    DB_DIR.mkdir(parents=True, exist_ok=True)
    META_FILE.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")


def print_stats(md_files):
    """打印文档统计信息"""
    print("\n" + "=" * 60)
    print("[ClassIn API 文档统计]")
    print("=" * 60)

    modules = {}
    for f in md_files:
        rel = f.relative_to(REFS_DIR)
        module = rel.parts[0] if len(rel.parts) > 1 else "基础文档"
        if module not in modules:
            modules[module] = {"count": 0, "files": []}
        modules[module]["count"] += 1
        modules[module]["files"].append(f.name)

    total_files = 0
    for module, info in sorted(modules.items()):
        total_files += info["count"]
        print(f"\n[{module}/] ({info['count']} 个文件)")
        for fname in sorted(info["files"])[:5]:
            print(f"   - {fname}")
        if len(info["files"]) > 5:
            print(f"   ... 还有 {len(info['files']) - 5} 个文件")

    print(f"\n{'=' * 60}")
    print(f"总计：{total_files} 个 Markdown 文件，{len(modules)} 个模块")
    print("=" * 60)


# ─── 主流程 ──────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="构建 ClassIn API 文档向量索引")
    parser.add_argument("--rebuild", action="store_true", help="强制重建全部索引")
    parser.add_argument("--stats", action="store_true", help="仅显示文档统计")
    parser.add_argument("--model", default=EMBED_MODEL, help=f"嵌入模型，默认 {EMBED_MODEL}")
    args = parser.parse_args()

    # 扫描文档
    md_files = scan_documents()
    if not md_files:
        print("[ERROR] references/ 目录下没有找到有效的 Markdown 文件")
        return

    # 仅显示统计
    if args.stats:
        print_stats(md_files)
        return

    # 导入依赖
    try:
        import chromadb
        from chromadb.utils import embedding_functions
    except ImportError:
        print("[ERROR] 缺少依赖，请先运行：pip install -r scripts/requirements.txt")
        print("[ERROR] 如果尚未安装 PyYAML，请同时运行：pip install pyyaml")
        raise SystemExit(1)

    DB_DIR.mkdir(parents=True, exist_ok=True)

    # 初始化 ChromaDB
    client = chromadb.PersistentClient(path=str(DB_DIR))
    embed_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name=args.model, device="cpu"
    )

    # 获取或创建 collection
    if args.rebuild:
        try:
            client.delete_collection(COLLECTION_NAME)
            print(f"[INFO] 已删除旧索引 collection: {COLLECTION_NAME}")
        except Exception:
            pass
        meta = {}
    else:
        meta = load_meta()

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        embedding_function=embed_fn,
        metadata={"hnsw:space": "cosine"},
    )

    # 打印统计
    print_stats(md_files)

    total_added = 0
    total_skipped = 0

    for md_file in md_files:
        rel_path = md_file.relative_to(REFS_DIR)
        fname = str(rel_path)
        fhash = file_hash(md_file)

        # 增量更新
        if not args.rebuild and meta.get(fname) == fhash:
            print(f"[SKIP] {fname}（未变化）")
            total_skipped += 1
            continue

        print(f"[INDEX] {fname} ...", end=" ", flush=True)
        text = clean_markdown(md_file.read_text(encoding="utf-8"))
        module = get_module_name(rel_path)
        chunks = split_markdown(text, source=fname, module=module)

        if not chunks:
            print("WARNING: 无有效内容")
            continue

        # 删除旧片段
        try:
            existing = collection.get(where={"source": fname})
            if existing["ids"]:
                collection.delete(ids=existing["ids"])
        except Exception:
            pass

        # 批量插入
        ids       = [f"{fname}__chunk_{i}" for i in range(len(chunks))]
        documents = [c["text"] for c in chunks]
        metadatas = [{"source": c["source"], "module": c["module"],
                      "section": c["section"]} for c in chunks]

        batch = 64
        for start in range(0, len(ids), batch):
            collection.add(
                ids=ids[start:start+batch],
                documents=documents[start:start+batch],
                metadatas=metadatas[start:start+batch],
            )

        print(f"[OK] {len(chunks)} 个片段")
        total_added += len(chunks)
        meta[fname] = fhash

    save_meta(meta)

    total = collection.count()
    print(f"\n{'=' * 60}")
    print(f"[OK] 索引构建完成!")
    print(f"   本次新增片段：{total_added}")
    print(f"   跳过文件数：{total_skipped}")
    print(f"   向量库总片段数：{total}")
    print(f"   存储路径：{DB_DIR}")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
