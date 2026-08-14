---
title: Parameter Exploration for RLVR via Variational Learning
title_zh: 基于变分学习的 RLVR 参数探索
authors:
- Vatsal Venkatkrishna
- Nico Daheim
- Iryna Gurevych
affiliations:
- INSAIT, Sofia University "St. Kliment Ohridski"
- Technical University of Darmstadt
- National Research Center for Applied Cybersecurity ATHENE
arxiv_id: '2608.09805'
url: https://arxiv.org/abs/2608.09805
pdf_url: https://arxiv.org/pdf/2608.09805
published: '2026-08-10'
collected: '2026-08-14'
category: Training
direction: LLM 强化学习 · 参数空间探索
tags:
- RLVR
- Parameter-space exploration
- GRPO
- LLM post-training
- Variational learning
- Exploration
one_liner: 提出 3PO 方法族，通过采样多个策略参数实现参数空间探索，相比 GRPO 在相近 FLOPs 下持续提升 LLM 推理性能
practical_value: '- 在基于 GRPO 的 RLVR 流程中（如训练生成式推荐/query 改写/对话 Agent），可引入参数空间探索：对 LoRA
  权重采样多个扰动副本生成 rollouts，与温度采样互补，能缓解奖励信号稀疏导致的训练停滞。

  - 借鉴 3PO 的分组奖励估计：将多个参数样本生成的 rollouts 分组计算优势，可减少零优势组，提升稀疏反馈（如点击/转化）下的训练信号利用率。

  - 该方法在 near-identical FLOPs 下提升性能，适合业务场景有限的训练预算；可在现有 LoRA + RL 框架中低成本实现参数扰动，无需增加推理开销。

  - 需注意：论文在数学/代码任务验证，迁移到推荐/搜索时需调整扰动强度与采样频率，并验证奖励函数（如延迟转化）下是否仍稳定。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：RLVR 是提升 LLM 推理的重要后训练范式，但当前算法受限于模型先验能力，高奖励轨迹概率过低；现有 action-space 探索（如温度缩放）只改变输出分布方差，无法重新排序 token，限制探索，易发散或停滞。

**方法关键点**：提出参数空间探索，从策略后验采样不同参数实例生成 rollouts；设计 3PO 方法族，包含不同采样策略和分组奖励估计，例如对扰动参数生成的 rollouts 分组计算优势。

**关键结果**：在 OLMo-3-1025-7B 和 Qwen2.5-Math-7B 上，数学推理和代码生成任务中，3PO 相比标准 GRPO 在 near-identical FLOPs 下持续提升平均下游性能，并产生更少零优势组和无效或错误 rollouts。
