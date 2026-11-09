---
title: Steerable Multi-Objective Group-Relative Preference Optimization with Jointly
  Trained Low-Rank Adapters
title_zh: 可转向多目标群体相对偏好优化及联合训练低秩适配器
authors:
- Constantinos Karouzos
- Nikolaos Aletras
affiliations:
- School of Computer Science, University of Sheffield, UK
arxiv_id: '2611.09634'
url: https://arxiv.org/abs/2611.09634
pdf_url: https://arxiv.org/pdf/2611.09634
published: '2026-11-06'
collected: '2026-11-09'
category: Training
direction: 多目标 LLM 对齐 · 偏好条件 LoRA
tags:
- multi-objective RLHF
- LoRA
- preference conditioning
- GRPO
- parameter-efficient
- steerable alignment
one_liner: LambdaMix 用每个目标一个 LoRA 的混合适配器实现推理时无需重训的多目标偏好可调策略族
practical_value: '- 电商/广告/Agent 场景中，LLM 常同时面对转化、安全、风格等多个目标且上线后偏好会变。LambdaMix 思路是把每个目标训成独立
  LoRA，推理时按偏好向量混合，无需重训；适用于对话式推荐解释、广告标题生成、Agent 工具选择等。

  - 多目标 RL 训练时，不同 reward 尺度不一致容易导致某个目标吞噬更新。该方法对每个目标的 reward 单独做 group-relative normalization，再按偏好加权更新，这个
  trick 可直接迁移到 GRPO/RLVR 流程。

  - 解耦“生成响应的 adapter mixture”和“更新 adapters 的 reward weights”，比固定权重或简单 policy merging
  更灵活；业务要做个性化偏好或 A/B 测试时，可以低成本覆盖 Pareto 前沿。

  - 相比维护多个 specialist GRPO 模型，联合训练低秩 adapters 能减少训练 completion 数和存储参数，对资源有限的团队更友好。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM 部署中多目标偏好会随用户和场景变化，但标准 post-training 通常只产出固定目标权重的单一策略，缺少推理时可控的灵活性。

**方法关键点**：LambdaMix 冻结 base model，为每个目标训练一个 LoRA adapter；推理时用偏好向量线性混合 adapter 生成响应。训练采用 group-relative online RL：每个目标的 reward 单独归一化后，按同一偏好向量加权更新对应 adapter。因此单次训练即可在推理时任意切换偏好，无需进一步优化。

**关键结果**：在 helpfulness/harmlessness 和数学解题+指令遵循两个任务上，四个模型的超体积均超过所有 conditioned 和 policy merging baselines；相比一组 GRPO specialist 策略，LambdaMix 训练 completion 更少、adapter 参数更少。固定架构和初始化时，联合变化 adapter mixture 与 objective weights 比单独变化任一获得更宽的分数范围和更高覆盖率。
