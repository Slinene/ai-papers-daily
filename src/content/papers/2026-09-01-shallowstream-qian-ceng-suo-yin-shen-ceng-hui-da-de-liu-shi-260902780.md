---
title: 'ShallowStream: Index Shallow then Answer Deep for Streaming Video Understanding'
title_zh: ShallowStream：浅层索引、深层回答的流式视频理解框架
authors:
- Jitai Hao
- Ke Yang
- Qiang Huang
- Jun Yu
affiliations:
- Harbin Institute of Technology (Shenzhen)
arxiv_id: '2609.02780'
url: https://arxiv.org/abs/2609.02780
pdf_url: https://arxiv.org/pdf/2609.02780
published: '2026-09-01'
collected: '2026-09-08'
category: Multimodal
direction: 多模态流式视频高效推理
tags:
- Streaming Video Understanding
- MLLM
- KV Cache
- Efficient Inference
- Diversity-aware Retrieval
- Multimodal
one_liner: 用 MLLM 浅层同时做帧编码与索引构建，查询时按浅层注意力打分并多样性选帧，延迟降低最高 52.1 倍且性能对齐强基线
practical_value: '- 直播电商/短视频理解场景可用“浅层预填充建索引、深层仅对选中片段推理”的两段式架构：常驻只保留浅层 KV cache，在线视频帧不断写入轻量索引，查询时只对高相关帧做完整深度计算，大幅降低延迟与显存。

  - 用浅层 attention score 做 query-aware 帧打分，不需要额外训练检索器；类似推荐里用注意力分数筛选候选 item 或行为序列，能把用户当前
  query / 意图与视觉片段相关性评估集中到轻量模型。

  - diversity-aware selection 可直接迁移到推荐/广告视频素材或直播切片选取：在相关帧集合上做多样性采样，避免连续重复/相似画面霸屏，提升信息覆盖与用户体验。

  - 工程上可借鉴“按 prefill depth 分层 KV cache”思路：在线流式处理时低频深算、高频浅算，对长视频/直播流式多模态 LLM 服务有直接成本收益。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：流式视频理解需持续处理未见未来问题的视频流，直接对每帧做全深度 MLLM prefill 成本极高，KV cache 随 prefill 深度线性增长；已有 token 剪枝/合并/量化/按需取帧等方法未触及模型深度这一维度。

方法关键点：ShallowStream 利用 MLLM 浅层同时完成帧编码和检索索引构建；流式阶段保留浅层 KV cache 作为 always-on 轻量索引。查询时用浅层产生的 attention score 对上下文帧打分，并采用 diversity-aware selection 选取精确且覆盖充分的证据，再只用这些帧进入深层回答。

关键结果：在流式视频理解 benchmarks 上性能与最强现有方法持平，每帧 prefill 延迟和 10 秒端到端延迟分别最高降低 52.1x 和 11.9x。
