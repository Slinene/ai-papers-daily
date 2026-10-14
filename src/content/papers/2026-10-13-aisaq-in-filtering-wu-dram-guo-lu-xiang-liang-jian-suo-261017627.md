---
title: AiSAQ-in-Filtering for DRAM-free Filtered Information Retrieval
title_zh: AiSAQ-in-Filtering：无 DRAM 过滤向量检索
authors:
- Kento Tatsuno
- Daisuke Miyashita
- Kazunari Sumiyoshi
- Hiroaki Yamanaka
- Kosuke Nakata
- Jun Deguchi
affiliations:
- Kioxia Corporation
arxiv_id: '2610.17627'
url: https://arxiv.org/abs/2610.17627
pdf_url: https://arxiv.org/pdf/2610.17627
published: '2026-10-13'
collected: '2026-10-14'
category: Other
direction: 向量检索 · 过滤搜索 · DRAM-free ANNS
tags:
- ANNS
- Filtered Search
- Product Quantization
- DRAM-free
- DiskANN
- SSD Index
one_liner: 提出 LiPQ 将标签与向量联合 PQ 编码，使过滤 ANNS 保持接近零 DRAM 且索引加载快
practical_value: '- 若业务使用 DiskANN/AiSAQ 做向量检索，带类目、品牌、属性等过滤条件时，可采用 LiPQ 把离散标签与 item
  embedding 联合 PQ，标签信息编码进压缩向量，避免标签单独占 DRAM，利于多租户和频繁索引切换。

  - 标签距离用负内积，二进制标签可扩展为 BM25/稀疏关键词权重，实现语义向量 + 关键词混合检索而不额外增加内存；注意 β 需手动调，β 过大时 LiPQ
  量化误差会上升。

  - 实验显示 Zipf 分布标签（贴近电商头部类目/品牌）比 uniform 更体现 LiPQ 优势，长尾标签 recall 提升最多 55%，可优先在长尾过滤属性上验证。

  - 索引加载时间从分钟级降到毫秒级（uniform 标签 SIFT1M 从约 970 秒降到 10.1 ms），对实时索引切换、多租户 SaaS 检索服务有直接价值。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
大规模向量检索中，过滤搜索（filtered search）需要同时处理向量和标签，DRAM 占用随数据规模增长成为显著成本。DiskANN 把 PQ 压缩向量放 DRAM，Filtered-DiskANN 把标签也放 DRAM；AiSAQ 将 PQ 向量卸载到 SSD 实现接近零 DRAM，但直接移植过滤会重新引入标签 DRAM 或增大 SSD 占用。

## 方法关键点
- **LiPQ（Label-inclusive Product Quantization）**：将每个对象的数据向量 𝒗 与标签向量 𝒂 按同一 M 切分，在子空间内对 (𝒗_m, 𝒂_m) 对做 K-means 聚类；距离用融合距离 dF = d(𝒗1,𝒗2) + β·dL(𝒂1,𝒂2)，其中标签距离为负内积。这样编码后 PQ 字节数不变，不增加额外存储。
- **索引与搜索**：PQ 向量和标签都写到 SSD，节点 chunk 保留全精度标签用于最终 rerank；DRAM 使用量接近零，索引切换快。
- **扩展性**：标签向量可为二进制或连续稀疏向量（如 BM25 分数），支持语义+关键词混合检索，而不仅是离散属性过滤。

## 关键实验
在 SIFT1M 128d 和 KILT E5 1M 1024d（e5-large-v2 embedding KILT KB）上，对比 Filtered-DiskANN（已移植到 AiSAQ）。
- **Zipf 分布标签**：单标签搜索 recall@1 约 90%，比 Filtered-DiskANN 最高提升 55%，磁盘 I/O 更少；minor label（label 10）优势最明显，长尾标签召回显著高于 baseline。
- **Uniform 标签**：SIFT1M 上 DRAM 从 2030.1 MB 降到 26.0 MB（约 1/78），索引加载时间从 9.70×10^5 ms 降到 10.1 ms；KILT E5 上召回略低，但加载时间优势仍然巨大。
- **消融**：β=0 时召回大幅下降，说明标签信息被有效利用；但在 uniform 标签的 KILT 数据上召回不如 Filtered-DiskANN，多标签搜索效果也较差。

## 最值得记住的一句话
把过滤标签融入 PQ 编码，让属性过滤不再额外占 DRAM，在长尾标签分布下能提升召回并大幅降低索引切换成本。
