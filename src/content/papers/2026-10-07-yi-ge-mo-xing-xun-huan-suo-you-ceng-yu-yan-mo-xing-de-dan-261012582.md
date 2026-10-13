---
title: 'One Model to Loop Them All: Elastic Latent Recurrence for Language Models'
title_zh: 一个模型循环所有层：语言模型的弹性潜在循环
authors:
- Faisal Ladhak
- Shantanu Acharya
- Santiago Akle Serano
- Simeng Sun
- Boris Ginsburg
- Krishna C Puvvada
affiliations:
- NVIDIA
arxiv_id: '2610.12582'
url: https://arxiv.org/abs/2610.12582
pdf_url: https://arxiv.org/pdf/2610.12582
published: '2026-10-07'
collected: '2026-10-13'
category: Training
direction: LLM 弹性深度与循环推理降本
tags:
- latent recurrence
- elastic depth
- LLM training
- MoE
- KV cache
- test-time compute
one_liner: 通过 adaptive-delta 更新与 rank override 混合深度训练，循环 LLM 在 1 loop 不损精度并随 loop
  增长持续提分
practical_value: '- **单模型多档线上服务**：ELR 提供一个 checkpoint 通过 loop count 旋钮控制精度/延迟，可替代为不同
  latency tier 维护多个模型；在电商搜索、广告文案生成、Agent 长 rollout 等场景可直接按流量层级切换 1-4 loop，无需重训或增加参数。

  - **低成本接入循环 LLM**：延迟混合深度训练只在最后 25% token 开启，训练 FLOPs 仅约 +16%；已有非循环模型可通过 continuation
  方式获得弹性深度，比从头训练循环模型更划算。

  - **MoE 推理优化技巧**：cross-loop route replay 复用首 loop 专家路由，训练 update time 降低 11.7%，推理
  forward 降低 1.2% 且精度几乎不变；对于电商大规模 MoE 模型，这是降低反复 router 计算的直接可抄方案。

  - **KV cache 与生成成本**：last-loop KV caching 让 attention KV 显存保持 1-loop 水平，同时保留大部分深度收益；高
  loop 还会缩短生成 tokens，适合长上下文 Agent/多轮对话降低显存与耗时。

  - **避免 one-loop tax 的关键**：必须用 adaptive-delta 更新和 within-step rank override 混合 1-loop
  与多 loop 梯度；纯 synchronized sampling 或加权采样无法保住 1-loop 精度，做循环化改造时要避免直接沿用 Huginn 式训练。'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
循环 / latent recurrent LLM 通过共享层重复执行，让一个 checkpoint 用循环次数换推理精度，但现有模型在 1 loop 时明显弱于同尺寸非循环模型，即 one-loop tax。这意味着低延迟场景仍需单独训练非循环模型，限制弹性深度的部署价值。

### 方法关键点
- **三段式架构**：input / recurrent / output 分块，k=1 时每个唯一层仅执行一次，参数与计算量完全等同非循环 baseline。
- **adaptive-delta 状态更新**：\(s_i = s_{i-1} + \beta_i \odot (r_i - s_{i-1})\)，其中 \(\beta_i\) 由 sigmoid gate 和 learned per-channel scale 组成，初始步长约 0.35，保证 1-loop 精度；替换为 replace / residual / fixed delta 均无法达到 baseline。
- **混合深度训练**：均匀采样 loop count，但用数据并行 rank override 让约 10-15% rank 固定走 1 loop，使同一次 optimizer step 混合 1-loop 与多 loop 梯度；这是保住 k=1 精度的关键。
- **loop-conditioned modulation**：用 progress τ=i/k 与 budget κ=k/K 生成 AdaLN/FiLM 式调制 + low-rank adapter + exit gate；零初始化引入，使 conditioning 从原 one-loop checkpoint 出发，进一步降低多 loop loss。
- **降本设计**：延迟混合深度训练只在最后 25% token 开启；MoE 中 cross-loop route replay 复用首 loop 路由；last-loop KV cache 保持 attention 显存为 1-loop 水平。

### 关键实验
- 4B dense 与 30B-A3B MoE hybrid，分别在 1T / 300B tokens 上与同数据非循环 baseline 对比：1 loop 十任务均分为 65.13 vs 65.65（4B，-0.52）和 66.08 vs 65.04（30B-A3B，+1.04）；4 loop 分别再提升 7.25 和 4.75 点。
- Koi-4B 后训练模型：一个 checkpoint 在 AA-Index v4.1 估计 1 loop 得 18（与 Qwen3.5-4B 相当），4 loop 得 29；且 4 loop 时生成 tokens 减少约 32.7%。
- 成本：延迟混合深度训练约 +16% FLOPs；cross-loop route replay 降低训练 update time 11.7%；last-loop KV cache 让 KV 显存保持 1×。

### 最值得记住的一句话
用 adaptive-delta 更新 + rank override 在同一 step 内混合 1-loop 与多 loop 梯度，是循环 LLM 不付 one-loop tax 的核心。
