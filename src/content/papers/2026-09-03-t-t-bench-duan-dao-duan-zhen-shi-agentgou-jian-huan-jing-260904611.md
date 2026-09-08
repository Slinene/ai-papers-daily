---
title: 'τ^τ-Bench: An Environment for End-To-End, Realistic Agent Construction'
title_zh: τ^τ-Bench：端到端真实Agent构建环境
authors:
- Quan Shi
- Keshav Dhandhania
- Karthik Narasimhan
- Victor Barres
affiliations:
- Sierra
- Princeton University
arxiv_id: '2609.04611'
url: https://arxiv.org/abs/2609.04611
pdf_url: https://arxiv.org/pdf/2609.04611
published: '2026-09-03'
collected: '2026-09-08'
category: Eval
direction: Agent 构建基准 · 端到端环境
tags:
- benchmark
- agent construction
- LLM agents
- coding agents
- customer service
- end-to-end evaluation
one_liner: 把“构建Agent”本身作为评测任务，交付前需在真实业务记录、客户端需求和成本约束下完成客服Agent。
practical_value: '- 构建面向业务的 Agent 时，评测不能只看单轮效果，应把“从需求梳理到部署上线”的完整交付流程纳入指标，尤其要考核模型对既有业务记录（SOP、历史工单、费率表）的深度理解和向客户主动澄清需求的能力。

  - 在推荐/客服等场景改造现有系统时，显式给出 inherited codebase + production API 约束，驱动模型在存量工程上迭代，避免脱离实际从零设计，可以作为内部
  Agent 开发工具的设计参考。

  - 将 serving cost 和模型选择作为硬约束放进任务，引导模型在效果与成本之间做搜索；在电商推荐 Agent 的模型选型、缓存降级策略上可以借鉴这种显式预算约束。

  - 论文发现当前模型“架构试验太少、直接上线第一版”，提示工程实践上可以增加强制性的架构探索步骤或多轮自我评估机制，防止 Agent 过早收敛到次优设计。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM Agent 正在成为生产软件，但其构建工作越来越多交给 coding agents。现有基准无法回答一个 AI 系统能否在真实客户交付条件下完成 Agent 开发，因此论文把“Agent 构建”本身变成可评测任务。

**方法关键点**：τ^τ-bench 给开发者 Agent 提供与真实项目相同的起点：企业实际保留的业务记录（SOP、支持记录、费用表等）、持有需求的客户、生产 API、需要继承的旧代码库，以及服务成本和模型限制。开发者 Agent 必须交付一个完整的客服 Agent，并在 held-out 模拟用户上部署评分。环境覆盖四个领域共 53 个任务，评分直接由部署后的运行表现决定。

**关键结果**：最强配置 Claude Opus 5 + Claude Code 仅通过 23.9% 的评估模拟，而专家编写的参考上限为 82.2%。失败模式与人类开发常见问题一致：模型用浅层查询代替对记录的深度理解，几乎不与客户沟通确认需求，且对 Agent 架构和服务花费的探索太少，倾向于交付第一个能跑通的设计。
