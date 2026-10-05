---
title: Query-aware routing for Cross-lingual performance gains in Encoders
title_zh: 跨语言检索中的查询感知路由与 LoRA 适配
authors:
- Akshay Jain
- Edward Kim
affiliations:
- ConfidentialMind
arxiv_id: '2610.02875'
url: https://arxiv.org/abs/2610.02875
pdf_url: https://arxiv.org/pdf/2610.02875
published: '2026-10-02'
collected: '2026-10-05'
category: RAG
direction: 跨语言检索 · LoRA 路由
tags:
- cross-lingual retrieval
- LoRA
- query routing
- multilingual encoders
- dense retrieval
one_liner: 用 query-only LoRA 适配器加语言路由，跨语言检索平均 nDCG@10 提升 20.9%，同时保持同语言性能
practical_value: '- 已有文档索引可以不变：只对 query 侧加 LoRA 训练，文档嵌入冻结复用，避免跨语言优化时重建全量向量库，适合电商/RAG
  线上迭代。

  - 语言路由是一种廉价的安全兜底：根据 query 语言和索引语言做确定性分支，同语言查询走原 encoder，跨语言查询走 adapter，可防止多语言优化回退同语言效果。

  - LoRA 微调只用 query 塔，参数量小、训练快，且天然避免破坏原有同语言检索能力，适合在多语言商品库或本地化搜索场景做增量优化。

  - 如果业务里已有跨语言点击/相关性日志，可以仿照该思路训练 query-only adapter，再配合简单语言 ID 路由上线，不需要改动召回链路。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：多语言编码器在同语言检索上表现良好，但查询与相关文档语言不一致时检索质量明显下降。跨语言检索需要提升芬兰语/瑞典语与英语之间的效果，同时不能破坏既有同语言性能和文档索引。

**方法**：使用 query-only 低秩适配器 LoRA，训练时冻结文档嵌入，只更新查询塔；推理时按查询语言和索引语言做确定性路由——跨语言查询走 adapter，同语言查询走原始 encoder。基于 Nemotron-3-Embed-1B 微调得到 SampoTron。

**结果**：在英、芬、瑞典六个方向平均 nDCG@10 从 0.241 提升到 0.291，相对提升 20.9%；六个跨语言方向全部改善；路由机制保持原始同语言性能，包括两个全量芬兰语评测。方案支持选择性跨语言特化，且文档向量可复用。
