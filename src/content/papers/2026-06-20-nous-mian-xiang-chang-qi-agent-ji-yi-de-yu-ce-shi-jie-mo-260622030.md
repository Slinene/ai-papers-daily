---
title: 'Nous: A Predictive World Model for Long-Term Agent Memory'
title_zh: 'Nous: 面向长期 Agent 记忆的预测世界模型'
authors:
- Pranav Singh
affiliations:
- Indian Institute of Technology Ropar
arxiv_id: '2606.22030'
url: https://arxiv.org/abs/2606.22030
pdf_url: https://arxiv.org/pdf/2606.22030
published: '2026-06-20'
collected: '2026-06-23'
category: Agent
direction: Agent长期记忆 · 预测世界模型
tags:
- Agent Memory
- Predictive World Model
- Bayesian Updating
- Long-term Memory
- LLM Agents
- Information Theory
one_liner: 基于信息论惊喜度和贝叶斯更新，用概率分布代替事实存储，实现Agent记忆的自然遗忘与身份解析。
practical_value: '- **用概率分布跟踪用户/商品属性变化**：在电商推荐Agent中，每个用户偏好或商品属性可维护一个分类分布，新交互通过贝叶斯更新增量调整belief，避免定期全量重建用户画像。

  - **惊喜度指标驱动重要记忆保留**：仅当观察的信息量$S=-\log_2 P$超过阈值时才记录“delta”，可自动过滤噪声信号，降低记忆存储开销，适配高频交互场景。

  - **自然遗忘机制处理数据时效性**：分布未获新证据时熵增向均匀分布收敛，自动淘汰过时信息，无需人为设计衰减规则，利于动态环境下的推荐策略调整。

  - **轻量级实现，无外部向量库依赖**：整套记忆逻辑基于闭式概率更新，不引入向量数据库或图谱引擎，易于集成到已有Agent管线，降低系统复杂度。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：现有LLM Agent记忆系统多将对话历史存为事实、向量或图谱，难以灵活更新和自然遗忘。受“知识即预测”启发，提出一种基于预测世界模型的记忆架构，用概率分布替代确定性存储。

**方法**：Nous为每个实体-属性对维护一个分类概率分布（称为维度）。新观察首先计算惊喜度$S=-\log_2 P(\text{obs}|D)$，然后通过闭式贝叶斯后验更新分布，存储先验到后验的偏移（delta）而非原始事实。遗忘通过分布向均匀分布收敛的熵增自然实现，身份解析利用实体维度集之间的互信息。整个系统无需外部向量库或图引擎。

**结果**：在LoCoMo长期对话记忆基准的10段对话、1540个问题上，以GPT-4o-mini为骨干，单跳F1=63.50，多跳=55.32，时序=58.57，开放域=62.50。相比A-MEM和BeliefMem自报结果有三项/四项提升，但存在对比不严格的可重复性讨论。
