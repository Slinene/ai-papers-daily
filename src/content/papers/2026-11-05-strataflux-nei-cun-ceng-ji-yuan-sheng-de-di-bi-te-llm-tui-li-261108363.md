---
title: 'StrataFlux: Memory-Hierarchy-Native Low-Bit LLM Inference'
title_zh: StrataFlux：内存层级原生的低比特 LLM 推理框架
authors:
- Jake Hyun
- Ziyu Zhao
- Jae-sun Seo
- Mohamed S. Abdelfattah
affiliations:
- Cornell University
- Carnegie Mellon University
arxiv_id: '2611.08363'
url: https://arxiv.org/abs/2611.08363
pdf_url: https://arxiv.org/pdf/2611.08363
published: '2026-11-05'
collected: '2026-11-06'
category: LLM
direction: LLM 推理 · 量化与内存层级优化
tags:
- Quantization
- KV Cache
- Offloading
- Low-Bit Inference
- Memory Hierarchy
one_liner: 利用宿主内存与SSD的选择性高精度流式传输，弥补低比特权重/KV量化精度损失且不牺牲吞吐
practical_value: '- 线上 LLM 推理服务（推荐解释、Agent 工具调用）可保留 2-3bit 权重/KV 占显存，按需从 CPU 内存或 SSD
  拉取高精度残差/修正项，用极低 GPU 内存成本恢复生成质量。

  - 工程上可借鉴其“选择性精度流式传输 + 传输与计算重叠 + 跨解码步骤复用已取高精度数据”的流水线设计，避免 offload 延迟阻塞 decode，适合低延迟在线场景。

  - 长上下文场景（如 128K 用户历史/商品序列）可用 3bit 权重 + 2bit KV 达到 vLLM 4bit AWQ + 8bit KV 相当质量，但
  GPU 内存减半，可提升单卡并发或支持更长上下文。

  - 对 RAG 或对话式推荐中的长文本生成，低比特 KV cache 加选择性精度补充能在有限 GPU 上提高吞吐而不显著牺牲准确性。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

动机：LLM 推理同时受精度、延迟、内存约束，量化降低存储/带宽但可能损害精度，offloading 保留高精度数据却因传输延迟拖慢生成。

方法关键点：StrataFlux 将宿主 RAM 与 SSD 作为额外精度来源，协同设计 refinement 表示、选择与交付；采用选择性精度流式传输减少传输量、传输与计算重叠、跨解码步骤复用已获取的高精度数据，使 decode 不必等待每次传输。

关键结果：2-bit Llama-3.1-8B-Instruct 权重下 WikiText-2 困惑度从 9.46 降至 8.40，RTX 5090 上保持 95.4% 的量化基线吞吐；2-bit 权重+KV 时 Qwen3-8B 的 AIME 2024/2025 准确率从 11.0% 提升至 47.1%，GPU 内存占用不变；128K 上下文下 Llama-3.1-8B-Instruct 用 3-bit 权重+2-bit KV 达到 vLLM 4-bit AWQ 权重+8-bit KV 的可比困惑度与速度，但 GPU 内存约减半。
