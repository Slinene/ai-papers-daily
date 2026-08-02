---
title: 'Beyond Frame Selection: Generative Latent Evidence Aggregation for Long-Video
  Understanding'
title_zh: 超越帧选择：长视频理解的生成式隐式证据聚合
authors:
- Bowen Liu
- Shuning Wang
- Xinpeng Ding
- Zhiheng Wu
- Bodong Du
- Xiaomeng Li
affiliations:
- The Hong Kong University of Science and Technology
- Baidu Inc.
- Alibaba Group
- Xidian University
arxiv_id: '2607.28516'
url: https://arxiv.org/abs/2607.28516
pdf_url: https://arxiv.org/pdf/2607.28516
published: '2026-07-30'
collected: '2026-08-02'
category: Multimodal
direction: 视频理解 · 隐式证据聚合
tags:
- Long-Video Understanding
- Evidence Aggregation
- Latent Evidence
- Cross-Frame Integration
- Adaptive Inference
- Multimodal LLM
one_liner: 通过查询条件分布引导隐式证据聚合，在帧选择后生成紧凑跨帧证据，以极低成本大幅提升长视频理解准确率
practical_value: '- 视频推荐或直播理解任务中，可借鉴隐式证据聚合模块，以微小开销增强多帧/多片段信息的跨时刻融合。

  - 自适应证据调用机制可迁移至推理阶段动态计算分配：根据查询难度决定是否插入额外计算模块，控制延迟。

  - 用于长序列用户行为建模时，可参照查询条件分布对历史行为片段加权聚合，提升关键信息提取效率。'
score: 6
source: arxiv-cs.CV
depth: abstract
---

**动机**：长视频理解常需将视频压缩为少量关键帧，但仅保留有效视觉内容（显式证据）并不能自动整合跨时刻的互补线索，限制回答质量。需要一种在帧选择后将分散证据组织成跨帧表示的后处理机制。

**方法**：提出 GenEvA（生成式隐式证据聚合），作为帧选择后的隐式证据接口。核心包括：1）查询条件证据分布，对已选帧的逐帧信息加权聚合，生成紧凑的跨帧隐式证据；2）自适应证据调用，同一分布同时预测是否需插入该隐式补充，避免不必要开销。GenEvA 可即插即用于现有 Video-MLLM，仅增加 0.11%–0.40% 的视频 tokens。

**结果**：在 LLaVA-Video 和 Qwen2.5-VL 两个骨干、四个长视频基准上，GenEvA 一致超越同帧数基线。8 帧设定下，LLaVA-Video 四基准平均提升 +5.2 点，Qwen2.5-VL 在 LVBench 上准确率提升 +10.1 点。分析表明分配具有任务感知性，自适应调用有效抑制了无关开销。
