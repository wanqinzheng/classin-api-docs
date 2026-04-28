---
name: classin-api-docs
description: >
  ClassIn API 知识库技能（RAG 版）。当用户在开发过程中询问任何关于 ClassIn API 的问题时使用此技能，
  包括：接口调用方式、参数说明、返回字段、鉴权签名、错误码、课程管理、课节管理、用户注册、
  学生管理、云盘操作、直播录制、消息订阅、Webhook、LMS活动、大直播方案等一切与 ClassIn API 开发相关的问题。
  触发词包括：ClassIn API、classinAPI、eeo、课堂接口、教育云API、接口文档、API调用、
  鉴权签名怎么配、参数怎么传、返回值是什么、报错了、怎么创建课程、怎么创建课节、
  怎么添加学生、怎么添加老师、直播推流接口、录制接口、消息订阅、Webhook、回调、
  LMS活动、大直播、API开发。
---

# ClassIn API 知识库（RAG 双模式版）

## 技能目的

基于 **RAG（检索增强生成）** 架构，通过向量检索精准定位文档片段，再由 AI 综合回答。支持约 **100 个 API 接口**，覆盖用户管理、课程课节、LMS、云盘、直播录制、消息订阅等全部模块。

支持两种检索模式，通过 `config.yaml` 配置：

| 模式 | 说明 | 依赖 |
|------|------|------|
| `local` | ChromaDB 本地向量检索，余弦相似度 | 无 |
| `llm` | 向量检索召回候选片段 → LLM 重排序精选 | API Key |

---

## 文档模块概览

| 模块 | 说明 |
|------|------|
| `user/` | 用户注册、老师/学生添加、密码修改、启用停用 |
| `classroom/` | 课程增删改查、课节管理、学生管理、老师管理 |
| `LMS/` | 单元管理、课堂活动、发布活动、成员管理 |
| `cloud/` | 云盘文件夹/文件操作、课件授权 |
| `broadcast/` | 录课设置、直播地址、回放地址 |
| `datasub/` | 消息订阅说明、实时推送、课后推送 |
| `school/` | 机构标签、学校设置 |
| `group/` | 班级群管理 |
| `onlineDoubleTeacher/` | 在线双师课节 |
| `Solutions/` | 快速入门、大直播方案、唤醒客户端 |
| `Error-Handling/` | 对接前、排课、接口调试常见问题 |
| `appendix/` | API v2 签名、参数规则 |

---

## 配置检索模式

编辑 `config.yaml` 中的 `retrieval_mode`：

```yaml
retrieval_mode: local   # 本地向量检索（零成本，完全离线）
retrieval_mode: llm     # LLM 辅助检索（更精准）
```

### LLM Provider 配置

```yaml
llm:
  provider: dashscope   # openai | claude | dashscope | ollama
  dashscope:
    model: qwen-plus
    api_key: ""         # 留空读 DASHSCOPE_API_KEY 环境变量
```

---

## 核心工作流

### Phase 1：检索

```bash
python scripts/search.py "你的完整问题" --top 6
```

- **local 模式**：直接向量检索，返回余弦相似度 Top-K 片段
- **llm 模式**：向量检索召回 10 个候选片段 → LLM 重排序精选 4 个

### Phase 2：评估结果

| 相关度 | 处理方式 |
|--------|----------|
| >= 0.6 | 直接基于片段回答 |
| 0.3~0.6 | 综合多片段，说明置信度 |
| < 0.3 / 无结果 | 换关键词重试，最多 2 次 |

### Phase 3：综合回答

- **标注文档来源**：`references/<模块>/<文件>.md` 中的具体章节
- **准确性优先**：不凭空补充参数或字段
- **主动提示关联**：推荐相关接口

---

## 命令速查

| 任务 | 命令 |
|------|------|
| 查看文档统计 | python scripts/build_index.py --stats |
| 建立索引 | python scripts/build_index.py |
| 强制重建 | python scripts/build_index.py --rebuild |
| 本地检索 | python scripts/search.py "问题" --mode local |
| LLM 检索 | python scripts/search.py "问题" --mode llm |
| 调试 JSON | python scripts/search.py "问题" --format json |
| 代码示例 | python scripts/generate_example.py --api xxx --lang python |

---

## 技术架构

```
用户提问
    ↓
search.py 读取 config.yaml
    ├── mode=local  → ChromaDB 向量检索（余弦相似度）
    └── mode=llm    → 向量检索召回 → LLM 重排序
    ↓
Top-K 相关片段（含模块名 + 章节）
    ↓
AI 综合回答，标注文档来源
```
