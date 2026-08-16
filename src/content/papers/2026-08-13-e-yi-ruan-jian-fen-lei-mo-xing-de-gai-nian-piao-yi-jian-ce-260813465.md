---
title: Concept Drift Detection and Adaptive Retraining of Malware Classification Models
title_zh: 恶意软件分类模型的概念漂移检测与自适应重训练
authors:
- Christofer Washington Berruz Chungata
- Martin Jurecek
- Katerina Potika
- William B. Andreopoulos
- Mark Stamp
affiliations:
- Department of Computer Science, San Jose State University
- Faculty of Information Technology, Czech Technical University in Prague
arxiv_id: '2608.13465'
url: https://arxiv.org/abs/2608.13465
pdf_url: https://arxiv.org/pdf/2608.13465
published: '2026-08-13'
collected: '2026-08-16'
category: Training
direction: 概念漂移检测与自适应重训练
tags:
- concept drift
- OCSVM
- adaptive retraining
- malware classification
- minibatch k-means
- MMD
one_liner: 用OCSVM等漂移检测触发模型重训练，在精度与周期重训相当下大幅减少重训次数
practical_value: '- 将 OCSVM 作为无监督漂移检测器，监控推荐模型输入特征分布或预测分数分布，超过阈值触发重训练；相比每日/每周定期全量重训，可大幅节省
  GPU/训练资源，同时保持效果。

  - 借鉴三场景对比实验：static（不更新）、periodic（固定周期更新）、drift-aware（检测到漂移才更新），用 Pareto Front 量化精度与训练成本
  trade-off，帮助决定线上模型的更新策略与触发阈值。

  - 生产上可对用户行为序列、商品属性、embedding 统计量（均值/方差/分布）构造特征向量，用 MMD 或 MK-Means 做轻量漂移检测，并与自动训练流水线集成，实现模型自适应更新。

  - 注意：恶意软件漂移模式与电商推荐漂移不完全一致，但“漂移检测 + 事件触发重训”的框架可直接迁移；OCSVM 实际部署需调优核函数与 nu 参数。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：恶意软件分类模型受概念漂移影响严重——攻击者持续修改样本导致数据分布偏移，静态模型性能下降，而周期性全量重训成本高、响应慢。

**方法关键点**：
- 提出基于 One-Class SVM (OCSVM) 的漂移检测方法，并与 Minibatch K-Means (MK-Means)、Maximum Mean Discrepancy (MMD) 对比。
- 使用四种分类模型：MLP、Random Forest、SVM、XGBoost。
- 设计三种场景：static（不重训）、periodic（固定周期重训）、drift-aware（检测到漂移才重训）。
- 在 drift-aware 场景下用 Pareto Front 分析精度与训练效率的权衡。

**关键结果**：三种漂移检测方法均能实现与 periodic 重训相当的分类精度，同时大幅度减少需要重训的模型次数；其中 OCSVM 方案通常优于 MK-Means 和 MMD。结果表明基于漂移检测的按需重训高效且可自动化，能在保持模型性能的同时显著降低训练开销。
