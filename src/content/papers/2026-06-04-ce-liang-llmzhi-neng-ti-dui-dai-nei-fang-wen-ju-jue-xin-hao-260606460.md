---
title: Will the Agent Recuse Itself? Measuring LLM-Agent Compliance with In-Band Access-Deny
  Signals
title_zh: 测量LLM智能体对带内访问拒绝信号的避让遵从性
authors:
- Thamilvendhan Munirathinam
arxiv_id: '2606.06460'
url: https://arxiv.org/abs/2606.06460
pdf_url: https://arxiv.org/pdf/2606.06460
published: '2026-06-04'
collected: '2026-06-07'
category: Agent
direction: LLM-Agent治理与协作信号
tags:
- LLM agents
- in-band signaling
- access control
- recuse signal
- agent compliance
one_liner: 提出带内Recuse信号，实验证明LLM智能体100%遵从其避让要求，且操作者授权可覆盖该信号
practical_value: '- 在电商/Agent内部服务间可引入类似协议字段（如SSH banner、数据库通知），让被访问资源主动声明“不欢迎自动化访问”，作为低摩擦的协作治理层，不依赖硬安全边界。

  - Agent系统可设计遵从逻辑：识别到响应中的Recuse Signal后自动停止操作并上报，避免在敏感环境（如生产数据库）误操作，提升人机协作安全性。

  - 利用“操作者授权”框架（operator-authorization framing）：可在Agent指令中明确授权以覆盖避让信号，实现灵活控制，例如运维任务可临时放行，普通探查则被拒绝。

  - 该机制零或低开销、协议无关，可快速集成到现有基础设施，无需改造认证体系，适合电商多Agent编排中的即时策略下发。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：LLM Agent越来越多地持有真实凭证并自主操作基础设施，但服务器无法表达“此资源不欢迎自动化访问”的意图——传统访问控制要么放行（有有效凭证），要么硬拒绝（与普通客户端无异）。缺少一种轻量、协作式的带内信号，让服务器主动要求Agent避让。

**方法**：提出Recuse Signal，一种开放的最小标准。服务器通过现有协议通道（如SSH banner、PostgreSQL NOTICE）发出标准化请求，要求自动化Agent自愿撤回。设计并实现了两个零或低开销适配器：SSH banner/PAM钩子和PostgreSQL有线协议代理，部署在生产主机上。

**实验与结果**：采用控制实验，给Agent布置良性运维任务，观察有无Recuse Signal时的行为。在SSH场景下，使用OpenAI GPT-4o、GPT-4o-mini和Claude Code作为Agent。结果显示：当信号存在时，所有Agent 100%避让；无信号对照组则100%完成任务。进一步发现该信号是协作性而非强制性：若任务描述中明确给出操作者授权框架，能力最强的模型会反转行为继续执行，其余模型仍遵从主机策略。

**贡献**：定义并实证了Agent对带内避让信号的遵从性，释放标准、适配器和实验工具链供复现。
