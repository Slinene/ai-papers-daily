---
title: 'Treadstone: A Social-Media-Inspired Platform for Multi-Agent Collaborative
  Data Analysis'
title_zh: Treadstone：受社交媒体启发的多智能体协作数据分析平台
authors:
- Hyunwook Lee
- Sungbeom Cho
- William Benjamin
- Changhee Lee
- Hyotaek Jeon
- Daeun Jeong
- Sungbok Shin
- Sungahn Ko
- Niklas Elmqvist
arxiv_id: '2609.19774'
url: https://arxiv.org/abs/2609.19774
pdf_url: https://arxiv.org/pdf/2609.19774
published: '2026-09-17'
collected: '2026-09-19'
category: MultiAgent
direction: 多智能体协作数据分析
tags:
- Multi-Agent
- Human-AI Collaboration
- Data Analysis
- Social Media Metaphor
- Visual Analytics
one_liner: 用社交信息流机制组织人与 AI 智能体在数据分析中的异步协作与证据追踪
practical_value: '- **把 agent 的中间结果变成 feed 流，而不是聊天记录**：在电商/推荐场景中做数据分析、实验归因或策略探索时，可以让多个
  agent 异步发布观察、假设和证据链接，人类分析师通过轻量 curation（点赞、置顶、标注）来控制方向，避免单一 chatbot 交互带来的上下文丢失和被动等待。

  - **线程化和证据链接提升可追溯性**：借鉴 Treadstone 的 threaded posts，为 agent 产生的每个结论强制附带 provenance（数据来源、处理步骤），便于审计和冲突消解。这在广告投放归因、推荐系统
  ablation 分析中很有价值，能快速定位错误假设。

  - **利用“主动广播假设”平衡 autonomy 与 human control**：让 agent 在置信度达到一定阈值时主动推送候选洞察，而不是等待用户提问。在电商大促实时监控中，可让
  agent 主动发现异常指标并给出解释草案，分析师只需确认或驳回，提高响应速度。

  - **学术贡献为主，工程落地需要改造**：平台本身面向通用数据分析，缺乏与推荐/广告系统的深度耦合，直接迁移成本较高；但“feed 化协作”的设计思想可以嵌入内部实验分析工具或
  agent 工作流编排中。'
score: 6
source: arxiv-cs.HC
depth: abstract
---

**动机**：人与自主 AI 智能体协同数据分析面临类似人类协作的挑战——共享中间结果、避免冲突、保持群体感知。现有工具依赖非结构化消息或单线程 chatbot，缺乏跟踪演化假设和链接证据的结构。

**方法关键点**：提出 agentic social data analysis 范式，将社交数据分析扩展为基于共享协调 feed 的协作模型，feed 模仿社交媒体时间线。实现平台 TREADSTONE 中，人类与 AI 智能体通过线程化消息异步发布、链接、质疑分析声明。agent 可以主动广播假设，用户通过轻量 curation 引导分析方向，平衡机器自治与人类分析控制。

**关键结果**：定性用户研究显示，Treadstone 能促进协作并保持人类分析主动权，相较于传统 chatbot 交互的孤立体验有显著改善；未提供量化指标。
