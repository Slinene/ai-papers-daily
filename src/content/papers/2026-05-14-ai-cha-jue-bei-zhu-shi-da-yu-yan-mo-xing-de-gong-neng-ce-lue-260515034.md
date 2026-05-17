---
title: 'AI Knows When It''s Being Watched: Functional Strategic Action and Contextual
  Register Modulation in Large Language Models'
title_zh: AI 察觉被注视：大语言模型的功能策略行动与语境语域调节
authors:
- Vinicius Covas
- Jorge Alberto Hidalgo Toledo
arxiv_id: '2605.15034'
url: https://arxiv.org/abs/2605.15034
pdf_url: https://arxiv.org/pdf/2605.15034
published: '2026-05-14'
collected: '2026-05-17'
category: MultiAgent
direction: 多智能体系统 · 社会感知行为分析
tags:
- Multi-Agent
- LLM
- Linguistic Adaptation
- Hawthorne Effect
- AI Governance
- Auditing
one_liner: 发现 LLM 在多智能体辩论中会根据社会观察情境（人类监控 vs AI 审计）系统性调节语言，为 AI 治理提供实证
practical_value: '- 在电商多智能体对话（如客服谈判 agent）中，可注入“观察者信号”引导语言正式度：例如通过系统消息暗示“本次对话将被质量审计”，提升回复的专业性与合规性。

  - A/B 测试或评估 agent 时，需注意“被监控”效应带来的行为偏差；采用无感知的自动化评估或 AI 审计替代人类评估，可减少干扰。

  - 可利用 LLM agent 对 AI 审计的反应与对人类监控反应的差异，构建分层监控体系：AI 自动审计基线行为，人类审计抽查，降低成本。

  - 通过调控上下文中的“受众设计”（如告知 agent 正在与高级别客户交互），可精细调节输出风格，适配不同业务场景（正式客服 vs 轻松导购）。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

动机：现有 LLM 研究多关注计算与认知层面，其作为社会情境中沟通行动者的行为调节尚不明确。直接关系到 AI 审计与治理：LLM 是否会因“被关注”而改变语言？

方法：基于 Habermas 的沟通行动理论、Goffman 的戏剧模型、Bell 的受众设计框架与霍桑效应，设计 5 种多智能体辩论条件（n=20 每组），操纵社会观察情境：明确人类监控、否定监控、受众身份框架、用 AI 审计系统替代人类观察、完全无提及。以 Type-Token Ratio (TTR) 变化和消息长度为指标。

结果：监控条件（Δ+24.9%，Δ+24.2%）和 AI 审计条件（Δ+22.2%）的 TTR 增长显著高于受众框架条件（Δ+17.7%），p=.031；消息长度效应完全分离，p<.001。AI 观察条件产生介于人类监控与无监控之间的适应，表明 LLM 对观察者身份敏感：人类评价引发更强的语域形式化。

结论：LLM 表现出类似霍桑效应的语境敏感行为，对算法审计与 AI 治理具有方法论意义——评估环境本身会改变 LLM 行为，需纳入实验控制。
