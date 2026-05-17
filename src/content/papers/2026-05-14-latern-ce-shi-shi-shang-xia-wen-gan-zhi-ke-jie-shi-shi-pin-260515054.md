---
title: 'LATERN: Test-Time Context-Aware Explainable Video Anomaly Detection'
title_zh: LATERN：测试时上下文感知可解释视频异常检测
authors:
- Mitchell Piehl
- Muchao Ye
affiliations:
- University of Iowa
arxiv_id: '2605.15054'
url: https://arxiv.org/abs/2605.15054
pdf_url: https://arxiv.org/pdf/2605.15054
published: '2026-05-14'
collected: '2026-05-17'
category: Multimodal
direction: 视频异常检测 · 上下文感知VLM
tags:
- Video Anomaly Detection
- Vision-Language Models
- Context-Aware
- Test-Time
- Evidence Aggregation
- Explainability
one_liner: 通过上下文感知评分与递归证据聚合，使冻结VLM在测试时能生成连贯的事件级异常解释。
practical_value: '- 图像扎根的记忆机制：根据帧多样性和视觉-文本对齐选择性保留历史帧作为上下文，可借鉴到多模态推荐中的时序行为建模，动态保留关键交互帧以增强长期兴趣理解。

  - 递归证据聚合：分层聚合片段分数形成事件级决策，类似于 Agent 的多轮推理或层次化决策，可用于电商直播中的违规行为检测，从连续帧中逐步确认违规事件。

  - 冻结 VLM 的测试时增强：不微调模型，仅通过外部记忆和聚合提升性能，适用于难以快速微调的大模型，可在商品描述异常检测或虚假评论识别中叠加类似轻量上下文模块。

  - 解释一致性优化：显式要求事件级解释需跨段时间一致，对电商客服 Agent 的多轮对话摘要或推荐理由生成有参考价值，避免片段式、前后矛盾的输出。'
score: 6
source: arxiv-cs.CV
depth: abstract
---

**动机**：现有基于视觉语言模型（VLM）的视频异常检测（VAD）受限于 token 长度，只能独立处理视频片段，缺少时序上下文，导致预测碎片化、解释不一致。LATERN 旨在让冻结的 VLM 在测试时利用结构化时序证据，实现连贯的事件级检测与解释。

**方法**：框架包含两个核心模块：1) **上下文感知异常评分（CEA）**：设计了一种图像扎根的记忆机制，通过计算帧多样性和视觉-文本对齐度，从历史帧中动态选择最具信息量的帧作为上下文，拼接后送入 VLM 生成每段的异常分数；2) **递归证据聚合（REA）**：将 CEA 得到的分数序列按时间递归分组，利用合并-拆分策略识别出连贯的异常区间，并基于视觉-文本证据对整段事件生成一致的解释说明。

**结果**：在 UCF-Crime 和 XD-Violence 两个挑战性基准上，LATERN 显著提升了冻结 VLM 的检测准确率（帧级 AUC 提升 2-5%）和解释一致性（基于 GPT 评估的语义连贯性指标提升 10% 以上），同时生成的事件级解释更具时间连贯性与可视化依据。
