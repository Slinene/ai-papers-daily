---
title: 'Steering Geometry: Validating Human Value Geometry in LLM Steering Space'
title_zh: 引导几何：验证LLM引导空间中的人类价值几何
authors:
- Mohammad Mahdi Abootorabi
- Armin Saghafian
- Ali Bazshoushtari
- Hamid Rezaei
- EunJeong Hwang
- Vered Shwartz
- Parvin Mousavi
- Purang Abolmaesumi
affiliations:
- University of British Columbia
- Vector Institute for AI
- Queen's University
arxiv_id: '2609.06289'
url: https://arxiv.org/abs/2609.06289
pdf_url: https://arxiv.org/pdf/2609.06289
published: '2026-09-04'
collected: '2026-09-10'
category: LLM
direction: 激活引导几何验证与对齐
tags:
- activation steering
- human values
- geometry
- alignment
- interpretability
one_liner: 分布驱动激活引导向量能恢复人类价值观理论拓扑，而行为中心方法几何不一致
practical_value: '- 若业务使用 activation steering 控制推荐文案/对话语气，优先采用分布驱动方法（CAA、SphericalSteer、ODESteer），其向量几何与人类价值结构一致，跨
  prompt 迁移更稳定，比行为中心方法（COLD-Steer、BiPO）更适合做可控生成。

  - 几何保真度随模型规模提升但在指令调优后下降，若需要在电商场景中注入价值观维度（如环保、价格敏感），可考虑在基础模型层提取 steering vectors
  或对指令模型做补偿修正。

  - 文中 26K 样本、20 类价值观 benchmark 可复用或改造成电商偏好维度评测集，用于评估 LLM 生成推荐解释时是否忠实体现目标偏好。

  - 跨价值迁移结论提示：引导一个价值会自动提升兼容价值、抑制对立价值，可用于多目标推荐文案联动控制，但需注意对立维度可能被误伤，需要精细调节。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：activation steering 被当作 RLHF/DPO 的轻量推理时替代方案，但以往只在孤立行为上验证，不清楚 steering vectors 编码的是连贯语义结构还是行为特定捷径。论文探究 LLM 引导向量的潜几何是否遵循人类价值观理论。

**方法关键点**：采用 Schwartz 基本人类价值观理论，构建 26K 样本、覆盖 20 类价值观的 benchmark；对比两类方法——分布驱动方法（CAA、SphericalSteer、ODESteer）和行为中心方法（COLD-Steer、BiPO），跨多个模型家族与规模分析 steering vectors 的几何结构，并与理论拓扑做相关性检验。

**关键结果**：分布驱动方法恢复的价值观拓扑与理论预测显著对齐（Spearman ρ 最高 0.51，p < 10^{-13}）；行为中心方法 steering 性能相当，但几何与理论几乎无相关。几何保真度随模型规模提升，但指令调优后下降。更好的几何对齐带来更符合人类一致性的跨价值迁移：引导某一价值会提升兼容价值、抑制对立价值。
