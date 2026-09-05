---
title: 'Enhancing Financial Question Answering: A Novel Benchmark Dataset of Banks''
  financial statements'
title_zh: 增强金融问答：银行财报新基准数据集 FinRAG-QA
authors:
- Arianna Miola
- Bruno Spaccavento
- Lorenzo Silotto
- Marco Bianchetti
- Luca Cagliero
affiliations:
- Intesa Sanpaolo Innovation Center
- Università degli Studi di Milano-Bicocca
- Politecnico di Torino
- IMI CIB, Intesa Sanpaolo
- University of Bologna
arxiv_id: '2609.03654'
url: https://arxiv.org/abs/2609.03654
pdf_url: https://arxiv.org/pdf/2609.03654
published: '2026-09-03'
collected: '2026-09-05'
category: RAG
direction: 金融财报 RAG 基准与组件增益分析
tags:
- Financial QA
- RAG
- Benchmark
- Chunk Enrichment
- Cross-encoder
- Long-document Retrieval
one_liner: 构建跨机构银行财报问答基准 FinRAG-QA，量化 RAG 各组件贡献，检索与上下文增强将 NDCG@10 从 0.322 提至 0.710
practical_value: '- 长文档、跨实体检索可借鉴「上下文 chunk enrichment + 检索优化 embedding」组合，NDCG@10
  从 0.322 提到 0.710，适合商品详情、商户证照、政策文档等长文本 FAQ 检索。

  - 生成阶段不要默认堆多 chunk：论文显示单个 top-ranked chunk 比更大上下文更准且延迟更低，可在业务 RAG/Agent 中优先精简上下文并做对比验证。

  - 首阶段检索已强时，cross-encoder rerank 可能带来负优化；在已有高质量 embedding 和丰富上下文后，应评估是否保留 rerank，以节省
  GPU 与延迟。

  - 采用 reasoning-optimised 生成器会带来约 20 倍生成延迟，适合高价值、低实时要求场景；搜索/推荐 Agent 中建议按 query 价值做分级或缓存降级。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

动机：银行财报平均 198k 词，跨机构、跨司法文本与数字格式差异大，现有金融 QA 基准多围绕美国 filings 或单机构，无法评估跨机构检索。

方法：发布 FinRAG-QA，含 999 道从业者标注问题，覆盖 10 个标准化指标，基于 209 份年报与 Pillar 3 报告，来自 24 家欧美银行（2019-2023）。用多阶段 RAG pipeline 评估，逐步分离各组件贡献。

关键结果：
- 上下文 chunk enrichment 结合检索优化 embedding 模型，将 NDCG@10 从 0.322 提升至 0.710；
- 在 ground truth 被召回的条件下，reasoning-optimised 生成器把答案准确率从 44.6% 提升到 79.0%（+34.4 个百分点），但生成延迟约为 20 倍；
- cross-encoder reranking 在首阶段检索已经较强时会降低检索效果；
- 生成时单个 top-ranked chunk 优于更大上下文。

实验运行于 2024 年末至 2025 年初，模型均为当时可用版本。
