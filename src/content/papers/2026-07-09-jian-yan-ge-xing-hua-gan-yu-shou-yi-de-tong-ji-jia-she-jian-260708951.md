---
title: A Statistical Test for the Benefits of Personalizing Interventions
title_zh: 检验个性化干预收益的统计假设检验
authors:
- Zhaoqi Li
- Emma Brunskill
affiliations:
- Stanford University
arxiv_id: '2607.08951'
url: https://arxiv.org/abs/2607.08951
pdf_url: https://arxiv.org/pdf/2607.08951
published: '2026-07-09'
collected: '2026-07-13'
category: Eval
direction: 个性化决策效果评估统计方法
tags:
- statistical test
- personalization
- policy evaluation
- heterogeneous treatment effects
- recommendation systems
one_liner: 提出一种统计检验，用历史数据评估个性化策略是否优于最佳单一干预，提供严格错误控制
practical_value: '- **线上决策门控**：在用户分群AB实验后，用该检验判断个性化推荐模型（如多臂老虎机、contextual bandit）相比全量最优固定策略是否有统计显著的收益，避免盲目上线复杂模型。

  - **成本收益评估**：在推荐系统迭代中，当个性化引入额外计算或冷启动成本时，检验能基于历史日志数据快速量化收益，辅助工程取舍。

  - **策略退化监控**：在已上线个性化推荐服务中，定期用检验评估个性化增益是否仍显著，若不再拒绝原假设，可能提示策略需更新或用户分布漂移。

  - **离线标杆验证**：在离线评估生成式推荐（如LLM生成item）时，可将其作为统计基线：对比生成式策略与最优固定推荐列表，提供“是否值得部署”的严格统计证据。'
score: 6
source: arxiv-stat.ML
depth: abstract
---

**动机**：个性化干预（如个性化推荐、精准营销）在实践中可能增加成本而不带来实质提升，决策者需要基于历史数据判断个性化是否真正优于最优统一干预。现有方法缺乏严格的统计控制，容易高估个性化收益。

**方法**：提出一种假设检验框架，原假设为“最优单一干预策略不劣于任何个性化策略”。基于半参数效率理论构造检验统计量，在对倾向得分和结果回归进行双鲁棒估计后，统计量具有渐近正态性且在半参数下界意义下方差最小，从而在保证I类错误控制的同时最大化检验功效。检验无需对策略进行具体建模，仅需历史观测数据。

**结果**：在就业培训、抑郁症治疗、教育和推荐系统四个真实数据集上验证，本检验在控制错误率（接近名义α）的同时，比替代方法（如基于值差的重抽样检验）更敏感地检测出个性化效应。在推荐场景实验中，当真实个性化收益存在时，检验能以更小样本量识别出显著差异。
