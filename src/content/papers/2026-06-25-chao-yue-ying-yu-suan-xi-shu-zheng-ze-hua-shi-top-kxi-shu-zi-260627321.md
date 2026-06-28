---
title: 'Beyond the Hard Budget: Sparsity Regularizers for More Interpretable Top-k
  Sparse Autoencoders'
title_zh: 超越硬预算：稀疏正则化使Top-k稀疏自编码器更具可解释性
authors:
- Nathanaël Jacquier
- Maria Vakalopoulou
- Mahdi S. Hosseini
affiliations:
- Université Paris-Saclay, CentraleSupélec, France
- Concordia University, Montreal, Canada
- Mila–Quebec AI Institute, Montreal, Canada
- Gustave Roussy, INSERM, Cancer Data Science Unit, France
arxiv_id: '2606.27321'
url: https://arxiv.org/abs/2606.27321
pdf_url: https://arxiv.org/pdf/2606.27321
published: '2026-06-25'
collected: '2026-06-28'
category: Training
direction: 自编码器 · 稀疏正则化
tags:
- sparse autoencoders
- sparsity regularization
- monosemanticity
- Top-k
- interpretability
- vision foundation models
one_liner: 为Top-k稀疏自编码器引入L1和L1/L2正则化，在不损失重建质量下提升特征单语义性
practical_value: '- 若在推荐模型中使用稀疏自编码器学习可解释的用户/物品表示，可借鉴其 L1/L2 软正则化，使特征更聚焦、单语义性更强，提升表示的可解释性。

  - 硬稀疏（Top-k）与软正则化结合的思想可迁移至其他需稀疏约束的场景，如注意力头的稀疏化或特征选择，避免固定预算带来的过拟合。

  - “仅对批内活跃单元施加正则”的技巧，在工程上可降低计算开销，适用于大规模推荐模型训练中稀疏约束的设计。

  - L1/L2 正则化使信息集中到更少隐变量，增强模型对推理时稀疏度变化的鲁棒性，有助于在生产环境中动态调整稀疏预算而不严重退化。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：Top-k 稀疏自编码器（SAE）已成为视觉基础模型可解释性的主流工具，但其硬性保留前 k 个活跃隐变量的做法存在缺陷：固定预算 k 不随输入复杂度变化，且易过拟合到训练时的 k 值。早期 SAE 使用的 L1 惩罚存在收缩偏差等弊端，但 Top-k SAE 完全摒弃了显式正则化。本文旨在探索硬架构稀疏与软正则化能否互补。

**方法关键点**：提出两种兼容 Top-k 结构的稀疏正则化器，均作用在 Top-k 选择前的激活值上：1) 对未被选中的单元施加 L1 惩罚，抑制噪声激活；2) 尺度不变的 L1/L2 比率惩罚，促使编码集中在更少的有效单元上。两种惩罚仅作用于“批内活跃单元”（即批次内至少被 Top-k 选中一次的单元），避免对全字典施加无差别压力。

**关键结果**：在两个数据集、三个视觉基础模型及不同 k 值下，两种正则化器均一致提升单语义性指标，且重建质量无损。L1/L2 正则化尤其突出，它将信息压缩到更少的隐变量中，使重建对推理时改变 k 的鲁棒性显著增强，并提升了在小 k 下的线性探测准确率。核心发现是硬稀疏与软稀疏正则化并非互斥，而是互补。
