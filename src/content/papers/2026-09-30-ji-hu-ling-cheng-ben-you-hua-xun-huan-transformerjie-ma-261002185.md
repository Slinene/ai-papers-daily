---
title: Decoding Looped Transformers Better for (Almost) Free
title_zh: 几乎零成本优化循环Transformer解码
authors:
- Weihao Liu
- Huangjie Zheng
- Tianrong Chen
- Rohit Dilip
- Richard He Bai
- Yizhu Jiao
- Yuyang Wang
- Ruixiang Zhang
affiliations:
- Apple
arxiv_id: '2610.02185'
url: https://arxiv.org/abs/2610.02185
pdf_url: https://arxiv.org/pdf/2610.02185
published: '2026-09-30'
collected: '2026-10-03'
category: LLM
direction: 循环Transformer对比解码优化
tags:
- Contrastive Decoding
- Looped Transformer
- Inference Optimization
- Training-free
- LLM Decoding
one_liner: 训练无关的LoopCD对比解码，利用循环中间状态引导最终预测，提升推理质量并大幅降低计算量
practical_value: '- 对比解码不依赖额外小模型或微调：可直接复用模型自身不同深度的输出，在 logit 或 hidden state 空间做差值引导。对线上已有
  LLM 推理服务，可即插即用地提升生成质量，无需重新训练。

  - 隐藏状态空间变体（LoopCD-Hidden）几乎零额外开销：适合对延迟敏感的电商搜索 query 生成、推荐理由生成等场景，无需增加输出层计算，直接对中间
  hidden state 做对比。

  - 循环 Transformer 架构下可动态调整深度：根据请求复杂度决定循环次数，再用 LoopCD 弥补浅层损失，实现精度与 FLOPs 的 trade-off。对需要弹性算力调度的在线推理系统有参考价值。

  - 中间状态作为弱预测的直觉可迁移到其他多阶段推理模型（如 MoE 不同专家输出、多步推理的中间结果），利用“弱-强对比”放大模型确信信号，抑制不确定 token。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**
循环Transformer通过重复执行同一模块实现参数高效，但标准解码只使用最终循环输出，丢弃了早期中间状态。早期循环计算量更少，与最终输出天然构成对齐的弱-强预测对，无需辅助模型或外部训练即可用于对比解码。

**方法关键点**
LoopCD 是训练无关的对比解码框架，利用最终预测与早期循环预测之间的差异引导 token 选择。两种变体：
- LoopCD-Logits：在 logit 空间对比，仅需额外一次输出层前向；
- LoopCD-Hidden：在隐藏状态空间对比，几乎零额外输出开销。

核心操作是对最终 logits 或 hidden state 施加 `final + ω (final - earlier)` 的对比，放大模型更确信的信号。

**关键结果**
在四个循环Transformer家族上，LoopCD 在全循环深度下带来一致且显著的提升：
- Ouro-2.6B-Thinking 在 AIME 2024 上 pass@1 从 61.88% 提升到 73.33%；
- Huginn 在 HumanEval 上 pass@1 从 22.56% 提升到 31.71%。

更关键的是，这些增益使得循环次数可以减半而仍匹配或超过全深度无引导基线，前向 FLOPs 减少 22.5% 至 48.2%，实现了推理质量与计算成本的双重优化。
