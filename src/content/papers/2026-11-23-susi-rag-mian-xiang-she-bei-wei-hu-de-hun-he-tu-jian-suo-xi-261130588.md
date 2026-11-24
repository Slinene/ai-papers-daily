---
title: 'SuSi-RAG: A Hybrid Graph RAG for Equipment Maintenance'
title_zh: SuSi-RAG：面向设备维护的混合图检索增强生成系统
authors:
- Hansi Zhang+
- Wilma Johanna Schmidt+
- Wanlin Yang
- Xiaozhi Shen
- Adrian Paschke
- Evgeny Kharlamov
affiliations:
- Robert Bosch GmbH
- Freie Universität Berlin
- Fraunhofer Institute FOKUS
- Fudan University
- University of Oslo
arxiv_id: '2611.30588'
url: https://arxiv.org/abs/2611.30588
pdf_url: https://arxiv.org/pdf/2611.30588
published: '2026-11-23'
collected: '2026-11-24'
category: RAG
direction: 混合图 RAG · 工业维护问答
tags:
- Graph RAG
- Knowledge Graph
- Subgraph Similarity
- Industrial Maintenance
- LLM
- Retrieval
one_liner: 用子图相似度实现混合图 RAG，在工业维护问答中将 top-1 检索准确率从 61.5% 提升至 96.2%
practical_value: '- 复杂关系型 query 召回：电商搜索/推荐中，用户 query 常包含因果、兼容、搭配等复杂关系（如“适合油皮的防晒”“与
  XX 兼容”）。可构建商品/属性知识图谱，用 query 子图与候选商品子图相似度做召回或重排，替代纯文本向量相似度，提升相关性与可解释性。

  - 混合检索架构：Graph RAG 不必取代向量检索，而是先向量召回候选，再用 KG 子图匹配精排，平衡图计算开销与复杂 query 相关性。电商知识问答、售后维修知识库可直接套用该模式。

  - Agent 检索工具设计：在购物助手/售后 Agent 中，用图谱子图而非纯文本片段作为上下文，可提供结构化证据链，约束生成并降低幻觉，适合多步因果推理。

  - 运营反馈闭环：系统在生产环境运行 8 个月并收集 10664 次交互，可借鉴其反馈循环设计——记录用户显式/隐式反馈，定期更新知识图谱和检索参数，用 top-1
  检索准确率与专家评分联合评估，持续迭代。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：制造领域设备维护依赖专家知识，文档分散在异构格式与来源中。传统向量 RAG 在处理真实维护查询时暴露两大弱点：复杂因果链和跨领域综合。

**方法关键点**：SuSi-RAG 采用混合图 RAG，将用户查询与每条维护记录通过子图相似度进行匹配，而不是仅依赖向量相似度；系统集成运营反馈闭环，持续更新图与检索。

**关键结果**：在 Bosch 实际产线运行超过 8 个月，处理 10,664 次问答，上界答案准确率 96.25%（确认错误率 3.75%）。在概念验证中，相比向量基线，top-1 检索准确率从 61.5% 提升至 96.2%，专家评分答案质量从 44.9% 提升至 84.1%。
