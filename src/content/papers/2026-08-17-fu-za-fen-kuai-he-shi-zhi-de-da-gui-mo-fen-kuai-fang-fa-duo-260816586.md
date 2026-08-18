---
title: When Is Complex Chunking Worth It? A Multi-Objective Evaluation of Chunking
  Methods at Scale
title_zh: 复杂分块何时值得？大规模分块方法多目标评估
authors:
- Laura Caspari
- Kanishka Ghosh Dastidar
- Michael Dinzinger
- Jelena Mitrović
- Michael Granitzer
affiliations:
- University of Passau
- Interdisciplinary Transformation University Linz
arxiv_id: '2608.16586'
url: https://arxiv.org/abs/2608.16586
pdf_url: https://arxiv.org/pdf/2608.16586
published: '2026-08-17'
collected: '2026-08-18'
category: RAG
direction: RAG 密集检索 · 分块多目标评估
tags:
- RAG
- Dense Retrieval
- Chunking
- Multi-Objective Evaluation
- Embedding Models
- Operational Cost
one_liner: 8种分块策略的规模化评测表明复杂分块很少一致优于简单分块，最佳选择高度依赖模型、数据和规模，且成本差异显著
practical_value: '- 在电商 RAG 场景（商品文档/评价/客服知识库）中，先以固定长度或递归分块作为 baseline，不必一上来用 Proposition/语义分块等复杂方法：它们往往只带来微小或不一致提升，但索引与维护成本更高。

  - 选型分块时把索引吞吐、查询延迟、向量库内存纳入评估，而不只看 nDCG/Recall；相同检索指标下，优先选择 chunk 数量少、平均长度小的策略，可显著降低线上召回和存储成本。

  - 分块效果与 embedding model 和 corpus size 存在交互，没有 universal best；上线前应在自己模型与目标语料规模下做小规模多目标
  ablation，并分别报告 Recall@k 与 nDCG@k，因为结论可能随目标指标不同而翻转。

  - 对于长文档召回，采用“更细分块 + MaxP/段落级聚合”常是一个稳的起点；复杂分块若不能在同一模型/数据上稳定提升，不建议为微弱效果付出工程复杂度。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：真实 RAG/密集检索系统常处理长文档，需要分块，但标准基准评测假设每篇文档单 embedding；现有分块比较侧重检索质量，忽视索引吞吐、查询延迟、内存等系统成本。

**方法**：在 2 个可扩展语料上，对 8 种代表性分块策略（固定大小、递归、结构/语义、Proposition 等）进行评测，结合 3 种 embedding models 和多个 corpus sizes，同时记录检索效果与系统级成本。

**结果**：计算昂贵的分块方法很少一致优于简单分块；最佳策略随 embedding model、数据集、corpus size、目标指标变化；检索性能相近的方法在索引吞吐/查询延迟/内存上可能差异很大，因此分块应被视为多目标设计决策。
