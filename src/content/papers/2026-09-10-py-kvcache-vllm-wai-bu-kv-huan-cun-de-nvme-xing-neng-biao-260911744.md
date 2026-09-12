---
title: 'Building py-kvcache: A Performance Characterization of External KV Caching
  for vLLM with NVMe SSDs'
title_zh: py-kvcache：vLLM 外部 KV 缓存的 NVMe 性能表征
authors:
- Joseph Kanichai
- Tiziano De Matteis
- Animesh Trivedi
affiliations:
- Vrije Universiteit Amsterdam
- IBM Research Zurich
arxiv_id: '2609.11744'
url: https://arxiv.org/abs/2609.11744
pdf_url: https://arxiv.org/pdf/2609.11744
published: '2026-09-10'
collected: '2026-09-12'
category: LLM
direction: LLM 推理 · KV cache 卸载优化
tags:
- KV cache
- vLLM
- NVMe
- TTFT
- prefix caching
- LLM serving
one_liner: 刻画外部 KV 缓存加载与重算的权衡，提出异步直接 I/O、有界 staging、调度感知预取，80k tokens 磁盘加载比 LMCache
  快 2 倍
practical_value: '- 在长上下文 LLM 服务（如 Agent 多步推理、长 prompt 推荐解释）中开启外部 KV cache 前，先用生产
  trace 做 break-even 分析：H100 等强 GPU 上短前缀重算可能比磁盘加载更快，外部缓存应作为按场景开启的准入策略，而非全局默认。

  - 缓存层设计要关注传输粒度与调度时序，而非只盯 NVMe 带宽：连续块传输 + 异步直接 I/O 绕过页缓存，并限制共享 staging buffer，避免挤占
  GPU/CPU 内存；请求排队时就启动预读，让磁盘 I/O 与 prefill 计算重叠，可显著降低 TTFT。

  - 对多轮对话和前缀链不规则场景，py-kvcache 的调度感知预加载有明确收益；若业务里 prompt 前缀复用度高（如推荐 agent 的固定 system
  prompt、RAG 检索后的公共上下文），可以在 CPU/NVMe 层缓存 KV，但需评估前缀长度分布和 GPU 算力后决定。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：长上下文 LLM 请求中，prefix caching 复用 KV state 可降低 TTFT，但外部缓存加载不一定快于重算，需要系统地表征其性能边界。

**方法**：在 vLLM 上使用合成负载、LongBench、SCBench 和生产 trace，分析 GPU/CPU/NVMe 三层 KV 缓存；发现性能由传输粒度、中间内存使用和调度时序共同决定，而非仅带宽。据此实现 py-kvcache，一个 vLLM KV Offload connector，采用异步直接 I/O、有界共享 staging 和调度感知预加载，在请求等待时启动磁盘读，与计算重叠。

**结果**：80k tokens 时，py-kvcache 磁盘加载比 LMCache 快 2.0 倍，预加载贡献 1.34 倍；三层缓存全开时比 LMCache 快 1.23 倍，与 native vLLM KV Offload 差距约 4%。LongBench/SCBench 验证对不规则前缀链和多轮负载同样有效。Bailian trace 回放显示在弱 GPU 上改善 TTFT，但在 H100 上平均请求低于 break-even 点，GPU 内存已够用。结论：外部 KV 缓存应作为特定部署的准入决策。
