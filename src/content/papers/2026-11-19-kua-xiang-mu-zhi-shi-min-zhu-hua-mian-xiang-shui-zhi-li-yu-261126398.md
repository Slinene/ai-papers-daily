---
title: 'Democratizing Cross-Project Knowledge for Transforming Water Governance and
  Climate Resilience: an Agentic AI Ecosystem'
title_zh: 跨项目知识民主化：面向水治理与气候韧性的 Agentic AI 生态
authors:
- Oriol Alàs
- Ian Palacín
- Iván Cester
- Edgar Rubión
affiliations:
- Eurecat, Centre Tecnològic de Catalunya, Barcelona, Spain
arxiv_id: '2611.26398'
url: https://arxiv.org/abs/2611.26398
pdf_url: https://arxiv.org/pdf/2611.26398
published: '2026-11-19'
collected: '2026-11-21'
category: RAG
direction: Agentic RAG 跨域知识检索
tags:
- Agentic RAG
- Embedding Fine-Tuning
- Hierarchical Indexing
- ReAct
- Multi-Domain Retrieval
one_liner: 通过层次化文档解析和领域微调嵌入，Agentic RAG 在跨项目检索中将 MRR 相对提升 26.7%
practical_value: '- 将商品文档、政策、活动资料按层级结构切分（如类目→商品→属性），保留结构化元数据做索引，能显著提高 RAG 召回一致性。

  - 在通用 embedding 基础上用自营领域语料微调（如电商商品描述、用户 query 日志），可低成本获得检索相关性提升（本文 MRR 相对+26.7%）。

  - 借鉴 ReAct 式检索预算分配：当需要跨多个知识库（商品库、内容库、客服知识库）回答 query 时，让 agent 动态分配检索次数，避免在错误库中浪费。

  - 对于多业务线/多国家站点的电商知识平台，采用“领域集合”分开索引并用控制器按证据累积决策，可提升跨领域问答稳定性。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

动机：
欧盟资助项目产生大量技术报告与案例研究，知识分散在多个项目与异构文档结构中，决策者难以快速定位可用的情境化信息。

方法关键点：
- 构建领域知识库：将三个 EU 项目文档重构为层次化 section tree，并用结构化元数据索引。
- 检索层：训练两个领域专用 embedding 模型（水和气候），提升对领域术语的理解。
- Agentic 检索：用 ReAct-style controller 迭代分配检索预算到不同领域集合，逐步累积证据直到满足停止条件。

关键结果：
在跨项目语料基准上，该方法相比单域 embedding 基线，MRR 相对提升 26.7%，表明相关证据检索更一致。
