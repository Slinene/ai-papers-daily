---
title: 'RemoteANN: A Native Vector Search Engine for Cloud Object Storage'
title_zh: RemoteANN：面向云对象存储的原生向量搜索引擎
authors:
- Yutong Gou
- Silu Huang
- Yue Wang
- Jianjun Chen
- Cheng Long
affiliations:
- Nanyang Technological University
- ByteDance
arxiv_id: '2610.25172'
url: https://arxiv.org/abs/2610.25172
pdf_url: https://arxiv.org/pdf/2610.25172
published: '2026-10-18'
collected: '2026-10-20'
category: Other
direction: 云对象存储上的向量检索系统
tags:
- Vector Search
- Cloud Object Storage
- IVF
- RaBitQ
- Request Merging
- Caching
one_liner: 通过 IVF+RaBitQ 量化与数据重排序、请求合并等协同设计，大幅降低云对象存储向量搜索的 I/O 与 API 请求成本
practical_value: '- 若将大规模 embedding 卸载到 S3 等对象存储以降低存储成本，应优先采用 IVF 类索引而非图索引：图索引多跳路由会叠加网络
  TTFB，IVF 单轮拉取候选簇更适合高延迟远程存储。

  - 借鉴 RaBitQ 量化思路：将向量压缩为 1-bit prefix 常驻内存用于粗筛和距离估计，其余低精度码放远程存储，可大幅减少远程请求，适合嵌入召回的大规模粗排阶段。

  - 数据重排序 + 请求合并是降低 API 调用费用的关键：对簇按质心最近邻路径排序（近似 Hamiltonian path），簇内按到质心距离排序，使查询目标范围局部集中，再用动态规划合并
  Range-GET 请求，可迁移到任何按请求计费的远程数据读取场景。

  - 本地 NVMe SSD 缓存采用自适应阈值：当请求范围大于阈值时整簇下载填充缓存，平衡带宽与缓存命中率，适合电商热门商品/用户 embedding 的冷热分层访问。

  - QGKMeans 用 SymphonyQG 加速 k-means 质心分配，索引构建时间可降低数倍，适用于需要频繁重建向量索引的业务（如商品库更新、A/B
  测试多版本索引）。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
云对象存储（如 Amazon S3）具有高扩展性和低成本，越来越多向量数据库采用存储-计算分离架构，将主向量数据放在对象存储，计算节点仅保留紧凑索引元数据。但传统向量索引未针对云对象存储的高 TTFB 网络延迟和按请求数计费特性优化，导致图索引多跳路由性能退化、请求数激增、API 成本高。

**方法关键点**
- **索引构建**：采用 IVF 索引 + RaBitQ 量化，1-bit prefix 常驻 DRAM 用于剪枝，8-bit suffix 存对象存储；提出 QGKMeans 用 SymphonyQG 加速 k-means 质心分配，显著降低聚类时间。
- **数据重排序**：簇间按质心最近邻路径（近似 Hamiltonian path）重排，提高目标簇空间局部性；簇内按到质心距离排序，使难剪枝的外围向量集中，便于范围下载。
- **查询优化**：利用 RaBitQ 理论误差界进行簇级剪枝，减少远程请求；对未剪枝簇执行细粒度 Range-GET 只下载候选字节范围；用动态规划合并相邻请求，最小化请求数与下载量；本地 NVMe SSD 缓存热簇，并用自适应阈值在范围下载与整簇下载间切换以兼顾缓存填充。

**关键结果**
在 SIFT、MSong、Contriever、GIST、MXBAI、OpenAI 六个百万级数据集及 Cohere、Deep-1B 大规模数据集上，对比 Lance-RQ 和 RemoteSPANN。在 97% 目标召回下，RemoteANN 吞吐最高提升 5.9×，对象存储请求数最多减少 16.1×；p50/p95 延迟显著低于基线；索引构建比 RemoteSPANN 快达 31×。

**核心结论**
通过算法-系统协同设计，RemoteANN 在不牺牲召回率的前提下，系统性地缓解了云对象存储向量搜索的 I/O 瓶颈与 API 成本问题。
