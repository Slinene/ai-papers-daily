---
title: Is One Layer Enough? Training A Single Transformer Layer Can Match Full-Parameter
  RL Training
title_zh: 一层就够了？训练单个Transformer层可匹配全参数RL训练
authors:
- Zijian Zhang
- Rizhen Hu
- Athanasios Glentis
- Dawei Li
- Chung-Yiu Yau
- Hongzhou Lin
- Mingyi Hong
affiliations:
- University of Minnesota
- Peking University
- Amazon
arxiv_id: '2607.01232'
url: https://arxiv.org/abs/2607.01232
pdf_url: https://arxiv.org/pdf/2607.01232
published: '2026-07-01'
collected: '2026-07-02'
category: Training
direction: RL训练效率 · 层贡献分布
tags:
- RL fine-tuning
- layer contribution
- transformer layer
- LLM post-training
- GRPO
- training efficiency
one_liner: LLM的RL后训练增益高度集中于中间少数层，单层训练即可恢复甚至超越全参数训练效果
practical_value: '- 在大模型推荐/Agent微调中，若使用RL（如GRPO），可优先仅更新中间层，训练参数量降至1/12~1/8，显存与时间成本大幅降低，效果不降甚至反升。

  - 层贡献排名在跨任务、跨模型上高度稳定，可预先对模型做一次层贡献分析，固定高贡献层，后续微调任务均只更新这些层，实现轻量级多任务适配。

  - 结合LoRA等参数高效方法时，不必在全层应用，可只在贡献值高的中间层插入适配器，减少可训练参数且保持性能。

  - 对于需要部署多个RL微调变体（如个性化推荐策略）的场景，可训练不同层组合再集成，利用层特化提升综合决策质量。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：LLM的RL后训练通常更新全部参数，但各层对RL增益的贡献分布未知，可能导致冗余计算。本工作希望揭示RL适应在Transformer层间的分布规律。

**方法关键点**：
- 定义“层贡献”：单层单独训练所恢复的全参数RL性能提升比例。
- 在两种模型族（Qwen3, Qwen2.5）、三种RL算法（GRPO, GiGPO, Dr. GRPO）、数学推理/代码生成/智能体决策等多个任务上，对每一层独立进行RL训练并评估。
- 分析层贡献的集中度、排名一致性及结构模式。

**关键结果**：
- 单个中间层训练可恢复全参数RL训练的大部分增益，部分情形甚至超越全参数训练。
- 增益高度集中在少量中间层，输入和输出端层贡献极低；该模式跨数据集、任务、模型族、RL算法均稳定存在，层排名相关系数高。
- 基于此设计的层感知训练策略（如仅更新高贡献层）可稳定超越标准全参数RL训练，集成层级特化模型可获得额外提升。
