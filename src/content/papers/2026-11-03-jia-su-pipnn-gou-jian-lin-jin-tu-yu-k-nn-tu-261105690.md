---
title: Turbocharging PiPNN for Proximity and $k$-NN Graph Building
title_zh: 加速 PiPNN 构建邻近图与 k-NN 图
authors:
- Tobias Rubel
- Richard Wen
- Guy Blelloch
- Laxman Dhulipala
- Lars Gottesbüren
- Jakub Łącki
- Vahab Mirrokni
affiliations:
- University of Maryland
- Carnegie Mellon University
- Google Research
arxiv_id: '2611.05690'
url: https://arxiv.org/abs/2611.05690
pdf_url: https://arxiv.org/pdf/2611.05690
published: '2026-11-03'
collected: '2026-11-05'
category: Other
direction: ANNS 索引与 k-NN 图构建
tags:
- ANNS
- k-NN graph
- quantization
- GEMM fusion
- GPU
- PiPNN
one_liner: PiPNN II/GPiPNN 用量化融合 Top-K GEMM 内核，在 CPU/GPU 上把 ANNS 索引与 k-NN 图构建提速数倍到数十倍
practical_value: '- 向量库构建链路：商品/用户 embedding 频繁更新时，PiPNN II 的构建速度可在分钟级重建十亿索引，使近实时索引成为可能，避免
  HNSW/Vamana 增量构建瓶颈。

  - 量化距离计算融合 top-k：在 GPU/CPU 召回粗排或聚类分配中，不要先物化 M×N 距离矩阵再做 top-K；直接 i8/TQ4 + wgmma/vpdpbusd
  在寄存器做 displacement sort，减少显存/带宽。

  - GPU 批量候选生成：把不规则的递归分片/桶拍平为 radix sort + 固定 score tile + segmented top-K，适合 kernel
  一次处理大量大小不一的子问题；可迁移到多路召回、类目分桶相似度计算。

  - 直接 k-NN 图构建：Item2vec / 语义邻居 / 聚类任务可借鉴 leaf 直接产出 top-k 邻居，省去 build-then-search
  双份开销；对高维 embedding 效果显著。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：图索引 ANNS 查询快但构建慢；PiPNN 已用分区替代构建期 beam search，但保留 FP32、物化距离矩阵，没有吃满硬件。快速构建对数据漂移、参数扫描、聚类/异常检测中的 k-NN 原语重要。

**方法关键点**：
- **量化**：TQ4/RSQ8 将向量压缩到 4/8 bit，构建期用 i8 整数内积，附带 norm/scaling 修正。
- **融合 kernel**：GEMM 与 top-K 在寄存器完成，CPU 用 VNNI vpdpbusd + panel 布局 + displacement sort；GPU 用 wgmma + segmented top-K，不再写 M×N distance matrix。
- **CPU PiPNN II**：AssignLeaders 对 K=1/3/10 特化；Leaf Top2 只算下三角并对称更新两个 tracker。
- **GPU GPiPNN**：递归转两轮 assign + radix sort；桶重排为固定 score tile；HashPrune 锁改为 sort-and-merge；DirectEdgePrune 避免 candidate 重算。
- **k-NN**：直接从 leaf 输出 top-k，省去 build-then-search。

**关键实验**：12 个数据集，最大 10 亿点（GPU 1 亿）。CPU 上 PiPNN II 较 PiPNN 快至 8×，较量化 Vamana 几何平均 5.9×、FP32 Vamana 40.7×；10-NN 图 10 亿点 <16 分钟。GPU 上比 Jasper 快至 43.7×、比 CAGRA 快 50×；10-NN 较 NN-Descent 快 6.6×。量化后 QPS/recall 曲线与 FP32 几乎重叠。

最值得记住：把图构建从 random-access graph search 变成 partition-local、dense、quantized、fused top-K 矩阵乘法，是同时吃满 CPU/GPU 的关键。
