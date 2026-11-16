---
title: 'StreamEmbed: Real-Time Indexing from Pixels for Screenshot Retrieval'
title_zh: StreamEmbed：基于像素差的截图实时增量索引
authors:
- Dayoon Ko
- Yichuan Wang
- Soyeong Jeong
- Joseph E. Gonzalez
- Gunhee Kim
- Sewon Min
arxiv_id: '2611.18516'
url: https://arxiv.org/abs/2611.18516
pdf_url: https://arxiv.org/pdf/2611.18516
published: '2026-11-13'
collected: '2026-11-16'
category: Multimodal
direction: 多模态检索 · 增量视觉嵌入
tags:
- Screenshot Retrieval
- Incremental Embedding
- KV Cache
- Token Pruning
- Visual Memory
- Real-time Indexing
one_liner: 用空间 token 剪枝与时间 KV 复用实现截图实时视觉嵌入加速
practical_value: '- 在电商/Agent 场景中，用户行为截图、商品详情页快照、广告落地页监控等视觉流可借鉴像素差异做增量嵌入：只对变化区域计算
  token，未变区域复用 KV cache，显著降低实时编码成本。

  - 空间 token 剪枝（跳过与邻近块重复的 token）与时间 KV 复用（跨帧缓存未变块的 key/value）可组合推广到视频帧、直播间画面、App 屏幕录制等多模态流式索引，尤其适合端侧或本地执行。

  - 用小规模 learned adapter 补偿剪枝与复用引入的分布偏移，是精度-延迟平衡的实用 trick：不必重新训练大视觉编码器，只训练轻量适配层即可保持与全量
  embedding 的高保真度。

  - 内存高效向量索引（如一年截图仅 0.13 GB）对本地 Agent 记忆、电商 session 历史搜索有直接参考价值，能支撑长周期、全本地、隐私友好的视觉检索。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**  
屏幕历史可作为人和 Agent 的可搜索视觉记忆，但需要在新截图到达时实时编码和索引。OCR 索引快但丢失视觉信息；视觉编码耗时超过 2 秒。屏幕变化是增量的：多数像素在单张截图内和相邻截图间重复。因此提出：视觉编码器是否必须为每张新截图从头计算表示？

**方法关键点**  
StreamEmbed 仅依赖像素差分指导增量视觉嵌入：空间 token 剪枝跳过与邻居重复的 block；时间 KV 复用直接重用未变 block 的缓存 key/value。一个小型 learned adapter 补偿剪枝与复用带来的偏差，保持与全截图嵌入的保真度。

**关键结果**  
在 ScreenMemEval 基准上（184 小时屏幕历史、10,426 个问题，来自两名人类和一个 computer-use agent），StreamEmbed 在 M2 Pro GPU 上达到新的 accuracy-latency Pareto frontier：编码速度比全截图编码最高快 3.7 倍且不损失精度；在相同延迟下，比 OCR 索引的 Recall@10 最高提升 6.3 点。内存高效向量索引仅用 0.13 GB RAM 存储模拟一年截图。该工作使屏幕历史的原生视觉形式实时索引成为可能，为完全本地化视觉助手奠定基础。
