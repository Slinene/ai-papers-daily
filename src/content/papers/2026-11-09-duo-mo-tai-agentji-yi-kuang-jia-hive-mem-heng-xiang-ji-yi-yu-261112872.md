---
title: 'HiVe-Mem: Interleaving Horizontal Memory Expansion and Vertical Evidence Composition
  for Multimodal Agents'
title_zh: 多模态Agent记忆框架HiVe-Mem：横向记忆扩展与纵向证据组合交错
authors:
- Haozhen Zhang
- Bohan Liu
- Jianzhu Bao
- Qingyuan Liu
- Haodong Yue
- Xiao Li
- Zi Pong Lim
- Wenya Wang
affiliations:
- Nanyang Technological University
- Tsinghua University
- Sun Yat-sen University
- Aumovio Singapore Pte. Ltd.
arxiv_id: '2611.12872'
url: https://arxiv.org/abs/2611.12872
pdf_url: https://arxiv.org/pdf/2611.12872
published: '2026-11-09'
collected: '2026-11-10'
category: Agent
direction: 多模态Agent记忆 · 图扩展与证据选择
tags:
- Multimodal Agents
- Memory Retrieval
- Evidence Selection
- Token Efficiency
- Graph Expansion
one_liner: 提出横向图扩展与纵向证据选择交错的多模态记忆框架，性能提升且token消耗降低约90%
practical_value: '- 记忆组织成关系图，用文本和视觉锚点做横向扩展，可弥补纯语义检索遗漏的互补信息，适合电商客服Agent或带图咨询场景。

  - 每个记忆保留多种证据形式（摘要、caption、视觉视图、原始图片、交互历史），用轻量级可训练选择器按query自适应组合证据，能大幅降低上下文token，可直接借鉴到RAG或对话系统的记忆管理。

  - 二维设计（横向扩展+纵向证据选择）解耦记忆覆盖率和证据粒度，工程实现上可先召回更多候选再按需选择证据，平衡效果与成本。

  - 选择器独立作用于每个检索到的记忆，而非全局固定表示，训练开销小且易插入现有Agent框架，适合需要长期多模态交互的产品。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：多模态Agent积累长交互历史后，有效检索和利用过去信息成为关键。现有记忆系统多基于压缩记忆做语义检索，且暴露固定表示，容易漏掉相关记忆，也忽视不同query对证据形式的异构需求。

**方法关键点**：HiVe-Mem采用横向记忆扩展与纵向证据组合交错。横向：将记忆episode组织成关系图，利用文本和视觉锚点，从语义检索到的种子节点扩展到相关邻居，恢复互补信息。纵向：每条检索到的记忆保留多种证据形式，包括紧凑摘要、caption、grounded视觉视图、原始图片和交互历史；一个轻量级可训练选择器针对每条记忆独立组合证据子集，实现query自适应利用异构多模态信息。二维设计同时扩大覆盖率和适配单条记忆贡献的证据。

**结果**：在三个多模态记忆基准上，HiVe-Mem一致提升不同base模型的任务性能，与最高效的竞争多模态基线相比，token消耗降低约90%。
