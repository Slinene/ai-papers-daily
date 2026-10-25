---
title: 'To Think or Not to Think: Pre-Decisional Reasoning Budgets for Referring Audio-Visual
  Segmentation'
title_zh: 指代音视频分割中基于预决策表征的推理预算控制
authors:
- Haojie Hu
- Senda Chen
- Ying Shen
- Lin Zhang
affiliations:
- Tongji University
- IEIT SYSTEMS (Beijing) Co., Ltd.
arxiv_id: '2610.21613'
url: https://arxiv.org/abs/2610.21613
pdf_url: https://arxiv.org/pdf/2610.21613
published: '2026-10-15'
collected: '2026-10-25'
category: Reasoning
direction: 自适应推理 · 生成前隐状态路由
tags:
- adaptive reasoning
- chain-of-thought
- multimodal
- routing
- overthinking
- linear probe
one_liner: 发现过长思维链对简单查询有害，利用生成前隐状态线性探测路由器省60% token且保留96%性能
practical_value: '- 在 LLM-powered 推荐或 Agent 工作流中，不要默认所有 query 都走长 CoT/多步工具调用：简单 query
  可能因过度推理产生 phrase 或 localization drift。可设计基于模型生成前隐状态（首 token 前的 state）的轻量路由器，判断是否需要深度推理。

  - 用线性探针对内部表征做二分类，比基于文本特征或不确定性 proxy 信号更有效；且只需单次前向，无需额外生成，适合在线低成本决策。

  - 报告的 60% token 减少且保留约 96% always-long 性能，可作为成本-质量 trade-off 的实用参考；对推理成本敏感的电商/广告
  Agent 场景值得尝试类似的 pre-decisional routing。

  - 该工作是 Ref-AVS 任务，未在推荐系统上实验；但思想可迁移到 RAG 是否检索、长上下文是否展开、多步推荐解释生成等自适应推理控制。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

动机：多模态推理系统普遍假设更长 chain-of-thought 能一致提升下游 grounding，但 Ref-AVS 中简单查询可能被过度推理损害，产生“overthinking trap”，表现为 phrase 和 localization drift；真正模糊的查询仍受益于多步推理。

方法关键点：构建反事实 reasoning-budget 标签，采用五折 out-of-fold 评估协议。将自适应推理重新表述为预决策表征问题：在第一个生成 token 之前，generation-onset state 包含线性可解的信息，能预测额外推理是否会改善分割。线性探针对二分类 reasoning need 达到 70.1% 准确率，显著优于纯文本特征和不确定性代理信号。作为路由器，onset-state controller 优于下游置信度路由，并接近 Short-then-Decide，但消耗 token 更少。代理比较显示 onset 表征包含手工特征无法完全恢复的预测信息。

关键结果：复用 onset state 进行轻量单次前向路由，减少自回归 token 消耗 60%，同时保留约 96% 的 always-long 性能。在 R²-AVSBench 上提供成本-质量 trade-off，而非对 always-long 的精度提升。错误分析将有害长推理与 phrase / localization drift 关联，说明在简单查询上跳过不必要推理的收益。
