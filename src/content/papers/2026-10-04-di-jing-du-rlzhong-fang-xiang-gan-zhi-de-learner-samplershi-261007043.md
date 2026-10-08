---
title: 'TRIAGE: Direction-Aware Mismatch Stabilization of Native NVFP4 Reinforcement
  Learning'
title_zh: 低精度RL中方向感知的Learner-Sampler失配稳定化（TRIAGE）
authors:
- Zhen Li
- Shuai Zhang
- Yanggan Gu
- Yiming Zhang
- Yang Yu
- Mingfa Feng
- Congkai Xie
- Shuang Yu
- Junjie Lai
- Hongxia Yang
affiliations:
- InfiX.ai
- NVIDIA
arxiv_id: '2610.07043'
url: https://arxiv.org/abs/2610.07043
pdf_url: https://arxiv.org/pdf/2610.07043
published: '2026-10-04'
collected: '2026-10-08'
category: Training
direction: 低精度 RL 训练稳定性
tags:
- NVFP4
- RL
- GRPO
- Low-precision
- Learner-Sampler Mismatch
- TRIAGE
one_liner: 提出TRIAGE，通过方向感知门控与修复稳定NVFP4强化学习，实现近BF16性能与2.3倍rollout吞吐
practical_value: '- 在生成式推荐/Agent RL 中采用低精度（FP8/NVFP4）加速 rollout 时，不要只按 importance
  ratio 的 magnitude 做 TIS，应结合 advantage sign 和 learner-sampler gap 的符号，选择性抑制会放大 mismatch
  的更新方向（A<0 & δ<0）。

  - 用 segment 级（如 64 tokens）而非 response 级或 token 级统计来诊断训练-推理不一致，能更早发现局部风险，避免全局均值掩盖崩溃前兆。

  - TRIAGE 的 bounded repair 设计可借鉴：只在 positive advantage responses 上施加 pseudo-Huber
  penalty，使修复项与 reward 方向一致，不与 policy gradient 对抗。

  - 保留 native 低精度前向，仅修改 loss/优化目标，可兼顾吞吐与稳定性，适合大规模线上 RL 训练。'
score: 8
source: huggingface-daily
depth: full_pdf
---

动机：LLM RL 训练中 rollout 成为瓶颈，NVFP4 可提供约 4 倍 BF16 吞吐，但 sampler 与 learner 的低精度差异导致训练不稳定。现有 TIS 等方法仅按 mismatch 幅度干预，忽略更新方向，可能误伤自纠正的更新而放过放大失配的更新。

方法关键点：
- 将 mismatch 定义为 δ = log π_learner - log π_sampler，结合 advantage A，分析一次更新对 mismatch energy 的贡献，得出 A<0 且 δ<0（A⁻）和 A>0 且 δ>0（A⁺）为放大区域。
- 在 native NVFP4 GRPO 轨迹中发现早期 A⁻ 区域不对称，尾部 token 集中于少数 64-token segments，response 平均值掩盖风险。
- TRIAGE：segment 级诊断（W=64），计算 mean gap 和 tail fraction，映射为 gate weight w_S；仅对 A<0, δ<0 的 token 施加 gating，并在 positive advantage responses 上添加 bounded repair（pseudo-Huber penalty）修正残差负 gap；全程保留 native NVFP4 W4A4 前向。

关键结果：
- 在 Qwen3-4B 上，TRIAGE 使训练稳定至 600 步，平均准确率 58.49%，超过 BF16 的 58.26%；naive NVFP4 在 300 步即崩溃（47.10%）。
- 在 Qwen3-30B-A3B 上，TRIAGE 1700 步平均 70.96%，接近 BF16 的 72.41%；NVFP4+TIS 仅 63.18%。
- TRIAGE 保留 2.30× rollout 吞吐和 1.30× 端到端加速，learner 额外开销 0.84%。

最值得记住：方向感知的 mismatch 控制（看 advantage 和 gap 的符号交互）比只按 magnitude 裁剪更能稳定低精度 RL，且 segment 级局部诊断能提前发现崩溃前兆。
