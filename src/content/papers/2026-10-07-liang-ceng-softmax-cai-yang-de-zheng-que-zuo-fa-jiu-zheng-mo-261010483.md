---
title: 'Two-Level Softmax Sampling Done Right: Correcting Bias from Size Imbalance
  and Dispersion'
title_zh: 两层 Softmax 采样的正确做法：纠正规模不平衡与离散度偏差
authors:
- Walid Bendada
- Guillaume Salha-Galvan
affiliations:
- Spotify
- SJTU Paris Elite Institute of Technology
arxiv_id: '2610.10483'
url: https://arxiv.org/abs/2610.10483
pdf_url: https://arxiv.org/pdf/2610.10483
published: '2026-10-07'
collected: '2026-10-09'
category: RecSys
direction: 推荐候选采样 · 两层 softmax 修正
tags:
- two-level softmax
- sampling bias
- candidate sampling
- embedding retrieval
- softmax approximation
one_liner: 提出 S-2LS 和 SD-2LS，修正标准两层 softmax 采样忽略簇规模不平衡与簇内离散度的偏差，几乎无额外计算开销
practical_value: '- 在电商/广告大规模候选召回中，如果采用两阶段 softmax（先 cluster 后 item），注意标准 2LS 的 cluster
  概率不是 item 聚合概率；对 cluster 打分时可直接加 log|C| 做 size 校正，避免热门大簇被系统性低估。

  - SD-2LS 进一步校正簇内相似度离散度，推荐用 cluster 内 log-sum-exp（而非质心点积）近似 cluster 的 softmax 质量；若担心计算量，可预计算每个
  cluster 的 dispersion 项，工程开销可忽略。

  - 作为产品 embedding 检索、短视频/商品候选采样、负采样训练中的替代方案，S-2LS/SD-2LS 能降低两阶段采样偏差，提升召回质量与采样保真度。

  - 业务中若簇大小极不平衡（头部类目 vs 长尾类目），优先用 S-2LS；若同簇 item embedding 方差大（同簇商品跨价格带/风格），用 SD-2LS。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：exact softmax 采样复杂度与 item 数量线性相关，大规模推荐/检索中不可行。两层 softmax（2LS）采样能实现子线性时间，但会因忽略簇规模不平衡和簇内相似度离散度而产生系统性偏差。

**方法关键点**：
- 标准 2LS 先将 item 分簇，再先采簇后采簇内 item，但 cluster 打分直接用质心相似度，导致簇被错误加权。
- S-2LS 通过校正簇大小（如加入 log|C| 项）修复规模不平衡偏差。
- SD-2LS 同时校正簇大小和簇内 item 相似度离散度，使 cluster 级概率更接近真实 item 聚合 softmax 质量。
- 两种方法都带来可证明更好的 softmax 近似，且计算开销可忽略，适合直接替换。

**关键结果数字**：在 5 个大规模数据集上验证了改进后的采样性质；论文未提供具体数值指标，但一致性优势明确。
