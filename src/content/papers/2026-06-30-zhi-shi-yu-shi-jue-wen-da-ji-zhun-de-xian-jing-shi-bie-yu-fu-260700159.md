---
title: 'Identifying and Resolving Pitfalls of Knowledge-Based VQA Benchmarks: Auditing,
  Repairing, and Augmenting'
title_zh: 知识与视觉问答基准的陷阱识别与修复：审计、修正与增强
authors:
- Qian Ma
- S M Rayeed
- Charles V. Stewart
- Qiong Wu
- Yao Ma
affiliations:
- Rensselaer Polytechnic Institute
- AT&T Chief Data Office
arxiv_id: '2607.00159'
url: https://arxiv.org/abs/2607.00159
pdf_url: https://arxiv.org/pdf/2607.00159
published: '2026-06-30'
collected: '2026-07-06'
category: Eval
direction: 知识增强多模态评测审计与修正
tags:
- KB-VQA
- Evaluation
- Benchmark Auditing
- Retrieval-Augmented
- Vision-Language Model
- Robustness
one_liner: 系统审计KB-VQA基准，揭示答案可推导性、问题约束和视觉设定上的缺陷，并引入修复与多实体增强协议，纠正模型评价偏差。
practical_value: '- 在电商多模态知识增强场景（如商品问答、属性校验）中，应审计知识库覆盖率与答案可推导性，避免模型利用图像或语言捷径获得高准确率。

  - 引入多实体同框的视觉歧义样本（如多商品对比图），迫使模型执行显式的视觉-知识对齐，而非简单匹配单个显著实体。

  - 评估指标不能仅依赖端到端答案匹配，需设计中间过程验证（如检索证据、推理步骤）来衡量真实推理能力，模仿“审计-修复”流程。

  - 构建知识增强推荐或Agent时，用受控的困难样本集进行诊断测试，发现模型在通道、推理上的薄弱环节。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

动机：现有 KB-VQA 基准将答案准确率作为知识推理的代理指标，却忽略了三个关键假设：答案必须能从关联知识库推导；问题必须约束充分；视觉场景需有歧义，迫使模型依赖知识进行消歧。这些假设常被违反，导致评估失真。

方法：对多个流行基准进行系统审计，发现大量实例存在答案缺失/矛盾、问题欠指定（如图中多个同类实体），且视觉场景多为单一实体，过于简单。在此基础上提出审计-修复协议：自动/半自动补全知识库缺失、修正矛盾答案、限制问题约束；并设计受控多实体增强协议，通过插入同类实体增加视觉歧义，迫使其先检索再推理。

结果：修复和增强后重新评估，模型排名发生显著变化，原先的高分模型推理能力被高估。例如部分模型在简单原版上准确率高，但在增强集上大幅下降，暴露出视觉-知识绑定能力的不足。结论呼吁构建交互感知、重视可验证推理的新一代 KB-VQA 基准。
