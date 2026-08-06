---
title: 'ToolArtist: Tool-Using Unified Multimodal Models for Agentic Image Generation'
title_zh: ToolArtist：工具使用统一多模态模型的智能图像生成
authors:
- Jiahao Zhao
- Xiaomin Yu
- Zhongxiang Sun
- Fengwei Teng
- Chengwei Qin
- Xiaobin Hu
- Jun Xu
- Shuicheng Yan
affiliations:
- RUC
- HKUST(GZ)
- NUS
- UCD
arxiv_id: '2608.04436'
url: https://arxiv.org/abs/2608.04436
pdf_url: https://arxiv.org/pdf/2608.04436
published: '2026-08-04'
collected: '2026-08-06'
category: Agent
direction: Agent 多步推理与工具调用
tags:
- Agent
- Multimodal
- Tool Use
- Reinforcement Learning
- Image Generation
one_liner: 通过后训练统一多模态模型，实现推理、工具调用与图像生成的端到端Agent策略优化
practical_value: '- 可将完整复杂任务流程（推理→工具调用→生成）交由单一策略模型端到端决策，适用于电商搜索推荐的Agent化改造，动态编排召回、排序、解释生成等步骤。

  - 教师代理收集轨迹后隐藏工具调用但保留生成结果，这一数据构造范式可直接用于训练推荐对话Agent，无需手动标注思考链。

  - RAD-GRPO结合意图和品质互补奖励的方法可用于推荐场景的多目标RLHF，同时优化相关性和内容质量。

  - 训练数据格式转换（工具调用痕迹转化为模型直接生成）为统一多模态模型接入外部工具提供了可复用的工程模板。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有文生图模型在复杂语义理解、多步推理和外部知识集成上受限，而现有的Agent化方法仅固定流程或部分控制，未协调推理、工具调用与生成为一体。

**方法**：提出ToolArtist，对统一多模态模型（UMM）进行后训练，使单一策略能动态决策推理、调用外部工具（如搜索）并生成图像。SFT阶段，用配备搜索+绘图工具的教师代理收集轨迹，再转化为UMM格式：隐藏工具调用但保留生成图像。RL阶段，开发Agentic RL基础设施，设计Reason-Act-Draw GRPO（RAD-GRPO），联合意图奖励和品质奖励优化模型。

**结果**：在开放世界图像生成任务上，端到端Agent策略全面优于固定流程及部分Agent控制的方法，提升了多步推理和工具整合的协同效果。
