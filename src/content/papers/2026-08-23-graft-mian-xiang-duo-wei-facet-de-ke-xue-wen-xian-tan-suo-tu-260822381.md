---
title: 'GRAFT: Graph-Distilled Generative Retrieval for Facet-Aware Scientific Literature
  Exploration'
title_zh: GRAFT：面向多维 facet 的科学文献探索图蒸馏生成式检索
authors:
- Italo Luis da Silva
- Hanqi Yan
- Yujing Wang
- Jiangnan Ye
- Lin Gui
- Yulan He
affiliations:
- King's College London
arxiv_id: '2608.22381'
url: https://arxiv.org/abs/2608.22381
pdf_url: https://arxiv.org/pdf/2608.22381
published: '2026-08-23'
collected: '2026-08-25'
category: GenRec
direction: 生成式检索 · 图蒸馏与 facet 归因
tags:
- Generative Retrieval
- Graph Distillation
- Facet-aware Retrieval
- Coverage-aware Distillation
- Graph-RRF
- Scientific Literature
one_liner: 将多维 facet 论文关系图蒸馏进生成式检索器，用 coverage-aware 蒸馏与 graph-RRF 保留覆盖和归因，免索引推理
practical_value: '- 多面关系建模：把商品/内容之间的关系显式拆成多个 facet（如功能、场景、风格、人群），每条边带类型+强度；召回/推荐时按
  facet 分别检索并保留「为什么推荐」的 provenance，直接输出推荐理由。

  - 生成式推荐 ID 设计：用自然语言 facet-item/卖点短语作为 DocID，而非数字 cluster ID，能显著复用 LLM 先验；论文中自然语言
  DocID 比 numeric codebook R@20 高 2.4×。

  - 解决长尾/冷启动的 coverage-aware distillation：生成式训练里若只按边均匀采样，稀疏图会导致 16% item 从未被作为 target
  训练；落地时可采用 min-coverage floor + reverse-neighbour fallback 补齐全量商品覆盖，尤其对冷启动物品有效。

  - 用 graph-RRF 做多路召回融合：对每个 facet 的生成候选按 RRF 打分后乘以 query-candidate 图边权重，无边的候选归零过滤；可借鉴到商品知识图谱/关系图与生成式推荐融合，防止模型生成「幻觉邻居」；论文中
  graph-RRF 相比 plain fusion R@20 +13.38%。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：科学论文的相关关系是多维的：两篇论文可能针对同一 problem 但用完全不同的 method，或仅因 evaluation protocol 相同而相关，同时还可能因 citation 邻近性而被限制在已知文献邻域。传统 document-level dense/lexical 检索把多维关系压成单一相似度，无法回答“为什么相关”。因此需要 facet-aware retrieval，让每个返回结果带 provenance。

**方法关键点**：
- 构建 **LITWEAVE**：从 S2ORC 选 11,359 篇 NLP 论文，建 typed paper graph，四个 facet（problem/method/result/contribution），边权重融合 facet item 语义相似度与 citation signals，每个 paper 每个 facet 保留 top-20 邻居。
- **GRAFT** 把 graph 蒸馏进生成式检索器：查询用 facet item 伪查询，DocID 是 paper 自身的 facet item 自然语言文本（截断 12 token），LLM 为 Llama-3.2-1B 全参微调；解码用 trie 约束保证合法 DocID。
- **Coverage-aware distillation**：均匀采样只覆盖 84% corpus；通过 edge-score 比例采样、Kmin=3 最低覆盖 floor、reverse-neighbour fallback 补齐无入度 paper，达到 100% 覆盖，训练样本 294k vs 213k。
- **graph-RRF**：融合四个 facet 候选列表时，用 query-candidate 图边权重缩放 RRF 项，无边的候选权重归零过滤，保留 facet attribution。

**关键结果**：在 LITWEAVE 测试集，GRAFT R@20=0.326，达到 dense-graph teacher（0.357）的 91%，超过所有无图基线（MiniLM 0.295、BM25 0.274、MINDER 0.284），推理时无需 encoder 和近邻索引。Out-of-corpus 500 queries 上，GRAFT R@20=0.548 反超 dense-graph 0.501；非显然检索占 47%，非显然检索的引用 lift 30.8×。消融显示 coverage-aware 比 uniform +0.030 R@20（+10.13%），graph-RRF 比 plain RRF +0.038（+13.38%），attribution precision 0.922。DocID 消融中自然语言 facet-item 比 numeric codebook 高 2.4×。

**最值得记住的一句话**：生成式检索要同时解决“哪些 ID 训得到”和“生成结果是否被图支持”；coverage-aware distillation + graph-RRF 是保持图结构、支撑 facet 归因和免索引推理的关键。
