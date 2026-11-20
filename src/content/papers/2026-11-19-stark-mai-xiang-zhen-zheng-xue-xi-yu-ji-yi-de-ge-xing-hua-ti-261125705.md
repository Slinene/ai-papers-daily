---
title: 'STARK: Moving towards Personalized Agents That Truly Learn and Remember'
title_zh: STARK：迈向真正学习与记忆的个性化智能体
authors:
- Aryan Jain
- Abhishek Jha
- Anish Nediyanchath
- Promod Yenigalla
affiliations:
- RBS Tech Sciences, Amazon
arxiv_id: '2611.25705'
url: https://arxiv.org/abs/2611.25705
pdf_url: https://arxiv.org/pdf/2611.25705
published: '2026-11-19'
collected: '2026-11-20'
category: Agent
direction: Agent 长期记忆与跨用户迁移
tags:
- Agent Memory
- Knowledge Graph
- Cross-user Transfer
- TransR
- Evidence Scoring
- Personalization
one_liner: 双图记忆架构将事件与行为洞察分离，以事件为边桥接证据，支持跨用户冷启动迁移
practical_value: '- **双图分离与事件作为边**：把 Episodic Graph（事实事件）和 Insight Graph（偏好/约束/目标等行为信号）拆开，用事件
  ID 作为 Insight Graph 的边标签连接信号与来源事件。电商导购/客服 Agent 可借鉴：用户行为信号（如价格敏感、品类偏好）单独建图，保留证据链，避免每次从原始会话重新推导。

  - **证据向量排序**：每个信号节点带 `s(v), n(v), w(v), c(v)`，检索时用 `rank = s*c*(0.5+w)`，失败信号保留半权重而不是丢弃。推荐系统用户画像构建可直接复用：偏好标签携带支持次数、结果权重和置信度，避免弱信号被误用。

  - **跨用户冷启动迁移**：共享行为信号节点不前缀，用户实体前缀隔离，用 TransR 关系嵌入 + 用户偏好指纹余弦相似度找相似用户；完全冷启动时用 link
  prediction 推断缺失信号。电商推荐冷启动可参考：建立跨用户共享的领域知识图谱，只共享信号节点不共享原始交互，既满足隐私又能迁移。

  - **工程实现要点**：写入路径重（两次 LLM 提取），读取路径轻（固定 token 预算约 3.8K，延迟 710–770ms，增量嵌入 O(1) 更新）。治理上用
  DELETE_NODE/UNLINK 支持遗忘，跨用户只共享信号节点和 embedding。适合生产落地的成本与合规设计。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
长期记忆对个性化 Agent 系统至关重要，但现有记忆系统多为单一扁平图，把事件、偏好、约束、目标混为无差别节点。这导致行为信号分散在事件节点中，查询时 LLM 必须重新推导，既冗余又不一致；同时每个用户的图自包含，无法跨用户迁移。在供应商谈判、论文写作等 domain-specific 场景，用户目标分布相似，跨用户知识迁移是自然需求。

## 方法关键点
- **双图架构**：Episodic Graph 记录时间、因果、语义链接的交互事件；Insight Graph 存储从事件中提取的行为信号（偏好、约束、目标、价值观），信号节点带证据向量 `ev(v)=(s,n,w,c)`，其中 n 为支持事件数，w 为结果权重，s 为强度，c 为置信度。
- **事件作为边桥接**：Insight Graph 用事件 ID 作为边标签，连接信号与其来源事件，实现双向溯源，不合并两张图。
- **检索**：按 `rank(v)=s*c*(0.5+w)` 排序，失败信号保留半权重；根据查询意图分配上下文预算。
- **跨用户迁移**：选择性前缀化（用户实体前缀，行为信号实体不前缀），构建 TransR 关系嵌入空间；用户用偏好指纹 `fp(u)` 聚合共享信号边，余弦相似度找 top-m 相似用户；完全冷启动时用 link prediction 推断缺失信号。

## 关键结果
- LoCoMo 多跳 3.56 vs MAGMA 2.64，开放域 4.08 vs Zep 3.15；LongMemEval 信息抽取 4.38，比 MAGMA 高 1.48。
- RealPref 开放题 4.19，比 LLM-only 高 2.04；PAL-Bench 双图结构单独带来小幅提升。
- LongLaMP 5% 图稀疏度下，TransR combined 2.0/5 和 ROUGE-L 15，比无迁移 1.3/12 提升约 1.5 倍。
- 生产 8 周 A/B（40 名经理，200 vendor triples）：memory-on 减少谈判轮数 18%、周期时间 15%，跨用户迁移贡献约 40% 收益，新员工收益最大。

## 最值得记住的一句话
行为信号与事件必须分离，并用事件作为边支撑证据，这是解决个性化 Agent 长期记忆一致性与冷启动的关键。
