---
title: 'Vibe-Trading: Towards Agent-Native Trading'
title_zh: Vibe-Trading：面向 Agent 原生的交易框架
authors:
- Haozhe Wu
- Zhonghang Li
- Chao Huang
affiliations:
- The University of Hong Kong
arxiv_id: '2611.24845'
url: https://arxiv.org/abs/2611.24845
pdf_url: https://arxiv.org/pdf/2611.24845
published: '2026-11-18'
collected: '2026-11-19'
category: Agent
direction: Agent 原生框架 · 状态溯源与权限控制
tags:
- Agent-native
- Provenance
- State Management
- Financial Trading
- Multi-Agent
- Research-to-Action
one_liner: 提出 Vibe-Trading 交易 Agent 框架，通过结果溯源、版本化证据与权限门控保障动态环境下的可靠决策与执行
practical_value: '- 在推荐/广告系统的 Agent 工作流中，对每个中间结果（召回集、排序分数、策略配置）强制记录数据快照版本、时间范围、运行
  ID、配置哈希，类似 Vibe-Trading 的 provenance，便于线上问题追踪和策略回滚。

  - 借鉴 authority gate：将离线实验与在线部署分离，要求策略变更经过审批或自动验证才能生效，防止未经验证的策略影响线上。

  - 多智能体协作时建立共享 evidence store，让负责用户理解、召回、排序的 agent 访问同一份实时特征和数据版本，避免状态不一致。

  - 利用版本化研究记录支持可复现 continuation：当线上策略效果异常时，可以从历史研究记录中恢复上下文，继续迭代而不丢失上下文。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有 Agent 框架依赖静态工作流，在金融交易等动态环境下难以保持可靠状态与溯源，导致结果无法可靠复用和执行。

**方法关键点**：Vibe-Trading 统一市场研究、金融数据、策略生成、回测、组合分析、paper trading、多智能体协作与可选 broker execution。核心架构保障 results、evidence、research history、trading authority 在全链路关联：每个结果保留来源、时间范围、配置与产生 run；共享 evidence grounding 支持验证；版本化研究记录支持可复现 continuation；显式 authority gate 分离策略研究与 live execution。

**关键结果数字**：原文未提供具体评测指标，核心贡献为架构能力，确保结果可追溯、可复现、仅在显式授权下执行。
