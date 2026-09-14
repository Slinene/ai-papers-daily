---
title: Attention Quantization for Tabular Foundation Models
title_zh: 表格基础模型的注意力FP8量化
authors:
- Jonas M. Kübler
- Benjamin Jäger
- Klemens Flöge
- Noah Hollmann
- Frank Hutter
affiliations:
- Prior Labs
arxiv_id: '2609.13031'
url: https://arxiv.org/abs/2609.13031
pdf_url: https://arxiv.org/pdf/2609.13031
published: '2026-09-11'
collected: '2026-09-14'
category: Other
direction: 表格基础模型推理优化 · FP8注意力量化
tags:
- FP8
- attention quantization
- tabular foundation models
- Triton kernel
- inference optimization
- TabPFN
one_liner: 开发FP8量化QKV的注意力Triton内核，通过训练/测试量化误差对齐实现1.7倍加速且精度无损
practical_value: '- 如果业务里用了类似 TabPFN 的 tabular transformer 做点击率、LTV、风控等表格数据建模，推理优化重点应放在
  attention 计算上，而不是像 LLM 那样优先做 weight 或 KV cache 量化；QKV 直接量化到 FP8 并用显式 FP8 matmul，可以在注意力热点上拿到
  1.5-1.7x 加速。

  - 关键实现 trick：训练和推理时对行（row）的量化误差必须对齐，否则精度会急剧下降。迁移到推荐/广告场景时，如果表格模型在训练和线上服务的数据分布或预处理不同，需要把量化校准纳入训练管线，保证一致性。

  - 动态开启量化内核的策略值得借鉴：在训练行数超过 8192 时才启用 FP8 attention kernel，短序列时用基线 kernel，避免小 batch/短序列下量化开销反而拉低吞吐。

  - 工程上用 Triton kernel 可以针对 attention 做轻量级量化优化，无需重新训练模型；在表格特征建模或 in-context tabular
  learning 的推理服务中，可以将 FP8 attention 作为无精度损失的加速开关，降低线上延迟和成本。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

动机：表格基础模型（如 TabPFN、TabICL）正在快速普及，其推理性能优化成为新的效率研究方向。这类模型架构类似 transformer-based LLM，但服务模式不同：主要计算瓶颈在 attention，而非 LLM 中常见的权重或 KV cache 量化。

方法：作者将 attention 中的 query、key、value 量化到 FP8，并用显式 FP8 矩阵乘法指令加速 attention 计算。通过 Triton kernel 实现该量化注意力，并发现一个关键前提——测试行的量化误差必须与训练行的量化误差对齐，否则精度会急剧下降。

结果：FP8 attention kernel 相比常规 16-bit kernel 最高加速 1.7 倍，端到端（fit + predict）也有显著 wall-clock 增益。在 TabPFN-v3 和 TabICLv2 上，TabArena 与 BeyondArena 的精度影响在种子噪声范围内，BeyondArena 全评估时间从 253.8 分钟降至 183.7 分钟。
