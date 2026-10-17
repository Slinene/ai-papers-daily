---
title: Disagreement-Guided Weak-to-Strong Routing
title_zh: 分歧引导的弱到强路由
authors:
- Sima Noorani
- Shayan Kiyani
- George Pappas
- Hamed Hassani
affiliations:
- University of Pennsylvania
arxiv_id: '2610.22245'
url: https://arxiv.org/abs/2610.22245
pdf_url: https://arxiv.org/pdf/2610.22245
published: '2026-10-15'
collected: '2026-10-17'
category: Agent
direction: 弱模型到强模型路由 · 无监督分歧信号
tags:
- weak-to-strong routing
- disagreement signal
- LLM inference
- agentic tasks
- model routing
one_liner: 提出用模型间分歧信号做无监督弱到强路由，无需正确性标签即可在成本与准确率间权衡
practical_value: '- 在电商搜索推荐或 Agent 工作流中，小模型常用于低延迟生成 query 改写、推荐理由或工具调用；当输出不确定时需路由到大模型。可直接借鉴：让弱模型生成多个候选（如采样多个
  query/理由），再用强模型对候选打分或比较，弱模型候选分布与强模型偏好分歧大则路由，避免依赖用户反馈或人工标注。

  - 多候选 + 分歧路由可作为默认路由信号：比较弱模型自身多个响应与强模型判断的一致性，无需训练正确性预测器，部署简单，特别适合开放域文本生成和 agentic
  任务，能显著降低大模型调用成本。

  - 实验结论表明，即使有 ground-truth 正确性标签可用于训练路由器，基于分歧的路由也能超越直接拟合正确性的方法。因此在业务中可优先采用无监督分歧信号，或将其作为特征加入有监督路由器，提升泛化能力。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

动机：小语言模型部署在边缘设备和机器人系统上受成本延迟约束，但能力有限；需要偶尔路由到强模型。现有路由方法通常依赖响应正确性信号，而在开放域和 agentic 任务中获取正确性监督成本高昂。

方法关键点：重新刻画最优弱到强路由策略，允许多个弱模型响应通过本地推理生成。基于该刻画，推导出基于模型间比较的无监督近似：引入模型分歧（disagreement）概念，直接测量模型生成响应之间的分歧，无需 ground-truth。当强模型越接近 ground-truth 分布，该近似越准确。

结果：在 agentic 和单轮任务上，该方法无需 ground-truth 监督即可有效权衡路由成本与响应准确率；即使有 ground-truth 正确性信号用于训练，基于分歧的路由也能超越直接预测正确性的方法。
