#!/bin/bash
# GitHub 发布脚本
# 执行前请确保已配置 GitHub Token

set -e

REPO_NAME="nl2sql-patent-paper-100"
GITHUB_USER="KyrieSun"  # 请修改为你的 GitHub 用户名

echo "=========================================="
echo "GitHub 仓库发布脚本"
echo "=========================================="

# 检查是否已初始化 git
if [ ! -d ".git" ]; then
    echo "初始化 Git 仓库..."
    git init
    git config user.email "data-team@example.com"
    git config user.name "Data Team"
fi

# 创建 README（使用 GitHub 版本）
cp README_GITHUB.md README.md

# 添加文件
echo "添加文件到 Git..."
git add .

# 提交
echo "提交更改..."
git commit -m "Initial release: NL2SQL Patent Paper 100 samples

- 100条专利/论文检索 NL2SQL 样本
- 中英双语对照
- 包含 Dataset Card 和加载脚本
- CC BY 4.0 许可证"

# 创建 GitHub 仓库（使用 gh CLI 或手动创建）
echo ""
echo "=========================================="
echo "下一步操作："
echo "=========================================="
echo ""
echo "方法1：使用 GitHub CLI（推荐）"
echo "  1. 安装 gh: https://cli.github.com/"
echo "  2. 登录: gh auth login"
echo "  3. 创建仓库: gh repo create ${REPO_NAME} --public --source=. --push"
echo ""
echo "方法2：手动创建"
echo "  1. 访问 https://github.com/new"
echo "  2. 填写 Repository name: ${REPO_NAME}"
echo "  3. 选择 Public"
echo "  4. 不要勾选 Initialize this repository"
echo "  5. 点击 Create repository"
echo "  6. 执行以下命令："
echo "     git remote add origin https://github.com/${GITHUB_USER}/${REPO_NAME}.git"
echo "     git branch -M main"
echo "     git push -u origin main"
echo ""
echo "方法3：使用 GitHub Token"
echo "  export GITHUB_TOKEN='your_token_here'"
echo "  curl -H \"Authorization: token \$GITHUB_TOKEN\" \\"
echo "       -d '{\"name\":\"${REPO_NAME}\",\"private\":false}' \\"
echo "       https://api.github.com/user/repos"
echo "  git remote add origin https://github.com/${GITHUB_USER}/${REPO_NAME}.git"
echo "  git push -u origin main"
echo ""
echo "=========================================="
