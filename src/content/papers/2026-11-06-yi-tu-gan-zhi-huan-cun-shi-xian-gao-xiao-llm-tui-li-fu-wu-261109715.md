---
title: Intent-Aware Caching for Efficient LLM Serving
title_zh: 意图感知缓存实现高效 LLM 推理服务
authors:
- Kazi Hasan Ibn Arif
- JinYi Yoon
- Dimitrios S. Nikolopoulos
- Hans Vandierendonck
- Deepu John
- Bo Ji
affiliations:
- Virginia Tech
- Inha University
- Queen’s University Belfast
- University College Dublin
arxiv_id: '2611.09715'
url: https://arxiv.org/abs/2611.09715
pdf_url: https://arxiv.org/pdf/2611.09715
published: '2026-11-06'
collected: '2026-11-09'
category: LLM
direction: LLM 推理缓存 · 意图感知淘汰
tags:
- prefix caching
- intent-aware
- KV cache
- LLM serving
- eviction policy
one_liner: 提出意图感知缓存淘汰策略 IAC，利用会话意图预测 KV cache 重用，将缓存命中率提升至 34.6%，延迟降低达 46.1%
practical_value: '- 多轮 LLM 应用（客服 Agent、导购对话）可直接借鉴：对会话请求做轻量意图分类，用近端日志统计各类意图的 continuation
  probability 和 inter-turn delay，优先保留高继续概率、短到达间隔会话的 KV cache。

  - 无需训练大模型，仅需在线维护最近请求的统计表即可实现意图感知淘汰，工程落地成本低，适合接入现有 vLLM/SGLang 等 serving 框架的缓存策略。

  - 电商推荐场景中若用 LLM 做 query 改写或会话式推荐，可将会话阶段或用户意图信号融入 prompt cache 管理，减少重复 prefill，降低
  TTFT。

  - 论文验证了真实 workload 中意图信号的有效性，可用于指导业务侧自定义意图类别：先分析日志中不同意图的重用模式，再决定缓存优先级，而非直接使用通用 LRU。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

现代 LLM 服务系统依赖 prefix caching 加速多轮对话：缓存历史前缀的 KV state，后续请求复用相同前缀时跳过 prefill。但缓存命中高度依赖会话是否继续以及下一轮到达延迟，传统 LRU 或学习型方法在真实多轮 workload 上命中率不高。

作者首先分析 WildChat 与 ShareChat 真实日志，发现用户意图是预测缓存重用的强信号：不同意图（如编程、写作、闲聊）展现出显著不同的 continuation probability 与 inter-turn delay。基于此提出 Intent-Aware Caching (IAC)：在线对每个请求做意图分类，从最近 serving logs 中为每个意图维护轻量重用统计，包括继续概率与平均到达间隔，再以 oracle-inspired 策略决定缓存淘汰顺序——优先保留高重用概率且延迟短的会话前缀。

在 WildChat 和 ShareChat 上的实验显示，IAC 达到 34.6% 的平均 cache hit rate，对比之前学习型方法仅 18.8%，LRU 为 12.2%；平均 serving latency 降低最多 46.1%。方法无需离线训练，在线开销低，可直接集成到现有 LLM serving 栈。
