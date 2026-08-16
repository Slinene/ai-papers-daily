---
title: 'Who Speaks Matters: Authority-Aware Multi-View RAG over Italian Parliamentary
  Proceedings'
title_zh: 谁发言重要：面向意大利议会记录的权威感知多视角RAG
authors:
- Mirko Tritella
- Riccardo Pozzi
- Matteo Palmonari
affiliations:
- University of Milano-Bicocca, Milan, Italy
arxiv_id: '2608.13410'
url: https://arxiv.org/abs/2608.13410
pdf_url: https://arxiv.org/pdf/2608.13410
published: '2026-08-13'
collected: '2026-08-16'
category: RAG
direction: 权威感知的多视角 RAG 专家检索
tags:
- RAG
- Expert Finding
- Authority Modeling
- Multi-View Summarization
- Quotation Faithfulness
one_liner: 以查询依赖的说话者权威模型驱动多视角摘要，在议会语料上实现高引文忠实度与政治团体覆盖
practical_value: '- 在电商评价、内容导购或专家问答中，可对 UGC 作者/KOL 构建查询依赖的权威度特征（职业、历史发言、主题相关度），而非仅按点赞量或影响力加权，降低头部作者主导。

  - 多视角摘要可迁移到商品评论区、直播切片观点提取：先检索相关 chunk，再识别跨立场的领域专家，最后生成综合摘要并强制附带原文引用，配合 faithfulness
  校验降低错误归因。

  - 可借鉴政治团体覆盖度指标，在推荐或内容聚合场景衡量不同品牌/品类/观点群体的覆盖，防止少数头部主导曝光，提升多样性。

  - 架构上将「检索 → 专家识别 → 综合生成」解耦，便于在 Agent 系统中替换各模块（如专家知识图谱、引用验证器）。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：议会记录是民主协商的原始档案，但体量大、碎片化，公民、记者和研究者难以获得多视角视图。直接对议会文本应用 RAG 存在三类风险：高频发言者主导结果、无法按主题专长给发言者赋权、政治敏感文本中的引用错误归属。

**方法关键点**：ParliamentRAG 系统将上述风险联合解决。核心是一个 topic-dependent authority model，将每个发言者的权威度建模为当前 query 的函数，融合职业、教育背景、历史发言等可解释特征。给定用户查询，系统先检索相关 speech chunk，然后在各议会团体中识别主题相关专家，最后生成综合不同视角的摘要，并附支持性引文。系统结合 Knowledge Graphs 支持专家识别与可解释性。

**关键结果**：在 15 个政策主题上，与 Google NotebookLM 进行自动指标和六位领域专家盲 A/B 对比。ParliamentRAG 的政治团体覆盖率为 0.97（NotebookLM 0.95），引文忠实度 1.00（NotebookLM 0.95），在来源相关维度上获得更强专家偏好；NotebookLM 在散文流畅性等维度上仍占优势。
