---
title: Decision-Aligned Evaluation of Uncertainty Quantification
title_zh: 决策对齐的不确定性量化评估
authors:
- Annika Schneider
- Tommy Rochussen
- Joshua Stiller
- Vincent Fortuin
affiliations:
- Technical University of Munich
- Helmholtz AI
- MCML
- Konrad Zuse School of Excellence in Reliable AI
- LMU Munich
arxiv_id: '2606.26990'
url: https://arxiv.org/abs/2606.26990
pdf_url: https://arxiv.org/pdf/2606.26990
published: '2026-06-25'
collected: '2026-06-29'
category: Eval
direction: 决策对齐的不确定性评估
tags:
- uncertainty quantification
- decision-alignment
- proper scoring rules
- evaluation metrics
- prior-weighted utility
- UQ evaluation
one_liner: 提出决策对齐准则与先验加权效用度量，使不确定性评估能真正反映下游决策效用
practical_value: '- 在点击率/转化率预估的不确定性评估中，避免仅依赖 NLL 或 ECE，而是直接使用与业务决策（如广告出价、推荐排序）对应的效用函数，构建决策对齐的离线评估指标。

  - 当有业务先验（如商品热度、用户活跃度）时，可将其编码为先验权重，设计先验加权效用度量，使 UQ 模型的选择自动偏向对高频或高价值样本更准确的预测。

  - 在 Agent 或推荐系统的策略学习阶段，用决策对齐的评分规则作为 reward 或验证标准，驱动模型不确定性估计更符合最终线上收益。

  - 工程上，可参考文中的先验加权评分规则实现，只需在现有对数得分基础上乘以由决策先验和效用函数决定的权重，低成本将通用 UQ 评估升级为决策敏感的版本。'
score: 7
source: arxiv-stat.ML
depth: abstract
---

**动机**：当前不确定性量化（UQ）的评估普遍使用负对数似然（NLL）、期望校准误差（ECE）等通用指标，但这些指标往往不反映下游决策的实际效用。好的 NLL 不一定意味着好的决策表现，导致 UQ 研究可能偏离真实应用需求。  
**方法关键点**：
- 提出**决策对齐**准则：一个 UQ 评估指标若与特定决策问题的期望效用序关系一致，则称其对该问题决策对齐。
- 分析发现，常用指标如 NLL、ECE 在很多常见决策场景下（如分类、回归、决策阈值问题）存在不对齐，甚至隐含不合理的先验假设（如极度偏好保守）。
- 提出**先验加权效用度量**（prior-weighted utility metric），属于恰当评分规则家族，将决策问题的效用函数与任务先验结合，构建成**决策对齐**的评估指标。
- 具体形式为：对每个预测分布，计算按先验加权并基于效用函数的期望得分，真实结果则按效用加权。理论证明其与贝叶斯决策理论下的期望效用完全对齐。  
**关键结果**：
- 在合成数据、UCI 回归/分类基准以及真实医疗预测案例中，所提指标始终与最终决策效用（如准确率、收益）高度相关，而 NLL、ECE 等传统指标无此一致性。
- 揭示当前 UQ 评估协议的缺陷，并给出了从通用指标向决策相关评估迁移的原则性方法。
