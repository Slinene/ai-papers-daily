---
title: End-to-End Context Compression at Scale
title_zh: 端到端大规模上下文压缩模型
authors:
- Ang Li
- Sean McLeish
- Haozhe Chen
- Nimit Kalra
- Zaiqian Chen
- Artem Gazizov
- Venkata Anoop Suhas Kumar Morisetty
- Bhavya Kailkhura
- Harshitha Menon
- Zhuang Liu
affiliations:
- New York University
- University of Maryland
- Princeton University
- Columbia University
- Meta FAIR
arxiv_id: '2606.09659'
url: https://arxiv.org/abs/2606.09659
pdf_url: https://arxiv.org/pdf/2606.09659
published: '2026-06-07'
collected: '2026-06-09'
category: LLM
direction: 长上下文推理加速 · 软令牌压缩
tags:
- context-compression
- soft-tokens
- encoder-decoder
- KV-cache
- LLM-inference
- agent
one_liner: 通过大规模端到端训练编码器-解码器，以软令牌压缩KV缓存，在长上下文任务上实现更优的速度-质量帕累托前沿
practical_value: '- **软令牌压缩可直接接入现有推理引擎**：与难以兼容 vLLM/SGLang 的 KV 缓存淘汰方法不同，LCLM 输出的软令牌序列天然适配分页注意力，可直接降低电商搜索、推荐模型在长用户序列中的
  prefill 延迟和显存占用。

  - **编码器窗口批量压缩策略**：通过固定窗口编码并批量并行，可将长用户历史或商品描述压缩为少量潜在向量，适应突发长上下文，适合在多智体任务中维护持久记忆，降低对话轮次间的
  KV 缓存重计算。

  - **自适应扩展 Agent 框架**：借鉴论文中的 EXPAND 工具设计，在推荐解释或多轮对话中，可以先用高压缩比概览全部用户行为，再按需精准解压相关片段，实现高效的长序列检索与生成结合。

  - **多阶段训练 recipe 可复用**：适配器预热 → 编码器训练 → 解码器解冻 → SFT 的阶段式训练，有效控制灾难遗忘，适合将现有生成式推荐模型改造为上下文压缩器，尤其在使用
  LoRA 微调时参考其分阶段学习率设置。'
score: 9
source: huggingface-daily
depth: full_pdf
---

**动机**：长上下文 LLM 推理受 KV 缓存内存瓶颈限制，现有 KV 缓存压缩方法或严重降质，或耗时巨大，且与主流推理引擎不兼容。软令牌压缩（编码器-解码器）理论上可并行压缩、兼容标准解码，但过去方法在通用任务上不具竞争力。

**方法关键点**
- 提出 **Latent Context Language Models (LCLMs)**，用 0.6B 编码器将原始长文本映射为少量软令牌，由 4B 解码器消费，实现 4× / 8× / 16× 压缩。
- 多阶段训练 recipe：Stage0 热身适配器，Stage1 解冻编码器，Stage2 端到端持续预训练，Stage3 SFT；引入交替压缩/非压缩块的预训练数据格式，并加入辅助重建任务以保留细节。
- 架构搜索确定：编码器窗口大小 1024、因果注意力、均值池化（高压缩比）或拼接（低压缩比），适配器仅用 MLP。
- 在 RULER、LongBench、LongHealth 上评估，对比 SnapKV、KVzip、FastKVzip、Expectation Attention 等基线。

**关键结果**
- LCLM 在 RULER @4k 上实现 **8.8× 更快的 TTFT**，在 LongBench @64k 上 **5.2× 更快**，且精度匹配或超过 KV 缓存压缩方法。
- 峰值显存随上下文长度增长缓慢，16× 压缩在 128k–512k 几乎平坦。
- 结合 agent 工具的 EXPAND 机制，在 NIAH 任务上显著提升精确字符串匹配，部分达到无压缩水平。

**值得记住的一句话**：LCLM 通过小编码器批量压缩长上下文为软令牌，在速度和显存上形成新 Pareto 前沿，且天生兼容标准推理框架。
