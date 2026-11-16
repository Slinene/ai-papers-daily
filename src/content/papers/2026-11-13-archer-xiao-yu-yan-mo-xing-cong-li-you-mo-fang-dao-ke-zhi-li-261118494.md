---
title: 'ARCHER: From Rationale Imitation to Executable Reasoning in Small Language
  Models'
title_zh: ARCHER：小语言模型从理由模仿到可执行推理
authors:
- Dhruv Dixit
- Khushi Patel
- Congcong Xu
- Min Song
affiliations:
- Stevens Institute of Technology
arxiv_id: '2611.18494'
url: https://arxiv.org/abs/2611.18494
pdf_url: https://arxiv.org/pdf/2611.18494
published: '2026-11-13'
collected: '2026-11-16'
category: Training
direction: 小模型数学推理 · 工具增强RL
tags:
- SLM
- tool use
- reinforcement learning
- executable reasoning
- math reasoning
one_liner: 将思维链编译为可执行动作轨迹，并通过分层强化学习训练小模型进行可验证数学推理
practical_value: '- 将自由形式思维链转换为结构化动作轨迹（推理步骤、工具调用、运行时观察、验证动作），可迁移到电商 Agent 的多步规划中，使模型输出可审计、可执行，便于与商品数据库、规则引擎等确定性工具对接。

  - 分层奖励设计（答案正确性、工具接地、过程纪律、轨迹对齐）可借鉴到推荐系统的 Agent 训练中，对多步决策的中间步骤进行细粒度奖励塑造，减少无效工具调用或跳跃推理。

  - 小模型 + 工具增强的路线在隐私敏感、低延迟的本地部署场景（如端侧用户意图理解、个性化文案生成）有实用价值，可降低对云端大模型的依赖。

  - 条件门控的轨迹奖励机制可用于动态调整不同训练阶段的优化重点，例如先强制工具接地，再放宽约束提升答案质量，避免模型过度依赖工具或产生幻觉。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：小语言模型（SLM）适合本地低成本部署，但在数学推理上不可靠，需要分解、精确计算、工具使用和验证。现有方法多注重模仿思维链文本，忽视可执行性和工具接地。

**方法**：提出两阶段框架 ARCHER。第一阶段将自由形式思维链编译为类型化动作轨迹，包含推理步骤、计算器调用、确定性运行时观察、验证动作和最终答案，使监督目标从模仿解释文本转向学习工具接地的推理策略。第二阶段通过非对称分层强化学习细化策略，使用分组和条件门控的轨迹奖励，分别针对答案正确性、工具接地、过程纪律和轨迹对齐进行优化。

**关键结果**：在五个 sub-10B 骨干上，ARCHER 比最强工具增强基线宏平均准确率提升 5.51 个百分点；MATH-500 提升 8.95 点，AIME-2024 和 AIME-2025 分别提升 5.33 和 5.34 点。在另外两个推理专用 7B 骨干上，可执行接地在推理聚焦 RL 或蒸馏后仍有益。结果表明可执行监督和奖励引导的行为细化是紧凑数学推理器的通用有效训练范式。
