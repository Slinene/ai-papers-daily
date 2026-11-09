---
title: 'MV-IVF: Multi-Vector Retrieval via Multi-Vector Clustering'
title_zh: MV-IVF：基于多向量聚类的原生 IVF 多向量检索索引
authors:
- Kishen N Gowda
- Laxman Dhulipala
- Lars Gottesbüren
- Rajesh Jayaram
affiliations:
- University of Maryland
- Google Research
arxiv_id: '2611.09040'
url: https://arxiv.org/abs/2611.09040
pdf_url: https://arxiv.org/pdf/2611.09040
published: '2026-11-06'
collected: '2026-11-09'
category: Other
direction: 多向量检索 · 原生 IVF 索引
tags:
- multi-vector retrieval
- IVF
- ColBERT
- MaxSim
- quantization
- ANN
one_liner: 提出原生 IVF 索引 MV-IVF，直接对多向量点云做聚类与路由，显著提升 ColBERT 检索的延迟和吞吐
practical_value: '- 如果业务里已经在用 ColBERT/ColPali 等 late-interaction 多向量表示（商品多模态 token、用户行为序列
  token 等），可以尝试把现有单向量 IVF/ANN 粗排替换成 MV-IVF 这类原生点云索引，避免先单向量代理粗排再精确重排导致 MaxSim 候选集损失。

  - 高吞吐场景（大促召回、feed 批量重排）可借鉴 leaf-grouped batch search：按 leaf 分组批量查询，复用 cache-resident
  的 leaf 数据，做 many-to-many MaxSim，比逐 query 独立执行更省内存带宽，适合 IVF 结构。

  - 工程优化可直接迁移：FHT 随机旋转 + sign/4-bit/8-bit 量化对多向量 MaxSim 聚合有误差平滑效果；查询端用 Ward''s method
  聚合冗余 query token，并用 sum 而非 average 保留分数尺度，能显著加速候选打分。

  - 离线评估候选集保留时，除 Recall@1 外重视 Recall-k@k（精确 top-k 邻域恢复），更适合衡量召回系统是否覆盖完整候选集，而不是只找回单个最相关
  item。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
多向量检索通过 ColBERT 风格的 MaxSim 细粒度 token 交互提升检索质量，但单 query-doc 评分也变成大量点积计算。现有系统大多走 PLAID/WARP/MUVERA 的路线，把候选生成降级为单向量代理或过滤后再重排，可能丢失 MaxSim 下的 top-k 文档。论文回到另一个方向：能否直接对多向量数据构建原生 IVF 索引，让候选过滤与 top-k 恢复都留在多向量空间。

**方法关键点**
- MV-Lloyd：定义 Chamfer(k,s)-median 聚类目标，每个 cluster 中心是大小不超过 s 的点云；关键观察是固定点云 assignment 后，center update 等价于对 cluster 内所有 flatten 后的向量做加权 s-median，因此可以直接复用优化的单向量 k-means 实现。
- MV-IVF：用 MV-Lloyd 递归划分文档点云，构建树形 IVF 索引；内部节点保存质心点云，查询时用 MaxSim 与质心点云做 beam search 路由，只对少量 leaf 里的文档做精确 MaxSim 评分。
- 优化：FHT 随机旋转 + Rand-1bit、TurboQuant 4-bit、Rand-8bit 低比特量化；Ward query compression 合并冗余 query token；batched search 按 leaf 分组查询，复用缓存内 leaf 数据并做 many-to-many MaxSim，提高 cache locality 和 SIMD 并行度。

**关键结果**
在 BEIR/LoTTE 共 8 个文本检索数据集上，用 ColBERTv2 多向量表示，对比 SVH、MUVERA、MV-Vamana、FastPLAID 和 IGP。90% Recall-10@10 下，MV-IVF 单 query 延迟最多降低 8.03x，QPS 最多提升 173.5x；相比 MUVERA、SVH、MV-Vamana 的吞吐几何平均提升分别为 2.19x、4.01x、2.07x，同时构建时间和索引大小适中。

**最值得记住的一句话**
多向量检索里，把 IVF cluster 中心也保留为点云而不是降级成单向量代理，能在 top-k 邻域恢复质量与吞吐上同时获益；其 center update 可退化为普通单向量 k-means，工程落地成本低。
