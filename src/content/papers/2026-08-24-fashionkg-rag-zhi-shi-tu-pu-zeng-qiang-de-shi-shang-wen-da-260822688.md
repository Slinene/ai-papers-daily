---
title: 'FashionKG-RAG: Knowledge Graph-Enhanced Retrieval-Augmented Generation for
  Fashion Question Answering'
title_zh: FashionKG-RAG：知识图谱增强的时尚问答检索增强生成
authors:
- Yujuan Ding
- Linyin Luo
- Shijie Wang
- Xu Yuan
- Yunshan Ma
- Yi Bin
- Wenqi Fan
- Qing Li
arxiv_id: '2608.22688'
url: https://arxiv.org/abs/2608.22688
pdf_url: https://arxiv.org/pdf/2608.22688
published: '2026-08-24'
collected: '2026-08-25'
category: RAG
direction: 知识图谱增强 RAG · 时尚问答
tags:
- Knowledge Graph
- RAG
- Fashion QA
- Agentic Pipeline
- Retrieval Reranking
- LLM
one_liner: 构建领域级时尚知识图谱 FashionEcoKG，并设计训练无关的 PG-RAG 框架，通过双粒度路径重排提升时尚问答准确率
practical_value: '- 构建领域知识图谱时不要止步于物品属性/关系，可借鉴 FashionEcoKG 的 agentic 三阶段管道：从权威教材抽取高保真知识核心，再做跨域增强和生成式扩展，捕获电商领域的完整生态（设计、生产、营销、穿搭等），降低
  LLM 幻觉。

  - PG-RAG 的 Dual-Granularity Path Re-Ranking 可直接迁移到通用 RAG 检索后排序：先用剪枝后的 query skeleton
  提升召回，再用原始完整 query 对候选路径逐条做 agentic 审查，兼顾召回和精确率。

  - 训练无关（training-free）框架适合快速落地，无需微调 LLM，只需在检索和重排环节做结构化处理，适合电商搜索推荐团队在现有 RAG 管线上增量部署。

  - 对时尚/导购类 Agent，可以将领域 KG 作为工具或知识源，结合 skeleton 提取和路径重排，让 Agent 回答“这件衣服适合什么场合”等知识密集型问题时更有依据。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：时尚是知识密集型领域，但 LLM 存在幻觉且缺乏领域专精；现有时尚 KG 多限于产品属性或物品关系，无法覆盖更广泛的时尚生态。

方法：构建 FashionEcoKG，一个通过三阶段 agentic 管道生成的领域级知识图谱：从权威教材抽取高保真知识核心，通过跨域增强和生成式扩展加强结构连通性。配套提出 PG-RAG（Pruning-Grounding RAG），训练无关框架，含 Dual-Granularity Path Re-Ranking（DGPR）模块：PSR 先对 query 蒸馏出 skeleton 形式提升检索召回，GAR 再基于原始完整 query 对候选路径逐条审视，确保全局相关性。

结果：在时尚 QA 数据集上，PG-RAG 利用 FashionEcoKG 提升检索和答案准确率，优于非 RAG 和现有 KG-RAG 基线（原文未提供具体数值）。
