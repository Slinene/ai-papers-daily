---
title: 'GeopoliticalQA: Benchmarking Retrieval and Generation over Intelligence Reports'
title_zh: GeopoliticalQA：情报报告检索与生成基准
authors:
- Veronika Solopova
- Ivan Havlytskyi
- Viktoria Skorik
- Ostap Vykhopen
affiliations:
- Mantis Analytics
arxiv_id: '2610.12617'
url: https://arxiv.org/abs/2610.12617
pdf_url: https://arxiv.org/pdf/2610.12617
published: '2026-10-08'
collected: '2026-10-13'
category: RAG
direction: RAG 检索与生成基准评测
tags:
- RAG
- Benchmark
- Geopolitical QA
- Retrieval
- LLM-as-judge
- Embedding
one_liner: 构建 415 份情报报告、5,525 条 QA 的地缘政治 RAG 基准，系统评估检索与生成
practical_value: '- 在电商/Agent 知识检索场景中，chunk 级检索质量不必依赖超大 embedding 模型；中等规模开源编码器 bge-m3
  可与大 10 倍模型持平且优于商业 API，可先用这类模型做成本可控的域内检索。

  - 文档画像先行的问题生成 pipeline 可用于构建电商搜索/推荐领域的合成评测集：先对商品/报告进行结构化画像再生成问题，并配合 LLM-as-judge
  做质量过滤，提升训练与评测数据可用性。

  - 即使给定黄金证据，复杂推理类问题（对应商品选品、活动归因、风险判断等）仍是生成瓶颈；在 RAG Agent 中应加强多步推理、证据整合与结果校验，而非只优化召回。

  - LLM-as-judge 协议验证数据集质量的方法可直接迁移到搜索 query 改写、推荐理由生成等任务的离线评估，减少人工标注成本。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

动机：地缘政治情报报告异构且分析复杂，现有 RAG 系统难以处理长文档、跨报告比较与风险推理类问答。

方法：构建 GeopoliticalQA 基准，覆盖 415 份开源战略情报报告，包含 5,525 条文档标注的 QA 对，题目类型分为事实、推理、比较、风险四类；提出文档感知的生成 pipeline，先对报告进行画像再生成问题；使用专家标注与 LLM-as-judge 协议验证数据质量；在基准上评估 15 种检索系统和 6 个开源 LLM 的 RAG 能力。

结果：文档级检索各模型表现相近；在更难的 chunk 级检索中，检索质量与 embedding 模型规模不相关：中等规模开源编码器 bge-m3 与数量级更大的模型持平，并优于商业 embedding API；即使给定黄金证据，答案生成仍具挑战，尤其推理类与风险类问题成功率明显偏低。
