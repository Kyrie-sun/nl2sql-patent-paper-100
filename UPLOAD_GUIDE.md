# 上传到 Hugging Face 的步骤

## 前置要求

1. 安装 Hugging Face 工具
```bash
pip install huggingface-hub datasets
```

2. 登录 Hugging Face
```bash
huggingface-cli login
# 输入你的 access token
```

## 上传步骤

### 方法1：使用 huggingface-cli

```bash
# 创建数据集仓库
huggingface-cli repo create nl2sql-patent-paper-100 --type dataset

# 克隆仓库
git lfs install
git clone https://huggingface.co/datasets/YOUR_USERNAME/nl2sql-patent-paper-100

# 复制文件
cp data/nl2sql_sample_100.jsonl nl2sql-patent-paper-100/
cp README.md nl2sql-patent-paper-100/README.md

# 提交并推送
cd nl2sql-patent-paper-100
git add .
git commit -m "Initial release: 100 samples"
git push
```

### 方法2：使用 Python API

```python
from huggingface_hub import HfApi, create_repo
from datasets import Dataset
import json

# 创建仓库
create_repo(
    repo_id="YOUR_USERNAME/nl2sql-patent-paper-100",
    repo_type="dataset",
    private=False
)

# 加载数据
with open("data/nl2sql_sample_100.jsonl", "r", encoding="utf-8") as f:
    data = [json.loads(line) for line in f]

# 转换为 Dataset
dataset = Dataset.from_list(data)

# 推送到 Hugging Face
dataset.push_to_hub("YOUR_USERNAME/nl2sql-patent-paper-100")
```

### 方法3：使用网页界面

1. 访问 https://huggingface.co/new-dataset
2. 填写数据集信息：
   - Owner: 你的用户名或组织
   - Dataset name: `nl2sql-patent-paper-100`
   - License: `cc-by-4.0`
   - 勾选 "Is this a public dataset?"
3. 点击 "Create dataset"
4. 在 Files 标签页上传文件：
   - `nl2sql_sample_100.jsonl`
   - `README.md` (复制 Dataset Card 内容)

## 上传后检查清单

- [ ] 数据集页面可以正常访问
- [ ] 可以成功加载数据集：`load_dataset("YOUR_USERNAME/nl2sql-patent-paper-100")`
- [ ] Dataset Card 显示正常
- [ ] 文件下载链接可用
- [ ] 添加适当的标签（Tags）

## 标签建议

在 Hugging Face 数据集页面添加以下标签：
- `task_categories: text2text-generation`
- `task_categories: text-classification`
- `language: zh`
- `language: en`
- `size_categories: n<1K`
- `license: cc-by-4.0`
- `domain: nlp`
- `domain: information-retrieval`

## 后续优化

1. **添加预览图**：在 Dataset Card 中添加数据样本截图
2. **创建 Space Demo**：制作交互式演示
3. **关联模型**：上传基线模型并关联
4. **社区互动**：回复 Issues 和 Discussions
