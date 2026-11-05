---
title: 'Systolic Linear Attention: Co-Designing Tile-Grouped Gated Delta Attention
  for TPUs'
title_zh: 面向 TPU 的 Tile 分组门控 Delta 注意力协同设计
authors:
- Gagik Amirkhanyan
- Nuojin Cheng
affiliations:
- Google
arxiv_id: '2611.06828'
url: https://arxiv.org/abs/2611.06828
pdf_url: https://arxiv.org/pdf/2611.06828
published: '2026-11-04'
collected: '2026-11-05'
category: Training
direction: 线性注意力 TPU 高效训练
tags:
- Linear Attention
- TPU
- Gated DeltaNet
- MoE
- Kernel Fusion
- Training Efficiency
one_liner: 重塑 gated delta attention 以匹配 TPU 256×256 矩阵单元，训练加速 11%–24%
practical_value: '- 若业务在 TPU 上训练基于线性注意力的序列模型（如用户行为长序列编码），可直接借鉴 SLA 的 tile-grouped
  设计：将 decay gate 分组为 4 个 64 通道 tile，key 维度扩到 256，完全用块矩阵乘法完成 chunk solve，避免向量单元瓶颈。

  - 在推荐模型中使用 gated delta attention 时，grouped value heads 的 head sharing 技巧可减少计算量同时保持模型质量，适合降本增效；可尝试在用户序列塔中替换
  softmax attention。

  - 工程实现上，SLA 的单融合 kernel 设计减少了中间显存占用和 launch 开销，对 TPU 等硬件上部署长序列模型尤其重要；即使 GPU 部署也可参考其减少
  kernel 数量的思路。

  - 若业务已用 MoE 架构做超大规模召回或 CTR 模型，SLA 证明线性注意力作为 MoE 内部层可在几乎不损失 perplexity 的前提下显著加速训练，适合大规模稀疏模型迭代。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：Gated-delta linear attention（GDN、KDA、GDN-2）为 GPU 优化，依赖小 tensor-core tiles 与快速向量寄存器；在 TPU 上，256×256 宽 systolic 矩阵单元及较慢向量单元导致矩阵 tile 半空、向量操作成为瓶颈。

**方法关键点**：SLA 围绕矩阵单元重塑 gated delta attention：将 key 宽度扩展到 256 并采用 grouped value heads；将 decay gates 分为四个 64 通道 tile；chunk solve 完全由块矩阵乘积完成，且全部放在一个融合 kernel 中。

**关键结果**：在 TPU v7x 上，SLA-R4 层比开源 Tokamax KDA kernel 快 1.6×–2.5×（精确 chunk inversion 为 1.4×–2.4×），主要源于 head sharing 与 kernel fusion。在 2048-chip TPU v7x 上对 6.5B 至 63.1B 稀疏 MoE 模型预训练，SLA 比 KDA 训练快 11%–24%，相似 perplexity；小规模 matched-seed 实验中 perplexity 略低于 KDA。
