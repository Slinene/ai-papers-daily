---
title: 'HiSA: Sparsifying the Hidden Dimension of RoPE Attention in LLMs'
title_zh: HiSA：稀疏化 RoPE 注意力的隐藏维度
authors:
- Ambroise Borbely
- Mathieu Salzmann
- Olivier Verscheure
affiliations:
- EPFL, Switzerland
- Swiss Data Science Center, EPFL and ETH Zurich, Switzerland
arxiv_id: '2611.26363'
url: https://arxiv.org/abs/2611.26363
pdf_url: https://arxiv.org/pdf/2611.26363
published: '2026-11-19'
collected: '2026-11-20'
category: LLM
direction: RoPE 注意力 hidden 维度稀疏优化
tags:
- RoPE
- Sparse Attention
- LLM
- Training Efficiency
- Inference Acceleration
- FlashAttention
one_liner: 提出 Hidden Sparse Attention，在 RoPE 隐藏维度静态稀疏化 QK 点积，训练性能不降反升且仅需约 1/3 计算量
practical_value: '- 如果在广告/推荐/搜索里需要自训或微调 LLM（例如 query 理解、文案生成、Agent 决策），HiSA 提供一种无需改变模型架构和参数的无参注意力稀疏化方案，训练时可只用约
  1/3 QK 计算量且效果可能更好，能直接降低训练成本。

  - 在线推理对延迟和显存敏感，HiSA 可加速解码并减少内存占用；同时作者已扩展到 FlashAttention-3 kernel，意味着可实际部署到生产级 Transformer
  服务，对实时推荐/搜索中的 LLM 调用有工程价值。

  - RoPE 隐藏维度部分在 dense attention 中被模型自行抑制，这一发现可作为先验：在设计稀疏注意力或剪枝时，优先考虑隐藏维度而非 token
  维度，可能减少搜索空间并避免额外学习。

  - 其静态、参数化规则由 token 位置决定，不依赖输入，便于硬件优化和确定性行为，适合接入现有训练/推理流水线。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM 注意力对每个 query 和 key 做完整点积，计算与内存开销大；已有稀疏注意力几乎都在 token 维度减少参与计算的 key，本文从 hidden（特征）维度研究 QK 点积能否部分省略。  
**方法**：保留 query、key 投影不变，利用 RoPE 的位置旋转结构，将 Q/K 分解成可省略与保留部分，采用静态、无参数、由 token 位置决定的规则，在隐藏维度做稀疏点积，即 Hidden Sparse Attention (HiSA)。该方法与 token 稀疏正交，且无需额外学习或动态路由。扩展实现到 FlashAttention-3 训练与推理 kernel。  
**结果**：从头训练 LLM 表明，HiSA 只计算约 1/3 QK 乘积时，性能不仅不下降，反而优于完整点积；推理时解码速度提升、内存占用下降。分析显示 dense attention 会学到抑制被 HiSA 丢弃的注意力分数部分，为稀疏规则提供依据。
