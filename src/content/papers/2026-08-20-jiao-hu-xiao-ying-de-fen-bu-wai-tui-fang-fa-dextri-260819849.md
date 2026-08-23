---
title: Distributional Extrapolation for Interactions
title_zh: 交互效应的分布外推方法 DExtrI
authors:
- Marin Šola
- Xinwei Shen
- Peter Bühlmann
affiliations:
- Seminar for Statistics, ETH Zürich
- Department of Statistics, University of Washington
arxiv_id: '2608.19849'
url: https://arxiv.org/abs/2608.19849
pdf_url: https://arxiv.org/pdf/2608.19849
published: '2026-08-20'
collected: '2026-08-23'
category: Other
direction: 组合外推与交互效应建模
tags:
- Extrapolation
- Interaction Effects
- Distribution Shift
- Drug Combination
- Hyperparameter Optimization
one_liner: 提出 DExtrI，从仅单变量活跃的训练数据外推多变量组合的交互效应，并给出可行性理论保证
practical_value: '- 推荐/广告中常需预测多策略同时生效的组合效果（如优惠券+置顶+新样式），而训练数据往往只有单策略生效的 A/B 实验。DExtrI
  提供了一种从单变量观测外推组合效应的统计学框架，可直接迁移到营销组合效果预估。

  - 对于特征交互敏感但线上实验昂贵的场景（如排序模型多目标权重、召回通道组合），可借鉴其 axis-aligned 采样策略：只需跑边际参数扫描，再用 DExtrI
  预测联合配置，显著降低实验成本。

  - 其理论保证刻画了“何时组合外推可行”的条件，可帮助判断在哪些业务问题上可以安全地从单变量实验外推到多变量组合，避免盲目用复杂模型外推导致不可靠结论。

  - 方法对分布外组合输入的稳定性有明确建模，对推荐系统在用户/物品特征组合出现长尾或未见组合时的鲁棒性设计有启发，尤其是交互项的结构假设可以简化线上模型的分布外泛化问题。'
score: 6
source: arxiv-stat.ML
depth: abstract
---

动机：药物组合、基因组学、超参数优化等领域，获取完全组合的数据成本极高，训练数据往往只有单变量活跃的轴对齐样本，而测试需要预测多变量同时活跃的交互效应。现代模型在分布外表现不稳定，限制了组合效应预测的可靠性。

方法：提出 DExtrI（Distributional Extrapolation for Interactions），从有限的单变量观测外推交互效应。核心是基于分布外推的回归框架，对交互项的结构进行假设，并给出理论保证刻画何种条件下组合外推可行。与简单模型外推不同，DExtrI 显式利用训练数据轴对齐的性质，对组合输入下的响应分布进行建模。

关键结果：在合成数据和真实数据集上，DExtrI 成功泛化到未见过的协变量组合；应用于药物组合预测和超参数优化，展现出对组合效应的可靠外推能力，相比基线在分布外组合上性能更稳定。
