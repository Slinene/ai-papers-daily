---
title: 'FLOWREADER: Min-Cost Flow Optimization for Multi-Modal Long Document Q&A'
title_zh: FLOWREADER：用最小费用流优化多模态长文档问答的证据组装
authors:
- Ambuj Mehrish
- Sebatiano Vascon
affiliations:
- Ca' Foscari University of Venice
arxiv_id: '2606.07235'
url: https://arxiv.org/abs/2606.07235
pdf_url: https://arxiv.org/pdf/2606.07235
published: '2026-06-05'
collected: '2026-06-08'
category: RAG
direction: 多模态RAG · 图优化证据路由
tags:
- RAG
- multimodal QA
- min-cost flow
- evidence assembly
- long document
one_liner: 将多模态文档的证据组装建模为最小费用流问题，统一控制评分、路由、选择和自适应计算
practical_value: '- **证据组装的图建模思路可迁移到电商多模态信息聚合**：将商品标题、详情图、表格参数、用户评价等视为异构节点，用最小费用流从碎片化来源中筛选最优证据组合，代替简单的
  Top-K 检索，提升回答或推荐理由的完整性。

  - **统一评分向量h控制多目标**：通过一个共享的评分向量同时驱动 MMR 去重、相关性筛选和长度感知的可回答性评估，可用于 Agent 的任务规划中，动态权衡信息收集的多样性、可靠性与成本。

  - **熵正则化复制者动态（replicator dynamics）用于紧凑子集选择**：在 Agent 多智体场景下，从多个候选证据路径中选出无冗余的紧凑集合，可避免信息重复，提升
  RAG 或决策模块的效率。

  - **双过程门控与自适应 System-2 精炼**：当生成一致性低或流图容量紧张时触发二次精炼，电商 Agent 可借鉴这种「成本感知的浅层回答 + 条件化深层推理」模式，优化
  API 调用开销与回答质量。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：长文档、多模态 QA 中，证据分散在文本、表格、图片、幻灯片等碎片中，传统 Top-K 分块检索独立处理每个碎片，无法建模证据间的连接与多跳依赖，导致回答不完整或错误。

**方法**：将证据组装转化为多模态节点图上的最小费用流问题。用一个共享评分向量 h 统一控制：① 源节点选择（基于 MMR，平衡相关性与多样性）；② 汇节点选择（长度感知的可回答性代理）；③ 边的成本与容量。最优流分解为候选证据路径，再用熵正则化复制者动态筛选紧凑无冗余子集。最后，并行 VLM 工作器在双过程门控下生成答案：仅当回答一致性低或流图容量紧张时，触发一次 System-2 精炼，实现自适应计算。

**关键结果**：在 VisDoMBench 上，FLOWREADER 在证据高度碎片化的 PaperTab 子集上达到 58.40（+1.30），SlideVQA 子集 72.93（+0.62），五子集宏平均 65.47，与最强基线 G²-Reader（66.21）仅差 0.74。表明最小费用流在碎片化多模态证据上显著优于 Top-K 检索，且提供了评分、路由、选择、计算统一的控制框架。
