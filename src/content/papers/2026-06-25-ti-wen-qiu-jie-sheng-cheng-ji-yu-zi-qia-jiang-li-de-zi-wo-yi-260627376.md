---
title: 'Ask, Solve, Generate: Self-Evolving Unified Multimodal Understanding and Generation
  via Self-Consistency Rewards'
title_zh: 提问、求解、生成：基于自洽奖励的自我进化统一多模态理解与生成
authors:
- Ritesh Thawkar
- Shravan Venkatraman
- Omkar Thawakar
- Abdelrahman Shaker
- Fahad Khan
- Hisham Cholakkal
- Salman Khan
- Rao Muhammad Anwer
affiliations:
- Mohamed bin Zayed University of Artificial Intelligence
- Aalto University
- Australian National University
- Linköping University
arxiv_id: '2606.27376'
url: https://arxiv.org/abs/2606.27376
pdf_url: https://arxiv.org/pdf/2606.27376
published: '2026-06-25'
collected: '2026-06-27'
category: Multimodal
direction: 自我进化 · 统一多模态理解与生成
tags:
- self-evolving
- multimodal
- consistency rewards
- visual understanding
- image generation
- entropy guidance
one_liner: 仅用无标签图像，通过内部提问-求解-生成的自洽信号同时提升多模态理解与生成能力的自进化框架
practical_value: '- **无标注自训练范式**：利用自洽奖励信号（问答一致性）微调多模态模型，大幅降低电商商品图文理解/生成任务的标注成本，适合海量未标注商品图片场景。

  - **熵引导的难度课程**：Solver Token Entropy（STE）可作为连续难度指标，在模型训练中实现自适应课程学习，优先选择信息量大的样本，提升训练效率与稳定性。

  - **多尺度生成评估**：组合问答保真度评分与循环一致性描述的内部评估方案，可迁移到商品图生成的质量自动评分，无需人工审核。

  - **架构无关的设计模式**：角色分解与奖励逻辑在不同生成架构（扩散/整流流/自回归）上即插即用，方便接入现有多种多模态模型底座。'
score: 6
source: arxiv-cs.CV
depth: abstract
---

**动机**：现有统一多模态大模型在后训练阶段高度依赖人工标注、偏好标签或外部奖励模型，成本高昂。本文探索能否仅利用无标签图像，让模型自主同时提升视觉理解与图像生成能力。

**方法**：设计三个内部协作角色——Proposer 根据图像生成视觉问题，Solver 回答并评估，Generator 合成图像。训练完全由自洽信号驱动：如 Solver 答案的正确性作为奖励，无需任何外部监督。为稳定训练，引入 **Solver Token Entropy (STE)**，从 token 级预测不确定性导出连续难度信号，即便样本级一致性失效仍能提供有效指导。生成侧采用多尺度内部评估：结合问答保真度评分与循环一致性描述（生成图像→描述→与原始问题匹配），形成 **Solver 介导的耦合**——理解能力增强带来更可靠的生成评价，进而提供更强的训练信号。框架保持角色分解、奖励逻辑和训练进度不变，仅需各模型原生接口，适配扩散模型（BLIP3o）、整流流（BAGEL）和自回归模型（VARGPT-v1.1）。

**结果**：在八个理解基准上一致优于基座模型；BAGEL 上 MMMU 提升 **+3.5%** 绝对，GenEval 图像生成从 82% 升至 **85%**。
