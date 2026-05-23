---
title: 'Toward AI VIS Co-Scientists: A General and End-to-End Agent Harness for Solving
  Complex Data Visualization Tasks'
title_zh: 迈向 AI 可视化协同科学家：端到端智能体自动生成定制可视化应用
authors:
- Haichao Miao
- Zhimin Li
- Kuangshi Ai
- Kaiyuan Tang
- Chaoli Wang
- Peer-Timo Bremer
- Shusen Liu
affiliations:
- Lawrence Livermore National Laboratory
- Vanderbilt University
- University of Notre Dame
arxiv_id: '2605.21825'
url: https://arxiv.org/abs/2605.21825
pdf_url: https://arxiv.org/pdf/2605.21825
published: '2026-05-20'
collected: '2026-05-23'
category: MultiAgent
direction: Agent · 多智能体协同 · 自动化可视化
tags:
- Agent
- Multi-Agent
- Data Visualization
- End-to-End
- Autonomous Agent
- SciVis
one_liner: 提出多智能体协同框架，仅凭数据与高层描述自动生成领域定制的交互式可视化分析应用
practical_value: '- 多智能体流水线设计：将复杂任务分解为探索、规划、实现、验证、评估等阶段，每个阶段由专门 Agent 负责，产出结构化文档驱动下游，可借鉴至推荐或
  Agent 系统的自动化流程编排。

  - 层级记忆系统：跨会话存储洞察和经验，回流学习机制可应用于 Agent 长期记忆与知识积累，提升后续任务效率。

  - 基于浏览器验证的闭环设计：利用真实环境反馈自动迭代修复，类似电商场景中通过仿真环境验证推荐策略或 Agent 决策，提升可靠性。

  - 任务驱动验证基准：以未明确规定的真实竞赛任务为测试集，提供一种脱离固定评测集的思路，可用于生成式推荐或 Agent 系统以任务完成度作为最终指标。'
score: 7
source: arxiv-cs.HC
depth: abstract
---

**动机**：科学数据分析与可视化需要跨领域专业知识，现有工具难以从高层描述自动完成长周期可视化任务。本文旨在构建 AI 可视化协同科学家，作为通用 AI 协同科学家的关键组件，实现仅凭数据和任务描述自主设计可视化分析应用。

**方法**：提出端到端智能体框架（harness），由主代码智能体协调多个子智能体与技能，执行多阶段流水线：探索性分析、环境配置、计划生成、界面实现、浏览器验证与任务完成评估。各阶段产生结构化文档，支持迭代优化。引入层级记忆系统跨会话存储洞察，并通过真实浏览器反馈实现闭环自动修复。

**结果**：在 2021–2026 年 IEEE SciVis Contest 多个科学工程数据集上验证，系统成功生成功能完整的单页可视化应用，具备链接视图交互，高度匹配领域专家需求，证明框架能应对模糊需求、多模态数据与设计权衡等现实挑战。
