---
title: Multi-Token Prediction Done Right
title_zh: 多 Token 预测的正确优化法：Soft-MTP
authors:
- Jayden Teoh
affiliations:
- MIT
arxiv_id: '2610.38331'
url: https://arxiv.org/abs/2610.38331
pdf_url: https://arxiv.org/pdf/2610.38331
published: '2026-10-27'
collected: '2026-10-31'
category: Training
direction: LLM 预训练 · Multi-Token Prediction
tags:
- Multi-Token Prediction
- KL Divergence
- Straight-Through Gradient Routing
- Self-Distillation
- Speculative Decoding
one_liner: 提出 Soft-MTP，通过一行代码改动移除标准 MTP 训练中的噪声残差梯度，只保留 KL 自蒸馏信号，全面提升性能与推理加速
practical_value: '- 若内部训练 LLM 用于生成式推荐（如商品描述、搜索 query 推荐、对话式导购），MTP 是一个可落地的训练技巧。采用
  Soft-MTP 的一行改动可同时提升模型困惑度和下游准确率，且无额外计算开销，适合直接加到现有预训练流程。

  - 在需要 speculative decoding 加速在线推理的场景（如实时搜索建议、Agent 规划生成），Soft-MTP 训练出的 MTP head
  能提供更准确的 draft tokens，显著提升 decoding 接受率和加速比，降低延迟。

  - 该 KL gradient-recovery trick 可复用到其他共享输出头的自蒸馏任务，例如知识蒸馏或辅助损失设计，避免直接计算大词表 KL 导致的内存瓶颈，兼容现有
  fused cross-entropy kernels，工程实现简单。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：Multi-Token Prediction (MTP) 已成为语言模型预训练常用组件，能提升下游性能和 speculative decoding 加速。但标准 MTP 训练中的交叉熵梯度包含一个残差项，干扰 next-token 和 multi-token 学习，且随模型规模增大影响显著。

**方法关键点**：作者将 MTP 交叉熵梯度精确分解为 KL 自蒸馏项（将 MTP head 拉向模型自身 NTP 分布）和一个低信噪比残差项。提出 KL gradient-recovery trick：当两个分布共享线性输出头时，通过 straight-through gradient routing 组合它们的交叉熵梯度，可精确恢复 KL 散度梯度，无需 vocab 大小的 logit 矩阵，兼容 fused cross-entropy kernels。基于此提出 Soft-MTP，一行代码改动，移除噪声残差，只回传 KL 自蒸馏信号，支持 DeepSeek 和 Meta 风格 MTP，无参数增加、无可测量开销。

**关键结果**：从 167M 到 1.2B 参数，Soft-MTP 相比标准 MTP 在 NTP perplexity、speculative decoding 加速、zero-shot 准确率上全面提升；MTP perplexity 从 689M 起更低，1.2B 微调后数学和代码推理更强，并匹配或超过直接最小化 KL 的效果。
