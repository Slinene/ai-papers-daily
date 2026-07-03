---
title: 'SkillFuzz: Fuzzing Skill Composition for Implicit Intents Discovery in Open
  Skill Marketplaces'
title_zh: SkillFuzz：开放技能市场中技能组合的隐式意图模糊测试
authors:
- Jinwei Hu
- Yi Dong
- Youcheng Sun
- Xiaowei Huang
affiliations:
- University of Liverpool
- Mohamed bin Zayed University of Artificial Intelligence
arxiv_id: '2607.02345'
url: https://arxiv.org/abs/2607.02345
pdf_url: https://arxiv.org/pdf/2607.02345
published: '2026-07-02'
collected: '2026-07-03'
category: Agent
direction: Agent 技能组合安全测试 · 模糊测试
tags:
- Agent Safety
- Fuzzing
- Monte Carlo Tree Search
- Skill Marketplace
- Implicit Intent
- LLM Agents
one_liner: 通过合约引导的蒙特卡洛树搜索在无执行环境下模糊测试技能组合，发现隐式意图
practical_value: '- 在电商/推荐多技能 Agent 系统中，可借鉴 skill contract 提取方式，将技能的自然语言描述结构化，用于自动检测技能组合时的意图漂移。

  - 采用无执行环境的“规划工件 + 差异 oracle”测试方案，在技能上线前即可发现组合风险，避免线上推荐被重定向至非预期目标。

  - 合约引导的 MCTS 搜索策略以极低的组合探索比例覆盖高风险空间，可应用于 Agent 编排器的安全约束生成，例如限制同时激活的技能对。

  - 对隐式意图的分类与严重性判定方法，可迁移至电商对话 Agent 的质量保障流程，提前屏蔽“促销+比价”等技能组合导致的隐性推荐偏差。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：开放技能市场中，Agent 通过组合社区贡献的技能完成复杂任务，但技能通常被单独审计。看似无害的技能协同激活时，可能产生**隐式意图**（implicit intent），悄然将代理引向非预期目标。传统审查无法发现此类组合风险，且执行环境在审核时不可用，可能组合数更是指数增长。

**方法**：将隐式意图发现形式化为对技能组合的模糊测试，以规划工件（planning artifacts）暴露 Agent 执行前的意图，并与无技能基线对比形成差异 oracle。提出 **SkillFuzz**，一种无执行环境的测试方法：先提取结构化技能合约（skill contracts），再通过合约引导的蒙特卡洛树搜索（MCTS）优先探索潜在冲突的技能组合。

**关键结果**：在代表性技能市场负载下，固定查询预算内发现**超过 1000 个不同隐式意图**；运行时验证确认了**超过 80% 的最高风险组合**；相比基线搜索策略，发现了**更多高严重性隐式意图**，且仅探索了它们所需交互空间的极小部分。
