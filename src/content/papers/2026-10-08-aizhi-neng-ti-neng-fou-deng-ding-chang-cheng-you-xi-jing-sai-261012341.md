---
title: Can AI Agents Learn Their Way to the Top? Evaluating Heuristic Learning in
  a Long-Running Game Agent Competition
title_zh: AI智能体能否登顶？长程游戏竞赛中的对抗式启发式学习评估
authors:
- Kaisen Yang
- Qingle Liu
- Kejin Wang
- Yicheng Zhao
- Jieming Li
- Shenghan Zheng
- Ruize Yang
- Bojun Yang
- Heng Gong
- Xiang Gao
affiliations:
- Department of Computer Science and Technology, Tsinghua University
- College of AI, Tsinghua University
arxiv_id: '2610.12341'
url: https://arxiv.org/abs/2610.12341
pdf_url: https://arxiv.org/pdf/2610.12341
published: '2026-10-08'
collected: '2026-10-10'
category: Agent
direction: Agent 在对抗游戏中的长周期自我改进
tags:
- Adversarial Heuristic Learning
- LLM Agents
- Game AI
- Benchmark
- Self-Improvement
one_liner: 提出 AHL 范式与 AAArena 基准，评估 LLM 智能体在 12 个对抗游戏中通过选对手、分析回放和改策略爬升排名
practical_value: '- 可借鉴 AHL 的“固定模型权重、让 LLM 作为教练从对局/日志回放中提取规则并修改策略代码”的闭环；在推荐/广告场景可让
  LLM 定期分析线上 bad case sessions，产出可解释规则或轻量策略补丁，而不直接改动模型，降低上线风险。

  - 论文发现 opponent selection 支持策略提升；对应推荐里困难样本/对抗样本挖取，让 agent 优先复盘高价值失败流量（如高竞价失败、低转化但高曝光），提升迭代效率。

  - dense feedback 支持改进；在设计 RLHF/策略迭代时，除了最终指标（GMV/CTR），给 agent 中间步骤奖励或分阶段反馈，避免长程稀疏奖励导致学习困难。

  - on/off-policy 回放都有效：线上策略迭代可以同时利用自己的日志（on-policy）和竞品/他组日志（off-policy）做分析，尤其冷启动期可借其他方案数据。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：对抗游戏从启发式搜索到 RL 进步巨大，但有限样本下学习策略仍难。AI agent 可将对局经验转化为策略修订，替代需要大量样本的权重更新。

**方法**：论文形式化 AHL——固定模型权重，以 LLM agent 为学习引擎，在真实竞赛协议下自行完成规则理解、对手选择、回放分析、修改参赛程序。提出 AAArena，含 12 个真实对抗游戏、1920 个人类程序，以固定比赛与评估预算衡量排名。

**结果**：7 个模型/harness 配置中，Opus5.5+Claude Code 获 6 金（排名第一），但无一配置登顶其余 6 个人类 ladder；规则规格越复杂表现越差。消融表明对手选择和密集反馈显著促进策略提升；agent 既能从自己比赛的 on-policy 回放学习，也能从他人比赛的 off-policy 回放获益。

**结论**：AHL 在对抗游戏有潜力，挑战仍在游戏理解、策略实现和长程策略开发。
