---
title: 'Functional Depth Is Learned: Isolating the Computation That Layers Produce
  Only Together'
title_zh: 功能深度是学习得到的：分离层间联合计算
authors:
- JaeSeong Kim
- KyungTae Lim
affiliations:
- Semyung University
- Korea Advanced Institute of Science & Technology
arxiv_id: '2611.27911'
url: https://arxiv.org/abs/2611.27911
pdf_url: https://arxiv.org/pdf/2611.27911
published: '2026-11-20'
collected: '2026-11-23'
category: LLM
direction: Transformer 深度功能分析
tags:
- functional depth
- cross-layer dependency
- pretraining
- mechanistic interpretability
- inclusion-exclusion
- identity ablation
one_liner: 用容斥分解证明预训练逐步组织跨层依赖，而非仅堆叠独立层
practical_value: '- 做 LLM4Rec/Agent 模型蒸馏或层剪枝时，不要只用层间 representation similarity（如 CKA/余弦）判断冗余；论文发现
  similarity 与 connected coordination 负相关，且在部分模型上分歧，建议同时测删除该层/block 对下游 loss 的影响，或引入
  inclusion-exclusion 的 connected component 强度作为剪枝指标。

  - 若业务上需要压缩多层 Transformer 推理（如电商搜索语义模型、广告 CTR 模型），可借鉴「identity ablation + 容斥」定位真正产生联合计算的层组，优先保留高
  coordination 的层组，而不是仅按深度均匀减层。

  - 论文的 write-relative connected coordination 可作为一种离线可计算的层重要性信号，用于指导 layer dropout
  / early exit 的层选择；在 Amber 等模型上 similarity 和 coordination 不一致，说明压缩策略需按模型族验证。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：Transformer 深度扩展有效，但层数只提供串行计算机会；模型可能训练成近乎独立的逐层修正，缺少跨层组合依赖。为判断“功能深度”是否真正被学习，需要把只有特定层组合联合才产生的计算分离出来。

**方法关键点**：论文提出精确的 inclusion–exclusion 分解，结合 identity ablation 隔离“connected component”——即指定层集共同作用才出现的计算。在 Pythia、OLMo、Amber 的公开 checkpoint 上跟踪不同交互阶数，并以 write-relative connected coordination 作为度量。

**关键结果**：随预训练进行，connected coordination 在所有测量阶数上均加强；删除 connected component 对 perplexity 的损害高于同位置 norm-matched 随机方向，覆盖 35 个模型-阶数单元；在 7 个模型上层间表示相似度与 connected coordination 持续负相关，但二者不可互换，基于相似度和基于 coordination 的 block 移除在 Pythia 常一致，在 Amber 上分歧。结论是深度提供机会，预训练逐步组织跨层依赖。
