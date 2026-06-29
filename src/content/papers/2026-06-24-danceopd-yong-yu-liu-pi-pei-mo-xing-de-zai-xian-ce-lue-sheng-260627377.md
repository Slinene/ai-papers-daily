---
title: 'DanceOPD: On-Policy Generative Field Distillation'
title_zh: DanceOPD：用于流匹配模型的在线策略生成场蒸馏
authors:
- Wei Zhou
- Xiongwei Zhu
- Zelin Xu
- Bo Dong
- Lixue Gong
- Yongyuan Liang
- Meng Chu
- Leigang Qu
- Lingdong Kong
- Wei Liu
affiliations:
- ByteDance Seed
- NUS
- UMD
- HKUST
arxiv_id: '2606.27377'
url: https://arxiv.org/abs/2606.27377
pdf_url: https://arxiv.org/pdf/2606.27377
published: '2026-06-24'
collected: '2026-06-29'
category: Other
direction: 多能力组合蒸馏 · 在线策略训练
tags:
- on-policy distillation
- flow matching
- multi-capability composition
- velocity field
- classifier-free guidance
- generative field distillation
one_liner: 提出一种在线策略生成场蒸馏框架，通过路由和查询学生自身状态来组合冲突的多能力，提升图像生成中的能力组合效果。
practical_value: '- **多任务组合的在线策略蒸馏**：在电商推荐中，点击、转化、时长等多目标常相互冲突，可借鉴 DanceOPD 的 on-policy
  场蒸馏思想，将每个目标视为一个速度场，模型在自身 roll-out 的状态上查询各场进行学习，避免离线预计算偏差，实现多目标平衡。

  - **吸收算子化目标**：类似于将无分类器引导（CFG）吸收为可蒸馏的场，在推荐中可将去偏、多样性控制等算子形式化为场，蒸馏进学生模型，简化推理管线。

  - **生成式推荐的训练范式**：若将物品 ID 表示为生成式 token，使用流匹配生成推荐序列，DanceOPD 的 on-policy roll-out
  训练方式可更好对齐生成与判别目标，减少曝光偏差。

  - **路由机制与能力解耦**：每个训练样本只路由到一个能力场，避免能力间相互干扰，对于多领域（如广告、内容、商品）合并训练时有直接参考价值，可按样本域标签路由到对应专家场。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现代图像生成需要同时具备文生图、局部编辑、全局编辑等多种能力，但这些能力天然冲突（编辑损害生成质量，局部与全局编辑互扰），如何有效组合多能力是核心挑战。

**方法**：提出 DanceOPD，一个用于流匹配模型的在线策略生成场蒸馏框架。将每种能力定义为共享流状态空间上的速度场，训练时每个样本随机路由到一个能力场，从学生模型自身的低噪声状态出发，查询该能力场并计算速度 MSE 损失进行蒸馏。由于学生是基于自身 roll-out 状态学习，避免了离线蒸馏的分布偏移，并能将各能力场的知识平稳组合。该框架还可将无分类器引导等算子形式化为额外的场一并吸收。

**结果**：在 T2I、局部+全局编辑、真实感场吸收和 CFG 吸收等任务上，DanceOPD 显著提升了多能力组合效果：编辑指标上优于联合训练和离线蒸馏，同时 GenEval 生成质量保持在 0.848+，证明了框架有效平衡冲突能力并保留锚生成质量。
