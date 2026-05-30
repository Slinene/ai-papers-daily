---
title: 'RUBRIC-ARROW: Alternating Pointwise Rubric Reward Modeling for LLM Post-training
  in Non-verifiable Domains'
title_zh: RUBRIC-ARROW：交替式评分准则奖励建模，提升非可验证领域LLM后训练
authors:
- Haoxiang Jiang
- Zihan Dong
- Tianci Liu
- Wanying Wang
- Ran Xu
- Tony Yu
- Linjun Zhang
- Haoyu Wang
affiliations:
- University at Albany
- Rutgers University
- Purdue University
- Emory University
- Georgia Institute of Technology
arxiv_id: '2605.29156'
url: https://arxiv.org/abs/2605.29156
pdf_url: https://arxiv.org/pdf/2605.29156
published: '2026-05-26'
collected: '2026-05-30'
category: Training
direction: 奖励建模与LLM后训练·评分准则的成对偏好优化
tags:
- Rubrics
- Reward Modeling
- LLM Alignment
- Pointwise Evaluation
- GRPO
- Non-verifiable Domains
one_liner: 交替训练评分准则生成器与准则条件评判器，以概率评分与成对偏好数据训练点式奖励模型。
practical_value: '- 在电商Agent或推荐解释生成中，可借鉴 rubrics 分解评估：将整体质量拆解为独立准则（如信息准确性、说服力、风格匹配），训练准则条件评判器获得细粒度奖励信号。

  - 概率评分规则能减少平局，提供更光滑的奖励分布，适合作为排序或策略优化的目标，比硬布尔聚合更稳定。

  - 交替训练生成器与评判器的架构可复用于自动评估流程：业务中可先有粗粒度准则，通过交替优化不断细化准则和评判能力。

  - 仅用 pairwise 偏好数据训练 pointwise 奖励模型，降低人工标注绝对分数的成本；对于成对偏好易得的场景（如用户 A/B 选择），可直接复用此方法。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM 后训练中，点式奖励模型在主观、不可验证任务（如开放式指令遵循）上常不可靠。基于评分准则（rubric）的方法将评估分解为明确条例，但现有方案依赖顶尖大模型生成准则，且硬布尔聚合易导致大量平局，损害区分度。

**方法**：提出 RUBRIC-ARROW，交替训练**评分准则生成器**和**准则条件评判器**。生成器根据提示自动产生细粒度评估准则；评判器基于准则给出概率化评分，避免布尔判断的平局。RL 阶段**仅使用成对偏好数据**，设计了阶段特定偏好奖励与交替 GRPO 算法，联合优化生成器与评判器，最终获得可靠的点式评估器。

**结果**：在多个基准上，RUBRIC-ARROW 取得与前沿模型相当甚至更优的奖励建模准确率，且将奖励模型用于下游策略后训练时取得一致提升，验证了框架的有效性和泛化性。
