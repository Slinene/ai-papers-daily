---
title: 'Finding the Right Balance: Relevance and Diversity in LLM Retrieval'
title_zh: 找到正确平衡：LLM 检索中的相关性与多样性
authors:
- Guillaume Brouillette
- Faustin Kagabo
- Usef Faghihi
- Nadia Ghazzali
affiliations:
- Université du Québec à Trois-Rivières
arxiv_id: '2610.09412'
url: https://arxiv.org/abs/2610.09412
pdf_url: https://arxiv.org/pdf/2610.09412
published: '2026-10-07'
collected: '2026-10-08'
category: RAG
direction: RAG 检索多样化自适应策略
tags:
- RAG
- Retrieval
- Diversity
- MMR
- Redundancy
- Reranking
one_liner: 提出基于候选池冗余与查询证据需求的查询自适应规则，选择性启用检索多样化，避免损害相关性与答案质量
practical_value: '- 在电商 RAG/商品问答中不要全局默认启用 MMR 或多样性重排：生产数据若候选池干净，多样化会降低相关性与答案质量；先用已有
  embedding 统计 top-k 最近邻中有效 distinct 文档数，再决定是否开启多样性。

  - 多证据场景（如从多个商品评价/卖点综合回答）可借鉴 query-adaptive 触发条件：当 top-k 选择的 distinct 文档数低于查询所需证据条数时再触发多样化，否则回退到最近邻；该规则无需额外模型，可跨数据集和
  encoder 迁移。

  - 当使用重叠 chunking 或商品库中有同款/相似描述时，可通过 RNG-Score 的 margin 检测重复结构，作为降级信号；margin 明显时说明冗余高，适合切换多样化，否则直接保留
  NN 结果。

  - 工程实现可把“有效不同文档数”做成轻量在线统计特征，与召回/重排解耦，避免因盲目开多样性浪费 context budget 或漏掉关键证据。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：RAG 检索多样化被广泛使用，但已有研究对是否提升检索和答案质量结论不一。该工作发现效果主要随候选池冗余变化，且与查询所需证据条数一致。

**方法关键点**：通过受控近重复注入和生产式重叠 chunking 实验，显示在 clean pools 上多样化会损害相关性、证据覆盖与答案质量；当冗余导致最近邻 top-k 重复 passage 时，多样化对多证据任务有益。提出 query-adaptive 规则：只有最近邻 top-k 中有效 distinct 文档数低于查询证据需求时才多样化。规则从现有 embedding 计算，能跨数据集/编码器迁移，并自动退化为最近邻。还提出 RNG-Score，一个几何 reranker，带 exact nearest-neighbor fallback，其 margin 可指示重复结构。

**关键结果**：该规则获得大部分可达成增益，并保持单证据查询的最近邻行为；结论是多样化应基于可观测冗余和证据需求选择性使用。
