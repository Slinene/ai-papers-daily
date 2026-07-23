---
title: 'Beyond Relevance-Centric Retrieval: Rubric-Oriented Document Set Selection
  and Ranking'
title_zh: 面向文档集整体质量：从评估基准到无训练优化
authors:
- Kailin Jiang
- Lei Liu
- Jian Xi
- Hui Xu
- Junlin Liu
- Baochen Fu
- Shaoqing Ren
- Bin Li
- Vichwang
- Yu Lu
affiliations:
- Tencent Yuanbao AI Search
- University of Science and Technology of China
- University of Chinese Academy of Sciences
- Shandong University
arxiv_id: '2607.19747'
url: https://arxiv.org/abs/2607.19747
pdf_url: https://arxiv.org/pdf/2607.19747
published: '2026-07-21'
collected: '2026-07-23'
category: Eval
direction: 文档集评估与选择 · 面向 RAG 闭环
tags:
- RAG
- document set selection
- evaluation benchmark
- rubric-based
- training-free
one_liner: 提出文档集评估基准 SetwiseEvalKit 和无训练选择方法 Rubric4Setwise，以更少文档提升 RAG 生成质量
practical_value: '- 电商 RAG 场景（智能客服、AI 导购）中，可借鉴 Rubric4Setwise：定义业务准则（如覆盖产品属性、避免矛盾），利用
  LLM 将准则转化为文档选择信号，以更少文档提升答案完整性与准确性。

  - 用 SetwiseEvalKit 的多维指标（冗余、冲突、互补）诊断多路召回融合后的文档集质量，指导重排序策略优化，弥补传统逐条相关性指标的局限。

  - 无训练方法适合快速迭代和冷启动，无需专门训练文档集选择模型，直接复用现有 LLM 的评估能力。

  - 开源基准与工具可直接用于线下评测不同 reranker 的文档集层面效果，为选型提供依据。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：RAG 系统中，检索到的文档集直接作为 LLM 的输入，其整体质量（冗余、冲突、互补性）决定生成效果，但现有评价系统仅按逐条相关性评分，无法衡量文档集级别的优劣。

**方法**：提出评估-诊断-优化框架。设计 SetwiseEvalKit，三级九维度评估基准，覆盖短文本和长文本场景，包含约 28K 条评估准则。系统性评测 12 种 reranker，发现跨文档协调维度普遍薄弱，最佳覆盖率不超过 45%。基于诊断结果，提出 Rubric4Setwise，一种训练无关方法，将基于准则的评估标准转化为文档集迭代选择信号，逐步挑选互补且低冗余的文档子集。

**结果**：Rubric4Setwise 在短文本和长文本 RAG 场景中均达到最优下游生成性能，所需文档数和搜索轮次更少，是唯一同时保持 SOTA 的方法，验证了从评估到优化的闭环有效性。
