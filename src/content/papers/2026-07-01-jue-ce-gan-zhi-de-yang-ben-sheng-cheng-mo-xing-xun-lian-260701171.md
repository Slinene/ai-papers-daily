---
title: Decision-Aware Training for Sample-Based Generative Models
title_zh: 决策感知的样本生成模型训练
authors:
- Kornelius Raeth
- Nicole Ludwig
affiliations:
- Tübingen AI Center, University of Tübingen
- University of Augsburg
arxiv_id: '2607.01171'
url: https://arxiv.org/abs/2607.01171
pdf_url: https://arxiv.org/pdf/2607.01171
published: '2026-07-01'
collected: '2026-07-05'
category: Other
direction: 决策感知生成模型训练
tags:
- generative models
- decision-aware training
- energy score
- proper scoring rules
- cost-sensitive learning
one_liner: 在能量得分中融入可微决策损失，使生成模型训练直接感知下游决策成本
practical_value: '- 在供应链预测（销量/库存）中，可将缺货成本或过剩成本作为可微决策损失，与能量得分联合训练，提升关键分位数的预测精度，降低业务损失。

  - 动态定价场景下，将利润损失函数嵌入生成式价格分布的优化目标，直接最小化预期决策成本，替代后处理决策优化。

  - 工程实现时，需对非可微的业务损失进行平滑近似（如用SoftMax代替argmax），确保梯度可反向传播；可参考文中对决策损失可微化的设计。

  - 该方法保持概率模型校准性，不仅输出点预测，还保留完整分布，适合风险敏感决策场景，如广告预算分配、促销门槛设定。'
score: 6
source: arxiv-stat.ML
depth: abstract
---

## 动机
概率预测模型（如基于样本的生成模型）普遍使用严格恰当评分规则（如能量得分）训练，但这些规则仅按数据密度分配训练信号，忽视下游决策的成本结构。在有限模型容量下，高密度区域的误差被优先优化，而决策关键的低密度区域可能严重欠拟合，导致高代价错误。

## 方法
提出决策感知训练，将能量得分与一个可微的决策损失加权组合。决策损失直接惩罚基于预测的决策行动所产生的期望成本，形式上仍是恰当评分规则，因此组合损失具有理论合理性。训练时，生成模型输出样本集，通过可微化公式估计决策损失并反向传播，实现端到端优化。

## 结果
在合成任务及两个真实场景（风电合同签约、霜冻保护决策）中验证，方法显著降低了成本敏感区域的决策损失，同时保持了整体概率预测的校准度。相比仅用能量得分训练，组合损失使模型在决策边界附近分配更多容量，实现针对性改进。
