---
title: An Explainable Agentic System for Detection of Conversational Scams with Summary-Based
  Memory
title_zh: 基于摘要记忆的可解释 Agent 对话诈骗检测系统
authors:
- Ahmed Omar Salim Adnan
- Yogananda Manjunath
- Shivanjali Khare
affiliations:
- University of New Haven
arxiv_id: '2607.11707'
url: https://arxiv.org/abs/2607.11707
pdf_url: https://arxiv.org/pdf/2607.11707
published: '2026-07-13'
collected: '2026-07-14'
category: Agent
direction: 可解释 Agent · 摘要记忆
tags:
- Agent
- ExplainableAI
- ConversationalScams
- Memory
- Benchmark
- UserStudy
one_liner: 以可解释 Agent 融合单消息与对话级检测，引入摘要记忆跨消息推理，在基准上达 97.8% 准确率
practical_value: '- 摘要式记忆机制可迁移至电商客服 Agent：对长对话压缩关键意图与上下文，避免窗口溢出，提升多轮交互下需求理解和推荐准确性。

  - 可解释性设计：输出检测理由，可借鉴到推荐系统的透明性解释，例如解释为何推荐某商品，增强用户信任。

  - 多阶段检测架构：结合单消息快速判别与对话全局分析，可类比推荐精排-粗排流程，平衡响应延迟与精度。

  - 用户研究评估方法：使用 SUS 量表和前后测对比验证用户信任和接受度，可复用于评估搜索推荐 Agent 的用户体验与 AI 辅助效果。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：传统钓鱼检测仅分析孤立消息，无法应对跨数周逐步建立信任的对话式诈骗。亟需对话级检测范式，同时提供可解释性以辅助用户判断。

**方法关键点**：提出可解释 Agent 系统，由单消息检测器和对话级检测器组成。单消息模型负责逐条消息的快速恶意判别；对话级 Agent 基于摘要记忆逐步累积关键信息，对完整对话进行全局推理，并输出可读的检测理由。此外，构建公开基准 ConScamBench-278，覆盖 8 类诈骗，包含 278 个对话，以支持可重复评估。

**关键结果**：在单消息层面，钓鱼召回率达 100%；对话级检测在 LoveFraud02 语料中检出全部 83 个诈骗对话，在 ConScamBench-278 上准确率 97.8%（95% CI [95.4, 99.0]）。用户研究（N=100, N=45）表明，系统显著提升用户对可疑对话判断的信任度、自信心以及对 AI 检测的需求（p<0.001），SUS 可用性评分 74.7，超过行业基准。
