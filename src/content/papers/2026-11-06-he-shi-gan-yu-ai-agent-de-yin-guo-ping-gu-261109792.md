---
title: 'Knowing When to Intervene: Causal Evaluation of AI Agents'
title_zh: 何时干预：AI Agent 的因果评估
authors:
- Ayush Sawarni
- Wenqian Xing
- Tijana Zrnic
- Ramesh Johari
- Vasilis Syrgkanis
affiliations:
- Stanford University
arxiv_id: '2611.09792'
url: https://arxiv.org/abs/2611.09792
pdf_url: https://arxiv.org/pdf/2611.09792
published: '2026-11-06'
collected: '2026-11-09'
category: Eval
direction: Agent 评估 · 因果推断
tags:
- Causal Inference
- Agent Evaluation
- Intervention Policy
- Safety Leaderboards
- Randomized Trials
one_liner: 首个基于随机干预实验的 agent 轨迹因果效应评估框架，可估计动态干预策略并构建安全排行榜
practical_value: '- 在电商客服、推荐对话等 agentic 流程中，可用随机干预实验（如随机触发人工审核或高能力模型验证）收集轨迹数据，估计不同状态/动作下干预的因果效应，从而优化审核策略，在控制成本的同时提升最终成功率。

  - 借鉴论文中的安全排行榜思路，对 agent 动作或状态的风险进行排序，优先审计高风险操作（如退款、价格修改、敏感信息输出），减少人工审核负担。

  - 利用估计出的结构参数设计上下文相关的干预策略：例如只在用户情绪激烈、订单金额高或模型置信度低时介入，而非全局固定规则。

  - 方法仅需小样本轨迹数据即可估计，适合业务冷启动；可迁移到搜索推荐系统中的多步 agent（商品筛选、比价、推荐理由生成），判断何时需要更强模型或人工校验。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：当前 agentic AI 系统的评估主要依赖静态 benchmark，无法回答部署时是否应在 agent 执行轨迹中干预（如人工审核、强模型验证或引导行为）。干预的价值本质是因果推断问题：干预对最终结果是否有益。动态环境下因果效应难以估计，因为干预效果依赖当前状态、环境和 agent 未来行为。

**方法关键点**：利用随机干预（如 verification 或 screening）下收集的少量 agent 轨迹，开发框架估计上下文干预策略的动态因果效应。估计的结构参数可进一步构建安全排行榜，量化不同 agent 动作的风险，用于审计优先级排序。方法适用于丰富的上下文干预策略类。

**关键结果**：在 tau-bench Retail、ToolSandbox 和 ImpossibleBench 上验证，发现干预效应随 agent 动作和状态显著变化，说明部署中需要动态、上下文相关的干预策略，而非全局固定规则。
