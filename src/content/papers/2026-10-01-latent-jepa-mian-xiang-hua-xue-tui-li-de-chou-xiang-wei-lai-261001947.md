---
title: 'Latent JEPA: Abstract Future Prediction for Latent Reasoning in Chemistry'
title_zh: Latent JEPA：面向化学推理的抽象未来预测
authors:
- Xinjian Zhao
- Yaoyao Xu
- Xuemin Chen
- Xiaozhuang Song
- Tianshu Yu
affiliations:
- School of Data Science, The Chinese University of Hong Kong, Shenzhen
- Shanghai Artificial Intelligence Laboratory
arxiv_id: '2610.01947'
url: https://arxiv.org/abs/2610.01947
pdf_url: https://arxiv.org/pdf/2610.01947
published: '2026-10-01'
collected: '2026-10-04'
category: Reasoning
direction: 潜在推理 · 联合嵌入预测
tags:
- Latent JEPA
- Chemical Reasoning
- LLM
- Joint Embedding Prediction
- Molecular Optimization
- Latent Reasoning
one_liner: 提出 Latent JEPA，在自回归学习中引入未来视图联合嵌入预测，提升化学推理与分子优化
practical_value: '- 在 Agent 或搜索推荐场景中，可以训练一个连续 latent state 预测未来结果（点击、转化、下一步状态），作为辅助目标，而不要求逐字生成中间推理，降低
  token 消耗并提升长期决策表征。

  - 使用 joint embedding prediction 对齐当前 latent 表示与未来视图表示，可作为 LLM 微调的 regularizer，让模型对最终业务指标更敏感，适合电商场景中直接优化
  GMV、留存等隐式目标。

  - 多视图预测设计可以借鉴：同时预测后续文本（如用户下一步查询）和结构化结果（如商品 Semantic ID 或属性），在隐空间建立从意图到结果的映射，提升生成式推荐的一致性。

  - 工程实现上，避免完整 CoT 显式生成，用 latent thought 预测未来视图，可在线上低延迟约束下保留规划能力，适合实时推荐或对话式购物助手。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**
LLM 为化学推理提供了知识融合与多步求解的基础，但化学直觉往往在完整解出前就能预判可能结果。受直觉与显式分析互补的启发，研究如何让连续 latent thoughts 在不逐字生成中间步骤的情况下，预判未来解答的信息方面。

**方法关键点**
Latent JEPA 将自回归学习与联合嵌入预测结合，对单个或多个未来视图进行预测。在化学推理中设计了两类目标：文本预测连接 latent thoughts 与后续推理步骤，分子预测连接 latent thoughts 与分子结果。核心是在隐空间对齐当前潜在表示与未来视图表示，避免显式中间推理。

**关键结果**
在 ChemCoTBench 上，分子优化任务以及多个编辑与反应指标均获得提升（摘要未给出具体数值）。表示分析表明，未来预测使 latent thoughts 对分子结果更具信息量，并增强其与化学结构的对应关系，验证了抽象未来预测作为连接连续潜在推理与科学结果的学习原则。
