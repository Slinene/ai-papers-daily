---
title: 'From Chunks to Functional Evidence: Function-Aware Retrieval for EDA Documentation
  QA'
title_zh: 从分块到功能证据：面向 EDA 文档问答的功能感知检索
authors:
- Xiaotian Qiu
- Kairui Liu
- Shi Chenyi
- Jinyuan Deng
- Qi Sun
- Cheng Zhuo
affiliations:
- Zhejiang University
- Shanghai Innovation Institute
arxiv_id: '2610.09361'
url: https://arxiv.org/abs/2610.09361
pdf_url: https://arxiv.org/pdf/2610.09361
published: '2026-10-07'
collected: '2026-10-08'
category: RAG
direction: RAG 检索单元重构 · 功能超边
tags:
- RAG
- Retrieval Unit
- Hyperedge
- EDA
- Document QA
- Dense Retrieval
one_liner: 用功能单元（超边）重组多类型文档碎片，训练编码器对齐 query 与功能单元，联合 chunk 检索与统一 reranker，大幅提升 EDA
  文档 QA 的 ROUGE-L
practical_value: '- 复杂技术文档、商品详情页、广告投放规则等多类型碎片场景，可借鉴「功能单元」思想：将相关代码块、参数表、图、约束等聚合成检索单元（如商品功能单元、活动规则单元），用超边链接源
  chunk，缓解 query 与孤立 chunk 失配问题。

  - 检索阶段采用单元检索与直接 chunk 检索并行，再统一 reranker 选证据，比单一 chunk 或纯图检索更稳；在电商知识库 QA、规则问答里可直接复用该混合召回架构。

  - 训练一个 encoder 对齐 query 与功能单元表示，而非只训练 chunk encoder，能更好捕获跨模态/跨类型信息之间的耦合关系；业务上可对商品多属性（标题、参数、卖点、图）学习统一功能表示。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：EDA 文档信息分散在代码块、参数表、图、流程、约束等异构多类型碎片中，传统 RAG 以 chunk 为独立检索单元，导致 query 与知识组织方式严重不匹配，证据召回不足。

**方法**：将 typed artifacts 聚合成 EDA 功能单元（functional unit），每个单元记录为超边并链接其来源 chunks；训练一个编码器对齐 query 与功能单元；检索时并行执行功能单元检索与直接 chunk 检索，再将选中的单元映射回源 chunk；最后通过统一 reranker 挑选最终证据交给生成器。

**结果**：在新建 EDADocEval-QA 数据集上，相比 Chunk RAG 的 ROUGE-L 提升 37.1%，比最强 graph baseline 提升 55.6%；在公开 ORD-MMBench 基准上，比最强 baseline 提升 30.0%，验证了功能感知证据组织在 EDA 文档场景的有效性。
