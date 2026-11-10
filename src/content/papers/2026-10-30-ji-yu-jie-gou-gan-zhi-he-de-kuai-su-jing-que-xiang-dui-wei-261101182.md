---
title: Fast and Exact Relative-Position Attention via Structure-Aware Kernels
title_zh: 基于结构感知核的快速精确相对位置注意力
authors:
- Delyan Boychev
- Ivo Petrov
- Dimitar I. Dimitrov
arxiv_id: '2611.01182'
url: https://arxiv.org/abs/2611.01182
pdf_url: https://arxiv.org/pdf/2611.01182
published: '2026-10-30'
collected: '2026-11-10'
category: Training
direction: Transformer 注意力 kernel 优化
tags:
- relative-position attention
- FlashAttention
- Triton kernel
- long-context
- memory efficiency
- attention optimization
one_liner: 提出将加性相对位置项精确融入 FlashAttention 分块计算的 Triton kernel，大幅加速并降显存
practical_value: '- 若业务中的 Transformer 序列模型使用了相对位置/时间间隔偏置（如用户行为序列、长文档、音频），可直接采用该 Triton
  kernel 替换 naive 实现，在长序列场景获得 2-6× 加速和 50-100× 显存降低，支持更长上下文。

  - 自定义 attention bias 时，可借鉴 offset-aware tiling 和 offset-based gradient sharding：按位置偏移分块，避免
  materialize 完整的 pairwise 偏置矩阵，并在反向传播中消除 atomic contention，对电商点击序列中时间衰减、位置间隔等结构先验的融合很有参考价值。

  - 在 LLM/Agent 推理和训练中，如果模型采用相对位置注意力而非 RoPE，该 kernel 可作为 drop-in 加速组件集成到 FlashAttention
  变体，尤其适合需要处理长 prompt 或长对话历史的场景。

  - 该方法统一支持多种相对位置注意力机制，说明可以抽象出通用的结构感知算子，将业务中反复出现的注意力偏置逻辑沉淀为高效 kernel，减少重复开发。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：相对位置注意力机制在语音、视觉等架构中常优于 RoPE，但其成对偏移依赖的计算/查表难以融入 fused attention kernel，导致显存、带宽和计算开销随序列长度急剧增长。

**方法关键点**：提出一种精确注意力算法，把加性相对位置项嵌入 FlashAttention 风格的分块计算。三个核心设计：
- offset-aware tiling：按位置偏移组织 tile，避免冗余索引和访存；
- 只计算必要的 key/query-relation 乘积，并在 forward 和 backward 阶段跨 token pair 复用，减少重复计算；
- 基于 offset 的梯度分片与聚合，消除原子竞争。
实现为统一 Triton kernel，可支持多种相对位置注意力机制。

**关键结果**：在 8K token 序列上，相比各机制最强基线，前向加速 1.8-6.4×，反向加速 2.0-21×；峰值显存前向最多降低 2.9-128×，反向最多降低 1.4-54×。端到端长上下文语音转录速度提升 1.8×，显存占用减少 2.4×。
