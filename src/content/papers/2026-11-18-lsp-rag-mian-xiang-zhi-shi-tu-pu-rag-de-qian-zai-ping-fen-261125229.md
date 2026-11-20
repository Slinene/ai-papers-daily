---
title: 'LSP-RAG: Latent Scoring Perspectives for Knowledge Graph Retrieval-Augmented
  Generation'
title_zh: LSP-RAG：面向知识图谱 RAG 的潜在评分视角框架
authors:
- Haochen Liu
- Guanghui Min
- Song Wang
- Yada Zhu
- Chen Chen
- Jundong Li
affiliations:
- University of Virginia
- University of Central Florida
- IBM Research
arxiv_id: '2611.25229'
url: https://arxiv.org/abs/2611.25229
pdf_url: https://arxiv.org/pdf/2611.25229
published: '2026-11-18'
collected: '2026-11-20'
category: RAG
direction: KG-RAG · 多跳检索打分优化
tags:
- KG-RAG
- Soft Prompt
- Multi-hop Retrieval
- Lightweight LLM
- KGQA
one_liner: 用多视角软提示打分提升轻量 LM 在 KG-RAG 中的多跳检索质量，成本低于大模型引导检索
practical_value: '- 在电商商品知识图谱或售后问答中，可借鉴“轻量 encoder/小 LLM + soft prompt 打分”替代 ChatGPT
  级检索引导，把逐跳 triplet 相关性判断做成低延迟、低成本服务。

  - contextual soft prompt 随 hop 更新，编码 query 与已访问实体/关系，适合 Agent 在商品属性/品牌/类目图中做多跳约束导航，避免下一步检索偏离用户意图。

  - 多视角 latent score 不预设语义角色、自适应聚合，可迁移到广告/推荐候选召回的 multi-signal 相关性融合，例如把购物意图、类目偏好、价格敏感度作为不同
  perspective。

  - 结果说明小模型 + 精细 prompted scoring 可以在 KG-RAG 检索质量上打平甚至超过大模型引导，预算有限时值得先做结构化检索优化，而不是直接上大模型。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：LLM 开放域问答事实性差、多跳推理不足；KG-RAG 通过外部知识图谱补充结构化知识，但现有方法要么依赖 ChatGPT 级模型引导检索、计算成本高，要么用轻量语言模型后多跳检索质量明显下降。

**方法关键点**：LSP-RAG 以多视角软提示打分实现逐跳 KG 检索。每个 latent scoring perspective 由两类软提示驱动：perspective-specific soft prompt 诱导出不同条件的 triplet 打分函数；contextual soft prompt 随每跳编码 query 和历史已探索 triplets，保持跨跳一致性与相关性。多个 latent perspective 自适应聚合，不预设人工语义角色，用轻量 LM 捕获异构相关性信号。

**关键结果**：在多个 KGQA benchmark 上优于现有 KG-RAG 检索系统，包括依赖更大语言模型的对比方法，展示有限算力预算下的有效性与鲁棒性。
