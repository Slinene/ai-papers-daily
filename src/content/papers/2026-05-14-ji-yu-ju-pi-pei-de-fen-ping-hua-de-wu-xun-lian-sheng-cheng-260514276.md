---
title: Training-Free Generative Sampling via Moment-Matched Score Smoothing
title_zh: 基于矩匹配得分平滑的无训练生成采样
authors:
- Zhenyu Yao
- Daniel Paulin
affiliations:
- College of Computing and Data Science, Nanyang Technological University
arxiv_id: '2605.14276'
url: https://arxiv.org/abs/2605.14276
pdf_url: https://arxiv.org/pdf/2605.14276
published: '2026-05-14'
collected: '2026-05-17'
category: GenRec
direction: 训练自由生成采样 · 矩匹配分数平滑
tags:
- diffusion models
- score matching
- training-free
- Langevin dynamics
- moment matching
- generative sampling
one_liner: 提出一种无训练的交互粒子采样器MM-SOLD，通过矩匹配和分数平滑在CPU上生成高质量样本
practical_value: '- **无需训练神经网络的快速生成**：可在CPU上直接应用，避免昂贵的扩散模型训练，适用于电商推荐中低资源或快速原型场景，如生成候选
  item 嵌入或用户行为序列。

  - **矩匹配保证分布一致性**：通过强制样本均值与协方差匹配训练数据经验矩，能保持关键统计特性，可用于推荐系统的数据增强或生成符合业务指标的合成数据。

  - **交互粒子系统实现多样性**：粒子交互机制天然促进样本多样性，避免模式坍塌，这对生成推荐中探索多样化 item 表示有借鉴意义。

  - **方法可扩展至潜在空间**：已展示在VAE潜在空间上生成图像，类似思路可用于推荐中的离散 token 生成或 Semantic ID 的低维表示采样。'
score: 6
source: arxiv-stat.ML
depth: abstract
---

**动机**：扩散模型训练代价高昂，而直接使用经验分数匹配的闭式解会导致样本记忆而非泛化。现有工作表明，分数匹配隐式平滑了经验分数，促进了泛化。本文探索如何在不训练神经网络的情况下，利用分数平滑和矩约束实现高质量生成。

**方法**：提出矩匹配分数平滑过阻尼朗之万动力学（MM-SOLD），一种无训练的交互粒子采样器。在采样过程中，粒子遵循分数平滑的朗之万方程演化，同时通过指数倾斜强制样本的经验均值和协方差与训练数据一致。理论证明，当粒子数量趋于无穷时，经验密度收敛到确定性极限，其一粒子边缘分布为指数倾斜的吉布斯-玻尔兹曼分布，精确匹配数据矩。

**关键结果**：在2D分布和潜在空间图像生成实验中，MM-SOLD仅用CPU即可快速生成样本，其保真度（FID）和多样性（召回率）与需要训练的神经扩散基线相当。方法无需反向过程，收敛快，鲁棒性强，在少步采样下已有竞争力。
