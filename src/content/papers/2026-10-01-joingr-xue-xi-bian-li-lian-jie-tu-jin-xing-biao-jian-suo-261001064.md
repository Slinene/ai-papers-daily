---
title: 'JoinGR: Learning to Traverse Join Graphs for Table Retrieval'
title_zh: JOINGR：学习遍历连接图进行表检索
authors:
- Sandipan De
- Abhijit Chakraborty
- Sambaran Bandyopadhyay
- Vivek Gupta
affiliations:
- Arizona State University
- Adobe Research, India
arxiv_id: '2610.01064'
url: https://arxiv.org/abs/2610.01064
pdf_url: https://arxiv.org/pdf/2610.01064
published: '2026-10-01'
collected: '2026-10-05'
category: Other
direction: Text-to-SQL 表检索 · 连接图遍历
tags:
- table retrieval
- join graph
- Text-to-SQL
- dense retrieval
- recall
one_liner: 将数据库连接图作为检索空间，用查询条件化评分器遍历边来提升多跳表检索召回
practical_value: '- 商品/内容图谱检索可借鉴：先选语义相似锚点，再用轻量边评分器沿关系边遍历，提升多跳关联实体的召回。

  - Text-to-SQL 或对话式 BI 场景中，把 schema 连成图，用 query-conditioned connector 代替独立的表打分，能缓解
  LLM 幻觉和 schema 错选。

  - 冻结 embedding + 轻量 MLP 边评分器的方式训练成本低、易于线上部署，适合推荐系统中召回阶段的图遍历增强。

  - 跨域迁移实验表明学到的遍历策略是可复用的，类似电商场景下训练好的商品关系遍历模型可能跨品类复用。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：Text-to-SQL 需要先做表检索，但 dense retrieval 独立排序表/列，忽略表之间的外键连接。多跳查询中，必需表往往未在问题里显式出现，只能通过已相关表的连接关系推断，导致召回不足。

**方法关键点**：JOINGR 把数据库 join graph 作为检索空间，列作为节点，表内关系和主外键作为类型边。给定问题，先选语义相似 anchor tables，然后用 query-conditioned scorer 遍历连接边，聚合“边贡献”得到表得分。scorer 是冻结 query/node/edge embeddings 上的轻量 MLP，用 pairwise margin loss 训练。

**关键结果**：在 BIRD 和 Spider 上与最强基线 competitive；在 BEAVER 企业多跳表需求基准上，大幅提升 recall，超过 dense retrieval 和 re-ranking 基线；跨域实验显示学到的 scorer 可迁移，说明捕捉到了可复用的 join graph 遍历行为。
