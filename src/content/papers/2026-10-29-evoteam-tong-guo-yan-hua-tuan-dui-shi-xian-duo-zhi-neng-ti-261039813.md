---
title: 'EvoTeam: Multi-Agent Collaboration via Evolving Teams'
title_zh: EvoTeam：通过演化团队实现多智能体协作
authors:
- Qinuo Cao
- Xin He
- Dianxuan Fu
- Lizhi Zhang
- Zhaoqing Xing
- Jiapu Wang
- Xin Wang
- Na Zou
- Yi Chang
- Qinggang Zhang
affiliations:
- Jilin University
- Nanjing University of Science and Technology
- Shanghai AI Lab
arxiv_id: '2610.39813'
url: https://arxiv.org/abs/2610.39813
pdf_url: https://arxiv.org/pdf/2610.39813
published: '2026-10-29'
collected: '2026-11-04'
category: MultiAgent
direction: 多智能体团队演化与协作优化
tags:
- Multi-Agent
- LLM
- Evolution
- Collaboration
- Team Organization
one_liner: 提出协作中心的多智能体演化框架，联合演化团队组织、交互规则与个体技能
practical_value: '- 团队库 + 任务路由：在电商多 Agent 系统中，可按 query 类型或场景维护可复用团队模板（如搜索意图理解团队、推荐策略团队），根据任务相似度选择或新建团队，避免每次从零组队。

  - 团队特定交互规则：不要全局统一 Agent 通信协议，针对不同协作上下文定义 team-specific interaction rules，例如广告投放中的“预算控制
  → 出价 → 创意”顺序与约束可随经验动态调整，避免规则跨场景污染。

  - 个体技能跨团队复用：将每个 Agent 的提示词/技能封装为可插拔模块，允许同一 Agent 在不同团队中使用，降低重复开发；团队级经验只在兼容上下文中积累，防止跨任务负迁移。

  - 演化机制可离线沙盒回放：在搜推任务中利用历史 session 作为反馈，对团队组织与交互规则做进化搜索，在线只保留最优团队配置，降低试错成本。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM 多智能体系统依赖专业化 Agent 协作解决复杂任务，但仅优化单个 Agent 的 prompt、技能或执行策略，未必能提升团队整体协作。已有工作将演化扩展到协作层，却常把团队重组限制在共享结构内，并在不兼容的团队上下文中复用交互规则，导致跨异构任务演化困难。

**方法**：EvoTeam 是一个以协作为中心的演化框架，基于执行经验联合演化团队组织、交互规则和个体 Agent 技能。它维护一个可复用团队库，根据任务选择或创建合适的 Agent 团队，并用团队特定的交互规则指导协作。协作经验在兼容的团队上下文中积累，而个体技能仍可跨团队复用，从而兼顾团队级协作优化与个体能力迁移。

**结果**：在四个 benchmark 上验证了该框架的有效性，代码已开源。
