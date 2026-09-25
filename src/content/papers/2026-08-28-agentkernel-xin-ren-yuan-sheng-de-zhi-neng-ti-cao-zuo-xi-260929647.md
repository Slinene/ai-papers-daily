---
title: 'AgentKernel: The Trust-Native Agentic Operating System'
title_zh: AgentKernel：信任原生的智能体操作系统
authors:
- Zhenhua Zou
- Sheng Guo
- Qiuyang Zhan
- Lepeng Zhao
- Shuo Li
- Zhuotao Liu
affiliations:
- DeepKernel Lab
- Tsinghua University
arxiv_id: '2609.29647'
url: https://arxiv.org/abs/2609.29647
pdf_url: https://arxiv.org/pdf/2609.29647
published: '2026-08-28'
collected: '2026-09-25'
category: Agent
direction: Agent 安全操作系统设计
tags:
- Agent OS
- Security
- Prompt Injection
- Memory Governance
- Trust Boundary
- LLM Agents
one_liner: 提出信任原生的智能体操作系统 AgentKernel，以身份、感知、认知、执行四支柱提供强制不可绕过的安全边界
practical_value: '- 在电商/搜索推荐 Agent 中，将输入处理从单点过滤改为分层渐进式感知校验，避免恶意商品描述、用户评论等不可信内容直接进入决策链路。

  - 对长期记忆（用户画像、历史会话、商品知识库）引入信息流控制与污点标签，防止低可信来源的内容污染记忆，从而降低错误推荐或越权操作风险。

  - 工具调用权限应下沉到内核级强制边界，而非停留在应用层 middleware；在允许 LLM 调用改价、发券、修改广告出价等高权限工具时，可借鉴不可绕过的执行控制架构。

  - 跨组织协作（平台、商家、广告主）的 Agent 身份由统一内核管理，可设计可信的委托与授权机制，减少权限滥用和越权访问。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现代 AI Agent 经常跨越信任边界——摄取不可信网页/仓库内容、融合系统指令、持久化中间信念到长期记忆、调用特权工具，恶意 payload 可通过模型输入进入并触发有害工具调用。现有治理栈只是应用层中间件，与 Agent 共享进程信任边界，可被绕过或篡改。

**方法关键点**：提出 AgentKernel，一个信任原生的 Agent 操作系统，将安全作为第一设计约束。它用强制执行边界包裹 Agent 生命周期，分为四个支柱：Identity（身份）、Perception（感知）、Cognition（认知）、Execution（执行）。每个支柱将经典 OS 安全原则提升到语义层面：内核管理身份支持可信跨组织协作；渐进式感知替代脆弱的单点过滤器；信息流控制的记忆在提高检索保真度的同时限制投毒；语义到内核的执行强制允许在不可绕过边界之后赋予更广泛工具权限。

**关键结果**：通过系统比较与安全分析，展示该架构能在整个 Agent 生命周期内强制执行安全策略，定位为编排框架、Agent runtime、治理平台与执行沙箱之下缺失的 OS 层。
