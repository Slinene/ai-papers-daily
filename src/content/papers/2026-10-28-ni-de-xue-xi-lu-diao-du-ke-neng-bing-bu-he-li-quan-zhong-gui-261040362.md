---
title: 'Your LR Schedule May Not Be Principled: Effective Learning Rate Scheduling
  in Weight-Normalized Training'
title_zh: 你的学习率调度可能并不合理：权重归一化训练中的有效学习率调度
authors:
- Qifan Yu
- Xinyu Ma
- Xingyan Bin
- Di He
affiliations:
- ByteDance Seed
- Peking University
arxiv_id: '2610.40362'
url: https://arxiv.org/abs/2610.40362
pdf_url: https://arxiv.org/pdf/2610.40362
published: '2026-10-28'
collected: '2026-10-30'
category: Training
direction: 大模型预训练优化 · Effective LR
tags:
- LLM pretraining
- weight normalization
- effective learning rate
- learning rate schedule
- MoE
- optimization
one_liner: 证明 WN 训练增益主要来自有效学习率轨迹，提出 AIR 调度，在 128B MoE 预训练上比 cosine 降损约 0.01
practical_value: '- 若你在 LLM4Rec / 生成式推荐模型预训练中采用 weight normalization 或固定范数约束，应把 LR
  schedule 设计对象从 nominal LR 切换到 effective LR，否则会错失 WN 的降损收益。

  - 工程上可直接用 AIR 替代 cosine：用 affine 修正 1/√t 衰减以匹配预设 peak/terminal LR，在 128B MoE 实验中比
  cosine 的 terminal training loss 低约 0.01，且超参鲁棒性更好，适合线上预训练 pipeline 快速替换。

  - 在优化器或训练约束切换（如 WN ↔ WD）时，保持相同 ELR 轨迹可复现训练动态，便于做 infra 对齐和消融实验，减少重新调参成本。

  - 优先优化 late-stage LR schedule：早期 LR 选择对最终损失影响较弱，晚期 ELR 调度是主要收益来源；调参资源应集中在后期 schedule
  上。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**  
Weight-normalized (WN) training 作为 weight decay (WD) 的替代，近期报告显著预训练损失改善，但其增益来源不明；且在相同 LR schedule 下，WN 与 WD 训练动态差异很大。

**方法关键点**  
作者证明 WN 的增益主要来自其诱导的 effective learning rate (ELR) 轨迹，而非归一化本身；匹配 ELR 轨迹后，WN 与 WD 的训练损失动态几乎重合。因此 schedule 设计应面向 ELR 而非名义 LR。基于此提出 AIR (Affine Inverse-square-Root decay)：将理论推导的 1/√t 衰减与 affine 修正结合，在有限训练范围内满足预设的峰值与终端 LR。进一步发现 late-stage ELR scheduling 是增益的关键来源，共享后期 schedule 会削弱早期 LR 选择的影响。

**关键结果**  
在 128B-token Mixture-of-Experts 预训练中，AIR 在训练损失、下游性能和超参鲁棒性上均优于 cosine 等候选 schedule；在 matched cumulative LR 条件下，terminal training loss 比 cosine 降低约 0.01。将相同 ELR 轨迹应用于 WD 能复现对应训练动态，说明 ELR 是通用的、有原则的调度设计对象。
