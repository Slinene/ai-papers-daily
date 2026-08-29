---
title: Assessing the Downstream Utility of Evidence-Aware Retrieval in RAG
title_zh: 评估 RAG 中证据感知检索的下游效用
authors:
- Utshab Kumar Ghosh
- Debayan Mukhopadhyay
- Shubham Chatterjee
affiliations:
- Missouri University of Science and Technology
- University of Calcutta
arxiv_id: '2608.26379'
url: https://arxiv.org/abs/2608.26379
pdf_url: https://arxiv.org/pdf/2608.26379
published: '2026-08-26'
collected: '2026-08-29'
category: Eval
direction: RAG 检索评估有效性
tags:
- RAG
- Retrieval Evaluation
- Evidence-aware
- LLM Judges
- System Selection
- Answer Support
one_liner: 证据感知检索信号会改变排序，但不总能改进训练、系统选择或答案质量预测
practical_value: '- 在 RAG / Agent 检索链路中，不要把 evidence-aware retrieval 分数直接当作系统选择或生成质量的金标准；排序变化不等于下游效果提升，需要按具体生成器指令和评估器验证。

  - 若用 evidence support 信号做检索器训练或证据过滤，收益高度依赖生成器如何使用证据；建议在业务侧做线上 A/B，并统一答案评估口径，避免单一
  LLM judge 结论误导决策。

  - 电商 / 导购 Agent 若引入证据感知过滤，应同时监控答案侧业务指标（如转化、满意度、人工审核），不能只看证据保留率或检索分数。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：RAG 检索评估正从主题相关性转向证据支持度，但尚不清楚这种更贴合下游证据需求的评估是否让基于它的决策更可靠。

**方法**：在 5 个检索基准和 TREC RAG 2025 端到端场景中，把 answer-support 信号用于四种角色：比较检索器、指导检索训练与系统选择、预测下游答案质量、过滤给生成器的证据。

**关键结果**：该信号会改变检索排序，但下游价值并不均匀：不能可靠改进检索器训练；用于系统选择时收益取决于生成器被指示使用证据的方式；基于它的检索分数无法在未见主题上稳健预测答案质量。人工标注证实过滤会优先保留有用证据段落，但不同答案评估器对答案是否改善结论不一致。结论是：让检索评估更贴近证据需求本身并不会自动让所有下游用途更可靠。
