---
title: 'Memory as Plans: World-Action Modeling with Memory-Grounded Planning'
title_zh: 记忆即计划：基于记忆接地规划的世界-动作建模
authors:
- Sizhe Zhao
- Haozhe Xie
- Weiyu Zhao
- Chenchu Zhang
- Huan Wang
- Chenyang Wang
- Qinglin Liu
- Shengping Zhang
arxiv_id: '2609.11561'
url: https://arxiv.org/abs/2609.11561
pdf_url: https://arxiv.org/pdf/2609.11561
published: '2026-09-09'
collected: '2026-09-12'
category: Agent
direction: Agent 长程记忆与计划执行解耦
tags:
- Memory
- Planning
- World Model
- Visual-Language-Action
- Long-Horizon
- KV Cache
one_liner: MaP-WAM 将长期记忆转化为稀疏视觉上下文与语言计划，由固定上下文执行器遵循，取得 RMBench 83.3% 成功率
practical_value: '- 在需要长用户历史的推荐/Agent 场景，可借鉴“记忆即计划”：把长时间跨度的行为序列压缩为若干关键帧（或代表性 item
  特征）+ 高层意图，供 planner 生成下一步计划，而非让 executor 每次都读全量历史。

  - 计划与执行分离：规划器可以处理长历史并生成轻量计划，执行器只接收固定长度上下文和当前计划，结合 progress 预估实现自适应切换，在线推理延迟与历史长度解耦；结构化注意力支持
  KV cache 可进一步降低重复规划成本。

  - 对电商视觉/短视频推荐，如果任务依赖细粒度视觉证据，语言摘要会丢失信息，可保留用户最近强交互的视觉特征帧作为稀疏长期记忆，而不是仅存文本标签。

  - 但这是机器人操作领域，所提 WAP 和进度对齐机制较复杂；直接迁移到推荐/广告需要简化：progress 可类比用户状态/会话阶段，可改造为 session
  切分与 memory refresh 信号。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**  
主流机器人策略常采用 Markov 假设，但复杂操作任务本质上是非 Markov 的，需要超越当前观测的长期记忆。现有语言摘要记忆会丢失细粒度视觉证据，而增长窗口记忆则在历史覆盖范围与执行效率之间权衡。  
**方法关键点**  
MaP-WAM 将记忆依赖的世界-动作建模分解为「记忆接地规划」与「计划条件执行」两部分。长期多模态情节上下文只用于规划阶段，执行器不再反复读取完整历史。记忆被表示为已完成 segment 的记录，包含语言指令和稀疏视觉上下文；规划器将其转换为紧凑计划：下一 segment 的语言计划与对应视觉引导。World-Action-Progress (WAP) 模型执行每个计划时，同时预测动作 chunk 与执行进度，并通过计划-观测对齐校准进度，实现自适应 segment 转移和闭环上下文更新。执行器上下文长度固定，结构化注意力支持 planning 和 execution 两阶段的 KV cache。  
**关键结果**  
在 RMBench 上达到 83.3% 成功率，真实机器人任务成功率 78.0%；随历史增长，执行器推理延迟保持近似恒定。
