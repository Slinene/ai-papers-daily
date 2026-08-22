---
title: 'The Embedder''s Dilemma: LLMs Are Better, but at What Cost?'
title_zh: 嵌入者的困境：LLM 更好，但成本多高？
authors:
- Adnan El Assadi
- Niklas Muennighoff
- Jinhyuk Lee
affiliations:
- Harvard University
- Stanford University
- Independent Researcher
arxiv_id: '2608.12875'
url: https://arxiv.org/abs/2608.12875
pdf_url: https://arxiv.org/pdf/2608.12875
published: '2026-08-12'
collected: '2026-08-22'
category: Eval
direction: 文本嵌入与 LLM 成本效益对比
tags:
- text embeddings
- LLM
- cost efficiency
- retrieval
- benchmark
- Pareto frontier
one_liner: 控制成本对比 10 个 LLM 与 26 个嵌入模型，发现 LLM 总体仅高 0.4 分，且仅在推理重型检索领先，成本最高贵 1431 倍
practical_value: '- 在商品相似度、分类、聚类等经典任务上，专用 embedding 模型（甚至小模型）性价比极高，不要盲目用大 LLM 替换；LLM
  仅在推理密集型检索（复杂 query 理解、多跳推理）才值得考虑。

  - 若用 LLM 做检索，注意 reasoning tokens 占推理成本 28-81%，可通过限制 reasoning budget（如关闭 thinking
  或降低 max tokens）在多数场景保持或提升检索质量，显著降低 API 成本。

  - 构建 embedding 服务时，用类似 MTEB(LLM) 的基准做成本-质量 Pareto 前沿分析，结合自身业务指标选择前沿模型；同时关注本地 GPU
  吞吐，open LLM 比同 GPU 上的 embedding 模型慢 2.5-736 倍。

  - 电商/搜索场景可分层：embedding 模型负责粗排和相似度召回，LLM 仅用于长尾 query 改写、意图解析或复杂检索，避免全量 LLM 推理。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：在选择文本嵌入方案时，团队常面临“专用 embedding 模型 vs 通用 LLM”的决策，但已有对比通常不控制成本，难以指导工程落地。

**方法**：作者在 37 个任务（分类、STS、聚类、配对分类、检索）上对 10 个 LLM（6 个家族）与 26 个 embedding 模型（118M-14B 参数）进行受控、成本感知的对比，统计 API 成本、GPU 吞吐、推理 token 占比，并绘制成本-质量 Pareto 前沿。

**结果**：两个范式整体打平：最佳 LLM Gemini 3.1 Pro 得分 77.6，最佳 embedding 模型 77.2，仅差 0.4。任务差异明显：LLM 在推理重型检索上领先，embedding 模型在分类上领先，聚类、STS、配对分类接近。成本差异悬殊：LLM 单次 benchmark 成本最高贵 1431 倍（$154 vs $0.11），open LLM 在同 GPU 上慢 2.5-736 倍；reasoning tokens 占 28-81% 推理成本，但降低 reasoning budget 对多数模型可保持或提升检索质量。Pareto 前沿包含领先 embedding 模型和一个 LLM（Gemini 3.1 Pro）。结论：推荐分工——相似度、分类、聚类用 embedding 模型，推理密集型检索才用 LLM。
