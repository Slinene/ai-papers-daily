---
title: 'MUSE-Autoskill: Self-Evolving Agents via Skill Creation, Memory, Management,
  and Evaluation'
title_zh: MUSE-Autoskill：通过技能创建、记忆、管理与评估实现自我进化的智能体
authors:
- Huawei Lin
- Peng Li
- Jie Song
- Fuxin Jiang
- Tieying Zhang
affiliations:
- ByteDance Inc.
- Rochester Institute of Technology
arxiv_id: '2605.27366'
url: https://arxiv.org/abs/2605.27366
pdf_url: https://arxiv.org/pdf/2605.27366
published: '2026-05-25'
collected: '2026-05-27'
category: Agent
direction: Agent 技能生命周期管理
tags:
- Skill Lifecycle
- Self-Evolving Agents
- Multi-level Memory
- Cross-agent Transfer
- SkillsBench
one_liner: 提出将技能视为统一生命周期资产的智能体框架，引入技能级记忆、测试驱动评估和跨智能体迁移。
practical_value: '- **将能力封装为可测试的技能包**：借鉴MUSE将每个技能打包为SKILL.md + scripts/ + tests/ 的标准化结构，电商推荐
  Agent 可将常用数据清洗、特征工程、报表生成等流程封装为技能，自带单元测试确保质量，避免每次重复推理。

  - **技能级记忆积累经验**：为每个技能维护独立的 .memory.md 记录跨任务的使用历史与失败模式，可迁移到推荐系统 Agent，让模型调用策略或特征组合时自动读取历史最佳实践，减少试错。

  - **低成本跨模型技能迁移**：MUSE 生成的技能文件不依赖特定 Agent 实现，可直接注入另一个 Agent 使用，这对多团队协作或 LLM 切换很有用，可建立公司内部的跨模型技能市场。

  - **自适应上下文压缩**：采用两级压缩（单节点摘要 + 连续节点合并）应对超长对话，适合推荐系统多轮交互场景，避免上下文溢出且保留关键信息。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：LLM Agent 面对复杂任务时，仅靠模型推理已不足够，需要可复用的技能。但现有自动技能生成方法往往只覆盖技能生命周期的部分阶段，缺少结构化技能记忆、测试驱动的自动评估与精炼，且技能之间相互孤立，难以跨任务积累经验和跨 Agent 迁移。本文提出将技能视为长周期的、有生命周期管理的资产，并设计了一个统一框架 MUSE-Autoskill，让 Agent 能在推理过程中动态创建、记忆、管理、评估和精炼技能，从而持续提升任务解决能力。

**方法关键点**：
- 定义技能的五个生命周期阶段：创建 (Creation)、记忆 (Memory)、管理 (Management)、评估 (Evaluation)、精炼 (Refinement)，所有非内置能力均通过此流程产生。
- 技能以标准目录结构 (SKILL.md + scripts/ + resources/ + tests/) 打包，创建后必须在沙盒中通过单元测试才能注册到技能库。
- 引入三层记忆：短期记忆 (短期上下文，可压缩)、长期记忆 (跨任务持久笔记) 和技能级记忆 (每个技能独立的 .memory.md，积累使用经验)。
- 上下文管理基于 DAG 的对话节点，采用两级自适应压缩：先对超大单节点做摘要，仍超限则合并连续节点为一个合成节点，同时固定首尾关键轮次不被压缩。
- 技能评估通过单元测试自动触发，测试失败时驱动精炼循环，使技能持续可靠。
- 技能创建通过内置的 skill_create 工具在 ReAct 循环内完成，消除创建与使用脱节。

**关键实验**：
- 在 SkillsBench 的 51 个任务上（覆盖科学工程、数据分析、文档处理、运维规划），MUSE-Autoskill 使用人工技能达到 68.40% 准确率，较无技能提升 +15.21pp，在三个超域上领先对比 Agent (Codex, Hermes)。
- 自动技能生成：在 35 个成功生成技能的任务上，Phase 2 准确率达 87.94%，超越人工技能上限；总体 51 任务得分 60.35%。
- 跨 Agent 迁移：将 MUSE 生成的技能注入 Hermes，Hermes 准确率从 47.89% 提升至 58.40% (+10.51pp)，缩小与人工技能下 Hermes 差距的 79%。
- 生成技能同时带来效率提升：MUSE 每任务 tokens 减少 20% (615K→493K)，延迟减少 37% (656s→411s)，实现 reward 与成本的帕累托改进。

**最值得记住的一句话**：将技能视为有记忆、可测试、可迁移的长期资产，而非一次性生成物，是 LLM Agent 能力持续进化的关键设计范式。
