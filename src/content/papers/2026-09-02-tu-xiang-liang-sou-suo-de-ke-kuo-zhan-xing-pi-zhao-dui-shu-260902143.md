---
title: 'A Power Law in Logarithm''s Clothing: On the Scalability of Graph-Based Vector
  Search'
title_zh: 图向量搜索的可扩展性：披着对数外衣的幂律
authors:
- Sajad Faghfoor Maghrebi
- Navid Eslami
- Niv Dayan
affiliations:
- University of Toronto
arxiv_id: '2609.02143'
url: https://arxiv.org/abs/2609.02143
pdf_url: https://arxiv.org/pdf/2609.02143
published: '2026-09-02'
collected: '2026-09-03'
category: Other
direction: 向量检索 · 图索引扩展性
tags:
- vector search
- HNSW
- scalability
- intrinsic dimensionality
- power law
- ANN
one_liner: 实测发现图向量搜索成本在数据规模小于内在维度时呈次线性幂律增长，之后才转入多对数增长，并给出统一理论模型
practical_value: '- 容量规划：若数据规模 N 未达到由内在维度决定的临界点，搜索延迟/算力按 N^c（0<c<1）增长而非多对数；电商/推荐团队做向量库扩容预算时不能假设对数级成本，可用论文模型估计
  c 和临界规模。

  - 内在维度监控：数据集内在维度随规模增大而升高，导致查询邻域更密集；可在 embedding 上线前/后持续测量 intrinsic dimensionality，预测搜索成本拐点。

  - 索引调参：论文提供预测不同 recall target 和索引配置下 power-law 指数的模型，可用来在 M、efSearch、efConstruction
  等参数间做 cost-recall 权衡，适合高召回场景（广告召回、相关商品召回）提前规划。

  - 评估方法借鉴：做 ANN 基准应跨多个数量级规模测试，而不是只在单点规模测量成本。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**  
向量数据库依赖图索引（HNSW、Vamana）做近似最近邻搜索，业界普遍认为搜索成本随数据集规模 N 呈多对数增长，但该结论只在特殊条件下证明过，实际索引未经验证，标准基准也常只在单一规模测量。

**方法关键点**  
作者跨多个数量级数据集规模进行实测，分析内在维度随规模的变化，并提出 beam search 成本的统一理论。该理论证明在 N 小于数据内在维度时搜索成本按 N^c 增长（0<c<1），称为次线性幂律；当 N 超过由内在维度决定的临界规模后，增长转为次多项式（与多对数一致）。同时给出预测任意 recall 目标和索引配置下幂律指数的模型。

**关键结果数字**  
次线性幂律在所有测试数据集、所有 recall 目标、查询难度和索引配置下均出现，且在多数数据集上持续到其完整规模；两个规模足够大（相对内在维度）的数据集观测到向次多项式增长的切换。内在维度随规模增大而升高，直到数据充分解析其底层分布，这是两种行为统一机制。
