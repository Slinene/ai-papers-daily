---
title: On-Policy Distillation with Negative-Policy Rollouts
title_zh: 基于负策略轨迹的在线蒸馏
authors:
- Jaehui Hwang
- Dongyoon Han
- Sangdoo Yun
- Byeongho Heo
affiliations:
- NAVER AI Lab
arxiv_id: '2610.07874'
url: https://arxiv.org/abs/2610.07874
pdf_url: https://arxiv.org/pdf/2610.07874
published: '2026-10-05'
collected: '2026-10-08'
category: Training
direction: LLM 训练 · 在线蒸馏负样本
tags:
- On-Policy Distillation
- Negative Policy
- LLM Post-Training
- Knowledge Distillation
- Reasoning
- Rollout Policy
one_liner: 在 OPD 的 rollout 阶段混入低能力负策略轨迹，不改变奖励公式即可注入显式负信号，显著提升推理性能。
practical_value: '- **在 LLM 微调/蒸馏中引入弱模型负样本 rollout**：如果业务中有同模型系的低能力版本（如小参数量的 base
  或旧版模型），可以将其作为负策略，按一定比例混入 on-policy 训练 batch，不动 reward 即可让模型远离低质量输出，相当于给 OPD 加了一个“反向参考”。

  - **负策略 rollout 可以预生成并缓存复用**：论文显示纯负策略 rollout（α=1）时，训练时间从 9h19m 降到 3h34m（排除预生成），这对落地
  LLM 蒸馏训练的成本优化很实用。

  - **负样本选择有讲究**：不是随便用差模型，而是同模型家族、能力明显低于 student 的版本；简单加大 temperature、persona prompt
  或 drop layer 等降级 student 的方法也能带来少量提升，但远不如单独负策略（+3.4 vs +0.9~1.0 avg）。

  - **可复用分析指标 NSP/NOR 做训练调试**：NSP 衡量抑制是否集中在负策略偏好 token 上，NOR 衡量学生与负策略的重叠是否下降；二者与最终性能正相关，可用于监控负信号是否按预期生效。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
On-policy distillation（OPD）只在学生自己 rollout 的轨迹上做 teacher 监督，提供了一个正向模仿方向，但没有显式指明学生该远离什么。当强 teacher 与学生分布重叠较低时，仅靠正向信号可能学习不充分。类似 DPO 使用 rejected response 提供负向参考，本文引入一个低能力负策略作为学生需要远离的参考。

## 方法关键点
- 不修改 OPD 的 token 级 reward 公式，而是修改 rollout 分布：每个 batch 按比例 α 混合 student 轨迹和负策略轨迹，α∈[0,1]，α=1 表示完全使用负策略 rollout。
- 负策略选自同一模型家族中能力更低、整体推理性能更差的模型，例如 Qwen3-0.6B 作为 Qwen3-1.7B 的负策略。
- 数学上，在 D_KL(π_n ∥ π*) > D_KL(π_n ∥ π_θ) 的假设下，负策略生成 token 的期望 OPD reward 为负，因此混合负策略 rollout 会增强对这些 token 的抑制，让学生远离负策略，同时保留原 teacher 正向监督方向。
- 方法天然兼容 ExOPD、OPD2 等修改 reward 的 OPD 变体，无需改动它们的 reward 设计。

## 关键实验
- 在 13 个 math/code/science 推理 benchmark 上，用 Qwen3-1.7B/4B/8B 和 Gemma-4-E4B 验证。
- 非思考模式下，Qwen3-1.7B 数学平均从 48.3 提升到 56.3，代码从 27.2 到 31.1，科学从 37.2 到 41.5；Qwen3-4B 数学 62.2→70.5，代码 40.2→51.1，科学 47.8→51.2。
- 与 ExOPD、OPD2 结合时，Qwen3-4B 在 thinking 模式下整体平均分别提升 1.86 和 2.10 个点。
- 分析显示 NP-OPD 的 NSP（负策略偏好 token 抑制精度）和 NOR（与负策略重叠减少）均高于 OPD，且与性能正相关。
- 训练效率：α=1 时，Qwen3-1.7B thinking 模式训练时间从 9h19m 降至 3h34m（8×H100，不含预生成负策略 rollout）。

## 最值得记住的一句话
负信号不必通过 reward 公式引入，只需改变 rollout 分布，就能让 OPD 同时拥有正向 teacher 监督和明确的反向移动方向，并可直接叠加到任意 OPD 变体。
