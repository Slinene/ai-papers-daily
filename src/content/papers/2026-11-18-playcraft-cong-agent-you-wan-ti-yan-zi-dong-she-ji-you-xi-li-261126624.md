---
title: 'PlayCraft: Designing Engaging Games from Agent Play Experience'
title_zh: PlayCraft：从 Agent 游玩体验自动设计有吸引力的游戏
authors:
- Weihao Cheng
arxiv_id: '2611.26624'
url: https://arxiv.org/abs/2611.26624
pdf_url: https://arxiv.org/pdf/2611.26624
published: '2026-11-18'
collected: '2026-11-22'
category: MultiAgent
direction: 多 Agent 闭环迭代优化游戏设计
tags:
- Game Design
- Multi-Agent
- Vision-based Agent
- Mastery
- Automated Iteration
one_liner: 提出 PlayCraft 框架，用视觉 Agent 反复游玩并基于学习曲线诊断自动修订游戏以优化 mastery
practical_value: '- 可借鉴 player-crafter 闭环：用模拟用户 Agent 在推荐/搜索界面实际交互并输出结构化行为报告（进度、结果、决策、反思），另一个
  Agent 基于报告诊断体验瓶颈并迭代策略或 UI，替代人工评测。

  - 把「mastery」量化为学习增益和学习斜率，在 A/B 测试中不仅看即时指标，还要看不同熟练度下的表现提升曲线，识别新功能是否具备“越用越好”的潜力。

  - crafter 估计不同技能水平的用户表现并与目标学习曲线对比，可用于个性化推荐/搜索中的新手到专家路径设计，提前发现冷启动或进阶流失问题。

  - 工程上让 player agent 跨 episode 保留记忆，crafter 消费完整报告而非单次反馈，能提高迭代质量；在线系统可采用「用户行为轨迹→反思报告→策略修订」的模块解耦。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：AI Agent 已能生成可玩游戏，但生成结果未必有吸引力。Mastery（玩家通过策略和技能成长逐步克服挑战）是核心吸引来源，但传统设计需大量人工试玩调优。本文研究如何自动化生成能支持 mastery 的游戏。

**方法关键点**：PlayCraft 从初始游戏开始，交替执行「游玩」和「修订」两个阶段。游玩阶段：基于视觉的 player agent 观看游戏画面、执行操作、在多 episode 中追求目标并保留记忆；每 episode 后输出进度、结果、决策和反思报告。修订阶段：crafter agent 读取报告，估计玩家能力，预测不同熟练度下的表现，与目标学习曲线比较，诊断差距后通过改进决策和操作机会来修订游戏，使玩家有意义的成长空间。

**关键结果**：在三种智能设置和全新运行中评估，相比初始游戏，PlayCraft 在多数游戏上带来更大的学习增益和更陡的学习斜率；在每个智能设置下，宏观平均指标均优于基线。
