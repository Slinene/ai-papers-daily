---
title: 'TimelyRAG: Semantic-Temporal Hybrid Retrieval for Time-Critical Question Answering
  in Overlapping-Evolving Documents'
title_zh: TimelyRAG：面向重叠演化文档的时间敏感混合检索框架
authors:
- Youngeun Nam
- Joeun Kim
- Hwanjun Song
- Susik Yoon
- Jae-Gil Lee
- Byung Suk Lee
affiliations:
- KAIST
- Korea University
- University of Vermont
arxiv_id: '2609.11572'
url: https://arxiv.org/abs/2609.11572
pdf_url: https://arxiv.org/pdf/2609.11572
published: '2026-09-10'
collected: '2026-09-11'
category: RAG
direction: RAG 时间敏感检索
tags:
- RAG
- Temporal Retrieval
- Time-Critical QA
- Benchmark
- Overlapping-Evolving Documents
one_liner: 提出 retriever-agnostic 的 TimelyRAG，用时间距离重排解决修订版本文档的时态问答，并发布 TimelyQABench
practical_value: '- 电商/政策类文档常存在修订而非完全替换，如促销规则、商品参数、平台协议；可直接在现有向量检索后加一层 retriever-agnostic
  的时间距离重排，无需重训 retriever。

  - 将文档生效时间/版本区间与 query 的时间参考（显式或隐式）作为特征，设计 hybrid score = semantic similarity + λ·temporal
  distance，λ 可按业务数据调优。

  - 构建评估集时，不要只用静态 QA 对；应加入同一政策/商品的多个修订版本，并标注 query 的时间锚点，避免语义重叠导致旧版本被误召回。

  - 对 Agent 使用 RAG 的场景，建议在检索输入中显式加入当前业务时间或用户询问的时间上下文，防止动态信息（价格、库存、政策）过期。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：LLM+RAG 在开放域问答虽强，但文档随时间修订时不可靠。现有时间敏感检索只解决 disjoint-evolving（每次更新是独立快照），而法律、政策等是 overlapping-evolving：修订覆盖早先条款但保留大部分内容，造成版本间语义高度重叠，检索易混淆。

**方法**：提出 TimelyRAG，一个 retriever-agnostic 框架，将 temporal distance 纳入排序，使 query 与对应时间版本的文档对齐；不依赖特定 retriever。构建 TimelyQABench，首个针对 regulation-heavy 领域 overlapping-evolving 场景的基准。

**结果**：多个实验一致提升，nDCG@10 最高 +28.6%，说明时间推理对演化文档 QA 的关键作用。
