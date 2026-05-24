---
title: 'AwareVLN: Reasoning with Self-awareness for Vision-Language Navigation'
title_zh: AwareVLN：具备自我感知推理的视觉语言导航
authors:
- Wenxuan Guo
- Xiuwei Xu
- Yichen Liu
- Xiangyu Li
- Hang Yin
- Huangxing Chen
- Wenzhao Zheng
- Jianjiang Feng
- Jie Zhou
- Jiwen Lu
affiliations:
- Tsinghua University
arxiv_id: '2605.22816'
url: https://arxiv.org/abs/2605.22816
pdf_url: https://arxiv.org/pdf/2605.22816
published: '2026-05-21'
collected: '2026-05-24'
category: Agent
direction: 视觉语言导航 · 自我感知推理
tags:
- VLN
- Self-awareness
- Structured Reasoning
- End-to-End
- Embodied AI
- Data Engine
one_liner: 提出自我感知的结构化推理机制，使视觉语言导航智能体明确理解自身状态和任务进展，实现更鲁棒的指令跟随。
practical_value: '- 结构化推理触发机制：仅在关键决策点动态触发显式推理，分析空间状态、任务进度及指令对齐，避免全程密集推理。电商对话或复杂任务
  Agent 可借鉴此设计，按需进行深层次状态审视，降低延迟与冗余计算。

  - 自动数据引擎与进度划分：利用任务进度自动标注生成训练数据，将导航过程切分为语义完整的子任务。可迁移至电商多轮交互场景，通过自动标注对话状态与进度标签，提升训练数据生成效率与模型对流程的理解。

  - 端到端空间-任务感知融合：不依赖3D传感器与显式建图，从RGB视觉输入中以数据驱动方式习得空间与任务自我意识。对于电商推荐中基于视觉或文本的状态跟踪（如用户浏览路径理解）有参考价值，可增强模型对环境与目标的整体把握。

  - 可解释性提升：显式的结构化推理输出（我看到了什么，我完成了什么，下一步计划）增强了决策透明度。可应用于电商推荐系统的可解释性设计，例如在生成推荐理由时融入类似“用户当前处于…阶段，因此推荐…”的推理链条。'
score: 6
source: arxiv-cs.CV
depth: abstract
---

动机：现有视觉语言导航（VLN）方法多依赖端到端动作预测，缺乏对智能体、指令与场景关系的显式理解；而基于显式建图的规划方法则依赖额外3D传感器，阻碍大规模视觉-语言预训练。为此，需赋予导航智能体以自我感知能力，在关键点进行结构化推理。

方法：提出 AwareVLN 框架，包含两大创新：1）结构化推理模块，培养空间与任务导向的自我意识，在导航关键点选择性触发，使智能体显式分析自身空间状态、任务进度及与指令的对齐程度；2）自动数据引擎，依据任务进度自动划分导航序列并生成推理标注，用于高效训练。整体以端到端、数据驱动方式实现，无需3D传感器。

结果：在 Habitat 模拟器的多个数据集上，AwareVLN 显著超越了先前最优 VLN 方法，验证了自我感知推理对导航鲁棒性与可解释性的提升作用。
