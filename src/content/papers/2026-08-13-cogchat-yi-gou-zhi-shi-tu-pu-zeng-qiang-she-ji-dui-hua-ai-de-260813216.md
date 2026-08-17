---
title: 'CogChat: Knowledge Graph-Augmented Conversational AI with Heterogeneous Graph
  Transformer for Cognitive Grounding in Design Generation'
title_zh: CogChat：异构知识图谱增强设计对话 AI 的认知接地
authors:
- Jiin Choi
- Kyung Hoon Hyun
affiliations:
- Design AI Lab, Hanyang University
- Human-Centered AI Design Institute, Hanyang University
arxiv_id: '2608.13216'
url: https://arxiv.org/abs/2608.13216
pdf_url: https://arxiv.org/pdf/2608.13216
published: '2026-08-13'
collected: '2026-08-17'
category: RAG
direction: 知识图谱增强对话 · 异构 Graph Transformer
tags:
- Knowledge Graph
- Heterogeneous Graph Transformer
- Conversational AI
- Context Management
- Personalization
- LLM
one_liner: 用个人异构知识图谱 + HGT 选择相关节点注入 LLM，提升设计对话的上下文保留与个性化意图理解
practical_value: '面向电商/广告/搜索推荐场景的可借鉴点：

  - 用户级动态知识图谱做长程上下文：在客服/导购/创意 Agent 中，实时从对话里抽取实体（商品、属性、类目、偏好）与关系，构建个人异构图谱，替代仅依赖 sliding
  window 的上下文；用 HGT 或轻量图注意力做子图选择，避免全量 KG 造成 prompt 噪声和延迟。

  - 同名词/多义词消歧：异构图中实体类型和关系结构可区分同一词在不同上下文（如“苹果”作为品牌或品类），适合电商搜索 query 理解与个性化召回；将图结构注入
  LLM 可提升意图识别准确率。

  - 主动探测问题生成：借鉴 CogChat 同时生成 intentional 和 exploratory probing questions 的机制，在推荐对话中用于偏好澄清、query
  改写建议（如“你指的是 A 还是 B？”），降低用户决策负担并收集偏好信号。

  - 工程实现：可用轻量抽取器构建图，HGT 只负责节点打分与选择，LLM 负责最终生成，保持低延迟；先在特定垂直领域（服装、家居、3C）试点，注意图谱更新频率和图谱规模控制。'
score: 7
source: arxiv-cs.HC
depth: abstract
---

动机：
LLM 对话系统用于设计实践时，仅按 token 序列和最近上下文维护状态，忽略用户如何组织知识，导致跨轮关系衰减、同名词语无法区分、对话浅层重复。

方法关键点：
- 从每个设计师输入中实时抽取 typed entities 和 relations，构建个人异构知识图谱；
- 用 Heterogeneous Graph Transformer (HGT) 在该图上选择与当前轮结构相关的节点子图，注入 response generation，并生成两类探测问题：intentional 和 exploratory；
- 对比 naive KG augmentation（不加选择地使用图谱），HGT 的选择机制能抑制噪声，而 naive KG 注入噪声会降低响应质量。

关键结果：
- 技术评估：HGT 实体选择显著优于 ungrounded LLM 与 naive KG augmentation；
- 9 名专业设计师的 within-subjects 研究：上下文保留、个性化意图解释、对话深度提升，认知负荷下降；
- 结论：将用户表达的概念与关系结构化为动态知识图谱，可以跨轮保留关系上下文，为 LLM 长程上下文管理提供图接入思路。
