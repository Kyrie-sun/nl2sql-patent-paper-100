# NL2SQL-Patent-Paper-100

<p align="center">
  <strong>首个面向专利和论文检索的中文 NL2SQL 数据集</strong>
</p>

<p align="center">
  <a href="https://huggingface.co/datasets/your-org/nl2sql-patent-paper-100">
    <img src="https://img.shields.io/badge/🤗_Dataset-Hugging_Face-yellow" alt="Hugging Face Dataset">
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-CC_BY_4.0-green" alt="License">
  </a>
  <img src="https://img.shields.io/badge/Samples-100-blue" alt="Samples">
  <img src="https://img.shields.io/badge/Languages-中文/English-orange" alt="Languages">
</p>

<p align="center">
  <a href="#-数据集介绍">数据集介绍</a> •
  <a href="#-快速开始">快速开始</a> •
  <a href="#-数据格式">数据格式</a> •
  <a href="#-使用示例">使用示例</a> •
  <a href="#-引用">引用</a>
</p>

---

## 📊 数据集介绍

### 什么是 NL2SQL-Patent-Paper-100？

这是一个专门面向**专利检索**和**论文检索**场景的 NL2SQL（Natural Language to SQL）数据集。每条数据包含：

- 📝 **自然语言查询**：用户用中文描述检索需求
- 🔍 **结构化表达式**：转换为机器可执行的检索表达式
- 🌐 **英文翻译**：中英双语对照

### 数据特点

| 特点 | 说明 |
|------|------|
| **领域专业** | 专注于专利/论文检索，包含 IPC 分类、引用数等专业字段 |
| **场景模拟** | 基于专利/论文检索场景设计的模拟查询 |
| **结构清晰** | 使用 query_paradigm 描述查询结构，便于解析 |
| **双语对照** | 提供中英双语版本，支持跨语言研究 |

### 数据统计

| 统计项 | 数值 |
|--------|------|
| 总样本数 | 100 |
| 专利检索 | ~70% |
| 论文检索 | ~20% |
| 混合查询 | ~10% |
| 平均 query 长度 | 35 字符 |
| 平均 nl2sql 长度 | 80 字符 |

---

## 🚀 快速开始

### 安装依赖

```bash
pip install datasets pandas
```

### 从 Hugging Face 加载

```python
from datasets import load_dataset

# 加载数据集
dataset = load_dataset("your-org/nl2sql-patent-paper-100")

# 查看第一条数据
sample = dataset["train"][0]
print(f"Query: {sample['query_zh']}")
print(f"NL2SQL: {sample['nl2sql_zh']}")
```

### 本地加载

```bash
# 克隆仓库
git clone https://github.com/your-org/nl2sql-patent-paper-100.git
cd nl2sql-patent-paper-100

# Python 加载
python << 'EOF'
import json

with open("data/nl2sql_sample_100.jsonl", "r", encoding="utf-8") as f:
    data = [json.loads(line) for line in f]

print(f"加载了 {len(data)} 条数据")
print(f"示例: {data[0]['query_zh']}")
EOF
```

---

## 📁 数据格式

### 文件结构

```
.
├── data/
│   ├── nl2sql_sample_100.jsonl    # 主数据文件 (JSONL)
│   └── nl2sql_sample_100.csv      # CSV 格式备份
├── README.md                       # 本文件
├── DATASET_CARD.md                 # Hugging Face Dataset Card
└── LICENSE                         # CC BY 4.0 许可证
```

### 字段说明

| 字段 | 类型 | 说明 | 示例 |
|------|------|------|------|
| `id` | int | 唯一标识符 | 4 |
| `query_paradigm` | string | 查询范式，描述查询结构 | `patent\|k3\|org+cited_count+ipc` |
| `query_zh` | string | 中文自然语言查询 | "看看华为这块，被引用不少于100次..." |
| `nl2sql_zh` | string | 中文结构化表达式 | `patent\|org_name:华为 AND cited_count...` |
| `query_en` | string | 英文自然语言查询 | "I'd like to find out: What patents..." |
| `nl2sql_en` | string | 英文结构化表达式 | `patent\|org_name:Huawei AND cited_count...` |

### 查询范式解析

`query_paradigm` 使用以下格式：

```
resource_type|query_type|fields|filters|base_date
```

| 组件 | 说明 | 示例 |
|------|------|------|
| `resource_type` | 资源类型 | `patent` (专利), `paper` (论文) |
| `query_type` | 查询类型 | `k3`, `k4` 等，表示复杂度级别 |
| `fields` | 涉及字段 | `org+cited_count+ipc` |
| `filters` | 过滤条件 | `base=20251111` |

---

## 💡 使用示例

