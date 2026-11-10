---
title: 'KiteNorm: Variance Regularisation for Stable and Scalable Post-LN Transformers'
title_zh: KiteNorm：用于稳定可扩展 Post-LN Transformer 的方差正则化
authors:
- Leon A. Trochelmann
- Sajad Movahedi
- Shiwei Liu
- Antonio Orvieto
affiliations:
- ELLIS Institute Tübingen
- MPI for Intelligent Systems
- Tübingen AI Center
arxiv_id: '2611.12729'
url: https://arxiv.org/abs/2611.12729
pdf_url: https://arxiv.org/pdf/2611.12729
published: '2026-11-09'
collected: '2026-11-10'
category: Training
direction: Post-LN Transformer 稳定训练
tags:
- Post-LN
- Variance Regularisation
- Transformer
- Training Stability
- Scaling Laws
one_liner: 提出 KiteNorm，通过约束隐状态方差并结合残差缩放与可学习双归一化，使 Post-LN Transformer 稳定扩展到 1.3B 参数并优于
  Pre-LN 基线
practical_value: '- 自研深度 Transformer（如用户行为序列编码、多模态塔）时，可试验用 Post-LN + variance 正则化替代
  Pre-LN，显式控制 hidden-state 方差上界，避免梯度消失与 rank collapse，同时获得更好的参数效率。

  - 借鉴 scalarised double-normalisation：对 skip 和 residual 分支分别学习缩放系数，可作为多路信息融合的通用组件，尤其在电商多域/多任务模型中分别调节子模块贡献。

  - 将 hidden state variance 与 rank 指标纳入训练监控，当 variance 异常增长时启用 KiteNorm 类正则或减小 LR，作为训练崩溃的早期预警。

  - 论文的 scaling laws 结论为采用 Post-LN 类架构提供了新证据，对需要深层网络或大规模训练预算的团队有参考价值。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：Post-LN Transformers 因难以扩展到大规模深度而实际采用有限，现有稳定化方法侧重改善初始化条件，但在大学习率下稳定性仍差，且在 decoder-only 设定中未能超越强 Pre-LN 基线。

**方法关键点**：KiteNorm 通过约束隐状态方差来稳定 Post-LN 训练，动机来自 LayerNorm Jacobian 的界——方差增长会导致梯度消失，并与 rank collapse 相关。具体做法：结合 residual scaling 与 variance regularisation，并使用标量化 double-normalisation 为 skip 和 residual 分支分别提供可学习 scale，从而在整个训练过程中保持稳定性。

**关键结果**：在 decoder-only Transformer 上扩展到 1.3B 参数，KiteNorm 提升训练稳定性，并在各自最优学习率下超越领先基线；scaling laws 显示 KiteNorm 在 depth、width、batch size 和 training budget 上均占优；消融实验表明每个组件对整体稳定性和性能增益都是必要的。
