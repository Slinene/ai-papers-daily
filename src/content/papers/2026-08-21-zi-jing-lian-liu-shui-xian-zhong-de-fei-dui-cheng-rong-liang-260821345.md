---
title: Asymmetric Capacity Allocation in Self-Refinement Pipelines
title_zh: 自精炼流水线中的非对称容量分配
authors:
- Zhuoyi Yang
- Ian G. Harris
- Salar Hashemitaheri
- Cassie Huang
- Yuangang Li
- Hyunwoo Oh
- Paul Dourish
- Tony Givargis
- Mohsen Imani
- Li Zhang
affiliations:
- University of California, Irvine
- Drexel University
arxiv_id: '2608.21345'
url: https://arxiv.org/abs/2608.21345
pdf_url: https://arxiv.org/pdf/2608.21345
published: '2026-08-21'
collected: '2026-08-24'
category: LLM
direction: LLM 自精炼流水线非对称容量分配
tags:
- Self-Refinement
- LLM Agents
- Model Scaling
- Inference Efficiency
- Critic-Generator Pipeline
one_liner: 首次按阶段研究自精炼流水线模型规模：生成与精炼需大模型，评论器小模型即可
practical_value: '- 多阶段生成/改写流水线不要均匀分配模型规模：生成器和精炼器用大模型，评论器可大幅缩小；评论器只做判别，容量不敏感，能省大量
  KV cache 和算力。

  - 部署自反思/reflection agent 时，用小模型作 critic 过滤中间结果、大模型做 revision，可保持质量同时显著降低耗时与成本；避免
  critic 也上大模型。

  - 注意 refiner 不要过度缩小：过小的 refiner 可能把已经不错的生成改坏，形成负增益；推荐理由、商品文案生成等场景应为 revision 保留充分容量。

  - 若业务使用生成-评论-改写 pipeline 做 query 推荐或 push 文案，可按此分配预算：先固定大 generator，选择尽量小的 critic，再粗测
  refiner 的敏感区间。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

动机：自精炼（generation→critique→revision）是 LLM Agent 的核心机制，但现有实现通常不区分三阶段模型规模，可能导致算力浪费；缺乏对阶段规模敏感性的系统研究。

方法：在 5 个不同领域 benchmark 上，用 Qwen3 的 6 个规模、Gemma 3 的 4 个规模，首次按阶段替换模型大小，分别测量生成器、评论器、精炼器对整体性能的影响。

结果：更大的 generator 与 refiner 通常带来提升；refiner 过小反而可能损害性能；评论器规模对结果高度不敏感，但引入小评论器始终优于完全不做 critique。结论是自精炼流水线不应平均分配模型容量，不同阶段有不同规模伸缩特性。
