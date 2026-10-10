---
title: Incremental Open-Ended Deep Research with Structured Harness
title_zh: 增量开放式深度研究：结构化 Harness 框架
authors:
- Meilin Chen
- Hongyuan Bao
affiliations:
- Xiaohongshu Inc.
- Zhejiang University
arxiv_id: '2610.11566'
url: https://arxiv.org/abs/2610.11566
pdf_url: https://arxiv.org/pdf/2610.11566
published: '2026-10-07'
collected: '2026-10-10'
category: LLM
direction: LLM 深度研究 · 结构化增量更新
tags:
- Incremental Learning
- Deep Research
- Structured Harness
- Open-Ended Generation
- Report Continuity
- LLM
one_liner: 用结构化 Harness 将深度研究报告视为可演化状态，实现增量更新，保持质量同时显著降低成本。
practical_value: '- 可将大模型生成的内容（商品描述、用户画像、知识库条目）视为可演化状态，通过结构化大纲和证据映射实现局部更新，避免每次从零生成，显著降低
  token 消耗和搜索调用。

  - 持久结构化证据池设计值得借鉴：为搜索/推荐系统沉淀外部检索结果（如市场趋势、用户评论），按证据引用关系缓存，支持跨轮次复用，减少重复检索成本。

  - 选择性更新策略可迁移到需要频繁迭代的内容场景，如广告文案、活动页、商品详情页，仅对受新信息影响的小节触发重新生成，保持历史内容连续性的同时控制成本。

  - 评估框架中引入内容级 ROUGE-L 和 outline 级 EM F1 度量报告连续性，可改造用于评价推荐理由生成或 item 描述更新的历史一致性。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有开放式深度研究（OEDR）系统每次从零生成报告，无法持续维护已生成的研究内容，导致效率低下、成本高昂。

**方法关键点**：提出 Incremental-OEDR 设置，将报告视为随时间演化的状态，增量保留有效知识、修正过时内容、吸收新信息。核心是 Structured Harness：将报告表示为结构化大纲、章节和支持证据的集合；提供结构化检索以定位需要更新的部分，持久结构化证据池缓存可复用的检索结果，结构化生成仅对变化部分进行重写，实现选择性更新和证据重用。同时建立十年时间跨度的时序评估框架，包含单步任务（Single-Step Task）和长链任务（Long-Chain Task），分别评估单次转移和长期更新链上的表现。

**关键结果**：在 DeepResearch Bench 和 DeepConsult 上，无论是开源配置还是专有配置，Incremental-OEDR 都能保持与从零生成方案相当的 report quality，同时大幅提高报告连续性并降低成本：内容级 ROUGE-L F1 最高提升 0.51，大纲级 EM F1 最高提升 0.63，token 消耗降低 33%，搜索调用次数减少 61%。
