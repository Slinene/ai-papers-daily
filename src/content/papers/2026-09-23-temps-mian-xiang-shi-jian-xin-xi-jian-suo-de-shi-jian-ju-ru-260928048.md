---
title: 'TEMPS: Temporal Sentence Embeddings for Temporal Information Retrieval'
title_zh: TEMPS：面向时间信息检索的时间句嵌入模型
authors:
- Mourad Hassani
- Julien Romero
- Amel Bouzeghoub
- Christian Jacquelinet
affiliations:
- SAMOVAR, Télécom SudParis, Institut Polytechnique de Paris
- Aldebaran Care
arxiv_id: '2609.28048'
url: https://arxiv.org/abs/2609.28048
pdf_url: https://arxiv.org/pdf/2609.28048
published: '2026-09-23'
collected: '2026-09-24'
category: RAG
direction: 时间感知检索 · 模块化时间分支
tags:
- Temporal IR
- Dense Retrieval
- RAG
- Temporal Embeddings
- Gaussian moment matching
one_liner: 在冻结语义检索器上附加时间分支，用时间表达式 grounding 提供监督，提升时间敏感检索
practical_value: '- 可直接复用到电商搜索：商品标题、query 中常含“2023 新款”“夏季促销”“去年款”等时间表达，冻结现有语义双塔模型，增加轻量
  temporal branch，解析时间区间并计算 Gaussian-KL 包含度作为时间相似度分数，在召回/排序阶段与语义分数加权融合，无需重新训练主模型。

  - 训练 supervision 来自时间表达 grounding，不需要人工标注时间相关性数据，适合业务中大量无标注文本；可在现有商品库/搜索日志上自动构造时间锚点对。

  - 时间分数设计为分布包含度量（KL inclusion），适合处理模糊时间词如“近三年”“最近夏天”，比精确日期匹配更鲁棒；可直接用于 RAG 知识库的时效性过滤，避免过期内容被检索。

  - 工程实现上 temporal branch 参数少、冻结 backbone，线上推理开销小，可作为排序阶段的一个独立特征接入现有点击/转化模型。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

动机：现代稠密检索和 RAG 管道在主题匹配上表现好，但对时间信息不敏感，临床、新闻、法律等场景中“何时发生”决定相关性。现有方法常返回主题相关但时间错误的内容。

方法关键点：定义 Temporal Textual Similarity（TTS）任务，衡量两个锚定文本在时间上的一致性，独立于主题相似度。TEMPS 在冻结的语义检索器外接一个模块化 temporal branch：将锚定时间表达式解析为时间区间，每个区间 moment-match 成一个 Gaussian 分布；由此得到的排序信号监督一个以锚点日期为条件的编码器。推理时将 temporal score（Gaussian-KL 包含度）与语义分数融合。训练监督完全来自时间表达式 grounding，无需人工标注时间相关数据。

关键结果：在三个时间基准上，对所有测试的语义 backbone 均提升 MRR；在 TS-Retriever 上 R@1 从 19.92 提升到 25.39，超过此前时间检索 SOTA。
