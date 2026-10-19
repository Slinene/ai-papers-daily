---
title: RL-Guided Temporal Localization for Dual-Channel Retrieval in Long-Horizon
  Agent Memory
title_zh: RL引导的时间定位用于长程Agent记忆双通道检索
authors:
- Dabin Sheng
- Zhe Wu
- Jinming Zhao
- Junliang Xing
- Yuanchun Shi
affiliations:
- Tsinghua University
- Qiyuan Lab
arxiv_id: '2610.23598'
url: https://arxiv.org/abs/2610.23598
pdf_url: https://arxiv.org/pdf/2610.23598
published: '2026-10-16'
collected: '2026-10-19'
category: Agent
direction: Agent长期记忆时间感知检索
tags:
- Temporal Retrieval
- RL
- Long-term Memory
- LLM Agents
- Dual-Channel Retrieval
- Time-aware RAG
one_liner: 用RL训练时间区间定位器，在检索阶段引入时间约束，缓解语义相似但时间不匹配记忆淹没目标证据
practical_value: '- 在用户长历史记忆/RAG检索里，若用户行为或事件语义重复度高，不要只靠语义相似度，可加一个独立的"时间窗口预测"通道：先由轻量模型预测答案证据可能出现的时间区间，再作为过滤或重排条件。

  - 检索决策本身是离散、不可微的，但可以用RL+复合奖励来优化：把仅有答案级别的稀疏监督，拆成对检索结果的时间命中、顺序等细粒度反馈，适合训练一个1.7B小模型而不是大模型。

  - "语义召回 + 时间召回双通道合并，再按时间窗口邻近度重排"是一个低成本插件式方案，可直接用于Agent长期记忆、用户会话历史、订单/行为日志等RAG场景。

  - 电商场景可迁移：例如用户问"我上次双11买的鞋是什么品牌"，语义召回可能返回多个相似商品，用预测时间窗口截断或重排，能显著减少错误证据。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：长程LLM Agent需要从不断增长的长期记忆中检索证据，但现有方法主要靠词法或语义相似度，导致目标记忆被大量语义相似但时间不匹配的候选淹没。部分时间感知方法只在记忆组织或答案生成阶段注入时间线索，没有在候选选择阶段施加时间约束，未能解决根因。

**方法关键点**：提出TIDER框架，核心是一个RL训练的时间区间定位器，推断证据可能所在的时间窗口。由于窗口定位是离散、不可微的检索决策，使用强化学习优化，并用复合奖励把稀疏答案监督转化为细粒度检索反馈。预测窗口先构成时间检索通道，再与语义通道结果合并，按与窗口的邻近度重排。这样时间对齐的证据不会被海量语义相似但时间错误的记忆淹没。

**关键结果**：用仅1.7B的轻量定位器，在LifeBench上达到61.52%（+8.82%），在LoCoMo上达到78.96%（+3.66%），均为长程记忆基准上的SOTA，说明在日常生活长期记忆中，时间线索对定位目标证据至关重要。
