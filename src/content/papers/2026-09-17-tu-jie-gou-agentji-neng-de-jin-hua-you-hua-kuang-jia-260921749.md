---
title: 'GraphSkillEvo: Evolutionary Optimization of Graph-Structured Agent Skills'
title_zh: 图结构Agent技能的进化优化框架GraphSkillEvo
authors:
- Rui Sun
- Zhi Zheng
- Zhenkun Wang
- Zhichao Lu
affiliations:
- City University of Hong Kong
- National University of Singapore
- Southern University of Science and Technology
arxiv_id: '2609.21749'
url: https://arxiv.org/abs/2609.21749
pdf_url: https://arxiv.org/pdf/2609.21749
published: '2026-09-17'
collected: '2026-09-21'
category: Agent
direction: Agent技能图结构化与进化优化
tags:
- Agent Skill Optimization
- Graph-structured Skill
- Evolutionary Algorithm
- LLM Agents
- Prompt Optimization
- Workflow Guidance
one_liner: 将Agent技能表示为有向图并用进化算子搜索优化，平均精度比SkillOpt提升1.76–4.01个百分点
practical_value: '- 在电商导购/客服 Agent 中，把任务 SOP 改成有向图技能：节点为执行步骤（意图识别、商品召回、属性比较、推荐解释），边为条件路由，能减少
  LLM 对非结构化指令的理解歧义和冗余，提升多步推理稳定性。

  - 将图技能作为可自动优化的结构化搜索空间：维护多个候选技能，用验证集或线上指标（转化率、点击率、任务成功率）做适应度，对节点/边执行 LLM 变异与交叉，组合不同技能的优质子图，比单条
  prompt 自改写更容易搜出强工作流。

  - 工程上可采用“初始化→验证打分→选 Top-N→变异/交叉→再验证”的离线或低流量循环，自动优化搜索推荐 Agent 的 prompt/workflow；重点是把上下文相关转移显式建模为边，避免非结构化
  prompt 的冗余。

  - 实现交叉/变异时需加入图结构校验，防止生成不可达或环状技能图；这在实际落地中比论文结果的精度提升更关键。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：LLM Agent 技能通常是非结构化自然语言指令，缺乏显式工作流引导、冗余大，导致执行困难；其无约束搜索空间过大，使迭代式技能优化效率低。

方法关键点：将技能表示为有向图，节点是执行步骤及操作指导，边编码步骤间的上下文相关转移；在此基础上提出 GraphSkillEvo，一种基于种群的进化优化框架，对图结构技能执行变异和交叉操作。与只用 LLM 迭代自反思不同，它同时维护多个候选技能，保留并组合有效组件，能更广地探索结构化技能空间。

关键结果：在 5 个 Agent benchmark 上，GraphSkillEvo 一致超过强基线 SkillOpt；GPT-5.4-nano 平均精度提升 4.01%，GPT-5.4 提升 1.76%。
