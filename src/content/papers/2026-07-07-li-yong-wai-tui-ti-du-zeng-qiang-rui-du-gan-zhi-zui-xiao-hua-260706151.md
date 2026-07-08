---
title: Leveraging Extragradient for Effective Sharpness-Aware Minimization in Deep
  Learning
title_zh: 利用外推梯度增强锐度感知最小化训练
authors:
- Yao Fu
- Chunxia Zhang
- Junmin Liu
- Yihang Jin
- Haishan Ye
- Yuanao Yang
arxiv_id: '2607.06151'
url: https://arxiv.org/abs/2607.06151
pdf_url: https://arxiv.org/pdf/2607.06151
published: '2026-07-07'
collected: '2026-07-08'
category: Training
direction: 训练优化 · 锐度感知最小化改进
tags:
- Extragradient
- SAM
- Generalization
- Optimizer
- Flat Minima
one_liner: 将外推梯度引入SAM形成EISAM，两步更新提升泛化且降低超参敏感度
practical_value: '- EISAM 可替换现有 SGD/Adam 训练推荐模型，尤其在数据稀疏或长尾场景下，平坦极小值带来的泛化提升可能直接改善冷启动物品的
  AUC 和线上指标。

  - 对扰动半径鲁棒的特性意味着超参调优成本更低，适合大规模工业模型快速迭代；可在召回、粗排等不同阶段复用同一组超参。

  - 两步更新（预测步探索 loss 地形 + 扰动步微调）提供了一种可工程化的模式：在现有框架中可按 batch 交替执行，额外计算开销主要通过梯度累积补偿，易于分布式实现。

  - 当业务模型出现明显过拟合（训练、线上指标背离）时，优先尝试 EISAM，因其不依赖特定架构，可直接融入 CTR 预估、多任务学习等现有训练流程。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

传统优化器（SGD、Adam）收敛至尖锐极小值，导致模型在未见分布上泛化能力不足。SAM 通过小范围扰动寻找平坦极小值，但高度依赖扰动半径这一敏感超参。为此，提出 EISAM，将 extragradient 技术与 SAM 框架结合：先用预测步探查损失曲面的几何结构，再用扰动步沿着平坦方向执行参数更新。这一设计同时继承了外推梯度的稳定性和 SAM 的锐度感知能力。

在 CIFAR-10/100、ImageNet 等基准上，EISAM 在多种架构（ResNet、WideResNet、ViT）上测试准确率一致超越 SGD、Adam 和 SAM，训练效率不因额外前向/反向传播而显著下降。更重要的是，它对扰动半径的敏感性大幅降低，在较大范围内均能保持性能，简化了超参选择。理论分析表明，EISAM 收紧泛化界，引导参数降至曲率更小的平坦区域。该工作为通用深度学习训练提供了更鲁棒、更易用的平坦极小值优化器。
