---
title: 'Cost Scales with Change, Not Corpus Size: Incrementally Maintaining an Evolving
  Semantic Substrate'
title_zh: 成本随变化缩放而非语料大小：增量维护演化语义基底
authors:
- Yusuke Takahashi
- Kyle Wild
- Asako Uraki
affiliations:
- Asia AI Institute
- Musashino University
- Endgame Labs, Inc.
arxiv_id: '2608.16621'
url: https://arxiv.org/abs/2608.16621
pdf_url: https://arxiv.org/pdf/2608.16621
published: '2026-08-17'
collected: '2026-08-18'
category: RAG
direction: 增量语义基底维护 · RAG 成本优化
tags:
- incremental SVD
- semantic substrate
- RAG
- embedding drift
- orthogonal Procrustes
- latent semantic indexing
one_liner: 增量低秩更新替代全量 SVD，使语义基底维护成本随变化量而非语料规模增长
practical_value: '- 电商商品库/内容库频繁上新时，可用增量低秩更新维护语义索引（LSI/SVD），单次更新成本与新增变更量成正比，替代周期性全量重建，适合高动态场景。

  - 切换 embedding 模型或版本时，不必全量重新嵌入所有商品/文档；用 orthogonal Procrustes 对齐新旧嵌入空间，只需重嵌约 10%
  代表性样本校准虚拟轴，可恢复 0.95 平均余弦相似度，大幅降低迁移成本。

  - 增量 SVD 维护的子空间与全量 SVD 接近一致（recall@10=1.0），可作为动态语义召回或 RAG 索引的底层机制，支持低延迟 ingestion
  和稳定检索质量。

  - 可推广到用户/商品向量索引（如 ANN）的更新策略：用增量更新 + 漂移校准代替定期全量重建，减少离线计算资源消耗。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
RAG 和 agentic QA 通常在查询时才重新推导语料语义，成本高；更优方式是在摄入时将语义编译为紧凑、可查询的语义基底并持续维护。但维护成本常被认为过高：全量重建 truncated SVD 代价大，embedding 模型变更也可能需要全量重新嵌入。

### 方法关键点
- 采用增量低秩更新维护 truncated SVD，而非每次变化全量重建。
- 对于 embedding 模型变更，引入 orthogonal Procrustes virtual axis update，只需重新嵌入约 10% 语料来校准新旧嵌入空间。

### 关键结果
- 合成实验（维度 256、秩 32、语料从 3000 增到 9000 篇、50 次更新事件）：增量更新单次成本为全量 SVD 的 1/33.7，累计成本为 1/23.8。
- 增量子空间与全量重算几乎一致：最大主角度漂移低于 1e-11 度；recall@10=1.0。
- Procrustes 对齐后，仅重嵌 10% 语料即可使新嵌入与真正重新嵌入向量的平均余弦相似度达到 0.95。

结果支持持续维护语义基底，而非反复重建。
