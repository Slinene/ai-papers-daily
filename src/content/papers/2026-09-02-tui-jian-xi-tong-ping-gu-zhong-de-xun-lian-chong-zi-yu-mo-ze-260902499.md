---
title: Training seeds and model-selection stability in recommender-system evaluation
title_zh: 推荐系统评估中的训练种子与模型选择稳定性
authors:
- Juan Manuel Rodriguez
- Oleg Lesota
- Antonela Tommasel
affiliations:
- Aalborg University
- Johannes Kepler University Linz
- ISISTAN
- CONICET-UNCPBA
arxiv_id: '2609.02499'
url: https://arxiv.org/abs/2609.02499
pdf_url: https://arxiv.org/pdf/2609.02499
published: '2026-09-02'
collected: '2026-09-06'
category: Eval
direction: 推荐系统评估可复现性与模型选择
tags:
- training seed
- model selection
- reproducibility
- evaluation protocol
- recommender systems
one_liner: 固定数据划分仅变训练种子，证明单种子结果会高估推荐模型评估稳定性，种子应纳入评估协议
practical_value: '- 离线对比召回/排序模型时，同一配置至少跑 3-5 个训练 seed，报告 metric 均值±方差；若两组模型 score
  差异落在 seed 方差内，不要下“有提升”结论。

  - 做 hyperparameter tuning / model selection 时，不要用单 seed 的 validation 最优直接定配置；可用
  multi-seed validation 平均或 bootstrap，并检查 validation→test 的转移是否稳定。

  - 除了 nDCG/Recall，同时看 top-k 列表的 Jaccard/agreement；分数接近但列表重叠低时，线上效果可能不稳定，尤其影响广告/推荐位的曝光一致性。

  - 若业务 pipeline 含 dropout、negative sampling、masking 等随机机制，固定 seed 的离线报告会掩盖真实方差；在
  launch review 中把 seed 稳定性作为通过标准。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：推荐系统实验通常只用一个随机训练 seed，假设随机性影响可忽略；但 seed 会影响参数初始化、mini-batch 顺序、dropout、masking、隐变量采样、训练时负采样等机制。

**方法**：固定数据划分，仅改变训练 seed，在多个超参数配置上分析 seed 影响，从三个层面展开：用户级指标敏感性、基于验证集的模型选择、推荐列表一致性。

**结果**：seed 变化常可被检测到；其影响取决于配置间是否明显分离、验证结果能否迁移到测试、相近分数是否对应相近 top-k 列表。单 seed 结果会高估推荐系统评估的稳定性，训练 seed 应作为评估协议的一部分而非偶然实现噪声。
