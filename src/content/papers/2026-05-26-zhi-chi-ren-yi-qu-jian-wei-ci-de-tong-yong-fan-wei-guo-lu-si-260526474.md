---
title: 'Generalized Range Filtering Approximate Nearest Neighbor Search: Containment
  and Overlap [Technical Report]'
title_zh: 支持任意区间谓词的通用范围过滤近似最近邻搜索
authors:
- Yingfan Liu
- Tong Wu
- Jiadong Xie
- Yang Zhao
- Jeffrey Xu Yu
- Jiangtao Cui
affiliations:
- Xidian University
- The Chinese University of Hong Kong
- Hong Kong University of Science and Technology (Guangzhou)
- Xi'an University of Posts and Telecommunications
arxiv_id: '2605.26474'
url: https://arxiv.org/abs/2605.26474
pdf_url: https://arxiv.org/pdf/2605.26474
published: '2026-05-26'
collected: '2026-05-27'
category: Other
direction: 向量检索 · 范围过滤 ANN 搜索
tags:
- approximate nearest neighbor
- range filtering
- proximity graph
- segment tree
- vector search
- index compression
one_liner: 提出多段树图 MSTG，统一处理包含、重叠等任意区间谓词的向量检索，性能最高比通用方法快 12.5 倍
practical_value: '- 电商搜索中商品向量 + 价格/时间区间等组合查询可直接借鉴 MSTG 的索引设计：为每个离散的属性前缀构建段树，每个树节点维护一个接近图（HNSW），查询时动态合并相关
  PG，避免扫描不满足谓词的向量。

  - 标签化增量压缩方法能将多个时间切片的索引合并为单个带生命周期标签的 HNSW，大幅减少内存占用，适合需维护多个过滤条件的在线推荐场景。

  - 复合区间谓词（如包含 + 重叠）可通过至多两个异构 MSTG 变体索引和两次搜索完成，工程上可避免为每种谓词组合重建索引。

  - 在时间相关性推荐（如近期浏览商品的相似推荐）中，可借鉴 TSANN 支持：将时间戳作为区间属性，快速检索“包含某时间点”的向量集合，比现有 TS‑Graph
  高效且省空间。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
现有近似最近邻（ANN）搜索与数值过滤的结合大多只支持点值或简单范围条件，现实中常见的区间包含、重叠等组合谓词（如“价格在 50–100 且区间与商品价格区间重叠”）缺乏高效统一索引。该问题被定义为广义区间‑区间过滤 ANN（RRANN），覆盖了 RFANN、IFANN、TSANN 等特例，在电商、时间序列分析等场景有广泛应用。

## 方法
- **多段树图（MSTG）**：按对象区间的下界排序，为每个前缀构建一棵基于上界的段树，每棵段树的节点存储一个接近图（默认 HNSW）。
- **查询处理**：根据查询区间下界定位对应段树，再在段树中检索满足上界条件的节点，合并节点 PG 后执行标准 ANN 搜索，完全避开不满足谓词的向量。
- **增量标签压缩**：通过为每条边附加生命周期标签 `(开始前缀, 结束前缀)`，将多次插入导致的重复图合并为单一 HNSW，使总索引大小与 iRangeGraph 持平（O(n m log|A|)），且支持增量构建。
- **四类原子谓词支持**：仅需两个方向的 MSTG 变体（按下界升序和按上界降序构建），即可处理任意析取组合的区间谓词，至多两次搜索完成。

## 关键实验
在 Sift、Gist、WIT‑Image、Paper、Redcaps 五个真实数据集上评估，RR 谓词为 1○∨2○∨3○∨4○（区间相交）。对比 ACORN、Milvus、Pre‑/Post‑filtering 等通用方法，以及 iRangeGraph（RFANN）、Hi‑PNG（IFANN）、TS‑Graph（TSANN）等专用方法。结果：
- **RRANN 场景**：MSTG 在 recall@10=0.99 且选择性 5% 时，QPS 是 ACORN‑γ 的 5.2–12.5 倍，是唯一能在高召回下保持高吞吐的方法。
- **RFANN 场景**：MSTG 与 SOTA iRangeGraph 性能相当，索引构建时间和大小接近。
- **IFANN 场景**：MSTG 的 QPS 显著优于 Hi‑PNG（如 Gist 上 1000+ vs 150+），因避免了多次子查询和对不满足谓词向量的无效距离计算。
- **TSANN 场景**：MSTG 的 QPS 和召回均远超 TS‑Graph，且索引构建时间减少 4 倍以上（Gist：2300s vs >10000s），索引大小仅 1.21GB vs 11.44GB。

**最值得记住的一句话**：通过段树与前缀排序的组合，MSTG 在理论上保证了仅与谓词匹配的向量参与图搜索，从而以接近普通 ANN 的搜索复杂度支持任意复杂区间过滤，且索引成本可控。
