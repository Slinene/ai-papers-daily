---
title: 'Self-Play Meets Skill Evolution: Self-Evolving Search Agents that Pose, Solve,
  and Remember'
title_zh: 自对弈与技能演化：自演化搜索智能体，能出题、求解并记忆
authors:
- Zenghuang Fu
- Zhaoyang Li
- Qiuyuan Ai
- Haoyu Wu
- Minghui Wu
- Chenxu Zhao
- Ante Wang
- Guannan He
- Changwei Wang
affiliations:
- University of Chinese Academy of Sciences
- Institute of Automation, Chinese Academy of Sciences
- Peking University
- Mininglamp Technology
- Tsinghua University
arxiv_id: '2607.29468'
url: https://arxiv.org/abs/2607.29468
pdf_url: https://arxiv.org/pdf/2607.29468
published: '2026-07-31'
collected: '2026-08-03'
category: Agent
direction: 自演化技能记忆 · 搜索智能体训练
tags:
- self-play
- skill memory
- search agent
- curriculum learning
- tool-augmented
- co-evolution
one_liner: 让技能记忆在工具增强的自对弈中与任务生成协同演化，失败案例蒸馏为可复用技能写回记忆
practical_value: '- 技能记忆演化机制可构建「失败→技能」蒸馏闭环，在电商搜索/推荐中用于积累有效的查询改写模式、多跳推理路径。

  - 技能存储为外部可检索库，训练时可融入模型参数，部署时灵活选择是否启用检索，类似 RAG 的离线在线解耦，适合需要低延迟的推荐场景。

  - 自对弈出题+求解的设计可迁移到对话推荐或广告创意生成，让 challenger 产出多样化用户意图，solver 从技能库中检索最优策略。

  - 协同演化使技能记忆不再是静态插件，而是改变策略学习和未来训练分布，这一思路可用来构建持续自进化的推荐策略库或用户模拟器。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：自对弈智能体虽能自主生成训练问题，但课程缺少持久状态——失败仅影响梯度，不显式塑造未来训练；外部技能记忆常从固定任务分布学习，无法适应分布漂移。

**方法**：提出 SESA，将程序性记忆作为工具增强搜索自对弈的演化状态。框架包含一个挑战者（出题）和一个求解器（单独参数，仅负责检索技能求解），求解失败时从轨迹中蒸馏可复用技能并写回外部记忆。记忆更新改变求解器行为和成功率，进而改变挑战者的奖励及未来出题分布，产生新的失败再次改写记忆，形成“出题-求解-记忆”双向演化闭环。技能既影响在线策略训练轨迹，使其收益融入模型参数，又保留在外部记忆库中，支持内存无关部署或可选推理时检索。

**关键结果**：在 7 个开放域/多跳 QA 基准上，SESA 平均准确率比 SSP 提升 1.2–3.2 个百分点，超越 SkillRL 基线 0.9 点。在 Qwen3 模型上，仅靠参数保留的 SESA-Off 仍比 SSP 高 1.8–2.2 点，最终技能库额外带来 0.5–1.0 点增益，证明演化技能记忆不仅提升推理，更改变了策略学习与训练分布。
