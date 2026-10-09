---
title: 'ReSPO: Reshaped Sequence Policy Optimization for Gradient Starvation in Off-Policy
  Learning'
title_zh: ReSPO：重塑序列策略优化以应对离线策略学习梯度饥饿
authors:
- Yihang Chen
- Yuanhao Ban
- Cho-Jui Hsieh
affiliations:
- Department of Computer Science, University of California, Los Angeles
arxiv_id: '2609.35433'
url: https://arxiv.org/abs/2609.35433
pdf_url: https://arxiv.org/pdf/2609.35433
published: '2026-09-27'
collected: '2026-10-09'
category: Training
direction: RLVR 离线策略训练优化
tags:
- RLVR
- Off-Policy Learning
- Policy Optimization
- Importance Weight
- LLM Reasoning
- Gradient Starvation
one_liner: 提出 ReSPO，用平滑两分支序列级核替换裁剪，修正重要性权重尾部梯度饥饿，加速 RLVR 训练
practical_value: '- 若在 RLVR 训练中复用 rollout 且使用 GRPO/GSPO 时，模型难以学到低频但高奖励的长轨迹（如多步 Agent
  决策、长链推荐理由生成），可替换为 ReSPO 的平滑序列级核：正分支保留低重要性权重正样本的非零梯度，负分支抑制高权重负样本，避免梯度饥饿。

  - 对 LLM 生成搜索 query、广告文案或推荐解释的强化学习微调，在 reward 稀疏、正样本稀缺场景下，ReSPO 正分支能加速早期优化，比传统 clipping
  更友好。

  - 工程实现上，ReSPO 核是序列重要性比 W=πθ(o|q)/πold(o|q) 的函数，可与现有 GRPO/GSPO 代码低耦合替换；只需缓存 old policy
  的 rollout 来计算比率，复用现有离线数据流即可。

  - 论文在 dense 和 MoE Qwen3 上验证有效，对工业级大规模模型与 MoE 架构有迁移参考价值，但需注意业务 reward 信号若噪声较大，仍需配合
  variance-control tilt 稳定训练。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：RLVR 常因生成成本高而重用 rollouts，导致当前策略与数据生成策略 mismatch。现有 GRPO、GSPO 用裁剪稳定训练，但裁剪会带来 sign-dependent gradient starvation：低重要性权重尾部欠生成的正确响应被抑制，而高权重尾部严重过生成的错误响应反而主导梯度。

**方法关键点**：ReSPO 用从 α-divergence 变分目标和指数方差控制倾斜导出的平滑两分支序列级核替代 clipping。核以序列重要性比 W=πθ(o|q)/πold(o|q) 为输入，正分支对欠生成正响应保留非零梯度权重，负分支对严重过生成负响应进行抑制。该设计让模型在早期训练中也能从长正确推理轨迹学习，即使累积策略漂移将它们推向低权重尾部。

**结果**：在 dense 与 MoE 架构的 Qwen3 模型上，ReSPO 加速早期优化、提高最终训练分数，在 rollout reuse 设置下取得更高 held-out benchmark 表现，验证了重要性权重尾部控制对 off-policy 学习的有效性。
