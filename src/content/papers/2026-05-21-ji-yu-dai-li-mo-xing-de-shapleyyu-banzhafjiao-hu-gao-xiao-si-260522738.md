---
title: Proxy-Based Approximation of Shapley and Banzhaf Interactions
title_zh: 基于代理模型的Shapley与Banzhaf交互高效近似方法
authors:
- Santo M. A. R. Thies
- Hubert Baniecki
- R. Teal Witter
- Eyke Hüllermeier
- Maximilian Muschalik
- Fabian Fumagalli
affiliations:
- LMU Munich
- Warsaw University of Technology
- University of Warsaw
- Claremont McKenna College
- Bielefeld University
arxiv_id: '2605.22738'
url: https://arxiv.org/abs/2605.22738
pdf_url: https://arxiv.org/pdf/2605.22738
published: '2026-05-21'
collected: '2026-05-23'
category: Other
direction: 可解释性 · 交互指数近似
tags:
- Shapley interactions
- Banzhaf interactions
- proxy model
- tree ensembles
- explainability
- residual correction
one_liner: 提出ProxySHAP，通过树代理模型与残差校正实现快速且一致的交互指数估计，达到SOTA性能。
practical_value: '- 在推荐系统模型解释与调试中，可采用树代理模型快速近似高阶特征交互，识别影响预测的关键特征组合，指导特征工程与交叉特征设计。

  - 利用论文中多项式时间交互计算算法，可在树集成模型（如GBDT）中高效计算精确交互值，直接应用于CTR预估模型的特征重要性分析。

  - MSR残差校正策略提供了一种在代理模型偏差与方差之间权衡的方法，可借鉴到其他需要代理估计的场景（如模型蒸馏、数据估值），避免方差指数增长。

  - 实验表明ProxySHAP在小样本预算下仍能高精度近似，这对在线推理阶段需要快速解释推荐结果、生成可解释性理由的场景有实用价值。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

动机：现有Shapley/Banzhaf交互估计器难以兼顾速度和精度，高阶交互面临指数复杂度。方法：提出ProxySHAP，先用树代理模型高效获取近似交互，再通过残差校正（MSR）恢复一致性；理论上推导出多项式时间的广义TreeSHAP算法，可精确计算树集成的交互指数，避免指数树深依赖；证明了MSR在模型残差与特征子集独立时能纠正偏差且方差不随交互阶数指数增长。结果：在多个基准测试中，ProxySHAP在所有预算范围内均达到最低误差，显著优于ProxySPEX和KernelSHAP-IQ；在下游交互检测与模型解释任务中表现最佳，并能扩展到数千特征的大规模应用。
