---
title: 'CAGE: Coherence-Aware Graph Encoding for Retrieval-Augmented Generation'
title_zh: CAGE：检索增强生成中的连贯性感知图编码重排序框架
authors:
- Tong Qi
- Jingyu Wu
- Youbing Yin
- Spencer Hong
- Daben Liu
- Erin Babinsky
affiliations:
- Capital One
- General Intelligence Company
arxiv_id: '2609.04647'
url: https://arxiv.org/abs/2609.04647
pdf_url: https://arxiv.org/pdf/2609.04647
published: '2026-09-04'
collected: '2026-09-07'
category: RAG
direction: RAG 重排序 · 图编码连贯性
tags:
- RAG
- Reranking
- Graph Neural Network
- Coherence
- Multi-hop QA
- Entity Graph
one_liner: 用异质实体图建模检索块间连贯性，通过图神经网络重排序提升多跳问答上下文质量
practical_value: '- 在搜索/推荐系统的召回后重排阶段，不要只对单个 item 和 query 打分，可以构建 item 之间的实体关系图（如互补、替代、共现），用
  GNN 编码集合整体连贯性，提升 top-k 集合的质量。

  - 对于电商场景下多跳查询（如“适合油皮的轻薄粉底液”），可以抽取商品属性实体构建图，利用 min-out-degree 重加权突出少连接但关键的事实锚点（如肤质、功效），增强上下文的事实一致性。

  - 在 LLM 生成推荐理由或广告文案时，检索出的商品信息可能存在矛盾或冗余，可借鉴 CAGE 的 Noise Resistance 和 Informational
  Bonding 维度，用图结构过滤噪声、强化信息互补性，减少生成幻觉。

  - 部署时可将 CAGE 作为轻量级 reranker 模块叠加在现有检索器后，无需改动生成模型，只需额外构建实体图并做一次图卷积，工程成本可控。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：传统 RAG 系统对每个 passage 独立评分，导致 top-k 上下文可能各自与 query 相关但彼此之间缺乏连贯性，甚至互相矛盾，成为下游生成质量的硬天花板。

**方法关键点**：提出 CAGE，一个重排序框架，显式建模检索块之间的连贯性，分为四个维度：域内相关性、噪声抵抗、信息绑定、事实一致性。流程为：将检索到的 passages 转化为有向异质实体图；通过 min-out-degree 重加权放大事实锚点（连接少但关键的实体）；用关系图卷积网络（R-GCN）编码图结构模式；最后将块间连贯性分数与 query 相关性分数融合进行最终排序。

**关键结果数字**：在四个多跳基准上评估，CAGE 在 bridge-dominated 数据集上的 Recall@5 达到或超过强基线 monoT5，并且在下游 Exact Match 指标上一致提升，即使检索召回率与基线相当或更低，也表明结构连贯的上下文能生成更精确的答案。
