---
dataset_info:
  features:
    - name: "id"
      dtype: "int64"
    - name: "query_paradigm"
      dtype: "string"
    - name: "query_zh"
      dtype: "string"
    - name: "nl2sql_zh"
      dtype: "string"
    - name: "query_en"
      dtype: "string"
    - name: "nl2sql_en"
      dtype: "string"
  splits:
    - name: "train"
      num_bytes: 0
      num_examples: 100
  download_size: 0
  dataset_size: 0
---

# NL2SQL-Patent-Paper-100 数据集

首个面向专利和论文检索的中文 NL2SQL 数据集，包含自然语言查询到结构化检索表达式的转换对。

## 数据集概述

### 数据集摘要

本数据集包含 100 条专利/论文检索领域的 NL2SQL 样本，每条数据包含：
- 中文自然语言查询（query）
- 对应的半结构化检索表达式（nl2sql）
- 英文翻译版本

这是更大规模数据集（742条）的样本子集，用于社区验证和基线测试。

### 支持的任务

- **Text-to-SQL**：自然语言到结构化查询转换
- **语义解析**：自然语言理解到形式化表达
- **信息检索**：专利/论文检索查询理解
- **机器翻译**：中英技术文本翻译

### 语言

- 中文（简体）
- 英文

### 领域

- 专利检索
- 学术论文检索
- 知识产权

---

## 数据集结构

### 数据字段

| 字段名 | 类型 | 描述 | 示例 |
|--------|------|------|------|
| id | int | 唯一标识符 | 4 |
| query_paradigm | string | 查询范式描述 | patent\|k3\|org+cited_count+ipc |
| query_zh | string | 中文自然语言查询 | 看看华为这块，被引用不少于100次... |
| nl2sql_zh | string | 中文结构化表达式 | patent\|org_name:华为 AND cited_count... |
| query_en | string | 英文自然语言查询 | I'd like to find out: What patents... |
| nl2sql_en | string | 英文结构化表达式 | patent\|org_name:Huawei AND cited_count... |

### 数据分割

| 分割 | 样本数 | 说明 |
|------|--------|------|
| train | 100 | 完整样本集（本版本暂不分割） |

### 查询类型分布

| 查询范式 | 数量 | 占比 |
|----------|------|------|
| patent (专利检索) | ~70% | 专利相关查询 |
| paper (论文检索) | ~20% | 论文相关查询 |
| patent+paper (混合) | ~10% | 混合查询 |

---

## 数据集创建

### 数据来源

- **数据类型**：专利和论文检索场景的模拟查询数据
- **构建方式**：基于检索场景需求人工设计并标注
- **采集时间**：2024年
- **数据版本**：v1.0.0-sample

### 数据构建流程

1. **需求分析**：分析专利/论文检索系统的典型查询场景和需求
2. **场景设计**：设计覆盖多种检索条件的查询场景
3. **范式定义**：定义查询范式（query_paradigm）描述查询结构
4. **人工编写**：专业标注员编写自然语言查询和对应的结构化表达式
5. **质量审核**：资深审核员检查语法和语义正确性
6. **翻译校对**：专业译者进行中英互译

### 查询范式说明

查询范式（query_paradigm）使用以下格式描述查询结构：

```
resource_type|query_type|fields|filters|base_date
```

示例：
- `patent|k3|org+cited_count+ipc|base=20251111`：专利检索，K3类型，包含机构、引用数、IPC分类字段
- `paper|k4|org+kw+reference_count|base=20251231`：论文检索，K4类型，包含机构、关键词、参考文献数

---

## 使用指南

### 快速开始

```python
from datasets import load_dataset

# 从 Hugging Face 加载
dataset = load_dataset("KyrieSun/nl2sql-patent-paper-100")

# 查看样本
sample = dataset["train"][0]
print(f"Query: {sample['query_zh']}")
print(f"NL2SQL: {sample['nl2sql_zh']}")
```

### 本地加载

```python
import json

# 从 JSONL 加载
data = []
with open("nl2sql_sample_100.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        data.append(json.loads(line))

print(f"加载了 {len(data)} 条数据")
print(f"第一条: {data[0]['query_zh']}")
```

### 任务示例：Text-to-SQL

