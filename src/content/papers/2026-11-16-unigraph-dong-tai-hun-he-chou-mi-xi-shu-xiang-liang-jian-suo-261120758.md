---
title: 'UniGraph: A Unified Graph-based Index for Dynamic Hybrid Dense-Sparse Vector
  Retrieval'
title_zh: UniGraph：动态混合稠密稀疏向量检索的统一图索引
authors:
- Keyu Chen
- Xiaoyao Zhong
- Jiabao Jin
- Peng Cheng
- Wangze Ni
- Jingkuan Song
- Heng Tao Shen
affiliations:
- Tongji University
- Zhejiang University
arxiv_id: '2611.20758'
url: https://arxiv.org/abs/2611.20758
pdf_url: https://arxiv.org/pdf/2611.20758
published: '2026-11-16'
collected: '2026-11-17'
category: Other
direction: 统一图索引 · 混合稠密稀疏检索
tags:
- hybrid retrieval
- graph-based index
- ANNS
- dense-sparse fusion
- dynamic weight
- pruning
one_liner: 通过合并多 α 邻域构建统一混合图，在不重建索引下支持查询级权重，Recall@100≥0.95 时 QPS 提升 27.6%–52.3%
practical_value: '- 电商搜索/广告混合召回：已有 dense embedding + 稀疏词权（BM25/SPLADE）时，可用 UniGraph
  替代两路召回+重排。按 α∈{0,0.1,...,1} 采样每个 item 的 top-kg 邻居，按出现频率合并并保留 top-M 出边；线上一个图支持不同
  query weight，避免单路 top-k 漏召回。离线用现有 dense/sparse 索引生成候选，避免全量 pairwise 距离；存储仅比双索引多约
  5%。

  - 在线 serving 做 dense-first pruning：先算 cheap 的 dense 距离，再用 Cauchy-Schwarz 下界 Ls=1-||qs||·||xs||
  估计 hybrid distance；item sparse norm 预计算，query norm 一次计算，γ=0.3 时平均 QPS 提升 10.3%，recall
  损失 <0.06 个百分点。适合 CPU 检索服务化。

  - 按 query weight 路由 entry point：α≤0.5 时用 sparse index 初始化 beam search，α>0.5 时用 dense
  index；在电商 Query 理解或融合权重可得的场景，可做 coarse-to-fine guided search，显著提升 recall 与效率。该策略不绑定具体图索引实现，可复用到现有
  HNSW/倒排候选召回链路。

  - 如果线上融合权重 α 动态变化（例如模型为每个 query 预测 dense/sparse 比例），不要为每个 α 建图；使用多 α 邻域覆盖的统一图，可稳定支持动态权重，且比固定权重图
  QPS 提升 4.5%–26.7%。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
混合稠密-稀疏检索能结合语义与词法信号，但常见两路召回先各取 top-candidates 再重排，容易漏掉单路不靠前、融合后才进入 top-k 的 item；固定权重图又无法适应查询级 α。因此需要一个图索引直接按 query-specific hybrid distance 搜索，且不用每次重建。

**方法关键点**
- α-cover 构建：在 α∈{0,0.1,...,1} 上分别取每个 item 的 top-kg hybrid neighbors，合并后按出现频率排序，保留最多 M 个出边，形成 Unified Hybrid Graph。
- 搜索：beam search 直接使用查询级 α 的混合距离；根据 α≤0.5 或 >0.5 选择 sparse/dense guide index 获取 entry points，做 coarse-to-fine。
- 加速：dense-first pruning。先算 dense distance，再用 Cauchy-Schwarz 下界 Ls=1-||qs||₂||xs||₂ 估计 hybrid distance；用缩放系数 γ=0.3 控制剪枝强度，若估计值 ≥τ 则跳过 exact sparse inner product。

**关键实验**
在 5 个 BEIR 数据集（NQ、HotpotQA、MS MARCO、FEVER、DBpedia-Entity，BGE-M3 1024d dense + sparse）上，对比 HNSW+SINDI、Naive/Opt Hybrid、LADR 等。mixed α∈[0.3,0.7] 下，Recall@100≥0.95 时 UniGraph 的 QPS 比最快 baseline 高 27.6%–52.3%；fixed α 下是 fastest baseline 的 1.18×–2.85×。消融：guided entry point 提升 Recall 约 7–12 个百分点；pruning 平均提升 QPS 10.3%，recall 损失 <0.06 个百分点；multi-weight 构图比固定 α=0.5 图 QPS 提升 4.48%–26.71%。

**最值得记住的一句话**
同一对象的多模态表示部分相关，离散采样多个融合权重的邻域并合并成单图，是支持动态融合权重检索的关键。
