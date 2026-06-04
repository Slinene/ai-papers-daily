---
title: 'Strabo: Declarative Specification and Implementation of Agentic Interaction
  Protocols'
title_zh: Strabo：声明式多智体交互协议的声明与实现
authors:
- Samuel H. Christie
- Amit K. Chopra
- Munindar P. Singh
affiliations:
- North Carolina State University
- Lancaster University
arxiv_id: '2606.05043'
url: https://arxiv.org/abs/2606.05043
pdf_url: https://arxiv.org/pdf/2606.05043
published: '2026-06-03'
collected: '2026-06-04'
category: MultiAgent
direction: 声明式交互协议与工业标准桥接
tags:
- MultiAgent
- Protocol
- Langshaw
- UCP
- Interoperability
- Declarative
one_liner: 用声明式协议 Langshaw 精确建模工业电商交互标准 UCP，并通过桥接层实现与现有系统互操作。
practical_value: '- **声明式协议减少隐式假设**：像 Langshaw 那样显式定义角色、数据所有权（sayso）、动作因果依赖和排斥约束，可让电商多智能体交互（如结算、退货）更清晰，避免因文档不明确导致的实现错误。

  - **桥接模式实现渐进迁移**：ProxyAdapter + route() DSL 将声明式动作映射为 HTTP 调用，无需彻底推翻现有 REST API，就能逐步引入协议规范，适合已有推荐系统或电商中台的多
  Agent 化改造。

  - **Enablement-based 编程降低合规成本**：Peach 适配器自动计算当前可行的动作，业务 Agent 只需从可行动作列表中选择并绑定值，把协议合规从应用代码中抽离，可在大规模
  Agent 部署中减少状态管理 bug。

  - **显式版本化控制并发修改**：增量协议中用组合键 (eid, v) 管理多次更新，避免直接覆盖状态，支持应用层灵活决策（如取最新版本），可为推荐流程中的会话状态管理提供参考。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**
工业界正推动 AI Agent 交互协议标准化（如 Google 的 UCP、A2A），但这些规范多为 JSON Schema 和文字描述，存在大量隐式假设（如同步顺序、数据所有权、覆盖语义），容易导致实现歧义和错误。学术界的声明式协议（如 Langshaw）能精确刻画交互约束，但尚未融入工业实践。本文试图展示声明式协议与工业标准的融合路径。

**方法关键点**
- 选取 UCP 的 Checkout 能力，用 Langshaw 协议建模为 `SimpleUCP`（原子式）与 `IncrementalUCP`（增量式），显式声明角色、关键属性、因果依赖、数据所有权和排斥规则。
- 使用 Peach 编程模型实现 Agent，适配器自动计算可执行动作，Agent 只需绑定业务数据，协议合规完全由适配器负责。
- 构建 `ProxyAdapter` 桥接层，通过 `route()` DSL 将 Langshaw 动作映射为 RESTful HTTP 调用，处理字段名转换和请求编排（如 Create 需再发 PUT 补充 UCP 不支持的首请求字段）。
- 增量协议通过引入版本键 `v` 将部分更新转化为独立的子 enactment，避免覆盖冲突，支持应用层灵活决定版本合并策略。

**关键结果**
- 与 Google UCP 参考实现端到端互操作成功，平台 Agent 代码量从约 915 行降至 97 行（SimpleUCP），代理端也大幅精简；新增能力只需追加协议文件和路由定义。
- 声明式模型显式化 UCP 的多种隐含假设（如实例 identity 生成方式、可选字段处理、同步顺序），消除模糊性。

**最值得记住的一句话**
声明式协议不是与现实脱钩的学术玩具，通过适配桥接可以无缝融入现有电商 Agent 系统，在保持互操作性的同时大幅提升交互协议的精确性和可维护性。
