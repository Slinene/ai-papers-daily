---
title: 'ResKV: Reconstructing Omitted Attention Contributions for Fixed-Budget KV
  Cache Compression'
title_zh: ResKV：固定预算下通过残差缓存重构被忽略注意力贡献的KV缓存压缩
authors:
- Yuhang Zhan
- Lisi Chen
- Shuo Shang
affiliations:
- University of Electronic Science and Technology of China
arxiv_id: '2607.29591'
url: https://arxiv.org/abs/2607.29591
pdf_url: https://arxiv.org/pdf/2607.29591
published: '2026-07-31'
collected: '2026-08-03'
category: LLM
direction: 固定预算KV缓存压缩
tags:
- KV cache
- compression
- eviction
- residual attention
- long-context inference
one_liner: 将KV缓存预算分为精确主缓存与紧凑残差缓存，同框归一化复原被丢弃token的注意力分子分母贡献，广泛提升长上下文性能。
practical_value: '- 在电商推荐的长用户行为序列建模中，若使用LLM生成式推荐，KV缓存膨胀是瓶颈，可借鉴ResKV的残差缓存思路：保留核心token作为精确主缓存，用紧凑残差统计量重构被丢弃token的注意力贡献，从而在内存受限下保持长上下文的注意力完整性。

  - 工程实现上，残差缓存的构建可通过离线验证决定每层每头的残差预算分配，解码时动态门控按query调整残差贡献，这种在线-离线协同策略可以迁移到推荐系统中的搜索/浏览长序列压缩，平衡效果与延迟。

  - 残差缓存参与同一softmax归一化，而不是事后修正，这一设计确保注意力分数的分子和分母质量都得到恢复，相比简单的eviction或合并方法，对下游生成质量更友好，适合高精度要求的选品文案生成、个性化搜索词推荐等场景。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有KV缓存驱逐方法永久丢弃未选token，丢失其聚合注意力贡献；合并方法保留更多信息但会扰动应保持精确的键值。\
**方法**：将固定KV预算划分为精确主缓存和紧凑残差缓存，残差缓存以统计量形式重构被忽略token的注意力贡献，并与主缓存token一起参与softmax归一化，从而恢复注意力的分子和分母质量。构建时通过验证代理决定每层每注意力头的残差分配，解码时用动态门控按每个查询调整残差贡献。\
**结果**：在LongBench和RULER上，覆盖query-aware/query-agnostic设定、多种骨干模型与缓存预算，与代表性压缩基线对比，相同KV预算下实现广泛性能提升，同时保持压缩解码的实际效率（峰值内存、长上下文吞吐量）。
