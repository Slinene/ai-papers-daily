---
title: 'Chunk Recomputation under Real Document Revisions: Measuring Update Cost and
  Retrieval Quality of Fixed, Recursive, and Content-Defined Chunking'
title_zh: 真实文档修订下的分块重算：固定、递归与内容定义分块更新成本及检索质量测量
authors:
- Yuning Bian
- Lele Xu
- Yifan Yuan
- Xinyu Yin
- Chengyan Zhan
affiliations:
- Anhui University of Technology
arxiv_id: '2610.31019'
url: https://arxiv.org/abs/2610.31019
pdf_url: https://arxiv.org/pdf/2610.31019
published: '2026-10-22'
collected: '2026-10-24'
category: RAG
direction: RAG 文档分块更新成本评估
tags:
- RAG
- Chunking
- Update Cost
- Retrieval Quality
- Wikipedia Revisions
one_liner: 在真实维基百科修订对上量化三种分块策略的嵌入重算成本与检索质量，发现更新成本差异显著且检索质量相近
practical_value: '- 对于维护动态知识库（如商品文档、政策页、新闻）的 RAG 系统，分块策略不能只看静态检索指标：固定大小分块在每次更新时重算
  57-68% 的嵌入，内容感知分块（递归/内容定义）可降低到 38-56%，但需注意内容定义分块在部分中文文本上失败（4/62），工程上可选择更稳健的递归分块。

  - 采用字节相同重用规则：只对内容发生变化的 chunk 重新嵌入，可显著降低更新成本；这要求存储 chunk 的哈希或原始文本，适合增量更新流水线。

  - 当检索质量差异很小时（<2 个百分点），优先选择更新成本低的分块策略，尤其在高频更新场景（如价格/库存变化引起的文档编辑）。

  - 评估分块器时应同时报告更新成本（重算比例）和检索质量，避免仅依据静态基准选型；参数长度会影响内容感知分块器的成本排名，需针对实际 chunk 长度做网格搜索。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

动机：RAG 分块策略通常在静态快照上评估，但知识库文档持续更新；由于 chunk 独立嵌入，边界移动会导致未修改文本被重新嵌入。

方法：在 120 对相邻中英文维基百科修订上，测试三种无状态分块器（非重叠固定大小、递归段落优先、内容定义），采用严格字节相同重用规则和冻结密集编码器，测量重算成本与检索质量。

结果：在 116 篇共同成功池中，使用冻结、长度校准参数：固定大小分块重算其新版本嵌入输入工作量的 57-68%，递归分块 38-56%，内容定义分块 43-54%（在 62 篇中文中失败 4 次）；在 2048 token 检索预算下，这些参数的平均证据召回在同一语言内差异小于两个百分点。成本参数网格显示，两种内容感知分块器的排名随块长设置变化，而非重叠固定大小分块在每个长度匹配条件下重算成本最高。受控编辑和逐字存在诊断支持边界漂移是导致上一版本已存在文本被重算的一个因素。

结论：更新成本是一个重要且参数敏感的维度，静态检索评估无法暴露，应与检索质量一同报告。
