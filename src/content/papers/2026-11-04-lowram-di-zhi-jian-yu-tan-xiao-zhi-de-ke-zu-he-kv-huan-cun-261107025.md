---
title: 'LowRAM: Low-Rank Keys and Amortised Values for Composable KV Cache Compression
  at Test-Time'
title_zh: LowRAM：低秩键与摊销值的可组合 KV 缓存测试时压缩
authors:
- Teresa Delgado
- Hugo Hazard
- Martin Benfeghoul
- Jun Wang
- Zafeirios Fountas
affiliations:
- Huawei Noah's Ark Lab
- University College London
arxiv_id: '2611.07025'
url: https://arxiv.org/abs/2611.07025
pdf_url: https://arxiv.org/pdf/2611.07025
published: '2026-11-04'
collected: '2026-11-10'
category: LLM
direction: LLM推理优化 · KV缓存压缩
tags:
- KV cache
- compression
- low-rank
- amortisation
- LLM inference
- throughput
one_liner: 利用注意力头中值可由键预测，结合低秩键压缩，实现近无损、可组合的 KV 缓存压缩
practical_value: '- 在长上下文 LLM 服务（如 Agent 长对话状态、用户行为序列编码）中，KV cache 是显存瓶颈；可借鉴 LowRAM
  对 key 做低秩压缩、对 value 用 key 预测残差，实现约 4 倍近无损压缩，直接提升 batch size 和吞吐。

  - 值摊销思路：注意力值往往可由键线性预测，因此仅存储预测残差；这类似对序列 embedding 做低秩分解，可尝试对用户/物品序列的缓存做预测压缩，降低存储开销。

  - 该方法支持与量化、驱逐（eviction）组合，达到更高压缩比；在实际部署时可分层压缩，在长上下文推理中平衡精度和显存。

  - 选择性重构在解码时只恢复部分 token 的 KV，避免全量解压开销，适合在线低延迟场景，尤其适用于多查询推理等一次性成本可摊销的服务。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：自回归解码依赖 KV cache，其内存随上下文线性增长，限制 batch size 和吞吐。现有方法利用 token、层、特征维度冗余或低精度，但未充分挖掘键值间的结构关系。本文发现每个注意力头中 value 很大程度上可由对应 key 预测，提出值缓存摊销。

**方法关键点**：在测试时对每个头拟合轻量预测器，从 key 预测 value，仅存储重构最差 token 的残差，实现约 4 倍近无损 value 压缩。预测器可用元学习初始化以大幅降低 prefill 开销，也可在一次性成本可接受时从头拟合。同时结合跨层低秩 key 压缩，形成 LowRAM 非对称压缩管线。解码时仅重构选定的 KV 对，保持低解码开销。

**关键结果**：在三个模型家族上接近无损；4 倍压缩时峰值解码吞吐提升最高 5 倍；与量化和驱逐组合，长上下文上达到 26.9 倍压缩，保持基线 94.5% 性能。表明将 key 和 value 视为结构上不同，可实现高效、激进且可组合的 KV 缓存压缩。
