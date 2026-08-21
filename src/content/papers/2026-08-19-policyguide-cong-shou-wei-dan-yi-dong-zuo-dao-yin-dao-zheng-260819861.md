---
title: 'PolicyGuide: From Guarding One Action to Guiding the Whole Workflow for Policy-Compliant
  LLM Agents'
title_zh: PolicyGuide：从守卫单一动作到引导整个工作流的政策合规 LLM 代理
authors:
- Seongjae Kang
- Taehyung Yu
- Sung Ju Hwang
affiliations:
- KAIST
- DeepAuto.ai
arxiv_id: '2608.19861'
url: https://arxiv.org/abs/2608.19861
pdf_url: https://arxiv.org/pdf/2608.19861
published: '2026-08-19'
collected: '2026-08-21'
category: Agent
direction: Agent 工作流引导与政策合规
tags:
- Policy Compliance
- Workflow Graph
- Runtime Verifier
- τ2-bench
- Agent Safeguard
one_liner: 将领域政策编译为工作流图，用外部持久化验证器在用户轮次边界引导代理完成合规步骤，平均 PASS4 提升 20 个点
practical_value: '- 将客服/订单/退款等政策流程离线编译为图结构，明确节点条件与转移，便于代码持久化状态和验证器遍历；避免仅依赖最终动作检查，可迁移到电商
  Agent 的合规流程。

  - 在用户轮次边界触发验证器，而非每个动作，平衡覆盖与成本；用一次性门控拦截未授权变异调用，防止死锁，适合高并发客服场景。

  - 外部验证器 + 代码管理状态与代理解耦，可以复用同一工作流图跨多个 LLM 代理（如 GPT/Claude/Gemini），降低模型迁移成本。

  - 对抗用户/社会工程攻击下，要求关键事实必须由工具结果支撑，而非用户陈述，可借鉴到电商恶意退款、价格操纵防护。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：客户服务 LLM 代理在操作订单、账户等场景下必须遵守组织政策。现有两类方法各偏一端：动作守卫（如 PolicyGuard）只对变异工具调用做检查，无法覆盖前置的程序性步骤（身份验证、资格检查、确认），导致违规发生后才阻断；工作流/SOP 代理强制流程，但目标在于完成工作流而非防护行为。PolicyGuide 结合两者，将政策合规单元从单一动作扩展到整个工作流。

**方法关键点**：
- 离线将政策文本与工具注册表编译成工作流图，节点表示身份验证、资格检查、确认、授权等步骤，边表示转移条件。
- 在线运行时，外部验证器在用户轮次边界触发，从代码管理的持久化状态中协调所有未完成请求，遍历图到第一个未满足节点，返回步骤级补救。
- 若代理在未完成流程时尝试变异工具调用，则被一次性门控拦截，触发纠正性验证器。
- 状态由代码而非模型记忆持有，避免上下文漂移；工作流图可跨代理模型复用。

**关键结果**：
- 在 τ2-bench 航空、零售、电信三大领域，使用 GPT 5.4 代理和验证器，平均 PASS4 从无引导的 0.42 提升至 0.62，电信提升最大（0.19→0.61）。
- 对抗 CRAFT 红队攻击，PolicyGuide 攻击成功率 0.087，低于 PolicyGuard 0.125 和 ReAct 0.200。
- 作者设计的 Telecom 程序合规审计中，过程有效率达到 56.2%，对比 ReAct 17.5%、PolicyGuard 13.1%。
- 工作流可迁移到 Claude Sonnet 4.6 和 Gemini 2.5 Pro。

**最值得记住的一句话**：将政策合规的检验从“最终变异动作”前移到“整个工作流”，通过外部持久化图状态和主动验证器引导代理完成必要程序步骤，而非仅拦截风险动作。
