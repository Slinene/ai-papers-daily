---
title: A knowledge-guided agentic framework for mitigating patient-context ambiguity
  in health queries
title_zh: 知识引导的智能体框架缓解健康查询中的患者上下文歧义
authors:
- Mahyar Abbasian
- Saba A. Farahani
- Arshia Ilaty
- Hung Cao
- Ramesh Jain
- Amir M. Rahmani
arxiv_id: '2608.19875'
url: https://arxiv.org/abs/2608.19875
pdf_url: https://arxiv.org/pdf/2608.19875
published: '2026-08-20'
collected: '2026-08-21'
category: Agent
direction: 知识引导的查询澄清Agent
tags:
- Agentic Framework
- Knowledge Graph
- Query Clarification
- LLM
- Uncertainty Reduction
- Healthcare
one_liner: 在LLM前插入知识图谱驱动的澄清Agent，主动追问缺失患者信息，大幅提升下游回答准确性与一致性
practical_value: '- 可在电商搜索/推荐入口前增加轻量级澄清层：用商品知识图谱（属性、类目、场景标签）枚举可能的意图假设，识别区分度最高的缺失属性（如价格带、适用人群、使用场景），生成1-2个针对性追问，而非直接让LLM回答，从而降低用户短查询的歧义。

  - 保持下游LLM/推荐模型不变，只需将原始query与收集到的用户上下文拼接成 clarified prompt 注入，避免微调成本；澄清问题由知识图谱驱动，减少无关追问，控制交互轮次。

  - 评估澄清效果可借鉴论文指标：对比澄清前后的 Top-1 准确率、Recall@5，以及多次生成结果的预测一致性（如熵或方差），用于衡量上下文补充对模型不确定性的降低。

  - 对线上系统可按不确定性触发澄清：先让LLM对query生成候选答案并计算置信度，仅对低置信度或意图分布分散的query启动澄清流程，平衡用户体验与转化率。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：患者向健康 chatbot 提交的查询往往简短且缺少患者特定信息（症状、诊断、用药、过敏等），导致同一查询可对应多个合理答案。LLM 直接回答会引入无根据的假设。

**方法关键点**：提出一个知识引导的 Agentic 框架，位于患者与下游 LLM 之间，不修改下游模型。该框架首先解释初始查询，利用任务特定知识图谱构造一组可能的假设；然后识别出区分这些假设所需的缺失患者上下文变量；接着主动向患者提出针对性追问；最后将原始查询与获取的上下文合并为澄清后的 prompt 交给下游模型。

**结果**：在两个受控基准上评测五种 LLM。诊断检索（1,034 个症状查询，临床相关证据被系统掩蔽）中，与直接 prompt 相比，整体 exact Top-1 准确率至少提升 57.1 个百分点，selective exact Recall@5 至少提升 77.7 个百分点；饮食安全分类（487 个查询，决定性健康上下文被省略）中，五种模型准确率全部提升，其中四个模型取得最高 Matthews correlation coefficient；重复生成分析显示澄清后的 prompt 还降低了 LLM 的预测不确定性。结论：主动获取缺失上下文的中间 Agent 无需微调即可显著提升下游回答的准确性与一致性。
