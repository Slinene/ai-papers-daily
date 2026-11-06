---
title: 'GINGER: Spicing Up Graph-Based Vector Search'
title_zh: GINGER：用嵌套量化与图压缩加速图向量搜索
authors:
- Daniel Salwasser
- Lars Gottesbüren
- Laxman Dhulipala
- Jakub Łącki
- Guy Blelloch
- Rajesh Jayaram
- Tobias Rubel
- Kshiteej Sheth
- Amir Zandieh
- Vahab Mirrokni
affiliations:
- Google Research
- KIT
- UMD
- CMU
- EPFL
arxiv_id: '2611.08306'
url: https://arxiv.org/abs/2611.08306
pdf_url: https://arxiv.org/pdf/2611.08306
published: '2026-11-05'
collected: '2026-11-06'
category: RecSys
direction: 向量检索 · 图索引 · 量化压缩
tags:
- ANNS
- Graph Index
- Quantization
- SIMD
- Graph Compression
- Vector Search
one_liner: 开源图向量检索库 GINGER 通过嵌套 TurboQuant 与图压缩，在 95% 召回下平均比最快竞品快 1.8 倍且内存更低
practical_value: '- 多级召回/粗排/精排架构中，可借鉴 NTQ 的“单一码字”设计：用 4-bit 前缀做快速导航或粗筛，剩余 bit 做高精度重排，避免为不同阶段维护多套向量，能大幅降低内存和带宽；在电商
  item embedding 或广告用户向量上，可尝试用旋转 + 高斯 Lloyd-Max 量化，12-bit 即可接近 float 精度。

  - beam search 的候选预过滤思路值得迁移到粗筛阶段：用一个便宜且不要求与导航距离可比的 sketch（如 Hamming 距离、低维前缀）先 gate
  候选，阈值按 beam 尾部分数动态更新。这在召回中相当于用轻量模型或量化表示做门控，能减少精排算力消耗。

  - 对大规模 user-item 近邻图或商品关系图，可用递归图划分重排 ID + gap 编码无损压缩邻接表约 2x，且不降低查询吞吐；适合低维 dense
  embedding 或图召回场景，尤其在内存受限的在线服务中。

  - 工程实现上可直接复用：SIMD 查表 + 软件预取隐藏 DRAM 延迟；用有序数组替代优先队列并批量合并候选；对量化码本用分段多项式拟合避免内存 gather，能把重排延迟减半。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
大规模 embedding 检索中，图索引已成为高召回场景的主流，但查询吞吐受内存带宽限制，索引内存占用和构建时间仍是瓶颈。已有 PiPNN 解决构建，GINGER 聚焦同时提升搜索吞吐和内存效率。

**方法关键点**  
- **Nested TurboQuant (NTQ)**：在 TurboQuant 的 4-bit 高斯 Lloyd-Max 码本基础上，将每个 4-bit 区间嵌套细分为 2^k 个子区间，形成 (4+k)-bit 码。导航用前 4-bit 前缀，重排用完整码；一个码字同时服务两级，避免存两套向量。12-bit 时内存为 float 的 1/2.6，精度接近浮点。
- **快速 SIMD 评分**：4-bit 导航码用 pshufb 查表 + vpdpbusd 做 int8 点积；重排用分段三次多项式在寄存器内计算码本值，避免内存 gather，10/12-bit 重排延迟减半。
- **搜索优化**：PCA 降维导航，投影矩阵行也量化到 4-bit；TurboSlice 用旋转后向量前缀作为 sketch，1-bit JL 用 Hamming 距离，两者作为保守 gate，阈值按 beam 尾部均值动态更新；beam 管理用有序数组加批量合并替代优先队列。
- **图压缩**：递归图划分重排顶点 ID 减小邻接 gap，配合 AdaptiveGap 亚字节位宽编码，保留 StreamVByte 的单次 shuffle 解码；图内存平均压缩 2.1x（最多 2.5x），不拖慢查询。

**关键实验**  
在 14 个公开数据集（最高 10 亿向量、4096 维）上对比 7 个库。95% recall 下 GINGER 平均比每个数据集最快竞品快 1.8x，高维平均 2.0x，最大 2.7x；13/14 数据集 QPS 最高。高维 12-bit NTQ 索引内存平均为原始向量的 43%，而 SVS 虽内存小 19.8% 但慢 2.9x。使用 PiPNN 构建时 11/14 数据集最快，十亿级平均构建 35 分钟，比 Faiss 快 2.0x。

**最值得记住的一句话**  
在召回链路中，一套嵌套量化码可以同时承担粗筛与精排，图邻接表也能通过重排 + gap 编码无损压缩，SIMD 友好的设计是兼顾内存与吞吐的关键。
