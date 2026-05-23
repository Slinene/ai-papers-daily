---
title: Quantifying Hyperparameter Transfer and the Importance of Embedding Layer Learning
  Rate
title_zh: 量化超参数迁移与嵌入层学习率的重要性
authors:
- Dayal Singh Kalra
- Maissam Barkeshli
arxiv_id: '2605.21486'
url: https://arxiv.org/abs/2605.21486
pdf_url: https://arxiv.org/pdf/2605.21486
published: '2026-05-20'
collected: '2026-05-23'
category: Training
direction: 训练超参数迁移与μP
tags:
- Hyperparameter Transfer
- μP
- Embedding Learning Rate
- Scaling Laws
- AdamW
one_liner: 揭示μP优于标准参数化的关键在于嵌入层学习率，提出三指标量化超参数迁移质量
practical_value: '- 在 AdamW 训练中，若不想完整迁移到 μP，可直接将嵌入层学习率相对于隐藏层放大（例如按宽度比例），即可获得类似 μP
  的训练稳定性和超参数迁移效果，对推荐模型中的大嵌入表尤其适用。

  - 评估超参数迁移时，可使用文中提出的三个指标：缩放律拟合优度、外推误差鲁棒性、参数化带来的渐近损失惩罚，为自己的 scaling 策略建立量化基准。

  - 固定 tokens/参数比时，慎用权重衰减：虽能改善缩放律拟合，但会降低外推鲁棒性，可能需在 loss landscape 平滑性与迁移可靠性间权衡。

  - 发现嵌入层学习率瓶颈后，可针对性地在混合精度训练或分层学习率设置中，为嵌入参数分配更高学习率，避免训练初期的不稳定。'
score: 7
source: arxiv-stat.ML
depth: abstract
---

动机：大模型训练中超参数调优成本巨大，超参数迁移通过小尺度实验外推大尺度最优超参数至关重要。μP 虽在实践中被证实有利于学习率迁移，但现有理论解释不足。

方法：首先提出量化超参数迁移的三个指标：(1) 缩放律拟合质量（决定系数 R²）；(2) 外推误差鲁棒性（小尺度到目标尺度的泛化误差）；(3) 参数化带来的渐近损失惩罚（与最优可能损失的差距）。随后在 Transformer 语言模型上系统消融 AdamW 训练中 μP 与标准参数化（SP）的差异来源。

关键发现：μP 相对于 SP 的优势几乎完全源于**嵌入层学习率**的设定。在 SP 中，默认学习率对嵌入层过低，成为训练瓶颈，引发梯度峰度剧烈波动、损失尖峰等不稳定性；将嵌入层学习率增大至宽度倍数（与 μP 一致）即可消除不稳定，且超参数迁移表现与 μP 持平。此外，权重衰减改善了 scaling law 拟合质量，但在固定 tokens/参数比时损害了外推鲁棒性。

结果：在 1.2 亿至 17 亿参数模型上，修正嵌入学习率的 SP（SP+LR）在损失缩放曲线、外推准确度上均与 μP 相当，说明 μP 的迁移效果可被简单技巧复现。这为理解 μP 提供了新视角，并给出了实用的训练配置建议。
