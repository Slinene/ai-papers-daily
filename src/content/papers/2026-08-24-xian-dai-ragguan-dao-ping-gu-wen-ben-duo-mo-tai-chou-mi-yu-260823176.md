---
title: 'Evaluating Modern RAG: Textual, Multimodal, Dense, and Late Interaction Pipelines'
title_zh: 现代RAG管道评估：文本、多模态、稠密与晚交互
authors:
- Emre Kuru
- Mehmet Onur Keskin
affiliations:
- Özyeğin University, Istanbul, Türkiye
arxiv_id: '2608.23176'
url: https://arxiv.org/abs/2608.23176
pdf_url: https://arxiv.org/pdf/2608.23176
published: '2026-08-24'
collected: '2026-08-25'
category: RAG
direction: RAG 管道选型与多模态权衡
tags:
- RAG
- Multimodal Retrieval
- Vision-Language Models
- Dense Retrieval
- Late Interaction
one_liner: 提出数据驱动的RAG管道选择方法，在检索效果与资源约束间权衡
practical_value: '- 电商详情页、广告落地页含大量布局、表格、图片，纯 OCR 文本管道会丢失结构语义；可在 RAG 检索阶段引入 VLM 多模态编码，但需按类目或高价值
  query 试点，用延迟与召回指标对比。

  - late interaction（如 ColBERT）是稠密检索与多模态之间的实用折中：保留 token 级交互提升细粒度匹配，同时避免每次查询调用 VLM
  的高开销，适合低延迟搜索推荐场景。

  - 建立管道选型决策表：依据文档类型（文本为主 vs 富媒体）、query 类型、资源预算，用离线 nDCG/recall@k 与在线 p50/p99 延迟、GPU
  成本联合选择，避免一刀切。

  - 对表格规格、价格/评分等结构化信息，优先用 layout-aware 文本解析或混合表示，减少 VLM 调用次数；可先文本召回再用视觉重排，在成本可控下提升准确率。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：传统文本 RAG 依赖 OCR 提取，对线性文档高效轻量，但在视觉复杂文档（布局、表格、图片引用）中丢失语义，导致检索不准。VLM 驱动的多模态管道能联合编码视觉与文本信号，提升质量但增加计算与内存成本，缺乏系统的选型方法。

**方法关键点**：提出定量、数据驱动的管道选择方法论，评估文本与多模态管道，涵盖稠密检索和晚交互架构；分析不同文档语料上的检索效果与资源约束，给出基于经验效果的权衡建议。

**关键结果**：论文未在摘要中提供具体数字，需查阅正文；核心结论是多模态管道在视觉复杂文档上显著优于纯文本，晚交互在效果与效率间提供较好折中。
