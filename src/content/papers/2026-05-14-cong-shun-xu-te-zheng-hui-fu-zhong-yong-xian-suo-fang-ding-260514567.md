---
title: 'Scaling Laws from Sequential Feature Recovery: A Solvable Hierarchical Model'
title_zh: 从顺序特征恢复中涌现缩放定律：一个可解的分层模型
authors:
- Arie Wortsman-Zurich
- Hugo Tabanelli
- Yatin Dandi
- Florent Krzakala
- Bruno Loureiro
affiliations:
- Ecole Normale Supérieure (PSL & CNRS)
- École Polytechnique Fédérale de Lausanne (EPFL)
arxiv_id: '2605.14567'
url: https://arxiv.org/abs/2605.14567
pdf_url: https://arxiv.org/pdf/2605.14567
published: '2026-05-14'
collected: '2026-05-17'
category: Training
direction: 特征学习顺序与缩放定律的理论解释
tags:
- scaling laws
- feature learning
- hierarchical model
- spectral algorithm
- random matrix theory
- power law
one_liner: 揭示多层网络如何通过顺序恢复不同强度的潜在组合特征来产生幂律缩放定律
practical_value: '- 推荐系统的特征重要度设计：可借鉴分层组合特征的幂律权重先验，在特征工程中明确区分强/弱特征，指导特征选择和样本分配。

  - 分阶段训练策略：在电商多模态模型中，可按特征强度顺序逐步引入训练目标，先用强特征快速收敛，再逐步学习弱特征，可能提升样本效率。

  - Agent多智体中的层次规划：分层恢复的理念可迁移至任务分解，先将简单子任务习得，再顺序攻克复杂子任务，形成由易到难的学习序列。

  - 理论启发：为推荐模型（如生成式推荐）中的深层次Semantic ID结构提供了新的分析视角，表明层级表示可能自然导致缩放行为。'
score: 6
source: arxiv-stat.ML
depth: abstract
---

**动机**：神经网络的经验缩放定律缺乏基于特征学习的理论解释。现有理论多依赖线性化或核模型，无法刻画深层网络中特征如何被顺序发现，以及如何产生平滑的幂律误差衰减。

**方法**：构建一个高维分层目标函数，它由多个不同强度的潜在组合特征叠加，特征权重按幂律衰减。提出逐层谱算法，每层利用随机矩阵理论精准定位一个特征方向的恢复阈值。通过解析扰动分析（resolvent-based perturbation），证明了特征恢复存在尖利的相变：强特征在极小样本量下即可被检测，弱特征需更多数据。将各阈值聚合后，推导出预测误差的显式幂律衰减公式。

**关键结果**：
- 从理论证明和数值实验展示顺序特征恢复：特征根据强度依次出现，临界样本量由特征权重决定。
- 误差缩放为$n^{-\beta}$，指数$\beta$由特征权重衰减速度决定。
- 相比非自适应的浅层核方法，分层谱算法显著提升缩放指数。
- 有限样本下相变平滑，但仍保持清晰的分离现象。
