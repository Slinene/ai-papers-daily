---
title: BeNice! Closing Looping's Inference-Memory Gap via KV-Sharing
title_zh: BeNice!：通过 KV 共享弥合循环架构推理内存差距
authors:
- Hayden Prairie
- Jacob M. Ryan
- Taylor Berg-Kirkpatrick
- Daniel Y. Fu
affiliations:
- University of California, San Diego
- Together AI
arxiv_id: '2610.31633'
url: https://arxiv.org/abs/2610.31633
pdf_url: https://arxiv.org/pdf/2610.31633
published: '2026-10-22'
collected: '2026-10-23'
category: LLM
direction: LLM 循环架构 · KV-cache 共享
tags:
- KV-cache
- looped architectures
- KV-sharing
- stochastic depth
- post-training
- inference efficiency
one_liner: 用随机深度预训练加末层KV广播后训练，实现循环模型跨层KV共享且不掉点
practical_value: '- 部署 LLM 作为长用户行为序列编码器或生成式推荐 backbone 时，如果采用 looped/weight-tied Transformer，KV
  cache 不再随循环次数线性占用显存；BeNice 的末次循环 KV 广播 + 首次循环适配可作为低显存长上下文推理方案，适合 Agent 长会话和超长商品描述场景。

  - 两阶段思路可迁移：想要模型获得 KV-shareability，不是直接微调，而是在（继续）预训练中引入 stochastic depth / 随机层丢弃，让残差路径收缩到近似固定点；否则同结构不同初始化可能不具备共享性质。

  - 后训练可以保持不变原模型主体，只训练首次 recurrence 对末次 KV 的兼容层（或轻量适配器），避免破坏已收敛表示；这与 MLA、GQA、Kimi
  delta attention 以及 fp8/nvfp4 等量化方案可叠加，可直接纳入现有推理优化 stack。

  - 若当前线上不是 looped 架构，建议先把该特性纳入生成式推荐 / Agent 长上下文模型选型：循环 backbone 的参数效率高，但需配套 KV 共享/压缩能力才能获得端到端低显存收益。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：循环架构通过重复同一层块在固定参数量下提升质量，但推理时每次循环生成独立 KV cache，显存随循环次数线性增长。此前虽有 KV 共享（跨深度复用 KV cache）的观察，但并非所有循环模型稳定具备该性质，机制不清。

**方法关键点**：分两阶段。预训练阶段加入 stochastic depth，形成收缩性残差动态，使不同循环的表示趋向共同极限；后训练阶段提出 BeNice!，把最后一次循环的 KV cache 广播到第一次循环，训练首次循环生成兼容的残差，同时保留原模型质量。

**关键结果**：BeNice! 在实现 KV 共享的同时，验证集困惑度与标准微调的无共享基线持平；KV 共享可与 MLA、Kimi delta attention 等序列混合器及 fp8/mxfp8/nvfp4 低精度 KV 量化叠加。模拟低显存长上下文推理显示缓存命中率最高提升 31.4%，吞吐最高提升 23.6%，p90 TTFT 最高降低 83.6%。
