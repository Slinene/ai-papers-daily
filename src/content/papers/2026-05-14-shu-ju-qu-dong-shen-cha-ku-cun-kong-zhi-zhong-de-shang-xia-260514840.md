---
title: In-Context Learning for Data-Driven Censored Inventory Control
title_zh: 数据驱动审查库存控制中的上下文学习
authors:
- Sohom Mukherjee
- Anh-Duy Pham
- Richard Pibernik
- Yunbei Xu
affiliations:
- Julius-Maximilians-Universität Würzburg
- Zaragoza Logistics Center
- National University of Singapore
arxiv_id: '2605.14840'
url: https://arxiv.org/abs/2605.14840
pdf_url: https://arxiv.org/pdf/2605.14840
published: '2026-05-14'
collected: '2026-05-17'
category: Other
direction: 库存控制 · 上下文生成式决策
tags:
- in-context learning
- generative model
- inventory control
- censored demand
- Bayesian regret
- normalizing flow
one_liner: 提出上下文生成式后验采样，用离线元训练+在线自回归生成解决审查需求下的库存决策
practical_value: '- 电商库存管理中常面临需求审查（缺货后未知真实需求），可借鉴ICGPS范式：离线用历史数据训练生成模型（如Time Series
  Transformer），在线进行上下文条件采样，实现稳健订货决策。

  - ChronosFlow的架构设计值得关注：冻结预训练时序Transformer作为主干，仅训练轻量归一化流头，既保留预训练知识又实现快速审查一致性采样；类似思路可用于推荐系统中缺失反馈的生成（如未曝光样本的CTR补全）。

  - 理论表明，只要覆盖性假设成立，离线预测质量能保证在线性能，为用离线数据训练生成模型并安全部署到在线决策提供了依据，可推广到其他受审查反馈影响的运营优化问题。

  - 对于推荐场景中的决策依赖审查（如用户只看到且点击被推荐物品），可将未观测反馈视为审查问题，用上下文生成模型补全后做bandit优化，替代传统Thompson
  Sampling或UCB。'
score: 6
source: arxiv-stat.ML
depth: abstract
---

**动机**：库存控制中需求审查（如报童问题，订单量限制需求观测）使传统参数化Thompson Sampling在先验失配时脆弱，而离线插补方法难以迁移到在线学习。需一种结合离线训练与在线适应的方法。

**方法**：提出In-Context Generative Posterior Sampling (ICGPS)，利用现代生成模型：离线元训练学习潜在需求完成核，在线部署时通过上下文自回归生成后验样本，做出决策。理论上，ICGPS的贝叶斯后悔 ≤ 理想TS后悔 + O(√T·完成不匹配的平方根)，且完成不匹配受控于离线预测质量，实现离线到在线的性能迁移。针对报童问题，将审查反馈约化为bandit凸优化反馈，得到次线性贝叶斯后悔。实践上实现ChronosFlow架构：冻结预训练时序Transformer主干，附加可训练条件归一化流头，实现快速审查一致性采样。

**关键结果**：ChronosFlow-ICGPS在基准实验中与正确指定TS表现相当，显著优于Myopic和UCB式基线，对先验失配和分布偏移鲁棒；在真实SuperStore数据集上，特别是重审查条件下表现突出。
