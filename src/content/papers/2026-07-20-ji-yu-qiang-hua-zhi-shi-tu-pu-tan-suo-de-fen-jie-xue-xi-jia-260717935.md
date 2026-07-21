---
title: 'DeLIVeR: Decomposed Learning for Information-grounded Veracity Recognition
  via Reinforced Knowledge Graph Exploration'
title_zh: 基于强化知识图谱探索的分解学习框架用于事实核查
authors:
- Cong Hoan Nguyen
- Thomas Hoang
- Hieu Minh Duong
- Long Nguyen
affiliations:
- University of Louisville
- Denison University
arxiv_id: '2607.17935'
url: https://arxiv.org/abs/2607.17935
pdf_url: https://arxiv.org/pdf/2607.17935
published: '2026-07-20'
collected: '2026-07-21'
category: RAG
direction: 推理增强 · 强化知识图谱检索
tags:
- Fact-checking
- Knowledge Graph
- Reinforcement Learning
- GRPO
- Question Decomposition
- RAG
one_liner: 将声明分解为多个查询，用强化学习优化知识图谱探索策略，事实核查 F1 提升 10–15%
practical_value: '- **复杂查询的分解与推理**：电商搜索中用户长尾/多条件意图，可借鉴 Planner LLM 将 query 分解为子问题，再到结构化
  KG（商品属性、品牌关系）中检索证据，提升复杂 query 的召回精度和可解释性。

  - **用 GRPO 优化检索策略**：若需训练 query 改写或检索路径选择模型，可采用 Group Relative Policy Optimization，以最终结果准确性+检索多样性为奖励，避免传统监督信号昂贵的问题，适合在线上持续优化搜索或推荐
  agent。

  - **知识图谱替代纯文本检索**：在 RAG 管线中，用 KG 存储商品/用户结构化信息，由分解后的子查询定向抽取子图，可有效减少 LLM 幻觉，适合需要事实级准确性的场景（如营养成分、尺码对比推荐）。

  - **多样性与可审计的设计**：奖励中加入结构多样性，能防止检索结果单一化，同时 KG 路径可天然提供审计链，这对电商合规和用户信任构建有直接价值。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

## 动机
LLM 事实核查常因传统检索系统的“查询脆弱性”而难以处理多跳推理。简单的一次性检索难以覆盖复杂声明需要的多源证据。

## 方法
- **框架核心**：将证据检索视为强化学习的策略探索任务。
- **查询分解**：使用 Planner LLM 将原始声明分解为一组聚焦的子问题，每个子问题用于定向探索知识图谱（KG）。
- **图谱探索**：子问题作为导航查询，在结构化 KG 上遍历以获取高精度证据。
- **策略优化**：用 Group Relative Policy Optimization (GRPO) 微调 Planner，奖励函数同时考虑证据的**结构多样性**和最终**真伪判别准确率**。
- **训练数据**：通过 LLM 自动生成声明-子问题对，并利用判断正确与否构造奖励信号，降低人工标注依赖。

## 关键结果
在 LIAR、FEVER、PolitiFact 三个基准上，使用 Qwen2.5-7B 作为 Planner，DeLIVeR 分别达到 83.73、84.57 和 79.70 的 F1 分数，比 HippoRAG2 提升 10–15%。消融表明 GRPO 和多样性奖励对性能贡献显著，分解策略有效弥合多跳推理鸿沟。
