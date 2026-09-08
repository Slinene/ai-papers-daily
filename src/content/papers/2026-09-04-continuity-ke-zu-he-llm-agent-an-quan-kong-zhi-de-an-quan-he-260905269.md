---
title: 'CONTINUITY: Security-Context Contracts for Composable LLM Agent Controls'
title_zh: CONTINUITY：可组合 LLM Agent 安全控制的安全上下文合约
authors:
- Chris Zheng
- Geng Yang
affiliations:
- ZAST.AI
arxiv_id: '2609.05269'
url: https://arxiv.org/abs/2609.05269
pdf_url: https://arxiv.org/pdf/2609.05269
published: '2026-09-04'
collected: '2026-09-08'
category: Agent
direction: Agent 安全控制组合验证
tags:
- LLM Agents
- Security
- Assume-Guarantee
- Provenance
- Policy Enforcement
- Verification
one_liner: 用 assume-guarantee 合约与认证安全上下文，保证 LLM Agent 跨组件端到端后果完整性
practical_value: '- 在电商/广告/搜索的 LLM Agent 系统中，跨工具、跨组件调用（商品库、广告投放 API、用户数据）时必须显式传递认证上下文，不能依赖组件内部假设；可借鉴「签名
  root grant + 接收回执」模式防止授权被中途丢弃或重放。

  - 设计多 Agent 协作或工具编排时，采用 assume-guarantee 合约显式声明每个组件的输入前置条件和输出保证，避免单组件安全测试通过但组合后出现上下文断裂；适合安全敏感的推荐策略、召回和排序服务。

  - 引入 transformation witness（字段级来源和变换证明）应对数据血缘要求：例如商品信息经清洗、聚合、过滤后产生推荐结果时，能追溯每个字段的修改链，满足合规审计。

  - 工程实现上，可信核心仅 1.5K LOC，验证延迟在毫秒级（proof 4.21ms，端到端 7.17ms），可嵌入实时推荐链路做安全校验，无需引入重型可信执行环境。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：LLM Agent 系统普遍组合 provenance tracking、task-scoped authorization、policy gateway、protocol adapter 等安全控制。但这些机制单独正确不保证端到端安全：跨组件边界时安全上下文可能被丢弃、自我声明权威、扩大委派、修改字段、执行过期或重放许可。作者称此为 security-context discontinuity。

**方法关键点**：定义 end-to-end consequence integrity (ECI)——每个外部效果必须有可验证 witness，连接 principal、task、field-level provenance、root grant、component contract、当前 policy、finality 与 single-use execution state。采用 assume-guarantee 合约模型，各组件通过 signed root grants、role-bound transition receipts、bounded typed releases、transformation witnesses 和 effect-bound execution permits 携带认证上下文。实现参考验证器和 32 类跨层故障注入测试。

**关键结果**：在 2,560 个攻击实例中，完整配置无有害外部效果；700 个良性任务全部完成，200 个模糊任务全部升级人工处理。最强的不完整参考配置在 65.6% 攻击实例中产生有害效果。消融实验显示每省略一个 invariant 会重新打开 4–24 个故障类。验证延迟中位数 4.21 ms，端到端 transition 生产、验证、permit 签发和 finality 中位数 7.17 ms。结论：安全 agent 执行不仅需要单个控制健全，还需要显式合约在完整 instruction-to-effect 路径上保持保证。
