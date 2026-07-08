---
title: 'Improving LLM-Generated Process Model Quality Through Reinforcement Learning:
  The Role of Reward Function Design'
title_zh: 强化学习优化LLM生成过程模型：奖励函数设计研究
authors:
- Alexander Rombach
- Chantale Lauer
- Nijat Mehdiyev
affiliations:
- German Research Center for Artificial Intelligence (DFKI)
- Saarland University
arxiv_id: '2607.06175'
url: https://arxiv.org/abs/2607.06175
pdf_url: https://arxiv.org/pdf/2607.06175
published: '2026-07-07'
collected: '2026-07-08'
category: Other
direction: 结构化生成 · 奖励函数设计
tags:
- Reinforcement Learning
- Reward Design
- LLM
- Structured Generation
- BPMN
- Process Modeling
one_liner: RL 通过奖励函数设计显著提升 BPMN 模型的语法和语用质量，并揭示等权重优于定向加权等关键发现
practical_value: '- 在多维度自动评估的生成任务（如推荐理由、搜索 query 改写）中，奖励函数采用等权重组合各维度指标通常优于刻意侧重某一维度，避免模型坍缩到局部最优。

  - 设计奖励函数时需结合模型架构进行实验：某些惩罚项（如无效输出惩罚）对一种模型至关重要，对另一种可能无效，应针对自身模型做消融。

  - SFT 初始化并非总是有益的，有时反而损害 RL 优化效果，实际落地前应验证无 SFT 的 RL 基线。

  - RL 能大幅降低生成输出的方差（本研究降低 6 倍以上），适合需要稳定输出的业务场景，如自动化消息推送文案生成。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：SFT 训练 LLM 生成 BPMN 模型受限于数据模式，RL 可通过外部质量指标突破天花板，但多维度质量下奖励函数如何设计缺乏研究。
**方法**：用 Llama 3.1 8B 和 Qwen 2.5 14B，在 48 种配置下，使用 Group Sequence Policy Optimization，奖励来自涵盖句法、语用、语义共 38 个指标的自动评估框架，系统考察等权重、侧重某一维度、添加无效惩罚等奖励设计。
**关键结果**：① RL 显著提升语用和句法质量，同时保持语义保真度，输出变异性降低超 6 倍；② 等权重奖励始终优于针对性加权，强调某一维度反而可能导致模型坍缩；③ 奖励设计选择与模型架构存在非平凡交互：无效惩罚对 Llama 必不可少，对 Qwen 几乎无影响；SFT 初始化对 Qwen 不可或缺，对 Llama 反而有害。结论：奖励构成是优化结果的主要决定因素，影响程度与是否采用 RL 本身相当。
