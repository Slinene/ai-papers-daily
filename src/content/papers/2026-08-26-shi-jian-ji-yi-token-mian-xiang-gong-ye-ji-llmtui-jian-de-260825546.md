---
title: 'An Event is Worth One Token: Event Tokenization for Industrial-scale LLM Recommendation'
title_zh: 事件即一Token：面向工业级LLM推荐的事件Token化
authors:
- Fan Xia
- Zhaoheng Zheng
- Iman Setayesh
- Ruogu Lin
- Yiqin Pan
- Samarth Mittal
- Wentao Bao
- Vinti Pandey
- Sachin Patil
- Jianpeng Cheng
affiliations:
- AI at Meta
arxiv_id: '2608.25546'
url: https://arxiv.org/abs/2608.25546
pdf_url: https://arxiv.org/pdf/2608.25546
published: '2026-08-26'
collected: '2026-08-27'
category: RecSys
direction: 事件Token化提升LLM推荐快照分辨率
tags:
- Event Tokenization
- LLM Recommendation
- Asynchronous Caching
- Representation Drift
- Snapshot Resolution
- Industrial-scale
one_liner: 将每个用户交互事件压缩为单个Event Token并异步缓存，在不增加在线特征物化成本的前提下提升LLM推荐的快照分辨率
practical_value: '- **异步Event Token缓存**：将用户历史事件（曝光/点击/转化等）在离线阶段用轻量Encoder压缩成固定维度向量，在线推理时只读取缓存Token，避免实时拉取和解析上百个稀疏/稠密特征，大幅降低特征服务与GPU计算压力。

  - **统一Tokenizer + 特征Mask**：一个共享Encoder通过二进制mask区分不同角色（用户/物品/上下文/标签），同时服务排序和检索任务，实现跨实体正迁移，减少多套编码器的维护成本。

  - **表示漂移缓解**：高频重训会导致缓存Token与旧版本不兼容，采用DANN+EMA对齐新旧Encoder输出空间，保持缓存可复用，避免每次更新后全量刷新用户序列。

  - **存储压缩技巧**：Matryoshka Dropout支持训练一次后灵活截断维度，量化感知训练实现INT4下8倍存储压缩，适合海量用户历史Token的存储需求。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：LLM用于推荐时，序列每个位置通常只编码文本或语义ID，丢弃了事件级丰富信号（用户、物品、上下文、结果）。在自回归建模下，单点信息弱会逐层放大，导致整体性能受限。传统方法为控制在线特征物化成本，被迫牺牲历史快照分辨率。

**方法关键点**：
- 提出Event Tokenizer，将每个交互事件的完整特征集（数百个稀疏/稠密特征）压缩成一个d_z维Event Token。Tokenizer由特征编码、双向Transformer交互、MLP投影组成。
- 训练分三阶段：预对齐（冻结LLM只训Tokenizer）、联合训练（解冻LLM端到端）、循环重训（跟踪分布漂移）。
- 排序任务用两个Token（context/label）做自回归BCE，检索任务用单Token做InfoNCE。统一Tokenizer通过特征mask同时服务多角色。
- 在线架构为异步：事件发生时离线计算Token并缓存到用户特征库，推理时下游模型直接消费缓存序列，解耦快照分辨率与在线计算。
- 针对循环重训导致表示漂移，使用DANN+EMA约束新旧Encoder输出一致。
- 存储优化：Matryoshka Dropout + 量化感知训练，INT4下减少8倍存储。

**关键实验**：在Meta工业级推荐平台（PB级日志）上验证。排序上，AMBER相对Incumbent (fair) NE降低0.40%，相对Semantic IDs+CU emb降低1.60%；与现有非LLM ranker集成后Ensemble NE降低0.10%~0.16%。检索上Soft Recall提升0.31%~0.51%，且在第8天仍保持正收益。跨架构迁移中，将Event Token作为历史特征接入非LLM ranker，NE降低0.06%（统计显著）。缩放分析表明，纳入服务FLOPs后，Event Tokenizer缩放比User LLM更高效。

**最值得记住的一句话**：把每个事件压缩成一个Token并异步缓存，是工业级LLM推荐在计算与信息密度之间最实用的平衡点。
