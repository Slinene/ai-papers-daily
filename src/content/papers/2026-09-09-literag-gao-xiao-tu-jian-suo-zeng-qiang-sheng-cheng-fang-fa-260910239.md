---
title: 'LiteRAG: Cost-Efficient Graph-Based Retrieval-Augmented Generation'
title_zh: LiteRAG：高效图检索增强生成方法
authors:
- Daniel Alejandro Coll Tejeda
- Pedro García López
- Daniel Barcelona-Pons
affiliations:
- Universitat Rovira i Virgili
arxiv_id: '2609.10239'
url: https://arxiv.org/abs/2609.10239
pdf_url: https://arxiv.org/pdf/2609.10239
published: '2026-09-09'
collected: '2026-09-10'
category: RAG
direction: 图 RAG 低成本高效检索
tags:
- GraphRAG
- RAG
- Multi-hop QA
- Token Efficiency
- Query-Adaptive Thresholding
- Hub Penalization
one_liner: 用查询条件算法探索替代检索时 LLM 控制，显著降低图 RAG 多跳问答延迟与成本
practical_value: '- 在电商知识库/政策规则/商品图谱等多跳问答场景，可把图检索中的在线 LLM 遍历或总结改为查询条件驱动的确定性算法，先做子图探索再构造上下文，避免每
  query 调大模型，显著降本。

  - 上下文不要塞入整个相关子图，而是按证据链/推理链选择边和节点；用 query-adaptive thresholding 动态控制保留范围，能减少大量无效
  token，尤其适合店铺/商品/规则相关问答。

  - 对图谱中的高连接度 hub 节点（如平台总则、大品牌/大店铺）做 community-aware 惩罚，降低宽泛上下文对生成的干扰；在电商商品知识图谱或活动规则图谱里可借鉴。

  - 对已经上线 GraphRAG 的团队，可先审计在线路径；把 LLM 从 query-time 关键路径移除，换为轻量算法，往往比换生成模型或复杂索引收益更大。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：图图谱 RAG 能提升多跳问答，但现有方法在检索时频繁调用 LLM 做遍历、社区总结或证据聚合，导致延迟高、成本大，且生成上下文过宽、含冗余信息，降低生成效率。

**方法关键点**：LiteRAG 将检索时的 LLM 控制替换为查询条件驱动的算法探索与推理链式上下文构造。它不再依赖 LLM 在线遍历图谱，而是基于 query 自适应地探索子图并沿证据链选择节点与边；引入 query-adaptive thresholding 控制上下文规模，并用 community-aware hub penalization 对高度 hub 节点降权，减少宽泛信息。

**关键结果**：在 DistComp 多跳检索基准上，LiteRAG 整体质量达到 0.798，为所有评测方法中最高；相比 GraphRAG Global 和 DRIFT，单 query 延迟降低超过 100 倍、成本降低超过 99%。在 UltraDomain 上，整体质量与 LinearRAG 持平，但 token 使用量减少约 14 倍。消融实验表明，query 自适应阈值与社区感知 hub 惩罚是 token 效率提升的主要来源。
