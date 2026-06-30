---
title: 'PolicyGuard: A Dialogue-Grounded Sub-Agent Verifier for Policy Adherence in
  LLM Agents'
title_zh: PolicyGuard：基于对话的子代理验证器用于LLM代理策略遵循
authors:
- Seongjae Kang
- Taehyung Yu
- Sung Ju Hwang
affiliations:
- KAIST
- DeepAuto.ai
arxiv_id: '2606.29225'
url: https://arxiv.org/abs/2606.29225
pdf_url: https://arxiv.org/pdf/2606.29225
published: '2026-06-27'
collected: '2026-06-30'
category: Agent
direction: 对话驱动的策略合规验证
tags:
- policy adherence
- LLM agents
- sub-agent verifier
- dialogue-grounded
- safeguard
one_liner: 提出对话级子代理验证器，依据策略推理并给出可操作反馈，大幅提升代理策略遵循度。
practical_value: '- 在电商客服/订单处理Agent中，可用子代理做策略合规检查，而非只做参数级拦截，能捕捉多轮确认、上下文依赖等复杂策略违规。

  - 子代理可共享完整对话历史，基于系统策略提示进行推理，生成自然语言反馈指导主代理下一步，而非简单拒绝，提升修复效率。

  - 与现有ReAct框架解耦，作为外挂验证层，可集成至不同基座模型与工具调用流水线中，复用性强。

  - 在策略频繁更新的场景（如促销规则、退款政策），可快速验证新提示是否符合策略，降低人工审核成本。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM代理在面向客户的自动化流程中必须严格遵守公司策略，但此前的方法仅将策略遵循视为外部参数检查，忽略了多轮对话中必须的用户确认、前置读取和对话内容依赖。实测显示，即使前沿ReAct代理在τ²-BENCH航空任务上仍有较大PASS@4缺口（GPT 5.4约46%，Claude 4.6约72%），亟需更强的策略执行保障。

**方法**：提出PolicyGuard，一种**对话驱动的子代理验证器**。它与主代理共享完整对话视图，直接依据系统策略提示进行推理，不仅输出合规判断，还给出指导下一轮动作的自然语言反馈。与仅检查单次函数调用参数的守卫不同，PolicyGuard理解整个对话上下文，能够捕捉需要确认、拒绝或前置操作的策略违规，并提供具体修正建议。

**关键结果**：在τ²-BENCH航空基准上，为GPT 5.4、Claude Sonnet 4.6、Gemini 2.5 Pro三种基座代理配备PolicyGuard后，PASS@4分别提升+12.0、+6.0、+12.0个百分点；同时，策略违规召回率更高，阻截频率却只有参数级守卫的一半左右，表明其精确阻断能力显著优于现有方法。
