---
title: Evidence-Guided Recovery for AI Agents with Ambiguous Tool Outcomes and Partial
  Execution
title_zh: 面向工具结果模糊与部分执行的 AI Agent 证据引导恢复
authors:
- Genliang Zhu
- Xiaobo Chen
- Ziyuan Wang
- Chu Wang
affiliations:
- Accentrust, Canada
- Georgia Institute of Technology, USA
- University of Massachusetts Amherst, USA
- Duke University, USA
- University of Illinois Urbana-Champaign, USA
arxiv_id: '2610.41453'
url: https://arxiv.org/abs/2610.41453
pdf_url: https://arxiv.org/pdf/2610.41453
published: '2026-10-29'
collected: '2026-11-13'
category: Agent
direction: Agent 工具失败恢复与规划
tags:
- AI agents
- tool use
- failure recovery
- planning under partial observation
- idempotency
- compensation
one_liner: 针对工具超时导致结果模糊与部分执行，提出基于公开证据、义务与提供商能力的恢复机制，并给出可判定完成证书
practical_value: '- 将工具调用结果显式建模为 failed / committed / in flight 三种状态，基于公开证据做可容许性检查，可避免订单、支付、库存等跨服务调用中的重复执行或漏执行；在电商工作流中可先落地为轻量状态机。

  - 设计终端证书区分“目标实际满足”与“公开证据支持的安全完成”，为交易关键链路提供可审计的兜底判定，避免把不确定结果当成成功。

  - 采用 observation-contingent planning 与 effect-history adjudicator 分离实现：模型只负责规划下一步动作，独立裁决器校验历史效果与依赖关系；这种架构可嵌入现有
  Agent 框架，减少模型幻觉带来的错误补偿。

  - 将保证绑定到声明过的提供商能力，而不是依赖第三方 exactly-once 执行；在对接外部物流、营销、支付服务时，先明确服务商的幂等性和补偿接口，再设计恢复策略，能显著减少盲目重试造成的资损。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：工具超时使 Agent 面临动作结果模糊与部分执行：某个动作可能已经失败、已提交或仍在途，而其他步骤已完成。盲目重试或跳过都会破坏工作流一致性，尤其涉及发票、业务记录、通知等跨服务操作时。

**方法关键点**：
- 将恢复问题形式化为在已批准义务、提供商能力和与公开证据兼容的状态集合上进行证据引导的任务恢复。
- 提出共享可容许性检查，统一处理密钥过期、授权时序、依赖关系和残留效应；通过终端证书区分实际目标满足与公开证据支持的安全完成，避免把不确定结果误判为成功。
- 已知模型实现结合标准观察条件规划与单独实现的效果历史裁决器，模型只提出候选动作，裁决器基于历史效果和证据过滤不可行方案。

**关键结果**：在 37 个任务的小样本研究中，规划与三个主动对照均认证 28 个完成；节省 4 个合成费用单位但额外计算开销。预注册的留出任务对比中，规划建议对证据提示，在 19 个已有任务族、58 个配对单元上，认证完成 30 vs 9，差异 36.2 个百分点（精确族符号翻转 p=0.0078），提案数 272 vs 399。全部 116 条轨迹通过独立回放。两个本地模型均显示正向完成差异。
