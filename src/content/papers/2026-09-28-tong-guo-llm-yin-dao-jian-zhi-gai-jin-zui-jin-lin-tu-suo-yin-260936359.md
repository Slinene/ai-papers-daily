---
title: Better Nearest Neighbor Graph Indices via (Efficient) LLM-Guided Pruning
title_zh: 通过 LLM 引导剪枝改进最近邻图索引
authors:
- Fangzhou Wu
- Haike Xu
- Sandeep Silwal
affiliations:
- University of Wisconsin–Madison
- MIT
arxiv_id: '2609.36359'
url: https://arxiv.org/abs/2609.36359
pdf_url: https://arxiv.org/pdf/2609.36359
published: '2026-09-28'
collected: '2026-09-30'
category: RAG
direction: LLM 离线精修图索引 · 语义检索
tags:
- Graph-based ANNS
- LLM-Guided Pruning
- DiskANN
- HNSW
- Semantic Retrieval
- Reranking
one_liner: 提出 LGP，在 DiskANN/HNSW 图索引上离线用 LLM 替换低价值邻居，弥合几何构造与语义评估错配
practical_value: '- 可在现有 HNSW/DiskANN 等图索引上增加离线 LLM 精修环节：对每个节点，用两跳非邻居构造小候选池，先按结构冗余/两跳可达性筛到
  M=12~24，再让 LLM 只选 B=2 个语义互补候选替换低价值边；不改查询链路，直接提升低 search width 下的召回与 NDCG。

  - 该方法的收益在窄 search width/低距离计算预算下最大，适合召回候选受限、重排器无米下锅的场景；可作为索引侧优化，和 query-time rerank/RGS
  等互补。

  - 工程上 LLM 调用只发生在离线构图阶段，按节点短list 调用，成本可控；可先对高流量 query 相关节点或重要类目做部分精修（β=0.25/0.5），再逐步放开到全图。

  - 语义选择模型越强收益越明显（Qwen3-32B > Qwen3-8B），且对 embedding 模型鲁棒；建议用非推理模式的小 LLM/VLM 控制成本，避免破坏图导航。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：图基 ANN 索引（DiskANN、HNSW）构图时只依赖 embedding 几何距离，但下游检索评估的是语义相关性，形成“几何—语义错配”。在低搜索预算下，图搜索可能优先访问几何近但语义不相关的文档，漏掉真正相关节点；事后 LLM rerank 受候选召回瓶颈限制，无法恢复未被贪心搜索访问到的文档。因此需要把语义信息前移到图索引构造阶段，同时保留高效贪心导航所需的稀疏几何结构。

**方法关键点**：
- 提出 LGP（LLM-Guided Graph Pruning），在现有图索引上做局部边替换，不改变查询时搜索过程。
- 对每个节点，先用其两跳非邻居扩展候选集，再用纯结构信号（额外两跳可达性、与当前邻域冗余度）筛选到 M 个候选，避免大量 LLM 调用。
- 用 LLM 在短list 中选最多 B 个能补充当前邻域语义的候选，替换可达性冗余高的旧边；保持出度约束和局部几何结构。
- 可实例化到 DiskANN（在第二遍构造时精修）和 HNSW（只精修 base layer），不改变查询期 greedy search。

**关键结果**：
- BRIGHT 上，DiskANN 宽度 20 时，LGP 使 greedy search 平均 NDCG@10 从 17.12 提升到 21.30（+24.4%），LLM rerank 后从 18.92 提升到 23.83（+26.0%）；Recall@10 分别 +25.2% 和 +27.4%。
- M-BEIR 多模态检索上，greedy NDCG@10 +11.7%，rerank 后 +13.2%。
- 搜索宽度越窄提升越大：BRIGHT 宽度 10 时 greedy NDCG@10 +32.3%；在距离计算预算 200 时 +33.2%，且在 Economics 上达到相同 NDCG 只需约 50% 距离计算。
- HNSW、换用 Qwen3-Embedding 均保持增益；Qwen3-32B 语义选择优于 Qwen3-8B。

**最值得记住的一句话**：与其只在查询期用 LLM rerank 补救，不如离线用 LLM 对图索引做局部语义化剪枝，把“语义可达性”直接编进图结构，低预算检索收益最大且不增加在线延迟。
