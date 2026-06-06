---
title: 'Absorbing Complexity: An Interaction-Native Knowledge Harness for Financial
  LLM Agents'
title_zh: 吸收复杂性：面向金融LLM代理的交互原生知识织带
authors:
- Ailiya Borjigin
- Igor Stadnyk
- Ben Bilski
- Maksym Chikita
- Dmytro Kyrylenko
- Sofiia Pidturkina
- Julia Stadnyk
affiliations:
- True Trading
- Inc4.net
arxiv_id: '2606.01886'
url: https://arxiv.org/abs/2606.01886
pdf_url: https://arxiv.org/pdf/2606.01886
published: '2026-05-31'
collected: '2026-06-06'
category: Agent
direction: Agent 认知架构 · 持续记忆与治理
tags:
- Financial Agents
- Temporal Knowledge Graph
- Memory Management
- Invalidation
- Governance
- Interactive-Native
one_liner: 交互原生知识织带通过被动注入、时序图记忆与写时失效，系统性吸收认知复杂性而非转嫁给用户。
practical_value: '- **被动注入代替主动检索**：在前端推理前，由系统根据事件自动注入领域知识到上下文缓冲，而不是让模型自己发起 wiki-walk
  或 RAG 检索。这可直接用于电商客服或推荐 Agent，在用户问题到达时提前注入其历史偏好、订单状态、风险标签，降低推理延迟和 token 消耗。

  - **时序图 + 写时失效处理旧知识**：市场条件变化后，旧知识不再可信。在推荐系统中，可利用类似机制在用户行为漂移或商品下架时主动失效记忆，避免注入过时偏好；工程上可用带时间戳的图边和矛盾检测实现自动失效。

  - **治理层根据行动风险控制知识准入**：高风险行动（如下单、投资建议）只允许成熟度足够高的知识条目被注入。电商场景中可设计“发货承诺信息”仅当订单状态已确认时生效，防止模型基于未结清状态给出错误承诺。

  - **分离检索底图和审计视图**：使用时序图做低延迟在线检索，同时维护可读的 wiki 页面用于人工审查与合规。推荐 Agent 可效仿：在线用向量图快速召回，离线维护可解释的用户画像页面供运营查验决策依据。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：金融 AI 落地的主要障碍不是模型本身，而是“金融认知摩擦”——用户需要反复重述碎片化信息、历史判断、风险偏好和变化的市场假设，而现有 Agent 多为回合式、用完即弃的问答模式，导致高延迟、重复错误和弱可追溯性。论文主张，系统应吸收复杂性，将交互痕迹持续转化为结构化、可治理的长期知识。

**方法关键点**：
- **交互原生架构**：将每个事件（用户、市场、工具调用）视为流，形成状态 St = (Ut, Mt, Rt, Xt, Gt)。
- **被动知识注入**：系统在每次推理前检测实体、意图和风险等级，从时序图中裁剪 h 跳邻域，排除已失效条目，按效用函数打分，再压缩注入固定 token 预算的上下文缓冲，代替 Agent 驱动的记忆搜索。
- **时序知识图 + 写时失效**：知识对象包含类型、置信度、成熟度、有效期等字段；新证据与旧知识矛盾时触发主动失效，且注入前剔除无效项。
- **治理约束**：知识条目能否影响某项金融行动，取决于其有效置信度、成熟度是否高于该行动风险对应的阈值，以及是否属于用户允许的叠加范围。
- **离线维护与审计**：后台提取工作流、更新图谱、输出可读的 wiki 页面，保证可审查性。

**关键实验**：在受控合成基准（24 种子，4 轮，每轮 80 任务，共 7680 条工作流）上对比 ModelOnly、ToolAgent、SimpleMem、WikiWalk、Khnoinv 和完整 InKH。InKH 以 900 ms 平均延迟取得 0.815 任务质量，相较 WikiWalk 延迟降低 82.95%，token 成本降 82.29%，过期知识使用减少 96.58%，决策可追溯性提升 0.461。在第三轮引入市场冲击后，仅 InKH 保持质量持续上升，其他记忆基线持平或回退。治理消融显示，InKH 与无失效版本存储等量知识，但通过失效过期条目带来增量收益。

**核心记忆**：更好的金融认知不是来自记住更多，而是来自在治理下记住应该记住的。
