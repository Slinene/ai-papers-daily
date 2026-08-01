---
title: 'BayesAME: Bayesian Active Model Evaluation'
title_zh: 贝叶斯主动模型评估：自动确定核心集大小的序列框架
authors:
- Paula Cordero Encinar
- Taylan Cemgil
- Arnaud Doucet
- Virginia Aglietti
- Silvia Chiappa
affiliations:
- Imperial College London
- Google DeepMind
arxiv_id: '2607.27023'
url: https://arxiv.org/abs/2607.27023
pdf_url: https://arxiv.org/pdf/2607.27023
published: '2026-07-29'
collected: '2026-08-01'
category: Eval
direction: 主动贝叶斯模型评估 · 核心集选择
tags:
- Bayesian active learning
- model evaluation
- coreset selection
- uncertainty quantification
- sequential design
- benchmark estimation
one_liner: 通过贝叶斯序列设计自动停止，用信息增益选评估项，以历史模型相似性为先验，实现高效基准评估
practical_value: '- 在评估大量推荐模型版本或A/B测试时，可直接用此方法动态选择评测子集，计算成本降低且自动决定何时停止

  - 当有历史模型在相同项目上的评分数据（如多个旧模型在商品集上的CTR），可利用潜在能力分组先验加速新模型评估

  - 多目标扩展能捕获模型间的性能相关性，适合同时评估多个候选模型（如对比多个精排模型）；工程实现可采用连续响应对数似然替代硬二元分数，提升估计精度

  - 信息增益驱动的主动选择策略可迁移到查询建议质量评估、生成式推荐结果的在线人工标注等稀疏评估场景'
score: 7
source: arxiv-stat.ML
depth: abstract
---

**动机**：大规模生成模型在基准上的全量评估计算成本极高，现有方法需人工指定评测子集大小，无法根据可靠性需求自动终止。

**方法关键点**：
- 将目标模型在测试项上的正确/错误建模为伯努利随机变量，通过引入共享历史模型表现的**项组潜在能力**，建立分层贝叶斯模型。
- 先验编码“目标模型与历史模型行为相似”的信念，利用后验推导**性能估计器**和**不确定性**。
- 每一步用**信息增益**准则选择下一个加入核心集的项，最大化对目标模型总体性能的信息获取。
- 定义两个阈值：①性能估计的滑动波动幅度；②性能不确定性（后验方差）；当两者都低于阈值时**自动停止**，输出当前核心集及估计结果。
- **多目标扩展**：对多个目标模型同时评估，共享项选择过程，利用模型间性能相关性进一步减少总评估量。
- 提出使用**连续响应对数似然**（如生成序列的log-prob）替代传统的二元正确/错误分数，显著提升估计准确性。

**关键结果**：
- 在MMLU、MATH、GSM8K等基准上的实验表明，BayesAME 始终优于所有序列自适应的基线（如基于不确定性、基于误差的主动采样），所需评估量更少且估计更准。
- 非随机核心集选择明确优于随机选择，反驳了近期文献中的怀疑；在相同预算下，BayesAME 的估计误差仅为随机样本均值的 1/2～1/5。
- 多目标扩展能在评估5个模型时，相比逐一独立评估再减少30%~50%的核心集大小。
- 使用连续分数（如per-token log-likelihood）比传统二元分数大幅提升估计精度，在MMLU上均方误差降低约60%。