```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# 加载模型（示例使用 T5）
tokenizer = AutoTokenizer.from_pretrained("t5-base")
model = AutoModelForSeq2SeqLM.from_pretrained("t5-base")

# 准备输入
input_text = f"translate to SQL: {sample['query_zh']}"
inputs = tokenizer(input_text, return_tensors="pt")

# 生成输出
outputs = model.generate(**inputs)
predicted_sql = tokenizer.decode(outputs[0], skip_special_tokens=True)

print(f"输入: {sample['query_zh']}")
print(f"预测: {predicted_sql}")
print(f"真实: {sample['nl2sql_zh']}")
```

---

## 基准测试

### 评估指标

| 指标 | 说明 |
|------|------|
| Exact Match (EM) | 完全匹配率 |
| Component Match | 组件级匹配率 |
| BLEU | 生成质量 |

### 当前基线

| 模型 | EM | BLEU | 备注 |
|------|-----|------|------|
| T5-base | -- | -- | 待测试 |
| ChatGPT-3.5 | -- | -- | 待测试 |

欢迎提交你的实验结果！

---

## 数据示例

### 示例 1：专利检索

```json
{
  "id": 4,
  "query_paradigm": "patent|k3|org+cited_count+ipc|base=20251111",
  "query_zh": "看看华为这块，被引用不少于100次、IPCG02B的专利有哪些？",
  "nl2sql_zh": "patent|org_name:华为 AND cited_count:[100 TO *] AND ipc_cpc:G02B",
  "query_en": "I'd like to find out: What patents by Huawei have been cited more than 100 times and belong to IPCG02B?",
  "nl2sql_en": "patent|org_name:Huawei AND cited_count:[100 TO *] AND ipc_cpc:G02B"
}
```

### 示例 2：论文检索

```json
{
  "id": 193,
  "query_paradigm": "patent|k4|org+kw+reference_count+ipc|base=20251231",
  "query_zh": "想搜广东微容电子科技股份有限公司相关的，关于功率器件、引用超过5次、IPCG01N的专利有哪些？",
  "nl2sql_zh": "patent|org_name:广东微容电子科技股份有限公司 AND key_words:功率器件 AND reference_count:[6 TO *] AND ipc_cpc:G01N",
  "query_en": "I'm looking for information about Guangdong Microelectronics Technology Co., Ltd., specifically regarding power devices, patents cited more than 5 times, and the IPCG01N patent.",
  "nl2sql_en": "patent|org_name:Guangdong Microelectronics Technology AND key_words:power devices AND ipc_cpc:G01N AND reference_count:[6 TO *]"
}
```

---

## 局限性

1. **样本规模**：本版本仅包含100条样本，用于验证和基线测试
2. **领域局限**：专注于专利和论文检索领域，通用性有限
3. **语言局限**：主要面向中文查询，英文为翻译版本
4. **表达式格式**：使用特定的半结构化格式，非标准 SQL

---

## 更新计划

| 版本 | 预计时间 | 内容 |
|------|----------|------|
| v1.1.0 | 2024-Q2 | 发布完整版（742条） |
| v1.2.0 | 2024-Q3 | 增加更多查询类型 |
| v2.0.0 | 2024-Q4 | 扩展至其他技术领域 |

---

## 引用

### BibTeX

```bibtex
@dataset{nl2sql_patent_paper_2024,
  author = {KyrieSun},
  title = {NL2SQL-Patent-Paper-100: A Chinese NL2SQL Dataset for Patent and Paper Retrieval},
  year = {2024},
  publisher = {Hugging Face},
  version = {1.0.0},
  url = {https://huggingface.co/datasets/KyrieSun/nl2sql-patent-paper-100}
}
```

### 引用格式

> KyrieSun. (2024). NL2SQL-Patent-Paper-100: A Chinese NL2SQL Dataset for Patent and Paper Retrieval [Data set]. Hugging Face. https://huggingface.co/datasets/KyrieSun/nl2sql-patent-paper-100

---

## 许可协议

本数据集采用 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 协议。

您可以：
- ✅ 共享 — 复制、分发和传播
- ✅ 改编 — 混音、转换和基于本作品创作

条件：
- 署名 — 您必须给出适当的署名

---

## 联系方式

- **数据集维护**：通过 Hugging Face 或 GitHub 联系
- **问题反馈**：[GitHub Issues](https://github.com/KyrieSun/nl2sql-patent-paper-100/issues)
- **Hugging Face**：[@KyrieSun](https://huggingface.co/KyrieSun)

---

## 更新日志

| 版本 | 日期 | 更新内容 |
|------|------|----------|
| v1.0.0 | 2024-03-31 | 初始发布，100条样本 |
