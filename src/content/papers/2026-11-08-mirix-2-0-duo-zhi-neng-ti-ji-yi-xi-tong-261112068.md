---
title: 'MIRIX-2.0: Multi-Agent Memory System'
title_zh: MIRIX-2.0：多智能体记忆系统
authors:
- Wei-Chieh Huang
- Weizhi Zhang
- Jiayan Nan
- Peng Xia
- Yu Wang
affiliations:
- MIRIX AI
arxiv_id: '2611.12068'
url: https://arxiv.org/abs/2611.12068
pdf_url: https://arxiv.org/pdf/2611.12068
published: '2026-11-08'
collected: '2026-11-17'
category: Agent
direction: Agent 长期记忆 · 溯源超图索引
tags:
- LLM Agents
- Memory System
- Provenance Hypergraph
- Procedural Memory
- Semantic Consolidation
one_liner: MIRIX-2.0 以带溯源超图索引完整记录，配合显式预算检索与离线身份/技能整合，兼顾准确、效率与可追溯
practical_value: '- 把原始用户/会话记录完整存向量库作为 system of record，图/索引只负责关联和路由；电商用户画像、订单、会话记忆可避免因压缩摘要丢失关键事实，所有推荐证据可回溯。

  - 用 n-ary frames 而非 triple 表示事件（订单、浏览、退货等多方事件），并保留角色、时间、数值 literal；有助于准确回答“用户买了什么花了多少钱”这类需关联多个实体的查询，比普通知识图谱召回更稳。

  - 显式预算检索：将查询分为 single/temporal/intersection/count 等 operator，限制 base recall rows
  和 relation-cited rows 数量，保证延迟不随记忆量增长；可用于推荐系统的知识检索或用户状态查询，控制 LLM 上下文开销。

  - 离线实体合并（AutoDream）只合并 identity-stable 类型的 anchors，不重写原始记录；可用于跨会话用户/商品 identity
  解析，降低碎片化，提升召回，风险可控。

  - 程序记忆：从失败任务 session 中蒸馏“避免”和“复用”经验，生成可更新技能并保留来源引用；电商任务型 agent（如购物助手）可积累操作例程，避免重复错误。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：LLM agent 长期运行需要记忆来个性化、保持一致性、复用经验。现有系统要么训练参数记忆（不实用），要么压缩摘要（丢失细节），要么全量检索（成本随历史增长）；图索引常把 n-ary 事实拆散，或只能先召回主题/摘要再找细节。MIRIX-2.0 目标同时满足准确性、实用性和效率。

**方法关键点**：
- 分层存储：六类 typed memory agents 由 Meta Memory Manager 路由，完整原始记录写入向量库作为 system of record，图只是索引；写库先行，图失败不 rollback。
- Provenance hypergraph：存储 anchors、n-ary frames（角色-锚点对+literals），每个 fact 引用源行；semantic frames 按谓词+参数去重，episodic frames 加 event time/memory id 保持不同事件身份；日期、价格、计数保留为 literals。
- Graph-owned retrieval：planner 将查询映射为 single/temporal/intersection/list-union/count 操作，设置 base recall rows 和 relation-cited rows 预算；从 anchor 进入两个车道（base recall、relation citation），返回 graph facts 与 source rows，证据量不随历史增长。
- AutoDream：离线合并语义 anchors（identity-stable 类型，余弦阈值+LLM verifier），只 union row ids 和 rewires，不改写证据；程序记忆分支由 Distiller 从任务 transcript 提取经验，Curator 生成可编辑技能并保留来源引用。

**关键实验**：
- 对话记忆：LoCoMo 91.4%（HyperMem 91.0%），LongMemEval-S 72.6%（HyperMem 58.3%），领先 14.3 分；图相对 flat 在 LongMemEval-S 加 11.2 分，AutoDream 再加 2.6 分。
- 文档 QA：SHDocQA 83.0%、MHDocQA 71.0%，分别领先 HyperMem 31.0 和 22.0 分；DetectiveQA 64.8%，低于 MemoryBank 67.6%。
- 程序记忆：ALFWorld 76.4%（AWM 73.6%，no memory 69.4%），WebShop 37.4%（AWM 36.0%），MetaClaw-Bench 49.2% vs MetaClaw Skills 44.0%。
- 效率：禁用 AutoDream 时回答速度在五个基准上快于 HyperMem；WebShop 训练/测试 tokens 最少；文档 ingestion 比 flat memory 慢 3.8-4.0x。

**最值得记住**：完整记录永远保留，图仅做带溯源的索引，并用显式预算约束检索，是兼顾准确与效率的关键设计。
