---
title: Efficient Retrieval-Augmented Generation via Token Co-occurrence Graphs
title_zh: 基于 Token 共现图的轻量高效 GraphRAG 框架
authors:
- Gianluca Bonifazi
- Christopher Buratti
- Michele Marchetti
- Federica Parlapiano
- Giulia Quaglieri
- Davide Traini
- Domenico Ursino
- Luca Virgili
affiliations:
- Università Politecnica delle Marche, Ancona, Italy
- Università di Modena e Reggio Emilia, Modena, Italy
arxiv_id: '2606.30093'
url: https://arxiv.org/abs/2606.30093
pdf_url: https://arxiv.org/pdf/2606.30093
published: '2026-06-29'
collected: '2026-07-01'
category: RAG
direction: Token 共现图高效 GraphRAG
tags:
- RAG
- GraphRAG
- token co-occurrence
- multi-hop QA
- knowledge graph
- retrieval
one_liner: 用 token 滑动窗口共现构造 KG 取代 LLM 抽取，实现多跳推理 RAG 的索引与推理开销大幅降低
practical_value: '- **电商搜索查询扩展**：用滑动窗口统计商品标题或查询日志的 token 共现，低成本构建词项联系图，辅助召回阶段的 query
  扩展或相关性特征，替代繁重的实体识别链路。

  - **多轮交互式推荐**：迭代实体驱动的检索策略可迁移至多轮对话推荐，从已召回商品或上下文抽取桥接属性（类目、品牌等）逐步精炼检索，提升复杂需求满足率。

  - **长尾知识构建**：在攻略、搭配推荐等场景，需要从多篇内容拼接证据，可借鉴无 LLM 的共现图快速索引文档段落，通过神经重排序确保证据链准确，同时控制在线推理延迟。

  - **工程落地降本**：方法省去了 LLM 抽取实体和关系的高频调用，索引时间、推理延迟和 prompt 长度显著降低，适合对成本和延迟敏感的生产环境直接复用。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：标准 RAG 在需要多跳推理的问答中难以整合分散证据，近期 GraphRAG 方案通过知识图谱增强检索，但其构图过程依赖 LLM 提取实体和关系，计算开销大且易出错。需要一种低成本、可扩展的图增强检索方案。

**方法**：提出 TIGRAG，核心是用**滑动窗口 token 共现统计**直接构建知识图谱，无需 LLM 抽取，从而大幅降低索引成本。推理时，先通过图上的语义扩展和神经重排序召回与查询相关的互连文本块；再引入**迭代实体驱动检索策略**——每一轮从已检索上下文提取“桥接实体”扩展查询，逐步收集多跳证据链。整个过程避免了昂贵的构图流水线。

**结果**：在三个多跳 QA 数据集（HotpotQA、2WikiMultihopQA、MuSiQue）上，TIGRAG 的检索召回率和下游问答 F1 均优于密集检索及多种 GraphRAG 基线，同时索引时间减少最高达 90% 以上，推理延迟显著降低，prompt 长度也明显更短。
