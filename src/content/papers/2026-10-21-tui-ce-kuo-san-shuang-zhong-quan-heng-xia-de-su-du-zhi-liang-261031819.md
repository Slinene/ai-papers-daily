---
title: Speculative Diffusion is a Tale of Two Tradeoffs
title_zh: 推测扩散：双重权衡下的速度-质量前沿
authors:
- Aaron Zorel
- Guy Van den Broeck
- Aditya Grover
- Daniel Israel
affiliations:
- University of California, Los Angeles
- Independent Researcher
arxiv_id: '2610.31819'
url: https://arxiv.org/abs/2610.31819
pdf_url: https://arxiv.org/pdf/2610.31819
published: '2026-10-21'
collected: '2026-10-27'
category: LLM
direction: LLM 推理加速 · 推测解码与扩散模型
tags:
- Speculative Decoding
- Diffusion LLMs
- Inference Acceleration
- Pareto Frontier
- Lossy Decoding
one_liner: 联合调节扩散努力与推测解码宽松度，可扩展速度-质量 Pareto 前沿
practical_value: '- 在电商/广告的 LLM 在线推理场景（如生成推荐理由、商品描述、Agent 工具调用），可考虑用扩散 LLM 作为 draft
  model 进行推测解码，其并行 token 生成能力有助于突破 AR 解码的内存带宽瓶颈。

  - 当业务对 latency 敏感但可接受一定质量损失时，不必固守 lossless speculative decoding，可以显式引入 acceptance
  leniency 参数，快速获得有损加速。

  - 工程实现上，不要只调 draft model 的 diffusion steps，应同时扫描 diffusion effort 和 speculative
  acceptance threshold 两个维度，找到适合自身业务的 Pareto 最优配置。

  - 对需要动态权衡质量与延迟的系统（如搜索推荐中的 LLM 重排、对话式推荐），可构建类似的双参数调节机制，让线上策略根据流量状况实时切换。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：自回归 LLM 推理受限于逐 token 解码的内存带宽瓶颈，speculative decoding 通过小模型 draft 加速但传统上保持无损；扩散 LLM 可并行生成 token，但以降低质量为代价换取速度。两者结合形成 speculative diffusion，存在 diffusion effort 与 acceptance leniency 两个独立权衡维度。

**方法关键点**：
- 将 speculative decoding 的接受标准推广为可调节的宽松版本，允许有损采样加速；
- 扩散 draft 模型本身可通过减少 diffusion steps 提升速度、降低质量；
- 联合扫描两个参数，刻画完整的 speed-quality Pareto 前沿。

**关键结果**：实验表明，联合调节 diffusion effort 和 acceptance leniency 相比固定单步扩散 draft，能显著扩展速度-质量 Pareto 前沿，为不同质量/延迟需求提供更优选择。
