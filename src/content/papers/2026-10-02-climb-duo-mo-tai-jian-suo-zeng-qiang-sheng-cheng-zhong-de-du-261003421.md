---
title: 'CLIMB: Confidence-Guided Complementary Evidence for Multimodal Retrieval-Augmented
  Generation'
title_zh: CLIMB：多模态检索增强生成中的置信度引导互补证据
authors:
- Hang Gao
- Wujiang Xu
- Zhixing Zhang
- Kai Mei
- Jingyi Yang
- Dimitris N. Metaxas
affiliations:
- Rutgers University
- Google
arxiv_id: '2610.03421'
url: https://arxiv.org/abs/2610.03421
pdf_url: https://arxiv.org/pdf/2610.03421
published: '2026-10-02'
collected: '2026-10-05'
category: RAG
direction: 多模态 RAG 互补证据与置信度控制
tags:
- Multimodal RAG
- MMR
- Confidence Control
- VQA
- Inference-time
- Evidence Filtering
one_liner: 训练无关的多模态 RAG 框架，用互补证据池与置信度引导的迭代细化提升知识密集型视觉问答效果
practical_value: '- 在商品图文问答、电商知识库检索中，可用 MMR 式去冗余代替单纯 Top-K，构建紧凑互补证据池，减少重复段落、提高信息覆盖。

  - 多维度 critic 评分（相关性、证据特异性、跨模态对齐）比单一相似度更精细，可迁移到多模态商品信息或图文评论的检索排序。

  - 置信度条件接受机制（只有置信度上升才更新答案）可作为 Agent 多轮检索-生成中的停止准则，避免无效迭代和 token 浪费。

  - 训练无关、不改动底层 MLLM 与检索器，适合在现有 RAG 流程上快速灰度实验，验证推理侧优化收益。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：多模态大模型在知识密集型视觉问答中依赖外部文本证据，但常见 Top-K 检索或重排会返回冗余段落，且无法判断答案更新是否被证据充分支持。

**方法关键点**：
- 先构建紧凑互补证据池：采用 MMR 风格目标，同时考虑 query 相关性与段落级冗余，从初检结果中筛选互补证据。
- 在固定证据池内做置信度控制的迭代细化：R/E/C critic 从相关性、证据特异性、跨模态对齐三个维度给段落打分；证据接地的置信度估计器只有当更新后的答案置信度上升时才接受，否则停止。
- 训练无关、推理时使用，不修改底层检索器或 MLLM。

**关键结果**：在 Encyclopedic-VQA 和 InfoSeek 上一致超越多模态 RAG 基线；消融实验表明互补证据池、critic 评分、置信度控制的迭代细化各自均带来性能贡献。
