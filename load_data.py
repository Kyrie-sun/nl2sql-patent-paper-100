#!/usr/bin/env python3
"""
NL2SQL 数据集加载脚本
支持从 Hugging Face 或本地文件加载
"""

from datasets import load_dataset, Dataset
import json
from pathlib import Path


def load_from_hf(dataset_name="your-org/nl2sql-patent-paper-100"):
    """从 Hugging Face 加载数据集"""
    dataset = load_dataset(dataset_name)
    return dataset


def load_from_local(jsonl_path="data/nl2sql_sample_100.jsonl"):
    """从本地 JSONL 文件加载数据集"""
    data = []
    with open(jsonl_path, "r", encoding="utf-8") as f:
        for line in f:
            data.append(json.loads(line))
    
    # 转换为 Hugging Face Dataset 格式
    dataset = Dataset.from_list(data)
    return dataset


def parse_nl2sql(nl2sql_str):
    """
    解析 nl2sql 表达式为结构化字典
    
    Args:
        nl2sql_str: 如 "patent|org_name:华为 AND cited_count:[100 TO *]"
    
    Returns:
        dict: 解析后的结构
    """
    parts = nl2sql_str.split('|')
    resource_type = parts[0]
    
    # 解析条件
    conditions = parts[1] if len(parts) > 1 else ""
    cond_dict = {}
    
    for cond in conditions.split(' AND '):
        cond = cond.strip()
        if ':' in cond:
            key, value = cond.split(':', 1)
            cond_dict[key.strip()] = value.strip()
    
    return {
        "resource_type": resource_type,
        "conditions": cond_dict
    }


def get_statistics(dataset):
    """获取数据集统计信息"""
    stats = {
        "total_samples": len(dataset),
        "avg_query_length": sum(len(q) for q in dataset["query_zh"]) / len(dataset),
        "avg_nl2sql_length": sum(len(n) for n in dataset["nl2sql_zh"]) / len(dataset),
    }
    
    # 统计资源类型
    resource_types = {}
    for nl2sql in dataset["nl2sql_zh"]:
        rt = nl2sql.split('|')[0] if '|' in nl2sql else "unknown"
        resource_types[rt] = resource_types.get(rt, 0) + 1
    
    stats["resource_types"] = resource_types
    
    return stats


if __name__ == "__main__":
    # 示例用法
    print("=" * 60)
    print("NL2SQL 数据集加载示例")
    print("=" * 60)
    
    # 本地加载
    print("\n1. 从本地加载...")
    dataset = load_from_local()
    print(f"   加载了 {len(dataset)} 条数据")
    
    # 显示统计
    print("\n2. 数据统计...")
    stats = get_statistics(dataset)
    print(f"   总样本数: {stats['total_samples']}")
    print(f"   平均 query 长度: {stats['avg_query_length']:.1f} 字符")
    print(f"   平均 nl2sql 长度: {stats['avg_nl2sql_length']:.1f} 字符")
    print(f"   资源类型分布: {stats['resource_types']}")
    
    # 解析示例
    print("\n3. NL2SQL 解析示例...")
    sample = dataset[0]
    parsed = parse_nl2sql(sample["nl2sql_zh"])
    print(f"   原始: {sample['nl2sql_zh']}")
    print(f"   解析: {parsed}")
    
    print("\n" + "=" * 60)
    print("完成！")
    print("=" * 60)
