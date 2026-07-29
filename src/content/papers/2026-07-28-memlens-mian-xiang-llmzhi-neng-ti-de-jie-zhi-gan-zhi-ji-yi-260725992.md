---
title: 'MemLens: A Value-Aware Memory Management System with Interactive Analytics
  for LLM-based Agents'
title_zh: MemLens：面向LLM智能体的价值感知记忆管理与交互分析系统
authors:
- Shuyue Wei
- Chang Liu
- Zimu Zhou
- Yongxin Tong
- Lizhen Cui
affiliations:
- 山东大学软件学院 & C-FAIR
- 北京航空航天大学SKLCCSE实验室
- 香港城市大学数据科学系
arxiv_id: '2607.25992'
url: https://arxiv.org/abs/2607.25992
pdf_url: https://arxiv.org/pdf/2607.25992
published: '2026-07-28'
collected: '2026-07-29'
category: Agent
direction: LLM智能体记忆价值评估与存储优化
tags:
- Memory Management
- Shapley Value
- LLM Agents
- Interactive Analytics
- Interpretability
one_liner: 提出基于Shapley值的记忆价值评估方法，实现细粒度、可解释的智能体记忆管理
practical_value: '- 记忆价值评估思路：借鉴Shapley值量化每条交互记录对最终响应的贡献，可在电商对话Agent中识别高价值用户反馈或决策关键上下文，优先保留。

  - 分层记忆存储架构：按价值分数将记忆分为短期、长期和归档层，可迁移到推荐系统的用户长短期兴趣建模，兼顾存储成本与召回效率。

  - 交互式可视化分析：提供记忆价值热力图、检索延迟对比等面板，帮助算法工程师调试Agent推理链路，快速定位低效检索或记忆冗余问题。

  - 多维度策略对比：系统内嵌响应质量、延迟、token消耗的AB对比，适合在业务Agent上线前评估不同记忆淘汰策略的性价比。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：现有LLM智能体的记忆管理多采用粗粒度策略，平等对待异构交互记录，造成大量低价值冗余记忆残留，影响长期推理效率与个性化质量。

**方法关键点**：
- **价值感知记忆**：将每条记忆记录视为一等数据对象，提出基于Shapley值的记忆贡献评估方法，量化每条记录对最终响应的边际价值。
- **全生命周期管理**：构建端到端交互分析仪表盘，覆盖记忆评估、价值感知存储（按价值分层）以及记忆辅助生成三个环节。
- **可视化与对比分析**：通过研究助教应用实例，用户可检视记忆价值分布、层级结构，并对比不同管理策略在回答质量、检索延迟和令牌消耗上的差异。

**关键结果**：系统实现了高效、可解释且个性化的记忆管理；实验表明，价值感知策略相较于统一保留基线，在维持响应质量的同时，显著降低无关记忆占比和检索计算开销（具体数值见原文）。
