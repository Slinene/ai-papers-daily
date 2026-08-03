---
title: 'ExtractBench: A Benchmark for Schema-Guided Enterprise Document Extraction'
title_zh: ExtractBench：模式引导的企业文档提取评测基准
authors:
- Boyang Zhang
- Adrian Lyjak
- Eli Stewart
- Zhaoqi Li
- Simon Suo
affiliations:
- RunLLAMA AI
arxiv_id: '2607.29677'
url: https://arxiv.org/abs/2607.29677
pdf_url: https://arxiv.org/pdf/2607.29677
published: '2026-07-30'
collected: '2026-08-03'
category: Eval
direction: 文档信息提取 · 评测基准
tags:
- schema-guided extraction
- benchmark
- grounding
- enterprise documents
- agentic extraction
- cost evaluation
one_liner: 首个同时评估值准确率、记录完整性、溯源和成本的模式引导提取基准，揭示长文档截断与成本权衡
practical_value: '- **电商文档自动化中的评测设计**：直接复用 value F1 与 grounding F1（word-level、page-level）评估发票、订单、表格等复杂文档的提取质量，尤其关注长列表字段的完整性截断问题，可避免线上漏单。

  - **成本与精度权衡的工程选型**：参照论文对商业 VLM（如 GPT-4o、Claude）与编程代理（coding agent）的成本/精度对比，在实时性要求高的电商场景用
  VLM，在离线批处理用 coding agent，或使用 LlamaExtract Agentic Plus 这类成本仅为 1/10 的系统。

  - **Schema 驱动 Agent 的落地验证**：论文中 schema 即 JSON Schema 定义字段与类型，可直接用于电商的 SKU 属性提取、报关单信息提取等有明确
  schema 的场景，强化 Agent 的指令遵循与证据追溯。

  - **挑战场景的针对性优化**：根据 13 种挑战标签（如扫描件、手写、密集文本）细分指标，定位自身业务中的高难度文档类型，针对性地调优预处理或模型选型。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：企业 Agent 工作流越来越依赖模式引导提取（给定文档和用户定义的 JSON Schema，输出符合 Schema 的 JSON 及证据溯源），但缺乏全维度评测基准，尤其缺少对值准确性、记录完整性、证据溯源和成本的综合度量。

**方法关键点**：构建 ExtractBench，包含 370 份企业文档、4869 页、8 个行业领域、67 种文档类型，并标记 13 种挑战场景（扫描件、手写、长表格等）。黄金标注管线通过独立系统交叉验证、已知值合成列表和人工核查表单得到。评测指标：
- **Value F1**：顺序无关的值准确率，同时衡量记录完整性和字段值正确性；
- **Grounding F1**：分别从词级别（word bounding box）和页级别评估证据溯源；
- **每页成本**：0.2¢ 到 34¢ 的跨度。
对比了 14 个系统，包括商用 VLM（GPT-4o、Claude）、编程代理及 LlamaExtract 等专用提取 Agent。

**关键结果**：商用 VLM 在短文档上表现良好，但在长文档中出现严重的记录列表截断（缺失率高达 40%+）；编程代理虽保持高准确但成本极高（$0.34/页）；LlamaExtract Agentic Plus 在所有三项指标上排名第一，准确率与编程代理相当，但成本仅为后者的十分之一。
