---
title: 'One Retrieval to Cover Them All: Co-occurrence-Aware Knowledge Base Reorganization
  for Session-Level RAG'
title_zh: 一次检索覆盖全会话：面向会话级RAG的共现感知知识库重组
authors:
- Shivam Ratnakar
- Yixuan Zhu
- Cecilia Cheng
- Chaya Vijayakumar
affiliations:
- University of Southern California
arxiv_id: '2606.31156'
url: https://arxiv.org/abs/2606.31156
pdf_url: https://arxiv.org/pdf/2606.31156
published: '2026-06-30'
collected: '2026-07-01'
category: RAG
direction: RAG知识库重组与检索策略优化
tags:
- RAG
- session-level retrieval
- co-occurrence clustering
- KB compression
- enterprise search
- coverage metric
one_liner: 通过共现聚类重组知识库，单次检索会话覆盖率从41%提升至58%，同时压缩KB至20%
practical_value: '- **会话级覆盖率作为评估指标**：在电商客服、推荐对话等多意图场景中，直接采用session-level coverage替代单query召回率，更能反映用户完整信息需求的满足程度，可指导检索系统优化。

  - **离线知识库重组方法**：利用历史问答会话中的文档共现关系构建图，通过聚类将相关文档预先分到同一簇。线上检索时，不仅返回top-k文档，还扩展至同簇其他文档，一次检索覆盖多个潜在意图。可借鉴到商品推荐：根据用户会话中共同点击/购买的物品，构建物品簇，实现“一揽子”推荐。

  - **检索效率与压缩**：通过簇合并将KB压缩至20%，大幅减少索引大小，适合大规模电商知识库。用更少的索引即可达到较高覆盖率，降低线上延迟。

  - **跨模型与跨领域一致性**：方法对多种嵌入模型和功能领域稳定有效，表明聚类模式基于共现而非特定编码器，迁移到不同业务数据时无需重新调参，易于落地。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：企业RAG系统往往只针对单次查询进行优化，但用户实际以会话形式提出多个相关问题，这些问题的答案分布在知识库中语义上较远的部分。实验发现，在标准KB上仅做一次检索只能覆盖用户会话级信息需求的41%，导致用户需要多次提问，体验差。

**方法**：提出离线KB重组方法：基于历史会话中文档的共现关系（同一会话内被共同检索到的文档对）构建共现图，然后进行聚类，将语义上相关但可能不在同一邻域的文档分到同一簇。线上检索时，用查询找到初始top-k文档，再引入它们所在的簇中的其他文档作为扩展候选，从而一次检索提供更全面的文档集合。

**结果**：在WixQA企业支持数据集（6221篇文档）上，该方法将单次检索的会话覆盖率提高到58%（+17%绝对，95%置信区间[14.1,20.4]）。若以70%覆盖率为目标，所需检索次数减少34%。同时，KB被压缩到原始大小的20%。效果在4种嵌入模型和6个功能领域上均一致。
