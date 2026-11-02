---
title: 'Chronos-2: A foundation model for multivariate time series forecasting'
title_zh: Chronos-2：多变量时间序列预测基础模型
authors:
- Abdul Fatir Ansari
- Oleksandr Shchur
- Jaris Küken
- Andreas Auer
- Boran Han
- Pedro Mercado
- Syama Sundar Rangapuram
- Huibin Shen
- Lorenzo Stella
- Xiyuan Zhang
affiliations:
- Amazon
- University of Freiburg
- Boston College
- Rutgers University
- Max Planck Institute for Biogeochemistry
arxiv_id: '2610.41956'
url: https://arxiv.org/abs/2610.41956
pdf_url: https://arxiv.org/pdf/2610.41956
published: '2026-10-30'
collected: '2026-11-02'
category: Other
direction: 时间序列基础模型 · 多变量预测
tags:
- time series foundation model
- multivariate forecasting
- zero-shot
- probabilistic forecasting
- covariates
- Chronos-2
one_liner: 零样本多变量时序基础模型，联合建模序列交互与异构协变量，精度与推理效率显著领先
practical_value: '- 把 Chronos-2 作为电商场景的 zero-shot 多变量预测底座：对销量、流量、广告消耗、库存等多条相关序列联合建模，并纳入价格、促销、节假日、市场指数等协变量，减少逐业务训练专用预测模型的工作量。

  - 可直接复用「历史上下文推断序列关系 + 异构协变量」思路：在推荐/广告的实时调控中，对 CTR、转化率、GMV、曝光量等多指标联合预测，输出概率分布而非点值，便于做风险控制和预算分配。

  - 其推理效率（100 序列/秒级）适合大规模商品/广告计划的批量预测与实时校准；若将预测结果作为特征或 reward 信号接入排序/Agent 决策，延迟成本可控。

  - 如需领域适配，优先考虑基于 Chronos-2 微调或蒸馏，而不是从零训练；同时注意协变量口径统一与缺失处理，因为模型对异构协变量的建模能力是收益关键。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：现有时间序列基础模型（TSFM）大多把每条序列独立处理，无法建模多变量序列之间的相互影响和外部驱动变量，而科学应用（流行病学、经济学、能源、地球科学等）普遍存在这种多变量、带协变量场景。

**方法**：Chronos-2 以大规模预训练为基础，直接在历史上下文中推断多条时间序列之间的关系，并联合异构协变量进行概率预测，无需针对下游任务做特殊适配；支持零样本预测和不确定性量化。

**结果**：在多个基准上，平均 skill score 相对最强基线提升 5.2 个百分点，胜率提升 10 个百分点；在单张中端 GPU 上预测 100 条序列不到 1 秒，端到端速度分别比最佳点预测和概率预测专用模型快 50 倍和 1000 倍。在传染病预测、宏观经济建模、碳通量预测和径流模拟等领域达到或超过各领域专用方法。