### 示例 1：专利检索查询

**输入 (query_zh)**:
```
看看华为这块，被引用不少于100次、IPCG02B的专利有哪些？
```

**输出 (nl2sql_zh)**:
```
patent|org_name:华为 AND cited_count:[100 TO *] AND ipc_cpc:G02B
```

**解析**:
- `patent` - 检索专利
- `org_name:华为` - 机构名为华为
- `cited_count:[100 TO *]` - 被引用次数 ≥ 100
- `ipc_cpc:G02B` - IPC 分类号为 G02B

### 示例 2：论文检索查询

**输入 (query_zh)**:
```
帮我查下谷歌，参考文献为50次的论文有哪些？
```

**输出 (nl2sql_zh)**:
```
paper|org_name:谷歌 AND reference_count:50
```

### 示例 3：Python 处理代码

```python
import json
import re

# 解析 nl2sql 表达式
def parse_nl2sql(nl2sql_str):
    """解析 nl2sql 表达式为结构化字典"""
    parts = nl2sql_str.split('|')
    resource_type = parts[0]
    
    # 解析条件
    conditions = parts[1] if len(parts) > 1 else ""
    cond_dict = {}
    
    for cond in conditions.split(' AND '):
        if ':' in cond:
            key, value = cond.split(':', 1)
            cond_dict[key.strip()] = value.strip()
    
    return {
        "resource_type": resource_type,
        "conditions": cond_dict
    }

# 使用示例
nl2sql = "patent|org_name:华为 AND cited_count:[100 TO *] AND ipc_cpc:G02B"
parsed = parse_nl2sql(nl2sql)
print(json.dumps(parsed, indent=2, ensure_ascii=False))
```

**输出**:
```json
{
  "resource_type": "patent",
  "conditions": {
    "org_name": "华为",
    "cited_count": "[100 TO *]",
    "ipc_cpc": "G02B"
  }
}
```

---

## 🎯 适用任务

1. **Text-to-SQL**: 训练自然语言到结构化查询的转换模型
2. **语义解析**: 理解用户检索意图并转换为机器可执行表达式
3. **信息检索**: 专利/论文检索系统的查询理解模块
4. **机器翻译**: 技术领域的中英翻译研究
5. **对话系统**: 检索型对话系统的意图理解

---

## 📈 基准测试

### 评估指标

| 指标 | 说明 |
|------|------|
| **Exact Match (EM)** | 完全匹配率 |
| **Component F1** | 组件级 F1 分数 |
| **BLEU** | 生成质量评估 |

### 当前结果

| 模型 | EM | Component F1 | BLEU |
|------|-----|--------------|------|
| T5-small | -- | -- | -- |
| T5-base | -- | -- | -- |
| ChatGPT-3.5 | -- | -- | -- |

> 欢迎提交你的实验结果！请参考 [CONTRIBUTING.md](CONTRIBUTING.md)。

---

## 🗺️ 路线图

- [x] v1.0.0 - 发布 100 条样本数据集
- [ ] v1.1.0 - 发布完整版 742 条数据
- [ ] v1.2.0 - 增加更多查询类型和领域
- [ ] v2.0.0 - 扩展至标准 SQL 格式
- [ ] v2.1.0 - 增加对话式多轮查询

---

## 🤝 贡献指南

我们欢迎社区贡献！你可以：

1. **提交 Issue**: 报告数据错误或建议
2. **提交 PR**: 改进数据处理脚本或文档
3. **分享结果**: 提交你的基准测试结果
4. **扩展数据**: 贡献更多标注样本

请参考 [CONTRIBUTING.md](CONTRIBUTING.md) 了解详情。

---

## 📄 许可协议

本项目采用 [CC BY 4.0](LICENSE) 协议。

您可以自由使用、修改和分发本数据集，只需注明出处。

---

## 📚 引用

如果你在研究中使用了本数据集，请引用：

```bibtex
@dataset{nl2sql_patent_paper_2024,
  author = {Your Data Team},
  title = {NL2SQL-Patent-Paper-100: A Chinese NL2SQL Dataset for Patent and Paper Retrieval},
  year = {2024},
  publisher = {Hugging Face},
  version = {1.0.0},
  url = {https://huggingface.co/datasets/your-org/nl2sql-patent-paper-100}
}
```

---

## 📞 联系我们

- 📧 **邮箱**: data-team@your-org.com
- 🐛 **Issue**: [GitHub Issues](https://github.com/your-org/nl2sql-patent-paper-100/issues)
- 🤗 **Hugging Face**: [@your-org](https://huggingface.co/your-org)

---

<p align="center">
  <sub>Built with ❤️ for the NL2SQL community</sub>
</p>
