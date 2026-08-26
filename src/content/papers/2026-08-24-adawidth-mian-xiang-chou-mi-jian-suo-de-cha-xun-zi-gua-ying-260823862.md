---
title: 'AdaWidth: Query-Adaptive Embedding Width for Dense Retrieval'
title_zh: AdaWidth：面向稠密检索的查询自适应嵌入宽度
authors:
- Shubing Yang
- Dongfang Zhao
affiliations:
- University of Washington
arxiv_id: '2608.23862'
url: https://arxiv.org/abs/2608.23862
pdf_url: https://arxiv.org/pdf/2608.23862
published: '2026-08-24'
collected: '2026-08-26'
category: Other
direction: 稠密检索 · 查询自适应嵌入宽度
tags:
- Dense Retrieval
- Embedding Compression
- Query-Adaptive Width
- Orthogonal Adapter
- Matryoshka
- Ranking Stability
one_liner: 正交前缀适配器加查询路由器，在共享前缀下按查询分配嵌入宽度，匹配 SOTA 且维度减少 55%-84%
practical_value: '- 双塔召回/商品搜索中，可以冻结已上线 encoder，加 Householder/WY 正交适配器对 query/item
  共同旋转，保证全宽内积不变、全宽 KPI 不变；item 离线旋转一次，在线只算前缀，风险低。

  - 在线先做 64 维前缀召回/排序，路由器只读已有排序的 score gap、熵等 rank-order 特征，判断是否不稳定；只对 top ρ 的 query
  升级到 128/256 维，平均维度下降且无需额外 encoder 前向。

  - 容量规划可参考 prefix sufficiency：所需维度随语料规模对数增长、随检索深度对数下降；大促候选池膨胀时不用线性扩维，可按 log N 调整。

  - 低资源场景用 F=8 的 Householder 适配器仅约 13.8K 参数，比 dense adaptor 少 50-280 倍，效果仍领先 baselines，适合轻量部署。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
高维 embedding 是稠密检索、搜索、推荐与 RAG 的基础表示，但线上实时评分成本与维度成正比。不同 query 稳定排序所需维度差异很大，固定宽度必须迁就最难 query，造成大量冗余计算。现有方法要么全局截断前缀，要么做 query-specific 非连续选维，但索引仍要存全宽、散射读取成本高。

**方法关键点**
- AdaWidth 冻结编码器，插入两个组件：正交前缀适配器与 per-query 前缀路由器。
- 适配器用 Householder 反射乘积的 compact WY 参数化学习正交旋转 R，对 query/doc 同旋，保留全宽内积，只把判别信号集中到前导坐标；训练目标包含多宽度对比损失与全宽分数/几何保持。
- 路由器仅读 stage-1 64 维排序的 order statistics，包括 σ10−σ11、熵、有效候选数等 18 个特征，用梯度提升树预测扩宽收益，只对预测不稳定 query 重排到更宽前缀。
- 理论前缀充分性分析表明：所需维度由 cutoff 处第 k 个最强竞争文档的 order statistic 决定，随 corpus size 对数增长、随检索深度对数下降。

**关键实验与结果**
在 6 个检索任务、5 个冻结 encoder 上对比 prefix truncation、Matryoshka-Adaptor、SMEC、Learning-to-Select。AdaWidth 几乎在所有共享操作点领先；匹配 SOTA 维度缩减方法的 NDCG@10 时，每查询少用 55%-84% 维度。32/48 维时，Matryoshka-Adaptor 需要 2.36x/3.04x 宽度才能达到 AdaWidth。适配器容量不敏感，F=8 时参数仅 13,824，仍领先最强 baseline 超过 7 个 NDCG@10。

**最值得记住的一句话**
正交旋转不改变全宽检索质量，只做判别信息的“能量压缩”到前缀，再用已有排序的 rank-order 特征决定是否扩宽，这是低风险、高收益的 embedding 降本路径。
