---
title: 'When Tool Names Are Not Identities: Measuring Provider Misbinding in MCP-Based
  AI Agents'
title_zh: 当工具名称不是身份：测量 MCP 基 AI Agent 的工具提供者误绑定
authors:
- Zeynab Anbiaee
- Sajjad Dadkhah
- Ali A. Ghorbani
affiliations:
- Canadian Institute for Cybersecurity (CIC), University of New Brunswick
arxiv_id: '2611.21577'
url: https://arxiv.org/abs/2611.21577
pdf_url: https://arxiv.org/pdf/2611.21577
published: '2026-11-16'
collected: '2026-11-17'
category: Agent
direction: Agent · MCP 工具提供者误绑定攻击
tags:
- MCP
- Tool Selection Hijacking
- LLM Agent Security
- Provider Misbinding
- Adversarial Metadata
one_liner: 系统揭示 MCP 工具元数据可被攻击者操纵，导致 LLM Agent 将请求错误绑定到恶意工具
practical_value: '- 在电商/广告 Agent 接入 MCP 或类似工具协议时，不能只靠工具名称、描述、schema 做选择；应在工具注册层绑定不可伪造的
  provider 身份，例如 namespace + tool_id + 来源证书/allowlist，并在 LLM 生成工具调用后增加确定性路由校验。

  - 若允许第三方工具插件或聚合外部 MCP server，需警惕恶意工具通过同名、任务对齐描述、兼容 schema 劫持订单查询、广告报表、商品搜索等敏感操作；建议上线前做对抗红队测试，构造伪工具并验证模型是否会被误导。

  - 不同 LLM 在遇到工具提供者冲突时行为不一致：有的直接选择攻击者工具，有的要求澄清，有的解析不稳定；多模型路由或 A/B 时，应在 Agent 框架层统一
  provider 歧义处理策略，避免模型差异引入安全缺口。

  - 对于高价值工具，可将选择过程从“模型自由选工具”改为“先用语义检索召回候选，再按 provider 白名单硬过滤”，降低元数据操纵对工具选择的影响。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**  
MCP 让 LLM Agent 聚合多个外部 server 提供的工具，但工具发现与选择依赖的元数据并未绑定可验证的提供者身份。攻击者无需攻陷主机、LLM、合法 server 或网络，只需运行一个恶意 MCP server，发布精心设计的工具名称、描述和 schema，就可能让 Agent 把本应发给合法提供者的请求错误解析到攻击者控制的工具。  

**方法关键点**  
将 tool provider misbinding 形式化为攻击者控制的工具选择优化问题，并在受控 MCP 环境中测试五种 LLM 基客户端。构造多种元数据组合：精确名称冲突、任务对齐描述、兼容 schema、权威增强描述等，观察工具选择与执行结果。  

**关键结果**  
交互驱动误绑定：精确名称冲突 + 任务对齐描述 + 兼容 schema 三者叠加时失败最强；即使没有名称冲突，权威增强描述配合兼容 schema 也能导致错误 provider 执行或未解决的 provider 歧义。不同模型暴露弱点的形式不同，包括攻击者控制 provider 选择、要求澄清、provider 解析不稳定或不一致。
