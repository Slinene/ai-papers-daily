---
title: Adaptive Bayesian Online Learning via Expert Aggregation
title_zh: 自适应贝叶斯在线学习专家聚合方法
authors:
- Jungbin Jun
- Ilsang Ohn
affiliations:
- Inha University
arxiv_id: '2607.20239'
url: https://arxiv.org/abs/2607.20239
pdf_url: https://arxiv.org/pdf/2607.20239
published: '2026-07-22'
collected: '2026-07-26'
category: Other
direction: 在线贝叶斯专家聚合自适应预测
tags:
- Bayesian online learning
- expert aggregation
- adaptive prediction
- conformal inference
- Gaussian processes
one_liner: 将不同超参的贝叶斯更新规则视为专家并在线聚合，实现自适应预测，无需预选最佳模型
practical_value: '- 在推荐系统的在线学习环境中，可对多组贝叶斯模型（不同学习率、先验）进行动态加权，自动适应数据分布变化，减少离线调参成本

  - 将不同探索策略（如UCB、Thompson采样）视为专家进行聚合，能在线平衡探索与利用，适合广告出价或冷启动场景

  - 提供了带有保证的置信区间（conformal inference），可用于推荐结果的不确定性量化，辅助下游决策（如是否向用户展示低置信度内容）

  - Agent多智体协作中，各Agent的预测可作为专家，聚合后提升整体系统的鲁棒性，避免单个模型失效'
score: 6
source: arxiv-stat.ML
depth: abstract
---

**动机**：贝叶斯在线学习在流数据上能估计不确定性，但性能高度依赖学习率、先验分布、变分族等选择，这些通常需在数据流开始前固定。**方法关键点**：将每个候选贝叶斯更新规则视为一个专家，基于累积预测损失在线聚合这些专家，使聚合后的预测在事后与最佳专家竞争。聚合代价由每轮专家性能评估方式决定。**关键结果**：在在线 conformal inference 中，得到了平滑贝叶斯版的自适应 conformal inference，保证长期随机化覆盖；在高斯过程回归中，给出了累积预测 KL 风险的神谕不等式，并能自适应未知 Hölder 平滑度（直至对数因子）。实验表明聚合策略无需 oracle 选择，能自动追踪表现最强的专家。
