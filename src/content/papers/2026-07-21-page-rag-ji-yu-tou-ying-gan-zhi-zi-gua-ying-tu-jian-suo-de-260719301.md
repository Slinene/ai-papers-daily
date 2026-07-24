---
title: 'PAGE-RAG: Evidence-Grounded Adaptive Graph Retrieval for Long-Document Question
  Answering'
title_zh: PAGE-RAG：基于投影感知自适应图检索的长文档问答
authors:
- Xingyu Chen
- Junxiu An
- Jun Guo
- Li Wang
affiliations:
- 成都信息工程大学
- 北京航空航天大学
arxiv_id: '2607.19301'
url: https://arxiv.org/abs/2607.19301
pdf_url: https://arxiv.org/pdf/2607.19301
published: '2026-07-21'
collected: '2026-07-24'
category: RAG
direction: 图增强检索 · 自适应路由
tags:
- GraphRAG
- Adaptive Retrieval
- Knowledge Boundary
- Long-Document QA
- Evidence Grounding
one_liner: 将图视为文档语义骨架，通过任务自适应路由和知识边界控制提升长文档问答的可靠性和效率
practical_value: '- **自适应检索路由可用于电商多源知识问答**：在商品知识库、政策文档等长文本场景，根据问题类型动态选择只查图、只查原文档或两者结合，平衡效率与质量，避免图检索的过度开销或信息遗漏

  - **图作为语义骨架而非独立知识源**：在构建商品属性图、类目关系图时，明确图仅是文档的辅助导航结构，最终答案仍需回源文档验证，可减少因图结构不完备导致的幻觉

  - **知识边界控制机制可直接迁移**：在客服Agent或商品推荐解释生成中，通过定义证据范围拒绝回答超出知识覆盖的问题，提升系统可信度，避免编造描述

  - **检索行为显式路由**：可启发在推荐/搜索中设计查询理解模块，动态选择不同检索策略（如稠密检索、图检索、混合检索），而非一刀切，提升长尾查询效果'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：GraphRAG通过引入图结构改进了长文档问答，但自动构建的图是源文档的不完全投影，将其视为独立知识源会导致检索不可靠和生成幻觉。

**方法**：PAGE-RAG将图视为组织与导航文档知识的“语义骨架”，而非替代原始文档。核心包含两部分：
1. **任务自适应检索路由**：基于查询需求动态选择检索行为——仅用图、仅用原文档或二者融合，避免图数据引入噪声或遗漏关键信息。
2. **严格知识边界控制**：生成回答时仅使用检索到的证据，对超出知识范围的问题主动拒绝回答，保证答案充分基于证据。

**结果**：在多个长文档QA数据集上，PAGE-RAG在保持竞争性答案质量的同时，显著提升了检索效率与知识可靠性，验证了投影感知图建模、自适应检索与显式知识边界控制对构建可信GraphRAG系统的价值。
