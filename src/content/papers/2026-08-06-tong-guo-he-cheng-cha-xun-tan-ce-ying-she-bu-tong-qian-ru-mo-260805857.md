---
title: Mapping Similarity Spaces across Embedding Models with Synthetic Query Probing
title_zh: 通过合成查询探测映射不同嵌入模型的相似度空间
authors:
- Marcin Rozmus
- Peter van der Putten
affiliations:
- Pegasystems
- Leiden University
arxiv_id: '2608.05857'
url: https://arxiv.org/abs/2608.05857
pdf_url: https://arxiv.org/pdf/2608.05857
published: '2026-08-06'
collected: '2026-08-09'
category: RAG
direction: 嵌入向量相似度跨模型校准
tags:
- RAG
- Embedding Models
- Similarity Calibration
- Score Mapping
- Synthetic Query Probing
one_liner: 提出无参考合成查询探测方法，学习分数映射使不同嵌入模型的相似度可比，提升阈值可迁移性
practical_value: '- **模型迁移时的阈值复用**：当切换或升级嵌入模型时，利用 isotonic 回归学习旧的相似度分数到新模型分数的单调映射，可直接复用原有检索阈值，避免重做大量
  A/B 测试或人工调参。

  - **无标注的快速校准**：Synthetic Query Probing 通过从文档自动生成查询（如用 LLM 生成）构建配对数据，无需人工标注，可在分钟级完成一次跨模型分数校准，适合频繁迭代模型的场景。

  - **多路召回分数融合**：在推荐或广告系统的多路召回中，不同路可能使用不同嵌入模型，先对各路分数进行跨模型校准再融合，可提升融合排序的合理性，避免因分数分布差异导致某一路被系统性压制。

  - **线上阈值自适应**：新模型上线时，仅需少量查询-文档校准对即可在线学习一个轻量映射函数，实现动态阈值调整，降低线上实验风险。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：RAG 系统依赖向量相似度检索，但不同嵌入模型输出的相似度分数不可直接比较，导致模型迁移时阈值必须重新设定，代价高昂。已有方法需对齐嵌入空间或依赖标注数据，不够轻量。

**方法关键点**：提出 **Synthetic Query Probing**，通过从文档本身生成查询，构造大量的查询-文档块对，无需参考模型或人工标注。基于这些配对数据，学习不同模型间的分数映射函数，包括线性变换、保序回归 (isotonic) 和分位数映射。

**关键结果**：在 SciFact 和一个私有企业语料上实验，发现不同模型在 document ranking 上高度一致，但原始余弦相似度分数存在系统性扭曲（某些模型分数整体偏高或偏低）。学习到的映射能部分对齐分数空间，其中 **isotonic 回归表现最优**，使跨模型的阈值可直接移植，显著降低模型迁移的调试成本。
