---
title: 'Bounded Agents: Delegation Security for Multi-Agent AI Systems'
title_zh: 有界智能体：多智能体 AI 系统的委托安全机制
authors:
- Xabier Muruaga
affiliations:
- Independent Researcher
arxiv_id: '2608.15888'
url: https://arxiv.org/abs/2608.15888
pdf_url: https://arxiv.org/pdf/2608.15888
published: '2026-08-15'
collected: '2026-08-22'
category: MultiAgent
direction: 多智能体委托授权安全
tags:
- Agentic AI
- Delegation Security
- Prompt Injection
- Authorization
- Composition Closure
- Multi-Agent
one_liner: 提出 Agentic Principal Chain，在模型外强制执行基于会话状态的授权检查，将 AgentDojo 数据外泄从 75-100%
  降至 0%
practical_value: '- 在电商/广告 Agent 工具执行前，增加独立于 LLM 的授权门控层：维护 session 状态，检查“当前工具调用 +
  之前动作”的组合是否触碰禁止规则，而不只评估单次请求权限；APC 的 composition closure 可直接对应“禁止读取用户手机号后调用外部 webhook”这类组合风险。

  - 对子 Agent 委托必须显式传递并收缩权限范围与预算：APC 证明的 Blast Radius Monotonicity 表明最小权限委托能控制爆炸半径，可复用于多
  Agent 架构中订单、优惠券、用户数据等工具的下发权限。

  - 工程上，0.24ms p99 授权延迟对推荐/广告 Agent 的实时链路可接受；将授权决策与模型推理解耦，使其不被 prompt injection 影响，适合作为在线风控旁路。

  - 注意 trade-off：AgentDojo 效用下降 8.6-13.9 个百分点，业务落地上需按场景灰度，在安全与任务完成率之间配置可调的禁止组合规则。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：LLM agent 权限静态、请求独立评估，无法防止越权组合或未受限子代理委托；prompt 注入风险本质是授权架构问题，而非仅靠模型解决。

方法关键点：提出 Agentic Principal Chain (APC)，在会话状态上累积委托权限，执行六项授权检查；携带并收紧委托 scope/budget；利用 composition closure 检查当前请求与先前动作的组合是否构成禁止结果，并在模型外强制决策。证明 Blast Radius Monotonicity 和 Composition Soundness（在完整限制集和串行准入下）。

关键结果：在 InjecAgent、AgentDojo、ASB 的 3154 个实例评估。AgentDojo 四个域的数据外泄从 75-100% 降到 0%；APC 阻止全部 544 个 InjecAgent 数据窃取；意图绑定使破坏从 38.6% 降至 4.0%，操纵从 90.5% 降至 12.1%；授权延迟 99 分位 0.24ms；效用降幅 8.6 和 13.9 个百分点。
