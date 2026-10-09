---
title: 'RIT-RAG: Navigating Document Corpora with Retrieval-Induced Trees'
title_zh: RIT-RAG：检索诱导树在文档语料中导航
authors:
- Meghanadh Pulivarthi
- Swaraj Kumar Biswal
- Kushagra Bhushan
- Yatin Nandwani
- Sachindra Joshi
- Dinesh Raghu
affiliations:
- IBM
- IIT Kharagpur
arxiv_id: '2610.11370'
url: https://arxiv.org/abs/2610.11370
pdf_url: https://arxiv.org/pdf/2610.11370
published: '2026-10-08'
collected: '2026-10-09'
category: RAG
direction: Agentic RAG 树结构导航
tags:
- RAG
- Agentic RAG
- Document Tree
- Structure Navigation
- Long Document QA
- Retrieval
one_liner: 用检索块位置诱导多文档子树，让 LLM Agent 在结构上导航并选择性阅读，提升复杂文档问答准确率
practical_value: '- 借鉴“检索提出位置、Agent 决定阅读”的分离设计：把检索结果映射到商品文档、帮助中心或政策文档的目录树片段，让 Agent
  在局部子树上推理而非直接读 chunk，能更好利用结构信息并控制上下文长度。

  - 离线为每个文档/类目构建树索引（TOC、sitemap、商品属性层级），在线用宽召回 chunk 诱导多个候选子树，避免“先选文档后无法纠错”，适合多来源、超长文档库。

  - 在客服/售后场景中，Agent 选择性读取节点并改写查询，可以降低 LLM token 消耗，同时提高回答准确率和可溯源能力；可以在现有 RAG pipeline
  上增加结构索引层。

  - EntQABench 是 284 万级技术文档 QA 基准，可用于评估大规模文档库的检索和 Agent 导航能力，但电商领域还需自建结构评估集。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：Agentic RAG 迭代检索返回孤立 chunk，模型难以区分相关证据和相似但无关的内容；结构感知方法如 PageIndex 可导航文档结构，但无法扩展到大型语料，且先选定单文档后无法纠错。

方法关键点：RIT-RAG 离线为每个文档用目录（TOC）或站点地图构建树；查询时先宽检索 chunks，用其位置跨文档诱导可管理的子树；LLM Agent 在子树上导航，选择性读取有希望的节点，必要时改写查询。分工是检索建议看哪里，Agent 决定读什么。

结果：在金融、科学、客户支持基准上取得最高回答准确率；在包含 284 万技术文档网页的新基准 EntQABench 上，三种 LLM 均比最强基线高 6.8–11.4 个百分点。
