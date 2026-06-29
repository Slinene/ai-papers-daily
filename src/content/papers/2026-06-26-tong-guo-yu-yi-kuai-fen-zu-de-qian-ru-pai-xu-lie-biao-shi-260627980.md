---
title: Listwise Explanation of Embedding-Based Rankings via Semantic Chunk Grouping
title_zh: 通过语义块分组的嵌入排序列表式解释
authors:
- Hyunkyu Kim
- Yeeun Yoo
- Youngjun Kwak
affiliations:
- Financial Tech Lab, KakaoBank Corp.
arxiv_id: '2606.27980'
url: https://arxiv.org/abs/2606.27980
pdf_url: https://arxiv.org/pdf/2606.27980
published: '2026-06-26'
collected: '2026-06-29'
category: RecSys
direction: 列表式 Shapley 解释 · 语义块分组
tags:
- Shapley
- listwise explanation
- dense retrieval
- semantic chunking
- interpretability
one_liner: 提出 ChunkGroupSHAP，用语义块组作为特征单元，适配密集嵌入排名列表的解释粒度
practical_value: '- **解释单元需匹配 ranker 表示粒度**：对于密集嵌入召回（如语义向量相似度），用语义块组（sentence/passage
  级）替代单词特征，避免解释碎片化；对于 BM25 等词汇匹配仍保留单词级。在电商搜索中，混合召回场景可依此类推，分别设计解释特征。

  - **列表级解释方法工程化**：ChunkGroupSHAP 保持 listwise Shapley 的文档对比特性，可直接用于线上排名调试或审计，定位“为何某商品排在前面”。配合特征分组降低计算开销，适合候选集较小的精排阶段。

  - **分组策略可迁移**：按 query-local、corpus-level 等粒度自动聚类语义块，在商品描述、用户评论等长短文本场景，可尝试基于商品属性或用户意图的聚类，生成可解释的属性组。

  - **解释可视化与信任构建**：在推荐理由中展示语义块组而非零散单词，能向运营和用户提供更连贯的自然语言解释，利于广告出价调优或搜索 badcase 诊断。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：密集嵌入排名使用句子/段落级表示，但现有列表式解释方法仍基于孤立单词，导致特征粒度失配，解释结果碎片化。需要将解释单元对齐到 ranker 的语义表示粒度。

**方法**：提出 ChunkGroupSHAP，一种列表式 Shapley 方法。首先将语义相关的文本块（如句子、段落）聚类为跨文档共享的特征组；然后通过 mask 整个组扰动所有包含相关证据的文档，计算 Shapley 值分配排名贡献。这样将解释粒度提升至语义组层级，既保留列表式对比，又匹配密集嵌入的表示习惯。

**关键结果**：在 MS MARCO、FinanceBench、AILACaseDocs、FinQA 四个数据集上，用 E5 ranker 和 BM25 对比：
- 词汇匹配的 BM25 适合单词级特征；
- 密集嵌入 ranker 适合语料级语义组特征；
- 异构 Web 检索适合查询局部分组。
结论：特征单元应由 ranker 表示粒度和检索语料库结构共同决定。
