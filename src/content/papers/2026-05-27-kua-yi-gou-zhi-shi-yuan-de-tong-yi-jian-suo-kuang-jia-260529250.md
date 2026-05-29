---
title: 'OmniRetrieval: Unified Retrieval across Heterogeneous Knowledge Sources'
title_zh: 跨异构知识源的统一检索框架
authors:
- Jinheon Baek
- Soyeong Jeong
- Sangwoo Park
- Woongyeong Yeo
- Minki Kang
- Patara Trirat
- Heejun Lee
- Sung Ju Hwang
affiliations:
- KAIST
- DeepAuto.ai
arxiv_id: '2605.29250'
url: https://arxiv.org/abs/2605.29250
pdf_url: https://arxiv.org/pdf/2605.29250
published: '2026-05-27'
collected: '2026-05-29'
category: RAG
direction: 统一异构知识检索 · 跨源查询
tags:
- heterogeneous retrieval
- knowledge sources
- source-native query
- unified interface
- natural language query
one_liner: 提出 OmniRetrieval，将自然语言查询自动分解为各知识源原生查询，实现文本、关系表、知识图的统一检索
practical_value: '- **多源数据统一检索接口设计**：在电商搜索/推荐中，产品信息散落在文档、关系数据库（价格库存）、知识图谱（属性关系）等，可借鉴
  OmniRetrieval 的“源选择 + 原生查询生成”模式，对用户 query 自动路由到合适数据源，避免预先构建庞大统一索引。

  - **Agent 工具链中的知识检索模块**：为 Agent 提供一种工具，能理解自然语言指令并转化为针对不同数据源的查询（SQL、SPARQL、Cypher
  等），无需 Agent 显式指定数据源类型，简化多智体系统中的知识获取。

  - **保留源结构优势的跨源证据聚合**：不强行将结构化数据嵌入单一向量空间，而是通过跨源证据选择保留表结构、图谱关系等原生表达能力，可迁移到推荐系统的多模态特征融合，如用户行为表、社交图、内容文本的异构证据整合。

  - **可复用的源选择与查询生成模块**：源选择分类器与基于 LLM 的原生查询生成可独立使用，在电商知识库问答、智能客服等场景，对用户问题自动识别需要查询哪些源库（如维修手册、商品参数表、QA
  对），并生成相应的精确查询，降低人工适配成本。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：真实场景的信息需求常跨越多种异构知识源，如非结构化文本、关系数据库、RDF 知识图谱和属性图。现有检索器仅能处理单一数据源且绑定固定查询语言，导致知识碎片化。直接化一会丢失各源的结构化优势（如模式、本体、组合算子）。

**方法**：提出 OmniRetrieval，作为统一访问层，接收自然语言查询，依次完成：1）源选择（Source Selection），识别与查询相关的知识源；2）查询生成（Query Formulation），针对每个选定源，生成其原生查询语言（SQL、SPARQL、Cypher 或自然语言）；3）在各源执行查询后，收集证据并通过跨源证据选择（Cross-Source Evidence Selection）聚合 top-k 相关证据。整个过程不修改底层数据源，保持其结构独特性。

**结果**：在涵盖 13 个数据集、309 个知识库的跨文本、关系、图谱基准上，OmniRetrieval 全面超越单源基线，证明了其作为通用多源检索接口的有效性。
