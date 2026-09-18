---
title: 'Fathom: Per-Query Read Depth for Sparse Decoding over Offloaded KV Caches'
title_zh: Fathom：面向 offloaded KV cache 的按查询读取深度稀疏解码
authors:
- Vivek Kalyanarangan
arxiv_id: '2609.17652'
url: https://arxiv.org/abs/2609.17652
pdf_url: https://arxiv.org/pdf/2609.17652
published: '2026-09-14'
collected: '2026-09-18'
category: LLM
direction: LLM 稀疏注意力推理优化
tags:
- sparse attention
- KV cache
- quantization
- offloading
- LLM inference
- top-k decoding
one_liner: 按查询动态分配 bit 预算扫描量化 KV cache，在 offload 场景下减少带宽并加速解码
practical_value: '- 如果业务中长上下文 LLM（如电商客服 Agent、浏览助手）的 KV cache 被 offload 到主机内存，top-k
  扫描会成为解码瓶颈；Fathom 的按查询动态位预算可以直接用于减少跨 interconnect 的字节流量。

  - 采用 4-bit K cache 按 channel-major 位平面存储，查询利用 reverse water-filling 在 variance-weighted
  channel importance 上分配读取位数，可以在相同 GPU 耗时下读更少字节、获得更低注意力误差，适合对延迟敏感且 buffer 在 host memory
  的线上服务。

  - 该方法在 RULER 任务上每个 token 扫描匹配 exact top-k，说明动态位分配不会牺牲 ranking 准确性，可安全替代固定位宽扫描（如
  Double Sparsity、Loki、SparQ）以降低带宽成本。

  - 注意：该方法仅在 KV 索引驻留主机内存时有效，GPU 常驻 cache 不需要；工程落地时需先判断索引位置，避免盲目引入。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：Agent 会话可达百万 token，多个会话同时常驻时，KV cache 及其排序索引放在 host memory，每个 decode step 扫描所有 n 个 key 以找出 top-k 的读取流量成为解码带宽瓶颈。现有稀疏注意力方法使用固定位数（如 136-bit 或 68-bit）的扫描表示，存在冗余。

**方法关键点**：Fathom 提出按查询决定每个 key channel 读取多少位。4-bit K cache 按 channel-major 以 bit planes 存储，读取 t 个 plane 前缀即该 channel 的 t-bit 量化；查询通过 reverse water-filling 在 variance-weighted channel importance 上分配 bit budget，实现每 token 扫描读取位数动态化。

**关键结果**：在 Qwen3-8B 百万 token 时，Fathom 的 decode GPU time 比 136-bit 扫描（Double Sparsity、Loki、SparQ r=32）快 1.67 倍；在相同 GPU 时间下，Fathom 比 SparQ 68-bit 读少 18% 字节，且在七个模型/上下文设置中六个注意力误差更低。RULER 任务上每个 per-token 扫描与 exact top-k 完全一致；真实 coding-agent 会话中 Fathom 以 92 位达到最准确 136-bit 扫描的 step agreement。该方法利用量化服务栈已有的 4-bit K 副本，但当索引驻留 GPU 内存时无加速。
