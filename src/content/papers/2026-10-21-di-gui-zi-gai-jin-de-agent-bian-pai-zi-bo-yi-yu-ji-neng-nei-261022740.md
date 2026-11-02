---
title: 'R^2Orch: Recursive Self-Improvement for Agent Orchestration via Self-Play
  within a Skill-Internalization Loop'
title_zh: 递归自改进的 Agent 编排：自博弈与技能内化循环
authors:
- Mingda Zhang
- Yun Huang
- Qiang Huang
- Yanjin Li
- Rui Qian
- Qichao Zhao
- Tiesunlong Shen
- Na Zhao
- Jian Wang
- Xiaoying Tang
affiliations:
- The Chinese University of Hong Kong, Shenzhen, China
- Fudan University, China
- University of Illinois Urbana-Champaign, USA
- Tsinghua University, China
- National University of Singapore, Singapore
arxiv_id: '2610.22740'
url: https://arxiv.org/abs/2610.22740
pdf_url: https://arxiv.org/pdf/2610.22740
published: '2026-10-21'
collected: '2026-11-02'
category: MultiAgent
direction: 多智能体编排自博弈 · 技能撤除
tags:
- Agent Orchestration
- Self-Play
- Skill Withdrawal
- Recursive Self-Improvement
- GRPO
- Curriculum Learning
one_liner: 通过双层递归自博弈，用技能撤除下的任务可学习性作奖励，实现零技能部署并全面超越基线
practical_value: '- 技能生命周期管理：用“with vs without skill”成对对比估计技能净贡献，而非单看成功率或单一噪声分数，避免在课程分布变化时误判；可用
  Bayesian 后验做撤除决策，设定预期损失上限，实现技能自动退役。

  - 课程设计：在 RL 训练中，奖励任务在关键组件/技能被移除后仍保持结果多样性（learnability），而不是奖励绝对难度或失败，可避免优势坍塌并鼓励泛化；该思想可迁移到生成式推荐或多
  Agent RAG 的任务采样。

  - 训练效率：复用同一组 rollouts 同时做策略更新和技能评估，不增加额外采样成本；随机隐藏部分上下文可让模型提前适应零技能部署，逐步摆脱对昂贵工具或提示的依赖。

  - 双层时间尺度架构：外层定期评估并撤除不再贡献的工具/提示，内层持续用自博弈优化编排策略，适合电商搜索推荐中多 Agent 流程的持续自我改进与降本。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
Agent 编排已用于解决复杂任务，但现有学习范式面临三个挑战：手设课程依赖人工收集任务池；群组 RL（如 GRPO）在任务所有 rollout 结果一致时优势坍塌；技能内部化用单一噪声分数判定技能去留，评估不可靠。这些问题使编排器难以规模化自我改进。

**方法关键点**
- 双层递归自博弈：内层 Proposer 选任务，Director 通过原子编辑构建 agent 图并用 GRPO 更新；外层评估技能贡献，撤除不再有用的技能，两层共享同一组随机 rollout。
- Recursive Learnability：Proposer 的奖励定义为任务在候选技能被隐藏后，rollouts 结果仍保持差异（learnability），防止优势坍塌，使课程与技能撤除联动。
- Skill Withdrawal：将每个 rollout group 随机分为隐藏技能和保留技能两部分，通过成对对比（paired contrast）估计技能效果，用 Bayesian bootstrap 后验做撤除/准入决策，以控制撤除代价。
- 双时间尺度更新：快尺度更新 Director 和 Proposer，慢尺度更新技能库；技能从失败中蒸馏，失败被撤除技能暴露，形成闭环，最终实现零技能部署。

**关键实验**
在 12 个基准（QA、数学、代码、交互）上对比六类基线（SFT、GRPO、AFlow、AgentFlow、FlowSteer、SKILL0、PATS、SESA、MetaSkill 等），R2Orch 全部领先；IID 平均 89.79，OOD 平均 78.79，最佳基线 PATS 分别 86.00 / 76.13。用 Qwen3.5-9B Workers 训练的 Director 无需重训提升 6 个其他 backbone，缩小模型间差距。消融显示两个循环都必需，Recursive Learnability 和 Skill Withdrawal 分别替代失败奖励/成功阈值等方法带来增益。

**最值得记住的一句话**：通过奖励任务在技能撤除后仍能产生差异化 rollouts，并将技能撤除建立在成对对比的后验估计上，编排器可以递归自改进并最终零技能部署。
