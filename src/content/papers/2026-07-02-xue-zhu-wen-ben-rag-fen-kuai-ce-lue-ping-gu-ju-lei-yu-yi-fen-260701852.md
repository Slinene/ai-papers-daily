---
title: Evaluating Chunking Strategies for Retrieval-Augmented Generation on Academic
  Texts
title_zh: 学术文本 RAG 分块策略评估：聚类语义分块未优于固定/递归分块
authors:
- Valentin J. J. Kreileder
- Johannes Reisinger
- Andreas Fischer
affiliations:
- Deggendorf Institute of Technology
arxiv_id: '2607.01852'
url: https://arxiv.org/abs/2607.01852
pdf_url: https://arxiv.org/pdf/2607.01852
published: '2026-07-02'
collected: '2026-07-04'
category: RAG
direction: RAG 分块策略对比评估
tags:
- RAG
- chunking
- semantic-chunking
- evaluation
- faithfulness
one_liner: 在结构化学术长文档上，聚类 semantic chunking 的检索与答案质量未能超越固定大小和递归分块
practical_value: '- 在结构化文档（如商品详情、政策文件）的 RAG 场景中，优先使用固定大小或递归分块，避免为语义分块付出额外计算成本，本次实验未观察到增益。

  - RAGAs 框架的 faithfulness 指标在评价长文档 RAG 时可靠性存疑，业务评估应结合人工校验或更稳定的自动指标（如 retrieval precision）。

  - 针对固定问题（如摘要类）与文档特定问题（如细粒度事实）的性能差异显著，实际部署时需为不同问题类型设计不同的分块与检索策略，例如对细粒度问题保留更细粒度 chunk
  或添加元数据。

  - 文档预处理（格式清洗、结构提取）对性能影响较大，在导入向量库前可强化对标题、段落的语义保留处理。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

动机：
检索增强生成（RAG）中长文档需分块才能被嵌入和 LLM 消费。已有研究推崇基于句子相似度的语义分块，但其是否真的优于简单策略？本文在结构化学术论文（长篇、有固定章节目录）上系统对比固定大小分块、递归分块和基于聚类的语义分块。

方法关键点：
- 数据集：若干本学术论文，分块后存入向量数据库。
- 评估框架：使用 RAGAs 的多项指标（特别关注 faithfulness），并自行设计固定问题（如摘要）与文档特定问题（需定位具体细节）。
- 检索与生成统一评估，考察答案质量与 chunk 召回。

关键结果：
- 聚类语义分块并未表现出优势，甚至在多项指标上略低于固定大小或递归分块。
- RAGAs 的 faithfulness 得分与人工判断不一致，在长文档设置下可靠性有限。
- 固定问题与文档特定问题的性能差异显著：简单分块对固定问题已够用，但文档特定问题更依赖 chunk 的粒度与上下文完整度，预处理格式影响很大。
