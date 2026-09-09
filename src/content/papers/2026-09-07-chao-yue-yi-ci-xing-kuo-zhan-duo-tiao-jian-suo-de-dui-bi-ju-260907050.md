---
title: 'Beyond One-Shot Expansion: Contrastive Evidence Exploration for Multi-Hop
  Retrieval'
title_zh: 超越一次性扩展：多跳检索的对比证据探索
authors:
- JungMin Yun
- YoungBin Kim
affiliations:
- Chung-Ang University
arxiv_id: '2609.07050'
url: https://arxiv.org/abs/2609.07050
pdf_url: https://arxiv.org/pdf/2609.07050
published: '2026-09-07'
collected: '2026-09-09'
category: RAG
direction: 多跳 RAG 检索 · 对比证据探索
tags:
- Multi-hop Retrieval
- RAG
- Query Expansion
- Contrastive Facets
- Coverage-aware Ranking
- Training-free
one_liner: 训练免的多跳检索框架，通过对比 facet 索引、证据条件探索和覆盖感知重排提升 RAG 证据召回
practical_value: '- 可直接迁移到电商搜索中的复杂意图查询：将原始 query 视为多跳证据链的起点，利用 LLM 基于已检索商品/属性生成下一轮
  probe，逐步发现缺失的品类、品牌或属性约束，避免一次性扩展引入噪声。

  - 借鉴 passage-specific contrastive facets 思想：为每个商品或知识片段离线生成“区分性问答对”（如“该商品与相似商品的差异点”），在召回阶段作为附加信号，帮助提升稠密检索对相似商品的区分度，避免同款/相似款混淆。

  - Coverage-aware 贪心选择可以用于重排：在电商推荐或广告素材排序中，用生成多个 probe 分别代表不同用户意图，通过最大化边际覆盖增益选择集合，保证最终结果覆盖不同意图而非重复满足同一需求。

  - 工程上，该框架 training-free，只需复用已有 embedding 和 LLM；但离线对比 facet 构建和在线多轮 LLM 调用成本较高，可以先在小而美的商品知识库上预计算，或者限制邻居数量和轮数来权衡
  latency。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
多跳 QA 中支持证据往往通过中间实体或关系隐式连接，原始 query 通常只表达一个检索意图。现有方法或依赖一次性 query expansion，或采用迭代检索，但中间信号噪声大且最终结果可能冗余。作者认为有效多跳检索应同时满足三方面：自适应探索、passage 级细粒度区分、以及证据覆盖互补，而非仅仅单点相关性排序。

## 方法关键点
- **离线对比 facet 索引**：对每个 passage 检索语义相似邻居，用 LLM 生成“目标 passage 能回答但邻居不能回答”的自然语言 query，作为该 passage 的对比 facet 集合，训练免且可在线复用。
- **在线顺序证据探索**：共 T 轮，每轮用 probe 检索 top-K 候选，然后基于已检索证据生成紧凑 evidence summary，再让 LLM 生成下一轮 probe，针对尚未解决的信息需求。
- **对比证据细化**：对每个候选 passage，用其对比 facet 与当前 probe 的相似度加权，构造 probe-conditioned 的表示修正，得到 contrastive relevance，并与基础 dense 分数插值。
- **覆盖感知最终选择**：将每个 probe 视为不同证据需求，计算候选 passage 对 probe 集合的边际覆盖增益，贪心选择同时兼顾个体相关性与互补覆盖的集合。

## 关键实验
在 MuSiQue、HotpotQA、2WikiMultihopQA 三个多跳 QA 数据集上，与 BM25、e5-large-v2、bge-reranker、HyDE、query2doc、LameR、IRCoT、Self-Ask 等方法对比，均取得最佳检索质量和下游 QA 性能。最显著的是 MuSiQue 上 FSR@10 从 best baseline 39.20 提升到 57.00；2Wiki 上 FSR@10 从 75.60 提升到 91.50；HotpotQA 上 FSR@10 从 93.30 提升到 96.20。消融表明顺序探索贡献最大（移除后 MuSiQue FSR@10 从 57.00 降至 36.50），覆盖感知和对比细化带来稳定小幅提升。

## 一句话记忆点
多跳检索不应把 query 当成静态意图，而应让检索方向随已发现的证据动态演化，同时用对比 facet 和覆盖目标保证“找到的证据既细微不同又整体互补”。
