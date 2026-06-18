---
title: 'Rethinking Reward Supervision: Rubric-Conditioned Self-Distillation'
title_zh: 重新思考奖励监督：基于评分标准的自蒸馏
authors:
- Siyi Gu
- Jialin Chen
- Sophia Zhou
- Arman Cohan
- Rex Ying
affiliations:
- Yale University
arxiv_id: '2606.19327'
url: https://arxiv.org/abs/2606.19327
pdf_url: https://arxiv.org/pdf/2606.19327
published: '2026-06-17'
collected: '2026-06-18'
category: Training
direction: 训练方法 · 评分标准自蒸馏
tags:
- Rubric
- Self-Distillation
- GRPO
- Token-level Guidance
- Reasoning
- Reinforcement Learning
one_liner: 用评分标准作为细粒度反馈，将准则级条件转化为 token 级指导，提升推理模型训练效果。
practical_value: '- **用评分标准替代标量奖励**：在 Agent 推理训练中，可以定义类似评分标准（如正确性、连贯性、步骤完整性）作为细粒度反馈，让模型明确改进方向，避免传统
  RL 的稀疏信号问题。

  - **两阶段训练可复用**：先训练一个评分标准生成模型，再用于指导主任务推理，这种分离设计在推荐解释、多步决策等需要可解释反馈的场景中可直接借鉴。

  - **自蒸馏减少标注依赖**：利用模型自身采样轨迹进行 token 级指导，无需高质量 chain-of-thought 人工标注，适合电商/推荐系统中快速迭代模型。

  - **细粒度信用分配提升效果**：在多个基准上平均领先 GRPO 1.0 点，表明 token 级奖励比结果级奖励更有效，可尝试将类似机制引入推荐 Agent
  的策略优化中。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有推理模型后训练中，蒸馏依赖昂贵且噪声多的思维链标注，即便最终答案正确，不完美的推理过程也会干扰学习；强化学习则将反馈压缩为标量奖励，无法指明具体哪些部分需要改进。  
**方法**：提出 **Rubric-Conditioned Self-Distillation (RCSD)**，将评分标准（rubrics）作为结构化细粒度反馈。先用标注数据训练一个评分标准生成器，然后以其条件化教师模型，对学生模型自采样的轨迹提供 token 级指导。学生模型在自生成样本上蒸馏，教师根据评分标准指出每个 token 的优劣，实现更精细的信用分配。  
**结果**：在 ARC、MMLU、SciBench 等科学推理基准上，RCSD 平均超过 GRPO 1.0 分，超过 OPSD 0.9 分，证明 token 级评分标准引导优于结果级标量优化。
