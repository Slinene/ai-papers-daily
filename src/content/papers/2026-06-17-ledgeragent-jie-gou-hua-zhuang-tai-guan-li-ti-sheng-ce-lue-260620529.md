---
title: 'LedgerAgent: Structured State for Policy-Adherent Tool-Calling Agents'
title_zh: LedgerAgent：结构化状态管理提升策略遵循工具调用Agent
authors:
- Md Nayem Uddin
- Amir Saeidi
- Eduardo Blanco
- Chitta Baral
affiliations:
- Arizona State University
- University of Arizona
arxiv_id: '2606.20529'
url: https://arxiv.org/abs/2606.20529
pdf_url: https://arxiv.org/pdf/2606.20529
published: '2026-06-17'
collected: '2026-06-20'
category: Agent
direction: Agent 工具调用状态维护与策略检控
tags:
- Structured State
- Policy Adherence
- Tool-Calling Agents
- Customer Service
- Prompting
- Multi-Turn Consistency
one_liner: 显式维护任务状态账本，在工具调用前做策略校验，显著减少违规与状态遗忘
practical_value: '- 在电商客服、订单查询/修改等会话Agent中，显式用「账本」存储订单号、用户约束、已确认事实，而非全部塞进prompt，可大幅降低多轮遗忘与错误决策。

  - 对于写操作（如退款、改地址），在调用工具前加一层基于账本的策略校验（如“是否满足退款条件”），直接阻断违规操作，降低人工兜底成本。

  - 该方法是推理时技术，无需微调，适用于已有工具调用Agent的快速加固，尤其对开源小模型提升一致性和遵循策略有明显收益。

  - 在搜索推荐对话Agent中，可维护用户偏好、过滤条件等状态账本，避免重复询问或推荐已被否决的选项，提升体验与效率。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：传统工具调用Agent将对话历史、工具返回、策略指令全部堆入prompt，状态管理隐式，导致两类常见失败：① 决策时基于过时、缺失或错误的信息；② 语法正确的工具调用却违反当前状态下的业务策略。客户服务领域（如订单处理、预约修改）对多轮状态保持和策略遵循要求极高，该问题尤为突出。

**方法关键点**：提出LedgerAgent，在推理阶段维护一个独立的结构化「账本」（ledger），专门存储从用户交互和工具返回中抽取的关键任务状态（事实、ID、约束、条件等）。每一轮将账本内容渲染进prompt，让模型直接基于明确状态进行决策；同时，在执行任何会改变环境的工具（如写操作）前，利用账本自动检查状态依赖的策略约束，若即将违反则直接拦截该调用。账本更新与策略检查均轻量实现，不改变底层模型。

**关键结果**：在四个客户服务领域及多个开源/闭源模型上，LedgerAgent相比标准prompt工具调用方式，平均pass^k指标显著提升，尤其在严格的多试验一致性指标（要求多次运行均不出错）上收益最大，证明显式状态管理有效减少了状态遗忘与策略违规。
