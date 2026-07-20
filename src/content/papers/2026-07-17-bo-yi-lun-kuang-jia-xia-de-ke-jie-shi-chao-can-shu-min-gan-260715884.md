---
title: Which Hyperparameters Matter? A Game-Theoretic Framework for Interpretable
  Hyperparameter Sensitivity Analysis
title_zh: 博弈论框架下的可解释超参数敏感性分析
authors:
- Nyi Nyi Aung
- Heepeom Shin
- Abigail Lawlor
- Adrian Stein
affiliations:
- Louisiana State University
arxiv_id: '2607.15884'
url: https://arxiv.org/abs/2607.15884
pdf_url: https://arxiv.org/pdf/2607.15884
published: '2026-07-17'
collected: '2026-07-20'
category: Training
direction: 超参数重要性分析 · 博弈论
tags:
- Hyperparameter Sensitivity
- Shapley Effects
- Pareto Front
- Multi-Objective Learning
- Game Theory
- Model Evaluation
one_liner: 用 Shapley 效应与 Pareto 前沿分析多目标场景下超参数对各目标的影响，识别关键超参数以缩小搜索空间
practical_value: '- **超参数重要性排序**：在训练 CTR/CVR 模型前，先用少量样本计算每个超参数的 Shapley 效应，快速锁定对关键指标（如
  AUC、LogLoss）真正敏感的参数，避免全量 grid search 浪费资源。

  - **多目标权衡可视化**：对于同时优化点击率与转化率的推荐模型，利用 Pareto 前沿分析可直观看到不同超参配置在双目标上的 trade-off，辅助业务决策（例如选择偏重
  CVR 的配置）。

  - **早期模型评估**：在模型开发初期，通过 Pareto 前沿分布判断当前超参空间是否已接近有效边界，若远离前沿则考虑重构搜索空间或更换架构，减少无效迭代。

  - **AutoML 流程增强**：可将该框架嵌入现有 HPO 流水线，在贝叶斯优化前先运行敏感性分析，自动剔除低影响超参数，提升搜索效率。'
score: 6
source: arxiv-stat.ML
depth: abstract
---

**动机**：深度模型超参数调优成本极高，黑盒优化方法（如贝叶斯优化）虽有效但缺乏可解释性，无法告知哪些超参数真正关键，导致冗余搜索。

**方法关键点**：将超参数分析建模为合作博弈，每个超参数视为玩家，使用 Shapley 效应（全局敏感性分析）量化其对不同目标（如准确率、参数量）的边际贡献，并与 Pareto 前沿结合，识别有效配置并支持早期模型评估。Shapley 效应通过所有可能子集的边际贡献均值计算，能公平分配每个超参数的重要性；Pareto 前沿则展示多目标下的非支配配置，揭示超参数间的交互效应。

**结果**：在三个不同领域的神经网络架构上验证，该框架能清晰指出哪些超参数对特定目标影响最大，帮助缩小搜索空间，并为多目标权衡提供直观解释，指导后续优化方向。
