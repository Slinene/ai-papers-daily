---
title: 'PRIME: Pre-Retrieval Index Modeling Enhancement for Structured Document Retrieval-Real'
title_zh: PRIME：预检索索引建模与增强结构化文档检索
authors:
- Cheuk Hei Chung
- Li Liu
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
arxiv_id: '2610.13296'
url: https://arxiv.org/abs/2610.13296
pdf_url: https://arxiv.org/pdf/2610.13296
published: '2026-10-09'
collected: '2026-10-12'
category: RAG
direction: 索引侧优化 · 层次检索与语义重构
tags:
- Index-side optimization
- Semantic Restructuring
- Hierarchical Retrieval
- Metadata Synthesis
- RAG
- Cross-encoder
one_liner: 确定性元数据匹配结构化分块检索质量，嵌入计算降45.8倍，语义重构再提升Answer-F1 13.7%
practical_value: '- **轻量元数据索引替代全量分段嵌入**：对商品详情页/活动页等结构化长文档，可仅用标题+类目标签+关键属性词+页面标题树构建元数据向量（如
  BGE-small 384 维），配合 BM25 做粗筛，能在保持检索质量的同时把 embedding 计算量和索引向量数降低 1-2 个数量级，适合大规模电商语料成本敏感场景。

  - **两阶段层次化检索架构**：先用 metadata 粗筛候选（BM25+稠密向量 RRF），再用 cross-encoder 对 section/字段级精排，避免
  query 时调用大模型 rerank，且能精确送回 top 相关小节，适合商品详情页/用户手册等多段式文档的 Agent 引用。

  - **LLM 重写提升上下文密度**：SR 的 explication+compression 可提高上下文语义密度，让下游生成用更少 token 达到更高
  QA 质量，但会牺牲 BM25 词面匹配；实践中应保留原始文本索引，或做 hybrid 融合，防止 lexical 信号丢失。

  - **先做语料结构审计**：无稳定标题树/短文本语料（类似 NFCorpus），元数据抽取可能有害；可在全量改造前抽样评估 heading 覆盖、段落长度分布、词面重叠度，决定是否采用索引侧重构。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
LLM Agent 需要高精度外部知识检索，但现有 IR 研究主要优化 query-side retriever 和 generator，corpus 侧表示长期只是 chunking，索引信息密度与结构是未充分挖掘的杠杆。问题：在强 reranker 存在时，索引侧能否贡献增量？

## 方法关键点
- **SR（Semantic Restructuring）**：按 H2 章节调用 LLM，对每节做 explication（补全隐式论证）与 compression（去 filler、保核心结论/数值），生成高密度文本并保留标题树。
- **MS（Metadata Synthesis）**：确定性抽取 top-5 TF-IDF 判别词和 heading tree；判别词评分含位置衰减（α=0.3）与标题加成（β=2.0），IDF 来自评估语料自身。
- **HR（Hierarchical Retrieval）**：粗筛用 BM25 与 metadata 稠密向量（BGE-small）RRF 融合 top-30 候选项；精排用 cross-encoder（ms-marco-MiniLM-L-6-v2）逐 H2 section 打分，取 top-5 节送 LLM。
- 两种模式：Offline 只做 MS+HR；Full 先 SR 再 MS+HR，且 SR 文本替换 BM25 和 CE 的索引。

## 关键实验
- QASPER 416 文档 / 1451 queries：共享强 pipeline 下各方法 NDCG@5 收敛于 0.389–0.398；Dense-only 中 PRIME(Full) 0.214 vs Raw 0.175（+22.2%），但 Hybrid+CE 下 SR 变体低于 Raw（0.325 vs 0.391），说明 CE reranker 对文档级排序有饱和效应。
- 确定性 metadata 与 structure-aware chunking 检索等价（NDCG@5 0.201），但 embedding 计算少 45.8×、向量数少 22.4×。
- Full 部署 Answer-F1 0.0957 vs Raw 0.0842（+13.7%）；SR 使语义密度 +127.3%，section 级 Recall@5 +59.9%，evidence tokens 减少 29.0%。
- BRIGHT 8 个结构化任务宏观 NDCG@5 +6.9%，呈现三种 regime：deficit-bridging、structural exploitation、structural saturation；NFCorpus 无标题结构时 metadata-only 掉 19.5%，full-text 恢复至 -2.1%。

## 最值得记住的一句话
索引侧优化在强 reranker 下对文档级排序不敏感，但对上下文证据定位和生成质量有显著增益；是否采用应基于语料结构做前置判断。
