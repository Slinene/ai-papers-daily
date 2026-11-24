---
title: 'The abc index: Exact Retrieval for Learned Sparse Representations'
title_zh: abc 索引：学习稀疏表示的精确检索
authors:
- Rossano Venturini
affiliations:
- University of Pisa
arxiv_id: '2611.28555'
url: https://arxiv.org/abs/2611.28555
pdf_url: https://arxiv.org/pdf/2611.28555
published: '2026-11-21'
collected: '2026-11-24'
category: RecSys
direction: 稀疏检索 · 倒排索引与查询处理
tags:
- learned sparse retrieval
- exact retrieval
- TAAT
- Block-Max MaxScore
- inverted index compression
- dynamic pruning
one_liner: 提出 abc 索引，用硬窗口 TAAT 与块最大 MaxScore 剪枝实现无需调参的精确稀疏检索，索引更小且在高 k 时快于近似索引
practical_value: '- 硬窗口设计可直接迁移到自研倒排索引或向量检索：将 doc-id 空间切成固定对齐块（如 8192），每块累加器常驻 L1 缓存，posting
  只存 16-bit 块内偏移，偏移即累加器槽位，省去解码和窗口搜索，实测比软窗口快约 30%。

  - 在 TAAT 循环内做 Block-Max MaxScore 剪枝，子块最大值按 1024 doc-id 对齐，保证各查询项的 bound 可加和，剪枝收益显著：在
  k=10 时比穷举快 3-4 倍，且保持精确结果，无需像 Seismic 那样为每个 k 建不同索引。

  - 权重存储精度权衡：8-bit 量化文档权重，每 list 使用仿射量化，query 权重折叠进量化参数，每条 posting 仅一次乘加，召回损失 <1%，速度比
  f32 快约 40%；对电商搜索的稀疏模型（如 SPLADE）可用同样方案降低存储和延迟。

  - 文档 ID 重排序采用快速图二分法，只需 5.2s 即可将 doc-id 压缩降低约 32%，并让 dense block 占比提升，节省空间 10% 以上；适合在电商索引构建中替代昂贵的
  Lucene BP，大幅缩短构建时间。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：学习稀疏检索（LSR）模型如 SPLADE 的查询有数十个学习权重项，传统动态剪枝算法失效，近似索引（Seismic、HNSW）被认为更快，但需要调参且索引大。本文用标准 IR 技术组合出精确索引 abc，证明无需近似也能达到竞争性能。

**方法关键点**：
- 硬窗口 TAAT：将 doc-id 空间切成固定对齐块（8192），块内累加器常驻 L1 缓存，posting 只存 16-bit 块内偏移，偏移直接作为累加器槽位，避免解码和比较。
- 块内 Block-Max MaxScore：每块进一步分 8 个子块（1024 doc-id），存储每子块最大权重（8-bit 对齐），查询项边界可加和，在块内对列表分 essential/non-essential，用成本模型决定跳过与探测。
- 压缩布局：稀疏格式用二进制打包（每 8 gap 一组），dense block 存完整权重向量；支持随机访问以探测候选。
- 快速 doc-id 重排序：改进图二分法，仅用 5.2s 比标准 rgbisect 快 19.5 倍，压缩 doc-id 仅大 1.2%。

**关键实验**：在 MS MARCO 四个 LSR 模型（CoCondenser、OS-gte、SparseUp、SPLARE）上对比七个精确索引和两个近似索引。abc-bmms 是最快精确索引，比 Qdrant 快 6.5–84 倍，比 Lucene 快 13–55 倍，比 BMP 快 2.9–18 倍且索引小 5–7 倍。与近似索引相比，k=10 时 Seismic/HNSW 最多快 4.3 倍，但 k=1000 时 abc-bmms 反超 1.7–7.4 倍；构建仅需 13–32 秒，而 HNSW 需 9–27 小时。

**最值得记住的一句话**：精确索引通过硬窗口 TAAT 和块内 Block-Max MaxScore，可在 LSR 上达到近似索引的延迟，且无参数调优，在高 k 时更快、索引更小。
