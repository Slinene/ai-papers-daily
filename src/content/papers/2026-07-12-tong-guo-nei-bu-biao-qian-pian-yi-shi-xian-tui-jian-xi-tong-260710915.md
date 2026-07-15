---
title: Normative Alignment of Recommender Systems via Internal Label Shift
title_zh: 通过内部标签偏移实现推荐系统的规范性对齐
authors:
- Johannes Kruse
- Kasper Lindskow
- Michael Riis Andersen
- Ryotaro Shimizu
- Julian McAuley
- Pierre-Alexandre Mattei
- Jes Frellsen
affiliations:
- JP/Politikens Media Group
- Technical University of Denmark
- University of California San Diego
- Inria, Université Côte d'Azur
- Copenhagen Business School
arxiv_id: '2607.10915'
url: https://arxiv.org/abs/2607.10915
pdf_url: https://arxiv.org/pdf/2607.10915
published: '2026-07-12'
collected: '2026-07-15'
category: RecSys
direction: 推荐系统规范性对齐 · 内部标签偏移
tags:
- Recommender Systems
- Aligned Recommendation
- Label Shift
- Normative Design
- Attribute Distribution
- User Engagement
one_liner: 提出NAILS方法，通过内部标签偏移在不重训模型的情况下使推荐输出属性分布对齐规范性目标，同时保持用户偏好
practical_value: '- 在现有多目标推荐系统上增加重排序层，利用NAILS无需重新训练即可控制推荐结果中物品属性的边际分布，低成本实现类目多样性、品牌均匀性或内容合规等业务目标。

  - 将推荐分数修改问题转化为内部标签偏移问题，在保持用户个性化偏好的前提下，通过调整模型输出的 logits 或概率来满足全局属性约束，可灵活植入排序流程。

  - 方法对用户参与度指标影响极小，适合对用户体验敏感的场景；需要设定目标属性分布，可以结合运营规则、业务指标或算法校准得到。

  - 架构上可解耦推荐模型（保持不变）与规范性对齐模块，便于迭代和A/B测试，适合快速业务适配。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：推荐系统仅优化用户参与度容易忽略公平性、多样性等规范性目标，尤其在新闻、电商场景中需要控制物品属性（如类目、来源）的分布。现有方法往往需要重新训练模型，成本高且易损害用户偏好。

**方法关键点**：
- 将推荐结果对齐问题建模为内部标签偏移（Internal Label Shift）：保持用户-物品的条件概率不变，通过调整物品属性的边际分布来拟合给定的目标分布。
- 在层级分类框架下操作：系统先预测用户对物品的偏好，再借助NAILS模块修正物品得分，使整个推荐列表的属性分布收敛至预设目标，无需修改底层模型。
- 采用校准矩阵（calibration matrix）在推理时对物品打分进行线性变换，理论保证收敛且保持用户排序的相对顺序，计算开销极低。

**关键结果**：在新闻推荐数据集上，NAILS在将类目分布对齐到目标分布的同时，用户参与度（点击、阅读时长）下降不足1%，显著优于其他后处理方法；可灵活适配多种规范性目标分布。
