---
title: 'Where Rounding Happens Matters: Rounding-Location Alignment Stabilizes LLM
  Reinforcement Learning'
title_zh: 舍入位置对齐稳定 LLM 强化学习
authors:
- Yijing Ke
- Tianle Cai
- Ruosong Wang
affiliations:
- ByteDance Seed
- Peking University
arxiv_id: '2610.32951'
url: https://arxiv.org/abs/2610.32951
pdf_url: https://arxiv.org/pdf/2610.32951
published: '2026-10-23'
collected: '2026-10-26'
category: Training
direction: LLM RL 数值稳定性
tags:
- RLHF
- BF16
- RoPE
- SwiGLU
- RMSNorm
- Numerical Stability
one_liner: 对齐训练与推理的 RoPE/SwiGLU/RMSNorm 舍入位置可避免 BF16 RL 崩溃
practical_value: '- 用 vLLM rollout + HF 重算 log-prob 的 RL 流程，优先检查/对齐 RoPE 路径的舍入位置；本论文中单独对齐
  RoPE 即可防崩溃，成本最低、不动推理引擎和 attention kernel。

  - BF16 RL 训练时，可把 RoPE/SwiGLU/RMSNorm 的中间激活保留 FP32 到输出再截断为 BF16；这是训练侧局部代码改动，避免了全局
  FP32 带来的吞吐损失。

  - 出现 LLM RL 不稳定的广告/推荐文案生成或对话 Agent 策略时，先别改算法或调 reward，先监控 rollout 与 training recompute
  的 log-prob 差异；差异可能来自 rounding location 而非数据或算法。

  - 该结论可迁移到基于 Qwen 等开源模型的搜索推荐 Agent 后训练：维持 BF16 matmul/kernel 性能，同时用局部舍入对齐降低 off-policy
  偏差。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：LLM 强化学习常用推理引擎（如 vLLM）生成样本，再用另一套训练栈（如 HF Transformers）重算概率；即使权重与 BF16 类型一致，实现差异也会让重算 log-prob 偏离生成策略，使 on-policy 更新变成 off-policy，导致训练崩溃。

**方法关键点**：不整体对齐推理/训练栈，也不改全局精度或学习算法，只对齐训练侧三处舍入位置：RoPE、SwiGLU、residual RMSNorm。具体做法是在这些区域保留部分中间量为 FP32，直到输出 BF16。推理引擎、矩阵乘/注意力 kernel、学习目标均不变。

**关键结果**：在四个 Qwen 系列模型上，对齐上述三个区域可避免默认 BF16 基线下的崩溃；且在研究运行中单独对齐 RoPE 路径也足够，尽管仍存在其他数值差异。
