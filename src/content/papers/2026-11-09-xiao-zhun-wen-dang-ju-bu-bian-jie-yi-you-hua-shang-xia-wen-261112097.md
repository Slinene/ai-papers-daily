---
title: Calibrating Document-Local Boundaries for Contextual Chunk Retrieval
title_zh: 校准文档局部边界以优化上下文分块检索
authors:
- Yuanxiang Wang
- Hui Jiang
- Da Zhu
- Zhihua Chang
affiliations:
- Qwen Business Unit, Alibaba Group
arxiv_id: '2611.12097'
url: https://arxiv.org/abs/2611.12097
pdf_url: https://arxiv.org/pdf/2611.12097
published: '2026-11-09'
collected: '2026-11-10'
category: RAG
direction: RAG 上下文分块检索 · 对比学习校准
tags:
- Late Chunking
- Contrastive Learning
- Contextual Retrieval
- Dense Retrieval
- Chunk Boundary
- InSeNT
one_liner: 分析同文档难负样本决策边界，提出自适应缩放与分块路由提升上下文分块检索
practical_value: '- 在电商知识库、商品详情等长文档做 RAG 时，常因同一商品多个描述块共享上下文而检索混淆；可借鉴本文把 gold chunk
  的最难同文档 sibling 作为显式难负样本，并通过缩放因子校准局部决策边界，提升证据定位准确率。

  - 如果采用 Late Chunking 进行文档分块编码，可在编码阶段加入 chunk-aware routing，将分块边界信息暴露给 attention，有助于获得上下文依赖的分块表示，适合商品详情页、政策文档等长文本场景。

  - 相比于固定温度系数，从 within-document margins 学习自适应判别尺度更能平衡同文档区分度和跨文档泛化；在相似商品、广告文案等难负样本密集的业务中，可尝试对
  margin 做可学习缩放。

  - 该方法主要提升检索质量，额外索引成本较低；但需要业务侧先有合理的分块策略，迁移到搜索推荐语料时需结合具体分块规则。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：长文档检索需要返回局部证据，但独立分块编码丢失上下文，单文档向量又无法定位证据。现有 Late Chunking 和分块级后训练虽保留文档上下文，却因同文档分块共享上下文，导致语义相近的同文档负样本难以区分。

**方法关键点**：论文聚焦 gold chunk 与其最难同文档 sibling 的局部决策边界。从 InSeNT 出发，分析其文档内梯度，发现固定 logits 下条件负样本分配的熵随缩放因子单调下降，说明缩放因子决定同文档区分能力。据此提出两部件框架：一是从文档内 margins 自适应学习判别尺度，校准区分难度；二是在文档编码中通过 chunk-aware routing 暴露分块划分信息给 attention，使分块表示感知边界。

**结果**：在 ConTEB 和 NanoBEIR 上，该方法在多种编码器设定下提升 contextual chunk retrieval，同时保持有竞争力的 passage-level retrieval 质量；消融显示自适应缩放与 chunk-aware routing 分别承担不同作用。
