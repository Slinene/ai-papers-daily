---
title: 'Fortunate Recall: Ontology-Driven Memory Lifecycle Management for Persistent
  Coherence in LLMs'
title_zh: 幸运回忆：本体驱动的记忆生命周期管理实现 LLM 持久一致性
authors:
- Ansuman Mullick
- Eray Tüzün
affiliations:
- Bilkent University
arxiv_id: '2609.10413'
url: https://arxiv.org/abs/2609.10413
pdf_url: https://arxiv.org/pdf/2609.10413
published: '2026-09-09'
collected: '2026-09-10'
category: Agent
direction: Agent 记忆生命周期管理
tags:
- memory lifecycle
- ontology
- temporal decay
- supersession
- confabulation
- LLM agents
one_liner: 提出 10+1 行为本体的确定性记忆生命周期策略层，将下游混淆率减半并提升时序消歧基准 16 个百分点
practical_value: '- 在电商客服/导购 Agent 中，对用户事实按行为域分桶并施加差异化衰减：地址/支付方式等 Identity 类慢衰减；临时优惠券、物流时间用事件时间核，过期自动失效；商品偏好用
  slot-key 覆盖最新值，避免旧偏好污染上下文。

  - 采用 slot-key supersession 处理同一 (user, attribute) 的更新：高置信覆盖，低置信保留多版本，适配“看中商品 A →
  加购商品 B”等多版本事实，降低旧状态导致的 bad case。

  - 检索时做 category-aware routing / forced retrieval：先判断 query 意图属于哪个行为域，强制召回该域边，缓解抽象
  query 与具体事实的 embedding 词汇 gap，适合订单状态、优惠券、偏好等结构化查询。

  - 将 LLM 限制在 ingestion 抽取与候选压缩，生命周期策略全用确定性规则（衰减、过期、覆盖）实现，延迟低且可审计；评估时用 safe response
  rate 而非单纯 retrieval hit，避免“召回干净但信息量低”的指标陷阱。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

## 动机
现有 LLM 记忆系统把所有个人事实等同对待，统一保留、统一衰减，导致存储无界增长、检索精度退化。核心问题不是检索，而是生命周期管理：哪些记忆该保留、哪些该替换、以什么速率衰减。已有系统（Mem0、A-MEM、MemoryOS 等）在基础设施上很强，但都缺少对“当前偏好 vs 被取代偏好”“已过期物流信息 vs 即将到期的预约”的结构化区分。

## 方法关键点
Fortunate Recall (FR) 提出一个可组合的生命周期策略层，将提取到的每个事实分类到 10+1 行为本体（Identity、Relational、Interests、Health、Projects、Hobbies、Preferences、Financial、Obligations、Logistical、Other），按行为域而非认知类型（episodic/semantic/procedural）决定动态。每类有差异化半衰期（Identity 19 天到 Logistical 4 天）、slot-key supersession、事件时间有效性和检索路由策略。关键机制：
- **slot-key supersession**：对归一化 (subject, attribute) 槽位更新，高置信覆盖旧值，低置信保留多版本。
- **event-time validity**：Obligations/Logistics 按事件距离激活，截止日临近时提升激活，过期后失效。
- **category-aware routing**：query 分类后强制召回对应类别边，绕过抽象 query 与具体事实的语义 gap。
- **LLM boundary**：LLM 仅用于 ingestion 抽取和 retrieval 时单个轻量 top-20 筛选；生命周期层是纯确定性数学，中位延迟 47μs，线性 O(k)。
理论证明 metadata basis (c, κ, ξ, h) 是生命周期感知排序的充分且最小必要信息，全局标量权重不可行，分类别参数化才能恢复校准。

## 关键结果
构建 LifecycleBench：40 个 persona、516 个时序消歧问题、9 类攻击向量。FR-Bank 达到 76.9% pass，超过 Mem0（61%）、A-MEM（65.3%）、Memory-R1（66.9%）、MemoryOS（70.5%）。LongMemEval-S 上 75.2%。端到端混淆率从 Mem0 的 45.1% 降至 22.4%（answered queries），all-query 从 32.2% 降至 13.0%，同时正确率更高。外部 BEAM 转移 46.8% vs Mem0 32.9%。预注册消融显示：通用 lifecycle 元数据承载正确性（无类型基线差异不显著），行为本体承载校准，将混淆率从 24.2% 降至 12.0%。粒度扫描表明约 7 个策略簇后收益饱和，10+1 是解释性选择。

**最值得记住的一句话**：把“事实的行为类型”而非“认知类型”作为记忆生命周期策略的入口；通用生命周期元数据决定找得对不对，行为本体决定记得干不干净。
