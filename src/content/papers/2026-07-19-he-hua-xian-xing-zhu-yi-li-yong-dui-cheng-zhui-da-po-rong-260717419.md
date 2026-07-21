---
title: 'Kernelized Linear Attention: Breaking the Capacity Wall with Symmetric Cones'
title_zh: 核化线性注意力：用对称锥打破容量墙
authors:
- Ayoub Ghriss
- Sourav Chakraborty
affiliations:
- Department of Computer Science, University of Colorado Boulder
arxiv_id: '2607.17419'
url: https://arxiv.org/abs/2607.17419
pdf_url: https://arxiv.org/pdf/2607.17419
published: '2026-07-19'
collected: '2026-07-21'
category: Training
direction: 高效线性注意力训练与推理
tags:
- linear-attention
- kernel-methods
- associative-recall
- throughput-optimization
- Triton-kernels
- LLM-training
one_liner: 提出 KATA 框架，利用自对偶锥保证非负注意力权重，大幅提升线性注意力的联想记忆容量与吞吐量
practical_value: '- 在用户长序列建模中可直接替换 softmax 注意力，KATA 的块状态形式和 O(log T) 深度扫描能将推理延迟降低一个数量级，适合稀疏行为序列的实时兴趣捕捉。

  - 关联扫描（associative scan）和秩一 PSD 特征映射提供了一种参数高效的状态放大方法，可迁移到推荐系统的长程用户表征压缩，无需增加 KV cache
  大小即可扩展记忆容量。

  - 论文中的 Triton 融合内核实现（Flash-Attention 风格前向、块状态并行）可作为参考模板，优化现有推荐模型中的注意力层，特别是在 GPU
  上处理超长序列时获得 2×-10× 的吞吐提升。

  - 核特征映射的几何设计思路（Welch 下界、球形码）可用于生成式推荐的 Semantic ID 编码，提升 token 空间的容量与分辨力，缓解生成式推荐中的哈希碰撞问题。'
score: 7
source: arxiv-stat.ML
depth: abstract
---

**动机**：线性注意力承诺常数时间推理，但在关联回忆（associative recall）任务上性能急剧退化，限制了其在大规模语言模型和长上下文场景中的应用。本质原因是线性注意力的特征映射容量不足，无法有效区分海量键值对。

**方法**：将注意力回忆建模为球形打包问题，提出核化线性注意力激活（KATA）框架。核心创新是通过自对偶齐次锥（symmetric cone）从第一性原理导出特征映射，确保非负注意力权重，从而突破线性注意力的容量墙。具体采用秩一正定（PSD）特征，推导出无参数的凸输出门，并利用 Welch 干扰界精确刻画联想记忆容量。在此框架下，可在不增加参数的情况下放大状态空间，并利用球形码在投影维度中支持指数级数量的键。

**实现与实验**：实现两种高效 Triton 内核：闪电注意力风格前向版本达到 FlashAttention-2 的约 1.6 倍吞吐；O(T) 块状态形式在 131k tokens 时达到约 11 倍吞吐。关联扫描将块间递归深度降至 O(log(T/C))，平均吞吐是序列线性注意力基线的 2.4 倍。在长序列多查询关联回忆（MQAR）和重复键覆盖任务上，多个 KATA 变体超越 Gated DeltaNet，在 16 倍分布外序列长度下保持 0.985 的 MQAR 精度，仅需 softmax 注意力四分之一的 KV 缓存条目。340M 参数 LLM 实验揭示了特征依赖的流畅性权衡，并阐明位置编码、delta 规则和衰减门与特征几何的交互方式。
