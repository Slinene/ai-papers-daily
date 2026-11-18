---
title: 'SIMQ: A Single Graph-based Index for Multi-Vector Query'
title_zh: SIMQ：面向多向量查询的单一图索引
authors:
- Yifan Lu
- Jiabao Jin
- Xiaoyao Zhong
- Peng Cheng
- Xiangyu Wang
- Haotian Li
- Hua Chen
- Junqing Chen
- Wei Xi
- Heng Tao Shen
affiliations:
- Tongji University
- Ant Group
- Xi'an Jiaotong University
arxiv_id: '2611.22079'
url: https://arxiv.org/abs/2611.22079
pdf_url: https://arxiv.org/pdf/2611.22079
published: '2026-11-17'
collected: '2026-11-18'
category: Other
direction: 多向量检索 · ANN 索引
tags:
- multi-vector retrieval
- MaxSim
- graph index
- data-aware clustering
- approximate nearest neighbor
- ColBERT
one_liner: 通过数据感知采样聚类与逐 token 图导航，用单一图索引近似 MaxSim，绕开交互矩阵和 GPU 聚类
practical_value: '- 商品/内容多向量表示（如标题、图片、属性各一个 embedding）需要 MaxSim 相似度检索时，可以参考 SIMQ 的「采样聚类
  + 单图索引 + 逐 token 图搜索」架构，避免每 query 计算全量 centroid 交互矩阵，CPU 即可支撑大规模召回。

  - 构建阶段不必做全量 k-means：均匀采样初始中心 → 临时图引导分配 → 超限簇局部二分分裂 → 更新中心，CPU 友好，在 Quora 上构建仅 68s，而
  PLAID 需 4282s；该 trick 可直接用于商品 embedding 聚类或向量库冷启动。

  - 当 proxy 分数区分度低时，SIMQ+ 的「命中计数 + 动态候选集」值得借鉴：用不同 query token 的命中次数替代内积打分，并按 count
  分层截断保留同层 tie，比固定 top-k 更稳健，适合粗排/召回阶段。

  - 图后端可替换为 HNSW/NSG/DPG，方便接入现有向量检索引擎（如 VSAG）；业务中可把该框架作为多向量召回的统一底座，根据场景选图后端。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

动机：ColBERT 等多向量检索模型通过 token 级 MaxSim 取得 SOTA 效果，但精确计算复杂度 O(m·N·p) 在大规模语料上难以扩展。现有近似方案各有硬伤：PLAID 的 centroid 交互矩阵每个 query 都要全量计算，且 k-means 聚类依赖 GPU；MUVERA 的 LSH 分区数据无关，导致 recall 不稳定；IGP 沿用 PLAID 的残差压缩管线；GEM 构建复杂且吃硬件。

方法关键点：
- 数据感知采样聚类：均匀采样 α 比例 token 作为初始中心，建临时图引导剩余 token 分配，超限簇递归二分，最后用簇内归一化均值更新中心，避免全量迭代 k-means。
- 单一图索引：在更新后的簇中心上构建 HNSW 图，查询时对每个 query token 做图搜索检索 nc 个最近中心，通过 Ψ 映射收集候选文档。
- 近似打分：对候选文档用命中的中心内积最大值累加得到 fM，不做全量交互矩阵，最终 top-kr 候选精确 MaxSim 重排。
- SIMQ+：用跨 query token 的命中计数 cnt(d) 替代内积打分，并用动态候选集按 cnt 分层截断保留 tie，缓解细粒度分区下 proxy 分数区分度低导致的排序反转。
- 理论分析：在低维流形和成功检索到正确 cell 假设下，数据感知分区的期望近似误差小于 MUVERA 的 data-oblivious LSH 分区。

关键实验：在 Quora、SciDocs、NQ、HotpotQA、LoTTE-pooled 五个数据集上对比 PLAID、MUVERA、IGP、GEM。构建时间上，Quora 上 SIMQ 仅 68s，PLAID 需要 4282s；SciDocs 上 SIMQ 33s，PLAID 1061s。PAG 聚类在相近 recall 下与 k-means 接近但 QPS 略高（Quora: PAG 0.834 recall/532.7 QPS vs k-means 0.840/516.2），而 LSH 在相同资源下 recall 大幅低于两者。SIMQ+ 相比 SIMQ 在多个数据集上提升了 recall，尤其在 LoTTE、NQ、HotpotQA 上随 nc 增加更明显。图后端可替换为 HNSW/NSG/DPG，验证了框架的模块化。

最值得记住的一句话：用采样聚类得到的细粒度中心和单一图索引，把多向量 MaxSim 检索变成每个 query token 的图近邻搜索，绕开了交互矩阵和 GPU 聚类这两个主要瓶颈。
