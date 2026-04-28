# classin-api-docs

> ClassIn API 知识库 Skill（RAG 双模式版）— 适用于 WorkBuddy（龙虾）平台

让 AI 助手变成你的 ClassIn API 专家。支持约 **100 个接口**的语义检索，基于向量检索精准定位文档，支持本地检索和 LLM 辅助检索两种模式。

---

## 功能特性

- 🔍 **语义向量检索（RAG）**：基于 ChromaDB + BGE 中文嵌入模型，精确定位相关文档片段
- 📚 **100+ 接口全覆盖**：用户管理、课程课节、LMS、云盘、直播录制、消息订阅等
- 🔄 **增量更新索引**：文档变化时只重新索引有改动的文件
- 💻 **多语言代码示例**：Python / Node.js / Java / PHP / Go
- 🚫 **零成本运行**：嵌入模型本地运行，无需 OpenAI API Key

---

## 项目结构

```
classin-api-docs/
├── SKILL.md                      # Skill 核心配置
├── README.md
├── config.yaml                   # 检索模式配置（local / llm）
├── .gitignore
├── references/                   # API 文档（约 100 个 .md 文件）
│   ├── index.md                  # 文档总索引
│   ├── overview.md               # 系统概述
│   ├── SUMMARY.md                # 接口目录
│   ├── user/                     # 用户管理（13 个接口）
│   ├── classroom/                # 课程课节（25 个接口）
│   ├── LMS/                      # LMS 活动（12 个接口）
│   ├── cloud/                    # 云盘操作（11 个接口）
│   ├── broadcast/                # 直播录制（4 个接口）
│   ├── datasub/                  # 消息订阅（8 个接口 + resources/）
│   ├── school/                   # 机构管理（4 个接口）
│   ├── group/                   # 班级群（1 个接口）
│   ├── onlineDoubleTeacher/      # 双师课（3 个接口）
│   ├── Solutions/               # 对接方案（8 个接口 + 媒体文件）
│   ├── Error-Handling/          # 错误处理（4 个文档）
│   └── appendix/                # 附录（9 个文档）
└── scripts/
    ├── requirements.txt
    ├── build_index.py           # 切片 + 向量化
    ├── search.py                # 双模式检索
    └── generate_example.py      # 多语言代码生成
```

---

## 快速安装

### 安装 Skill

**方法 A：zip 安装** → 龙虾技能中心导入 `classin-api-docs.zip`

**方法 B：手动复制**
```bash
# Windows
xcopy /E /I classin-api-docs %USERPROFILE%\.workbuddy\skills\classin-api-docs

# macOS / Linux
cp -r classin-api-docs ~/.workbuddy/skills/
```

### 安装依赖

```bash
cd ~/.workbuddy/skills/classin-api-docs
pip install -r scripts/requirements.txt
```

### 建立向量索引

```bash
python scripts/build_index.py
```

> 首次运行会自动下载嵌入模型（约 400MB），之后本地缓存

### 配置检索模式（可选）

编辑 `config.yaml`，将 `retrieval_mode` 改为 `llm` 启用 LLM 辅助检索：

```yaml
retrieval_mode: llm
llm:
  provider: dashscope
  dashscope:
    model: qwen-plus
    api_key: "your-api-key"
```

---

## 接口模块速查

| 模块 | 接口数量 | 主要接口 |
|------|----------|----------|
| 用户管理 | 13 | 注册用户、添加老师/学生、修改密码 |
| 课程课节 | 25 | 创建/编辑/删除课程、创建/修改/删除课节 |
| LMS | 12 | 单元管理、课堂活动、发布活动 |
| 云盘 | 11 | 文件夹/文件操作、课件授权 |
| 直播录制 | 4 | 录课设置、播放地址 |
| 消息订阅 | 8+ | 实时推送、课后推送 |
| 机构管理 | 4 | 机构标签、学校设置 |
| 双师课 | 3 | 创建/编辑/删除双师课节 |
| 附录 | 9 | API v2 签名、参数规则 |

---

## 脚本命令速查

```bash
# 查看文档统计
python scripts/build_index.py --stats

# 建立/更新索引（增量）
python scripts/build_index.py

# 全量重建
python scripts/build_index.py --rebuild

# 检索（自动使用 config.yaml 中的模式）
python scripts/search.py "创建课程需要哪些参数"

# 强制指定模式
python scripts/search.py "创建课程" --mode llm
python scripts/search.py "创建课程" --mode local

# 调试输出 JSON
python scripts/search.py "创建课程" --format json

# 生成代码示例
python scripts/generate_example.py --api create_classroom --lang python
```

---

## 技术架构

```
用户提问
    ↓
[search.py] 读取 config.yaml
    ├── local → ChromaDB 向量检索（余弦相似度）
    └── llm   → 向量检索召回 → LLM 重排序
    ↓
Top-K 相关片段（含模块名 + 章节）
    ↓
AI 综合回答，标注文档来源
```

| 组件 | 技术选型 |
|------|----------|
| 向量库 | ChromaDB（本地持久化） |
| 嵌入模型 | BAAI/bge-small-zh-v1.5（本地运行，无需 API Key） |
| LLM（可选） | OpenAI / Claude / 通义 / Ollama |

---

## 注意

- `.rag_db/`（向量库数据）不要提交到 Git
- 首次运行 `build_index.py` 会下载嵌入模型（约 400MB）
- Python 版本要求：>= 3.9
