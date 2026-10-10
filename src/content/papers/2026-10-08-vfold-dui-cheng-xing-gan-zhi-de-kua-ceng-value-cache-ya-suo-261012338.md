---
title: 'VFold: Symmetry-Aware Cross-Layer Value Cache Compression'
title_zh: VFold：对称性感知的跨层 Value Cache 压缩
authors:
- Neha Verma
- Sungwon Kim
- Kenton Murray
- Kevin Duh
affiliations:
- Johns Hopkins University
- George Mason University
arxiv_id: '2610.12338'
url: https://arxiv.org/abs/2610.12338
pdf_url: https://arxiv.org/pdf/2610.12338
published: '2026-10-08'
collected: '2026-10-10'
category: LLM
direction: LLM 推理 KV cache 压缩
tags:
- KV cache
- Value cache
- Compression
- Symmetry
- Long context
- Memory
one_liner: 利用 value cache 跨层对称性做无损合并，不改模型结构，可与量化/剪枝组合进一步压缩
practical_value: '- 适合长上下文 Agent/RAG/LLM 排序服务：在不改模型结构、不重新训练的前提下，于 decode 前对 value
  cache 做跨层对称合并，可直接降低显存占用，线上可插拔。

  - 可与 KV cache 量化或 key cache pruning 组合：先做 VFold 式 value 合并，再做高压缩比量化/剪枝，能在 memory
  受限条件下换更大 batch 或更长上下文；需用 LongBench/RULER/多轮工具调用等业务指标回归。

  - 工程实现上只需读取 value cache 并做轻量融合/索引，对注意力结构无侵入，适合已经冻结模型参数的线上推理框架（如 vLLM、TensorRT-LLM）外挂使用。

  - 可离线检测各层 value 表示的余弦相似度/CKA，定位高冗余层，再决定合并范围；若用 LLM 做序列推荐或用户行为编码，类似跨层冗余也可能存在，值得做一次成本极低的探测。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

动机：长上下文解码中 KV cache 逐渐成为显存瓶颈，且 value cache 中存在跨层相似性但未被充分利用；现有压缩方法多需改变模型结构或引入较高开销。

方法关键点：提出 VFold，一种对称性感知的跨层 value cache 合并策略。在 decoding 阶段识别并合并具有对称/相似分布的 value 状态，减少 cache 内存；不修改 LLM 架构、无需重新训练，额外开销小。进一步将 VFold 与现有高比率量化或 key cache pruning 组合，可达到单一方法无法获得的压缩率。

关键结果：论文展示该组合能突破单独 KV 压缩技术的压缩上限，同时保持长上下文性能，验证 value cache 中存在大量未开发容量。摘要未披露具体数值，主要贡献在于提供一种简单高效且可与现有方案叠加的压缩路径。
