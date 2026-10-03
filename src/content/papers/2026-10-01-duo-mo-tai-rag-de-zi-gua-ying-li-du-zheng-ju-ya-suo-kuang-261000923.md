---
title: 'CANOPY: Adaptive-Granularity Evidence Compression for Multimodal RAG'
title_zh: 多模态 RAG 的自适应粒度证据压缩框架
authors:
- Hyojeong Yun
- Jueun Kim
- Wook-Shin Han
affiliations:
- POSTECH
arxiv_id: '2610.00923'
url: https://arxiv.org/abs/2610.00923
pdf_url: https://arxiv.org/pdf/2610.00923
published: '2026-10-01'
collected: '2026-10-03'
category: RAG
direction: 多模态 RAG 证据压缩与迭代检索
tags:
- Multimodal RAG
- Evidence Compression
- Adaptive Granularity
- Hierarchical Scoring
- Iterative Retrieval
one_liner: CANOPY 用层级节点评分与父相对细化选择多粒度证据区域，结合 critic 触发补充检索，压缩 token 同时保持准确率。
practical_value: '- 在电商多模态知识库/商品问答场景，对检索到的商品详情图、表格、视频片段构建层级表示，用微调的小型节点编码器做 query 相关打分，替代
  LLM 逐节点判断，压缩成本低且可并行。

  - 父相对细化：比较父节点与子节点得分的相对差异来选择保留区域，可迁移到商品详情页中“整块描述 vs 局部属性”的自适应裁剪，避免统一细粒度丢失关键上下文。

  - critic 触发补充检索对多跳问题（如跨商品属性对比）很有价值：当现有证据不足时，主动发起针对性二次检索，可提升复杂 query 的答案质量；工程上可用轻量规则或小模型实现。

  - 压缩减少 reader 输入 token 14.2–27.7% 且准确率不受损的结论，支持在 RAG 服务链路中加入后置压缩模块，降低 LLM 输入成本，适合线上成本敏感场景。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：多模态 RAG 检索到文本、表格、图像、视频等异构证据，但现有检索粒度选择无法决定每个条目内部保留多少上下文。粗粒度会混入无关内容，统一细粒度可能丢失解读证据所需的上下文。现有压缩器多为模态特异，缺乏跨异构项的共享自适应保留过程。

**方法关键点**：CANOPY 将每个检索项表示为层级结构，使用在黄金证据上微调的节点编码器对区域与 query 的相关性打分；父相对细化通过比较父节点与子节点得分来选择多个不同粒度区域，节点级剪枝不调用 LLM；此外，一个 critic 判断累积证据不足时请求有针对性的补充检索，新检索项同样被压缩后加入。

**关键结果**：在 33M 项异构语料的五个 QA 基准上，CANOPY 平均答案准确率高于评估的检索基线；消融显示在多跳 QA 上，补充检索是主要准确率提升来源；在未路由的 Qwen3-VL-8B-Instruct 设置下，与无压缩的迭代管道相比，压缩减少 reader 输入证据 token 14.2–27.7%，答案准确率相当。
