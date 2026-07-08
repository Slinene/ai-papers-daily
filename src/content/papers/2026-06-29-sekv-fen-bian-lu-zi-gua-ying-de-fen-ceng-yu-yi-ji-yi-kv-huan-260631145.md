---
title: 'SeKV: Resolution-Adaptive KV Cache with Hierarchical Semantic Memory for Long-Context
  LLM Inference'
title_zh: SeKV：分辨率自适应的分层语义记忆 KV 缓存
authors:
- Amirhossein Abaskohi
- Giuseppe Carenini
- Peter West
- Yuhang He
affiliations:
- University of British Columbia
- Microsoft Research
arxiv_id: '2606.31145'
url: https://arxiv.org/abs/2606.31145
pdf_url: https://arxiv.org/pdf/2606.31145
published: '2026-06-29'
collected: '2026-07-08'
category: LLM
direction: 长上下文推理 · KV 缓存压缩
tags:
- KV cache
- semantic compression
- long-context
- memory hierarchy
- zoom-in
- SVD
one_liner: 用熵引导语义分段 + GPU-CPU 分层存储 + 按需 zoom-in 实现长上下文 KV 缓存压缩，避免丢弃信息
practical_value: '- **长序列建模内存优化**：电商推荐中用户行为序列可能很长，可借鉴语义分组与 GPU-CPU 分层存储思路，将高频访问的抽象摘要保留在
  GPU，细节离线存储在 CPU，按需加载，减少线上显存压力。

  - **按需检索历史细节**：在 Agent 长期记忆或个性化对话中，当需要回溯具体 token 级信息时，zoom-in 机制可选择性展开相关片段，避免全量解压，适合精准检索。

  - **低成本适配方案**：冻结主模型，仅训练少量参数（0.05%）即可实现长上下文压缩，对业务快速实验友好，可将该范式用于微调推荐模型的长期依赖建模。

  - **熵引导分段**：利用注意力熵判断语义边界，对用户行为序列的时间切分或会话分割有启发，可尝试用于动态构建更具语义一致性的行为子序列。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM 在长上下文推理时，KV 缓存大小随序列长度线性增长，成为 GPU 内存瓶颈。现有压缩方法要么直接丢弃 token 损失信息，要么在 prefill 阶段固定压缩决策，无法在生成过程中按需恢复 token 级细节。

**方法**：提出 SeKV，一种分辨率自适应的语义 KV 缓存。首先，基于注意力熵将上下文分割为语义跨度，形成树状结构。每个跨度在 GPU 保留一个轻量级摘要向量用于粗粒度路由，在 CPU 存储低秩 SVD 基用于细粒度重建。解码时，一个训练的 zoom-in 机制根据 query 相关性选择性地展开跨度，从 CPU 取回低秩矩阵并重建 token 级 KV，实现按需高精度检索，全程无需在 GPU 落盘完整 KV 缓存。核心 LLM 完全冻结，仅额外训练不到 0.05% 的参数。

**结果**：在四个长上下文基准上，SeKV 比最强语义压缩基线平均提升 5.9%（如 LongBench 上从 41.6 到 43.8）。在 128K 上下文下，GPU 内存使用较全 KV 缓存减少 53.3%，同时保持竞争力性能。
