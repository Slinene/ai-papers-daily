---
title: Agentic Permissions Policy Algebra for Taint Confinement in LLM Agents
title_zh: LLM Agent 污点约束的代理权限策略代数
authors:
- Arseny Kravchenko
- Vadim Liventsev
- Innokentii Konstantinov
- Ildar Iskhakov
- Matvey Kukuy
affiliations:
- Archestra AI
arxiv_id: '2607.24625'
url: https://arxiv.org/abs/2607.24625
pdf_url: https://arxiv.org/pdf/2607.24625
published: '2026-07-27'
collected: '2026-07-28'
category: Agent
direction: Agent 安全 · 信息流控制
tags:
- LLM agents
- prompt injection
- information flow control
- taint tracking
- context branching
- declassification
one_liner: 通过上下文分支与前瞻权限检查，将 LLM Agent 的数据泄露攻击成功率从 31-50% 压至 0-7%
practical_value: '- **上下文分支隔离**：在处理不可信数据（如用户评论、外部 API 返回）时，可借鉴子轨迹设计，将高风险操作隔离在临时上下文中，仅将净化后的有界结果传回主流程，避免污染推荐系统的核心状态。

  - **前瞻性权限检查**：在 Agent 调用工具或访问数据源前，可插入类似“标签预评估”的步骤，提前生成授权/接受方案，防止越权调用，尤其适用于涉及用户隐私数据（订单、浏览记录）的电商对话
  Agent。

  - **细粒度污点净化**：允许受信任的净化器对敏感信息进行脱敏或聚合后再返回主上下文，既保留数据效用又不泄露原始隐私，适合推荐系统中混用 PII 与公共特征的安全场景。

  - **形式化的合并约束**：双幺半群模型为多轮对话、多工具调用提供了可验证的标签保持证明，可作为构建高安全 Agent 框架（如购物助手、搜索代理）的理论基础。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：自主 LLM Agent 处理混合机密数据时，提示注入攻击与推理错误可导致严重数据泄露。传统动态信息流控制通过污点追踪提供安全保证，但一旦读取未审查数据便永久污染上下文，严重损害下游可用性。

**方法关键点**：
- 提出 APPA 框架，引入引擎管理的**上下文分支**与**前瞻性获取执行**。
- **前瞻评估**：在数据实际获取前，评估标签降级与缺失前置条件，生成可操作的补救计划（Authorize / Accept）。
- **安全审查**：为检查不可信数据，生成带标签的子轨迹，在本地吸收标签降级，并由受信任净化器返回有界衍生品给未改变的父上下文，保持父标签不变。
- **形式基础**：基于安全标签与共享事件日志的双幺半群模型，形式证明父标签保持与合并约束性。

**关键结果**：
- 在四模型多轮工具链基准上，APPA 将数据泄露攻击成功率从 31%–50% 降至 0%–7%。
- 在四个模型中的三个上，分支机制恢复了因纯污点追踪而丧失的绝大部分效用。
