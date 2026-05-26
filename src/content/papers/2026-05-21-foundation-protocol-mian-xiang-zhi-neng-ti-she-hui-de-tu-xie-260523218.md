---
title: 'Foundation Protocol: A Coordination Layer for Agentic Society'
title_zh: Foundation Protocol：面向智能体社会的图原生协调层协议
authors:
- Bang Liu
- Yongfeng Gu
- Jiayi Zhang
- Zhaoyang Yu
- Sirui Hong
- Maojia Song
- Xiaoqiang Wang
- Mingyi Deng
- Zijie Zhuang
- Ronghao Wang
affiliations:
- FoundationAgents
- Université de Montréal & Mila
- DeepWisdom
- HKUST(GZ)
- Singapore University of Technology and Design
arxiv_id: '2605.23218'
url: https://arxiv.org/abs/2605.23218
pdf_url: https://arxiv.org/pdf/2605.23218
published: '2026-05-21'
collected: '2026-05-26'
category: MultiAgent
direction: Agent 多智体协调协议设计
tags:
- MultiAgent Coordination
- Agent Protocol
- Economic Primitives
- Auditable Provenance
- Graph-Native Architecture
- Progressive Disclosure
one_liner: 提出以图为核心的 Foundation Protocol，将实体、组织、经济交换和可审计溯源统一为智能体社会的协调基板。
practical_value: '- **统一实体模型**：在电商多智能体系统中，可将供应商、客服、风控、物流等均视为 Entity，通过统一地址、身份、能力声明管理，避免异构协议拼接。

  - **渐进式披露与低开销**：仅先交换轻量元数据，按需加载详细 schema，类似推荐系统中延迟加载物品特征，可显著降低大模型 token 消耗。

  - **协议层审计与政策执行**：将审核、预算控制、人工审批等设计为检查点流水线，使订单处理、退款等关键动作自带可查验的证据链，适合金融或监管场景。

  - **经济原语与可组合组织**：内置计量、收据、结算钩子，支持以组织为单位的角色与权限管理，可直接参考用于构建多主体交易市场或自动化企业流程。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：随着自主智能体广泛参与浏览、采购、部署等在线活动，智能体社会面临的核心瓶颈从单体能力转向协调、治理与问责。现有协议（MCP、A2A、DIDComm 等）各自解决一部分边界问题，但碎片化导致跨协议协作时身份、会话、权限、溯源语义断裂，集成成本高、可审计性差。

**方法关键点**：
- 采用**图原生视角**：将智能体、人、工具、机构等均建模为图中节点，关系、会话、成员身份为边，交互为活动。
- 定义**四个协平面**：实体与信任平面（统一身份、能力、隐私）、传输与路由平面（可插拔传输、发现）、交互与组织平面（会话、角色、经济原语）、监管与监督平面（策略执行、溯源、审计）。
- 精简核心语义，仅包含七个通用对象：Entity、Session、Activity、Envelope、Event、Receipt/Settlement、Provenance。
- **渐进式披露**：通过 EntityCard 先交换摘要，减少 token 开销，并按需获取完整 schema。
- **检查点流水线**：所有消息必经可组合的策略执行点（如访问控制、预算、人机审批），证据自动生成。
- 通过**协议桥接**复用 MCP、A2A 等已有生态。

**关键结果**：论文以协议设计和架构阐述为主，包含一个 AI 公司运营的端到端场景模拟，展示了实体注册、跨组织发现、异构协作、经济结算与审计等流程如何在统一基板上运行。开源参考实现验证了 AI 提供商（Claude Code、Codex CLI）和 MCP 工具服务器的桥接可用性，尚未提供量化评测。其核心主张是：通过将问责固化到通信基板，使多智能体系统可在规模化时依然保持可控性和可发展性。
