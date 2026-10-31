---
title: 'Prefix Executability: Evaluating Tool-Using Agents Beyond Final Success'
title_zh: 前缀可执行性：评估工具使用代理超越最终成功率
authors:
- Amir H. Rezaeian
- Weiyi Sun
- Yassine Benajiba
- Dan Roth
affiliations:
- Oracle AI
arxiv_id: '2610.40444'
url: https://arxiv.org/abs/2610.40444
pdf_url: https://arxiv.org/pdf/2610.40444
published: '2026-10-29'
collected: '2026-10-31'
category: Eval
direction: Agent 工具调用轨迹评估
tags:
- tool-use agents
- trajectory evaluation
- prefix executability
- multi-turn
- reliability
one_liner: 提出前缀可执行性评估协议，量化工具调用轨迹每一步的可执行性，揭示仅看最终成功的盲区
practical_value: '- 在电商客服、导购等工具型 Agent 评估中，不要只统计最终任务成功率；引入 Prefix Executability 指标（TER、FED、AUC-PEC）量化多步工具调用的轨迹可靠性，提前发现“最终成功但中间调用非法”的隐患。

  - 可将显式 pre-execution plan checking 作为工作流校验层：在 Agent 执行 tool call 前检查工具 schema、状态前置条件和数据依赖，能提升可执行前缀生存率且不损失最终成功率，适合嵌入生产级
  agent 编排。

  - 用 First-Error Depth 定位首次失败步骤，结合 Recovery Rate 评估 Agent 从早期错误恢复的能力，用于线上故障归因和版本对比。

  - 对订单处理、库存查询、营销活动配置等多轮工具调用场景有直接迁移价值，可在 A/B 测试中作为可靠性辅助指标。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有工具型 Agent 基准只看最终任务成功率，难以暴露中间工具调用是否真正可执行。在电商订单、客服等多步工具调用场景，早期无效调用会产生隐藏的恢复行为或状态污染，导致“最终成功但轨迹不可靠”的假象。

**方法关键点**：提出前缀可执行性（Prefix Executability）评估协议。对预测的工具调用序列，逐前缀检查其是否在工具 schema、状态前置条件和数据依赖下可执行。引入系列指标：Prefix Executability Curves（PEC）、First-Error Depth（FED）、Trajectory Executability Rate（TER）、horizon-normalized AUC-PEC 和 Recovery Rate（RR）。在 BFCL-v3 多轮、ToolSandbox 和 τ³-bench 的 Airline/Retail 完整数据上实例化。

**关键结果**：仅看最终成功与看前缀可执行性会导致排名分歧。执行受未验证计划约束的 Agent 往往点估计最终成功率更高，但 TER 和 AUC-PEC 显著更低，说明其成功依赖不可执行轨迹或事后恢复。显式的执行前计划检查能提升可执行前缀生存率，同时保持有竞争力的最终成功率。最终成功率不足以评估工具使用 Agent，前缀级可执行性提供可操作的可靠性信号。
