---
title: 'KGVoyager: Knowledge Graph Agnostic Question Answering via Agentic Navigation'
title_zh: KGVoyager：基于 Agent 导航的知识图谱无关问答
authors:
- Essam Wisam
- Chengkai Li
affiliations:
- University of Texas at Arlington
arxiv_id: '2609.01780'
url: https://arxiv.org/abs/2609.01780
pdf_url: https://arxiv.org/pdf/2609.01780
published: '2026-09-01'
collected: '2026-09-03'
category: Agent
direction: Agent 自主导航知识图谱问答
tags:
- KGQA
- Agent
- SPARQL
- Knowledge Graph
- LLM
- Think-Act-Observe
one_liner: 一种知识图谱无关的 Agentic 架构，仅用查询端点和轻量类索引即可动态发现图谱结构并生成 SPARQL，F1 提升约 8 点
practical_value: '- 在电商商品知识图谱问答或智能导购中，可以用“轻量类索引 + 动态探索”替代完整 ontology 硬编码：仅维护类目/一级类索引，让
  Agent 在查询端点实时发现属性与关系，适应类目和属性的频繁变更。

  - 采用 think-act-observe 循环，将 NL→SPARQL 拆成搜索（term→IRI 映射）、探索（发现 schema）和执行反馈（根据空结果/错误修正），比一次性生成更鲁棒，适合线上自然语言到结构化过滤条件的生成。

  - 执行反馈作为信号：让 Agent 根据结果异常自动调整约束，减少人工维护规则；该思路可迁移到推荐系统的标签/属性过滤或动态 query 理解模块。

  - 工程上只要求 SPARQL endpoint 可查询，不依赖昂贵的 text-SPARQL 标注对，适合快速冷启动新领域或新类目；轻量类索引也减少 prompt
  长度，直接降低 LLM 成本与延迟。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：领域特定知识图谱问答（KGQA）通常缺乏正式本体和 curated text-SPARQL 对，现有 LLM 方案严重依赖二者，难以在真实端点落地。需要一种仅基于查询端点即可工作的方案。

**方法关键点**：KGVoyager 采用 think-act-observe 循环，配备三类工具：搜索工具将自然语言术语映射到图 IRI；探索工具动态发现图谱结构和语义（类、属性、关系）；执行工具运行 SPARQL 并根据返回结果或错误进行迭代细化。整个过程无需预置本体或示例，只要求一个轻量级 class index，极大降低了部署门槛。

**关键结果**：在四个基准上，KGVoyager 相比先前 SOTA 将 F1 提升约 8 个百分点，同时成本和运行时间各降低约 22%。
