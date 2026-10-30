---
title: Contextual Embeddings Beyond the Gold Chunk
title_zh: 上下文嵌入：超越单一黄金块的分级蒸馏
authors:
- Sedigheh Eslami
- Markus Krimmel
- William Barber
- Antoine Chaffin
- Maximilian Schall
- Jonas Golde
- Louis Milliken
- Ekaterina Glazkova
- Denis Bykov
- Bo Wang
affiliations:
- Perplexity AI
- turbopuffer
arxiv_id: '2610.38854'
url: https://arxiv.org/abs/2610.38854
pdf_url: https://arxiv.org/pdf/2610.38854
published: '2026-10-28'
collected: '2026-10-30'
category: RAG
direction: 上下文嵌入训练与评测
tags:
- Contextual Embeddings
- Dense Retrieval
- Knowledge Distillation
- RAG
- Multi-vector
- Visual Document Retrieval
one_liner: 用查询感知压缩模型蒸馏分级 chunk 相关性替代 gold-chunk 标注，发布 9B/0.6B 模型并刷新多基准 SOTA
practical_value: '- 用 query-aware 压缩模型/reranker 产生 token 级 graded relevance，聚合为任意
  chunk 软标签，替代二值 gold chunk；既避免标注绑定分块，又让支撑证据不再被当负样本。电商搜索、长商品详情、合同、政策文档检索可复用这套在线蒸馏链路。

  - 文档级检索可采用 multi-vector + MaxSim：每个文档保存多个 chunk embedding，查询-文档相似度用最高 chunk 分数；在
  RAG/商品召回中比单向量更细粒度，且不增加 chunk 数存储。

  - 评测不要只看单一 gold chunk，应标注 answer groups + evidence groups，并报告 Answer@K、Evidence
  recall、Tokens to full coverage；这能暴露排序在 aspect coverage 与读取代价上的真实差异。

  - 大模型蒸馏小模型保持共享 embedding space，让索引侧用 9B、查询侧用 0.6B，配合 MRL 1024/2048 维度 + int8 量化，可在不同存储/延迟预算下切换。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
RAG 对长文档分块检索，常规 dense embedding 独立编码 chunk 丢失文档上下文；上下文嵌入虽然解决此问题，但训练依赖 gold-chunk 标注，默认每个 query 只有一个相关 chunk，支撑证据被当成负样本，标注昂贵且与 chunking 绑定；现有评测也只奖励单一 gold passage，无法检验答案跨块、证据检索、文档消歧。

### 方法
- 教师：部署在 Perplexity answer pipeline 的 query-aware context compression model，token 级预测相关概率，细粒度、软标签且推理便宜，可在线打标。
- 9B 学生：chunk 相关分数取 chunk 内 top-k token relevance 均值，softmax 温度得到 teacher chunk 分布；学生用上下文编码器生成 chunk embeddings，前向 KL 拟合该分布；document-level 用 MaxSim 取文档内最高 chunk 相似度，InfoNCE 将正文档拉高。损失为 w_dist=1、w_con=2。
- 0.6B：对 9B 做 representation distillation，沿用 LEAF 风格，共享 embedding space。
- 训练不依赖任何 chunk-level 标注；440 数据集/57M pairs，50+ 语言；LoRA + MRL 1024/2048 + int8。
- 图像：视觉塔按水平条带切 chunk，插入 separator token，支持 VDR。

### 结果
- context-bench：9B Answer@10 45.5%，比 voyage-context-4 高 14.4 点；Document@10 61.6。
- Q2D-Chunk base queries：Answer@10 86.4%，比 voyage-context-4 高 2.5 点、比 pplx-embed-context-v1 高 11.5 点；Tokens to full coverage 中位 1,954，最少。
- ConTEB 平均 nDCG@10 83.4%，超过 v1 的 82.1% 和 voyage-context-4 的 80.4%。
- 9B 为 ViDoRe-V3 上 SOTA dense VDR；2-chunk + 1024d 超过 Nemotron-3.5-8B 且索引小 4 倍。
- 消融：去掉蒸馏损失，Q2D Answer@10 掉 15.2 点，ConTEB 掉 14.6 点。

### 值得记住
用查询感知压缩模型产生 token 级 graded relevance 并聚合到任意 chunking 的软标签，替代 gold-chunk 监督，让 embedding 学会同时召回答案与证据。
