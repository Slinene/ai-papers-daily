---
title: Cluster with Auctions for Vector Search
title_zh: 基于拍卖机制的向量搜索聚类索引方法 CwA
authors:
- Swann Bessa
- Pierre Fernandez
- Gergely Szilvasy
- Matthijs Douze
- Hervé Jégou
affiliations:
- Meta FAIR
arxiv_id: '2607.13728'
url: https://arxiv.org/abs/2607.13728
pdf_url: https://arxiv.org/pdf/2607.13728
published: '2026-07-15'
collected: '2026-07-16'
category: RecSys
direction: 向量检索索引优化 · 拍卖分配簇
tags:
- vector search
- index partitioning
- probing function
- auction algorithm
- out-of-distribution
- ANN
one_liner: 联合学习平衡分区与神经探测函数，通过拍卖算法优化查询分布下的检索吞吐，OOD 场景提升 4.7 倍吞吐
practical_value: '- 电商搜索推荐中查询与商品嵌入分布常不同（OOD），CwA 可针对性优化索引，在相同召回下大幅提升吞吐，直接降低线上检索成本。

  - 拍卖算法保证分区的均衡性，适合大规模商品向量索引，避免热点簇，减少尾部延迟。

  - 即使线性探测函数也能在 ID 场景超越深度方法，工程上更易部署和推理，可优先尝试轻量模型。

  - 笛卡尔积簇扩展能柔性增加分区粒度，便于在亿级商品库中控制扫描比例与召回平衡。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：现有向量搜索中数据库分区与查询探测函数通常共享同一分配函数，未考虑查询分布偏移，导致 OOD 场景性能大幅下降。

**方法关键点**：
- 将数据库分区与可学习的神经探测函数解耦，直接针对查询分布优化搜索性能。
- 交替优化：（1）梯度下降训练探测函数网络；（2）用并行拍卖算法求解大规模簇分配组合优化，天然保证簇平衡。
- 进一步引入簇的笛卡尔积，提升分区粒度，支持更大规模索引。

**关键结果**：
- OOD 设置下，相同召回时吞吐量比 SOTA 方法提升最多 4.7 倍。
- ID 设置下，仅线性探测函数的 CwA 即超越多数深度神经方法。
