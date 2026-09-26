---
title: Learning to Discover Interesting Mathematics
title_zh: 学习发现有趣的数学定理
authors:
- Niket Patel
- Ahmad Rammal
- Amaury Hayat
- Remi Munos
- Julia Kempe
affiliations:
- FAIR @ Meta
- New York University
- CERMICS, ENPC, Institut Polytechnique de Paris
arxiv_id: '2609.28603'
url: https://arxiv.org/abs/2609.28603
pdf_url: https://arxiv.org/pdf/2609.28603
published: '2026-09-22'
collected: '2026-09-26'
category: Reasoning
direction: LLM 数学定理发现 · 形式化证明库
tags:
- LLM
- Theorem Discovery
- Proof Difficulty
- Interestingness Metric
- Self-Expanding Library
- Formal Math
one_liner: 定义证明长度/陈述长度比作为定理有趣度代理，训练27B模型预测证明难度并用于自扩展数学库
practical_value: '- **轻量代理指标设计**：在业务中可类比“信息密度/交互深度”定义内在质量分（如 query 长度 vs 后续点击/转化链长度），训练低成本打分模型替代大模型或人工标注，用于候选排序。

  - **中等规模 reward/scorer 模型**：27B 即可超过 frontier 通用模型，说明特定领域可训小模型做难度/效用预测，降低线上打分成本，适合广告创意/商品文案候选筛选。

  - **自扩展库 + 去重过滤**：生成候选后按指标选择并过滤与已有库高重叠项，从 91.9% 降到 30.6%，可借鉴到推荐/广告生成场景，避免生成结果与历史素材同质化。

  - **迭代构建优质候选池**：以自扩展方式逐步加入经证明有效/有趣的候选，可迁移到 query 推荐、push 文案库的自动扩量。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM 已能证明许多数学猜想，但产生的新定理是否有趣/有用仍缺乏可量化信号，难以自动扩展数学知识库。

**方法**：提出定理内在有趣度 = 证明长度 / 陈述长度，并验证其与下游效用强相关；将给定前提下的证明难度作为核心原语，训练 27B 模型预测该难度，准确率超过 frontier 通用模型。基于该指标优化生成，使模型产出更有趣的定理，同时与 Mathlib 的实质/完全重叠从 91.9% 降至 30.6%。系统可生成候选定理、按有趣度选择并迭代构建自扩展数学库。

**结果**：指标与下游效用相关，27B 难度预测模型优于通用大模型，重叠率大幅下降，展示无需人工指定目标即可扩展形式化数学库的路径。
