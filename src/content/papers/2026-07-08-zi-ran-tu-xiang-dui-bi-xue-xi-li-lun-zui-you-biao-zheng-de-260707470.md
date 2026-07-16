---
title: A Theory of Contrastive Learning with Natural Images
title_zh: 自然图像对比学习理论：最优表征的正弦基与白化
authors:
- Antonio Torralba
- Yair Weiss
affiliations:
- CSAIL, MIT
- School of Computer Science and Engineering, Hebrew University of Jerusalem
arxiv_id: '2607.07470'
url: https://arxiv.org/abs/2607.07470
pdf_url: https://arxiv.org/pdf/2607.07470
published: '2026-07-08'
collected: '2026-07-16'
category: Training
direction: 对比学习理论 · 正弦基与白化
tags:
- contrastive learning
- representation theory
- sinusoidal filters
- whitening
- waterfilling
- stationary statistics
one_liner: 证明对比学习最优表征为傅里叶正弦基加部分白化，可用注水算法解析计算
practical_value: '- 推荐系统中常用对比学习训练用户/物品表征，该理论揭示增强变换与最优表征结构的关系，可指导如何设计更适合协同过滤的增强（例如，图像增强等价于频率域的选择性加权，可类比到序列推荐中的
  mask 或裁剪策略）

  - 部分白化作为对比学习隐含的最终投影层，可显式引入到推荐模型的输出层，提升特征的解耦性与判别性，替换简单的 L2 归一化

  - 注水算法直接根据数据功率谱计算最优滤波器权重，该思想可迁移到特征交互建模中，自适应地分配不同频率或阶次交互的权重

  - 虽然对象是视觉，但结论“第一层学习正弦波”暗示对比学习倾向于发现频域结构，这一点可用于解释推荐模型中 Embedding 在对比训练下的收敛特性，辅助排查训练不稳定问题'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：对比学习（Contrastive Learning, CL）在无监督表征学习中取得巨大成功，但其有效性的理论机制尚不清晰。作者希望解释为何简单的图像增强与对比损失能产生可迁移的表征。

**方法关键点**：假设数据集具有平稳统计特性（即图像块统计量平移不变），在给定一系列基本增强（水平翻转、裁剪、颜色抖动等）下，解析求解对比损失的最优表征。推导得出，最优表征可由一个浅层 CNN 实现：第一层卷积核为不同频率的正弦波，随后经过逐点非线性、全局平均池化，最后通过一个线性层执行部分白化（仅去除部分高频分量的相关性）。正弦波的频率选择与权重分配可通过“注水”算法，根据数据集的期望功率谱直接计算。

**关键结果**：在 CIFAR-10、1/f 噪声、Dead Leaves 等合成与真实图像上，SGD 训练的 CNN 确实收敛到上述结构，第一层滤波器呈现正弦模式，输出层近似部分白化。该理论统一了解释了不同增强下对比学习习得表征的共性，并揭示了增强操作的本质是对频域信息的筛选。
