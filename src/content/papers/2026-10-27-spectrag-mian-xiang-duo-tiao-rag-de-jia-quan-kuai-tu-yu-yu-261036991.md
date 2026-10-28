---
title: 'SpectRAG: Weighted Chunk Graphs for Token-Budgeted Context Selection in Multi-Hop
  Retrieval-Augmented Generation'
title_zh: SpectRAG：面向多跳 RAG 的加权块图与 token 预算上下文选择
authors:
- Zafer Sahinoglu
- Abdulazeez Mohammed
- Buse Yaren Kazangirler
- Cahit Berkay Kazangirler
affiliations:
- Mitsubishi Electric US
- Mitsubishi Electric Innovation Center (MELIC)
- Karabuk University
arxiv_id: '2610.36991'
url: https://arxiv.org/abs/2610.36991
pdf_url: https://arxiv.org/pdf/2610.36991
published: '2026-10-27'
collected: '2026-10-28'
category: RAG
direction: RAG · 图检索 · 谱图上下文选择
tags:
- RAG
- GraphRAG
- Spectral Graph
- Token Budget
- Multi-Hop Retrieval
- Context Selection
one_liner: 用加权块图的谱坐标与预算化选择，把 RAG 检索从 top-k 相似改成连通证据集优化，以更低索引成本提升多跳证据召回
practical_value: '- 电商 RAG/购物助手：除文本相似外，把商品同款/互补、类目层级、共同属性、会话共现/共点击、query 改写关系作为边构建商品或内容
  chunk 图；用 Laplacian 谱坐标做结构化特征，可在召回阶段纳入连通性，减少相似商品冗余，补回缺失的桥接属性/卖点。

  - Token 预算选择直接用于 LLM 推荐解释、Agent 工具/知识上下文化：设定固定 token 预算，做 protected core + tail
  precision + backfill，而不是固定 top-k；按 token 长度归一化 utility，避免长 chunk 吃光预算。

  - 混合种子 + 两跳扩展：用 RRF 融合向量、BM25、历史或生成式问题匹配，再沿图做两跳扩展，可找回多跳证据；适合售后/导购等需要跨产品、跨文档推理的场景。

  - 成本与效果：chunk 级稠密图 + 谱特征比实体级 GraphRAG 索引小一个数量级且 recall 更高；生产上可离线缓存图与谱坐标，在线只做轻量扩展/PPR，避免每条
  query 都调大模型抽实体。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
标准 RAG 用 dense embedding 做 top-k 检索，每个 chunk 独立打分，容易返回冗余段落、漏掉多跳推理需要的桥接证据，并忽略文档结构。真实问答需要的是一个相关、多样、结构连通的证据集合，而不是 k 个最相似 chunk。因此把检索建模为 token 预算约束下的集合选择，同时利用语料图谱结构，成为关键问题。

**方法关键点**
- 离线构建加权块图：节点是 chunk；边权重融合六类信号——语义相似、文档邻接、章节层级、共享实体/术语、引用/依赖、LLM 生成的 utility question 相似度；稀疏化后保存。
- 计算 normalized Laplacian，取最小 32 个非平凡特征向量作为每个 chunk 的谱坐标，编码社区/结构位置，不同于文本语义向量。
- 在线检索：RRF 融合 dense FAISS、BM25、utility-question 匹配形成高召回种子集（20 个）；在图上做两跳 BFS 扩展，最多 200 候选；用 relevance 与谱空间 closeness + Personalized PageRank 混合重排。
- 最终 token 预算选择（约 12k）：目标函数包含 relevance、冗余惩罚、coverage、connectivity；实际用 protected core + 尾部 precision floor + 文档覆盖 tie-break + backfill，生成约 10–15 个 chunks。

**关键实验**
在 MultiHopRAG 和 UltraDomain 四个领域上对比 NaiveRAG、HybridRAG、LightRAG、HyDERAG。相比 LightRAG 实体图，节点数少 2.8–6.6×，MultiHopRAG 持久化索引 46 MB vs 274 MB；Recall@5 64.7 vs 49.2，MRR 70.4 vs 61.5；EM 72.0 / F1 72.4，超过 NaiveRAG 约 7 点，与 LightRAG 持平。UltraDomain pairwise 上对 NaiveRAG 全面占优，diversity win rate 55.0%。

最值得记住：不要把 dense top-k 当最终检索目标；用 dense 做高召回入口，用图结构做证据集去冗余、补桥接，并在 token 预算内做集合级选择，能以更低索引成本获得更强证据召回。
