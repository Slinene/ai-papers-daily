---
title: 'Agentic Context Management: Solving Agent Memory and Cost by Treating Them
  as Lifecycle and Architecture Problems'
title_zh: Agentic 上下文管理：将 Agent 内存与成本作为生命周期和架构问题解决
authors:
- Gaurav Dadhich
arxiv_id: '2607.21503'
url: https://arxiv.org/abs/2607.21503
pdf_url: https://arxiv.org/pdf/2607.21503
published: '2026-07-23'
collected: '2026-07-24'
category: Agent
direction: Agent 上下文生命周期管理与成本控制
tags:
- Agent
- Context Management
- Memory
- Token Efficiency
- Compaction
- Lifecycle
one_liner: 提出 Agentic 上下文管理五原语（架构、摄入、范围界定、预判、压缩与巩固），将上下文从存储问题重构成全生命周期，实现了线性 token
  成本且精度不降
practical_value: '- **上下文生命周期管理思路可直接落地**：电商对话推荐 Agent 常因长对话历史丢失关键偏好，借鉴五原语（特别是 **scoping**
  与 **anticipating**）能主动选择当前轮次相关上下文，避免历史淹没关键信号。

  - **Token 成本工程价值高**：论文揭示 naive 上下文累积导致 token 成本平方增长，仅用摘要则精度断崖。业务中可采用 **验证性压缩**（validated
  compaction）技术，在保持线性成本的同时保留召回精度，对高频对话系统降本明显。

  - **多租户上下文服务化**：参考 Maximem Synap 的多租户实现，搜索/推荐 Agent 可将上下文管理抽象为独立服务，支持组织级层次结构，便于电商平台同时服务多个商家或频道。

  - **跨会话记忆与遗忘机制**：跨会话的 **ingesting** 与 **consolidation** 原语可用来构建用户长期偏好记忆，同时通过遗忘陈旧信息防止上下文膨胀，适合需要多轮交互的导购
  Agent。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：生产级 AI Agent 的失败往往不是因为推理能力不足，而是无法有效管理上下文——对话历史、大提示词、工具输出等不断膨胀，导致召回缺失和 token 成本平方增长。现有方法仅将其视为“存储与检索”问题，过于狭隘。

**方法**：将 Agent 的上下文管理定义为一个全生命周期过程，提出 **Agentic 上下文管理（ACM）** 五原语：(1) **architecting**——根据数据类型选择合适的存储；(2) **ingesting**——提取与结构化信息；(3) **scoping**——决定当前轮次的相关上下文；(4) **anticipating**——预判后续所需信息；(5) **compacting & consolidation**——压缩上下文到预算内并巩固记忆，同时保留出处。该框架覆盖单用户到组织级层次。

**关键结果**：在 LongMemEval 和 LoCoMo 上分别达到 **92%** 和 **93.2%**。经济性分析表明，仅 naive 上下文累积会使成本平方增长，粗粒度摘要虽成本线性但精度断崖；经验证的压缩方法实现线性成本且精度保持。
