---
title: 'A Comprehensive Empirical Evaluation of Vector Database Systems for Approximate
  Nearest Neighbor Search: Performance, Quality, and Resource Trade-offs'
title_zh: 向量数据库近似最近邻搜索综合评测：性能、质量与资源权衡
authors:
- Ashen Rashmiks
- Tiroshan Madushanka
affiliations:
- University of Kelaniya
arxiv_id: '2608.12812'
url: https://arxiv.org/abs/2608.12812
pdf_url: https://arxiv.org/pdf/2608.12812
published: '2026-08-13'
collected: '2026-08-16'
category: Eval
direction: 向量数据库 ANNS 基准评测
tags:
- Vector Database
- ANN Search
- Benchmark
- RAG
- Latency
- Throughput
one_liner: 在6个数据集上评测7个向量数据库，揭示FAISS吞吐最高、Weaviate召回最好、Qdrant延迟最低，并开源框架
practical_value: '- 在电商/RAG/推荐系统中，向量检索是高频依赖，选型时可参考评测结论：追求极致吞吐选 FAISS（但需自建数据库管理）；需要开箱即用高召回选
  Weaviate；对延迟敏感选 Qdrant；快速冷启动/索引构建选 LanceDB。

  - 作者开源了基准测试框架，可将自家业务数据集和查询负载直接套用，横向对比候选向量库在真实 query 分布下的 Recall@K、P99 延迟、内存/存储占用，避免盲目选型。

  - 关注 cold-start latency（首次查询或容器冷启动）指标，对在线服务弹性扩缩容和 serverless 部署有实际参考价值；评测显示部分系统冷启动开销差异大。

  - 结合资源消耗（索引构建时间、内存、存储）与查询性能做权衡：LanceDB 通过牺牲召回换取极快索引构建，适合频繁重建索引或数据快速流入的场景，如实时用户行为
  embedding 更新。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：向量数据库已成为 RAG、语义搜索和推荐系统的关键基础设施，但缺乏覆盖检索质量、延迟、吞吐和资源消耗的全面可复现基准。

**方法**：系统评测 7 个主流向量数据库：FAISS、Qdrant、Milvus、Weaviate、Chroma、pgvector、LanceDB。使用 6 个数据集（SIFT、GIST、MS MARCO、GloVe 等），覆盖 400 万+ 向量，维度 96-960。测量 15 个指标，包括 Recall@K、Precision@K、MRR、NDCG@K、Hit Rate@K（质量），延迟分位数、QPS、冷启动延迟（查询性能），以及索引构建时间、内存、存储（资源消耗）。

**关键结果**：在 SIFT1M 上，FAISS 单节点吞吐最高 866 QPS，但缺乏数据库管理功能；Weaviate 开箱即用召回率 >99%；Qdrant 在完整数据库中延迟最低（中位数 4.55 ms）；LanceDB 索引构建显著更快但检索质量下降。综合权衡后给出选型指南，并开源基准测试框架。
