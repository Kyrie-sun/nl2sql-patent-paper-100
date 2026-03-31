# NL2SQL-Patent-Paper-100 发布检查清单

## 📋 发布前检查

### 数据文件
- [x] 数据文件已准备 (`data/nl2sql_sample_100.jsonl`)
- [x] CSV 备份已准备 (`data/nl2sql_sample_100.csv`)
- [x] 数据验证通过 (100条，6个字段完整)
- [x] ID范围: 4-1316
- [x] 资源类型: patent 92%, paper 8%

### 文档文件
- [x] Dataset Card 已编写 (`README.md`)
- [x] GitHub README 已编写 (`GITHUB_README.md`)
- [x] 上传指南已编写 (`UPLOAD_GUIDE.md`)
- [x] 加载脚本已编写 (`load_data.py`)
- [x] LICENSE 已添加 (CC BY 4.0)

### Hugging Face 准备
- [ ] 注册/登录 Hugging Face 账号
- [ ] 创建 Access Token
- [ ] 安装 huggingface-cli: `pip install huggingface-hub datasets`
- [ ] 登录: `huggingface-cli login`

---

## 🚀 发布步骤

### Step 1: 创建 Hugging Face 数据集仓库

```bash
huggingface-cli repo create nl2sql-patent-paper-100 --type dataset
```

或访问: https://huggingface.co/new-dataset

### Step 2: 克隆仓库并上传文件

```bash
# 克隆仓库
git lfs install
git clone https://huggingface.co/datasets/YOUR_USERNAME/nl2sql-patent-paper-100
cd nl2sql-patent-paper-100

# 复制文件
cp ../data/nl2sql_sample_100.jsonl .
cp ../README.md .
cp ../LICENSE .

# 提交
git add .
git commit -m "Initial release: NL2SQL Patent Paper 100 samples"
git push
```

### Step 3: 验证上传

```python
from datasets import load_dataset

# 测试加载
dataset = load_dataset("YOUR_USERNAME/nl2sql-patent-paper-100")
print(f"成功加载 {len(dataset['train'])} 条数据")
print(dataset["train"][0])
```

### Step 4: 完善数据集页面

1. 访问 `https://huggingface.co/datasets/YOUR_USERNAME/nl2sql-patent-paper-100`
2. 点击 "Edit dataset card" 完善信息
3. 添加标签 (Tags):
   - [ ] `task_categories: text2text-generation`
   - [ ] `language: zh`
   - [ ] `language: en`
   - [ ] `size_categories: n<1K`
   - [ ] `license: cc-by-4.0`

---

## 📢 发布后推广

### 立即执行
- [ ] 在 Twitter/X 发布上线公告
- [ ] 在知乎/公众号发布技术文章
- [ ] 发送邮件给相关研究者

### 一周内
- [ ] 创建 GitHub 仓库并上传代码
- [ ] 在 Papers With Code 关联数据集
- [ ] 在相关社区发帖（如 Reddit r/MachineLearning）

### 持续运营
- [ ] 回复 Issues 和 Discussions
- [ ] 收集用户反馈
- [ ] 规划下一版本（完整版 742 条）

---

## 📊 关键指标追踪

| 指标 | 目标（1周） | 目标（1月） |
|------|------------|------------|
| Downloads | 50 | 200 |
| Likes | 5 | 20 |
| GitHub Stars | 10 | 50 |

---

## 🔗 相关链接

- **数据位置**: `~/.openclaw/workspace/nl2sql_hf_upload/`
- **原始数据**: `/Users/sunxinkai_1/Downloads/nl2sql_2000_final_cn_en.xlsx`
- **Hugging Face 上传指南**: `UPLOAD_GUIDE.md`

---

**准备就绪！执行 Step 1 开始发布。**
