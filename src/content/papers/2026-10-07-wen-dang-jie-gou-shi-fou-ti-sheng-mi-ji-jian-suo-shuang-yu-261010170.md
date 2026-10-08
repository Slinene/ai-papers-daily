---
title: Does Document Structure Help Dense Retrieval? A Placebo-Controlled Ablation
  of Four Mechanisms Across Two Corpora
title_zh: 文档结构是否提升密集检索？双语料四机制安慰剂对照消融
authors:
- Andrey Kuehlkamp
- Priscila Correa Saboia Moreira
- Samuel Rund
affiliations:
- Center for Research Computing, University of Notre Dame
arxiv_id: '2610.10170'
url: https://arxiv.org/abs/2610.10170
pdf_url: https://arxiv.org/pdf/2610.10170
published: '2026-10-07'
collected: '2026-10-08'
category: RAG
direction: RAG 密集检索 · 文档结构消融
tags:
- Dense Retrieval
- Document Structure
- Ablation Study
- RAG
- Chunking
- Hierarchical Retrieval
one_liner: 在双语料上做安慰剂对照消融，证明结构对齐分块与真实标题路径能小幅但稳定提升稠密检索 nDCG
practical_value: '- 做商品文档/详情页 RAG 时，尽量按标题、段落等结构对齐分块，而不是固定窗口；给 chunk 加真实标题路径可小幅提升检索
  nDCG，成本不高。

  - 避免把标题路径等元数据当任意 token 前缀：收益来自语义内容，不是文本扰动；打乱或占位符无效，所以要保留真实结构语义。

  - 分层两阶段检索在业务里可能不如单阶段，尤其第一阶段 section 召回率是瓶颈；上线前需对比单阶段与两阶段的 recall/nDCG。

  - LLM 重建文档结构不一定优于原始结构，Wikipedia 上原始结构更好，QASPER 上无差异；不要盲目用 LLM 诱导结构，按语料做小样本验证。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**  
RAG 系统越来越依赖文档结构处理：结构对齐分块、LLM 生成 chunk 上下文、标题路径元数据、分层两阶段检索。但已有研究分散在不同语料、嵌入模型和指标上，且未控制共同混淆变量——任何前置文本都会扰动 chunk 嵌入。结构到底是否有效、哪个机制起作用不明。

**方法关键点**  
在同一协议下做机制隔离消融，匹配各条件 chunk 大小，并加入语义无效安慰剂（跨文档打乱但结构有效的标题路径）。在 200 Wikipedia Featured Articles（951 查询）和 1,585 QASPER 论文（4,303 问题）两个语料上，用 coverage-aware nDCG 评分，通过 document-clustered bootstrap + Holm correction 做预先注册的 4 个对比。

**关键结果**  
结构对齐分块 + 真实标题路径比上下文固定窗口高 +0.022 / +0.012 cov-nDCG@10，比安慰剂高 +0.010 / +0.016，说明收益来自内容而非 tokens。Naive 两阶段分层检索反而差（-0.033 / -0.015），归因于第一阶段 section 召回不足。Gold structure 在 Wikipedia 上优于 LLM 诱导结构，QASPER 上无显著差异。效应量小（dz 0.06-0.11），但 Holm 显著且跨语料一致。
