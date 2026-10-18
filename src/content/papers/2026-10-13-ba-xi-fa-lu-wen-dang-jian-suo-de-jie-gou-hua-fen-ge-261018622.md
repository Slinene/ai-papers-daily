---
title: Structural Segmentation for Brazilian Legal Document Retrieval
title_zh: 巴西法律文档检索的结构化分割
authors:
- Leandro Carísio Fernandes
- João Alberto de Oliveira Lima
- Hudson de Martim
- Eduardo Seiti de Oliveira
- Roberto Lotufo
- Jayr Pereira
affiliations:
- Câmara dos Deputados
- Senado Federal
- Universidade Estadual de Campinas (UNICAMP)
- Universidade Federal do Cariri (UFCA)
arxiv_id: '2610.18622'
url: https://arxiv.org/abs/2610.18622
pdf_url: https://arxiv.org/pdf/2610.18622
published: '2026-10-13'
collected: '2026-10-18'
category: Other
direction: 长文档结构化分块与稠密检索
tags:
- legal IR
- document segmentation
- dense retrieval
- chunking
- metadata enrichment
one_liner: 长法律文档按结构分块索引可提升稠密检索效果，完整层级非必需，核心块加文档元数据即可
practical_value: '- 对长文档场景（商品详情、政策条款、合同、帮助中心 FAQ），优先使用结构化分块而不是整篇文档做 dense 索引，可显著提升语义召回；但注意索引单元数会大幅增加，需要评估线上
  QPS 与存储成本。

  - 不需要维护完整层级树；把核心分块（如商品核心参数、条款正文）加上文档级元数据（类目、品牌、标题、文档 ID）作为上下文，就能达到甚至超过复杂层级表示的效果，工程实现更简单。

  - 结构化分块对 BM25 等 lexical 检索提升不一致，因此不要全链路替换；可以保留整文档 BM25 召回，同时用结构化分块做 dense 召回，混合加权或多路召回更稳妥。

  - 分块时要注意元数据上下文注入，避免孤立块语义漂移；类似地，电商长描述或评论聚合可以按要点/属性切块，并带上商品 title 或类目信息，让向量更聚焦。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

动机：长法律文档通常作为单个检索单元，会稀释相关内容，限制检索效果。尤其是在 dense retrieval 下，单个向量难以准确表示多主题长文档。

方法：利用法律法案的层级结构，将文档表示为一组 chunks。对比四种表示策略：完整的多层层级表示，以及三种基于核心块（articles 和非规范性文档组件）的简化版本，附带不同上下文细节。在两个巴西公开法律数据集（规范性法案和立法提案）上，分别用 lexical 和 dense 检索模型测试。

关键结果：与整文档索引相比，结构化分割能提升 dense retrieval 的检索效果，尽管索引单元数大幅增加；但 lexical retrieval 没有一致收益。进一步发现完整层级表示没有必要：核心块加文档元数据即可达到可比或更好的效果。
