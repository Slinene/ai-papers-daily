---
title: 'The Life Cycle of a Massive Activation: Stochastic Birth, Weight-Decay-Driven
  Growth, and Competitive Consolidation'
title_zh: 大规模激活的生命周期：随机诞生、权重衰减驱动的增长与竞争性巩固
authors:
- S. Aaron McClendon
- Jorge Gallego-Feliciano
- Antonios Saravanos
affiliations:
- Aimpoint Digital Labs, Atlanta, GA, USA
- Mistral AI, Paris, FR
- New York University, New York, NY, USA
arxiv_id: '2610.00423'
url: https://arxiv.org/abs/2610.00423
pdf_url: https://arxiv.org/pdf/2610.00423
published: '2026-10-04'
collected: '2026-10-13'
category: Training
direction: Transformer 训练动态 · 激活规模调控
tags:
- massive activations
- attention sinks
- weight decay
- AdamW
- training dynamics
- activation magnitude
one_liner: 揭示 transformer 中 massive activations 由 AdamW 预条件增长与 weight decay 平衡驱动，权重衰减控制其峰值与衰减
practical_value: '- 在微调 LLM 或生成式推荐模型时，若发现 attention sink 激活异常，可通过增大 weight decay 压制峰值；继续预训练时降低
  weight decay 则允许 large activation 继续增长，需结合梯度流稳定性权衡。

  - 监控 residual stream 激活时不要只看单个 channel，应关注 sink token 的 collective RMS：梯度衰减由整体规模决定，单通道指标会误导。

  - 在做量化或 KV cache 优化前，先检查 massive activation 的规模；weight decay 调度可作为训练期控制激活量级的杠杆，避免异常激活导致量化误差或注意力偏差。

  - 对训推一体的推荐/Agent 系统，AdamW 的 weight decay 系数可影响模型激活分布，进而改变推理时 attention sink 强度，需要纳入超参搜索范围。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：Transformer 中 massive activations（残差流坐标的异常大值）与 attention sinks 相关，但其尺度在训练中如何被调控尚不清楚。

**方法关键点**：结合训练轨迹分析与受控训练 continuation；跨随机种子追踪 sink-carrying channels；通过移除或保留 weight decay 的消融；分析 AdamW 预条件梯度增长与 weight decay 的平衡；建立平衡模型。

**关键结果**：sink 通道在早期稳定但跨种子不同，后期向少数冗余载体集中；梯度衰减由 sink token 的 collective RMS 控制，而非单个通道；在峰值附近移除 weight decay 允许全局激活尺度继续上升，保留则导致下降（即使学习率不变）；峰值时间随 λ 近似 log-linear，峰值幅度近似 λ^{-1/2}；AdamW 的预条件可以维持大通道群体对抗 decay，即使原始维持力不足。
