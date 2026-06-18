---
title: A Technical Taxonomy of LLM Agent Communication Protocols
title_zh: LLM Agent通信协议技术分类法
authors:
- Linus Sander
- Habtom Kahsay Gidey
- Alexander Lenz
- Alois Knoll
affiliations:
- Technische Universität München
arxiv_id: '2606.19135'
url: https://arxiv.org/abs/2606.19135
pdf_url: https://arxiv.org/pdf/2606.19135
published: '2026-06-17'
collected: '2026-06-18'
category: MultiAgent
direction: 多智体通信协议分类法
tags:
- Agent Communication Protocols
- Taxonomy
- Multi-agent systems
- Schema Flexibility
- LLM Agents
- Protocol Stack
one_liner: 提出五维度分类法，归纳9种开源LLM Agent协议的核心模式与趋势
practical_value: '- 选型参考：在搭建多Agent推荐/搜索系统时，对照 counterparty、payload、session state、discovery
  和 schema flexibility 五个维度评估候选协议，避免因碎片化导致后期集成困难。

  - 实现建议：Agent间通信必须保持会话状态（session state），且 payload 应支持混合传输（文本消息+结构化数据），才能支撑多轮推理与工具调用。

  - 架构分层：借鉴论文提出的“发现→执行→交互”分层栈，将工具/数据接入用轻量协议（如MCP），复杂Agent协商采用 schema 可演进的协议（如Agora/ANP），降低整体耦合度。

  - 去中心化趋势：当前多数协议依赖中心化注册，若业务需要大规模分布式Agent，可预先探索 P2P 发现机制（如LMOS的混合发现），提升系统鲁棒性与扩展性。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**  
随着LLM-based 多智体系统（MAS）快速发展，异构Agent间的无缝通信成为制约系统扩展与互操作的关键瓶颈。当前协议生态碎片化，尚无统一分类框架帮从业者理清选型逻辑。研究切中痛点：没有标准化的通信基础设施，Collective Intelligence 难以实现。

**方法**  
采用Nickerson的迭代式分类法，以9个开源活跃协议（MCP、A2A、LAP、agents.json、Agora、ANP、LMOS、ACP、agntcy）为对象，经过3轮经验→概念、2轮概念→经验共5次迭代，构建出五维度分类体系：
1. **Counterparty**：Agent、Context、Hybrid，区分通信对方是Agent还是工具/数据。
2. **Payload**：Structured data/artifacts、Conversation focused、Hybrid，区分传输数据类型是纯结构化还是包含自由文本。
3. **Interaction State**：Stateless、Session state，协议是否维护通话级会话。
4. **Discovery Mechanism**：Static、Centralized、Partially centralized、Decentralized、Hybrid，Agent如何发现对端。
5. **Schema Flexibility**：Single、Multiple、Evolving，通信结构是否可以动态调整。

**关键结果**  
- 所有采样的Agent-to-Agent协议均提供Session state和Hybrid payload，以支撑多轮对话与工具调用；仅MCP和agents.json是为工具/数据接入设计，属Stateless且Payload为纯结构化。
- 7/9协议支持多个预定义Schema，仅Agora和ANP具备运行时Schema协商能力（Evolving），是未来动态协作的关键特性。
- 去中心化发现机制稀缺，只有LMOS提供混合发现，多数依赖中心化注册或静态配置，可能限制大规模分布部署。
- 将分类投影到“通用性-效率-可移植性”三维度，揭示出不可能存在单一全能协议，从而论证了分层协议栈的必要性（类似OSI模型），并给出候选五层架构：身份/传输→发现→执行→交互→商议。

**值得记住的一句话**  
没有单一协议能同时最大化通用性、效率和可移植性，LLM Agent的通信未来必然走向分层、联邦化的协议栈。
