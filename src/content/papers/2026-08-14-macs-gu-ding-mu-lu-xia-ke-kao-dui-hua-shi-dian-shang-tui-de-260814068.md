---
title: 'MACS: A Hybrid Multi-Agent Framework for Reliable Conversational E-Commerce
  Recommendation'
title_zh: MACS：固定目录下可靠对话式电商推荐的混合多智能体框架
authors:
- Juli Huang
- Hannah Clay
- Sajjad Beygi
- Thomas Sarda
- Negin Golrezaei
- Amin Saberi
affiliations:
- Stanford University
- University of Southern California
- Amazon
- Massachusetts Institute of Technology
arxiv_id: '2608.14068'
url: https://arxiv.org/abs/2608.14068
pdf_url: https://arxiv.org/pdf/2608.14068
published: '2026-08-14'
collected: '2026-08-17'
category: MultiAgent
direction: 多智能体对话式推荐 · 硬约束确定性执行
tags:
- Conversational Recommendation
- Multi-Agent
- Constraint Enforcement
- E-commerce
- Knowledge Graph
- Session State
one_liner: 混合 shopping/merchant 双 agent 架构，用确定性 SQL 约束与跨轮 slot 状态实现最高约束合规与零漂移
practical_value: '- 架构分离防幻觉：LLM 只做语言交互与偏好抽取，产品检索、SQL 过滤、品牌排除、价格/规格硬约束全部由 merchant
  agent 确定性执行，shopping agent 不直接碰 catalog。这个可以直接迁移到电商 agent 或对话推荐系统，确保不返回目录外商品、不违反品牌排除。

  - Session-persistent slot dictionary：把预算、排除品牌、最低规格作为 typed slot 跨轮持久化，支持覆盖（预算更新）与反转（“HP
  也可以”），并直接映射到 SQL WHERE；比靠 prompt 记忆可靠得多，适合多轮导购场景。

  - 渐进放松 + 显式披露：当硬约束结果 <3 个时，按优先级放松可选规格，但价格上限与品牌排除永不放松；回复中明确告知用户放松了哪些约束。这样既能保证有结果，又不误导用户，对电商推荐体验重要。

  - 评估拆分为确定性约束检查 + LLM 文本质量评分：约束用 SQL 验证、品牌用 regex 验证，文本质量用 G-Eval；避免 LLM-as-judge
  循环。业务上可以复用这种混合评估框架，快速定位是约束违规还是表达质量差。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

动机：在固定目录、禁止 web 搜索的电商对话推荐中，LLM 会幻觉产品规格、跨轮忘记品牌排除、预算过滤不一致，可靠性成为核心痛点。现有 prompt-only 方法无法保证硬约束执行。

方法关键点：
- 混合双 agent 架构：shopping agent（LLM）负责自然语言理解、意图路由、偏好抽取与回复生成；merchant agent 以确定性方式执行产品检索、SQL 硬约束过滤、品牌排除、渐进放松和知识图谱遍历。
- 通过 UCP/ACP/MCP 结构化协议通信，shopping agent 不得直接访问 catalog，从架构层杜绝目录外产品。
- Session-persistent slot dictionary：跨轮累积预算、排除品牌、最低规格等硬约束，支持预算覆盖与排除反转；品牌排除在 SQL 与后检索标题过滤器双重执行。
- 结果 <3 个时渐进放松可选规格，但价格上限与品牌排除永不放松，并显式披露放松内容。
- 知识图谱 Similar_To / Compatible_With 支持替代品与兼容配件查询，Cypher 遍历约 17ms，可审计；缓存层命中时约 12x 延迟降低。

关键实验：
- 单轮 140 query：MACS pass rate 87.1%，brand compliance 1.000，filter compliance 0.970；GPT+Catalog 72.1%，Gemini+Catalog 68.6%，响应质量接近。
- 多轮 10 场景：macro Pass@5 MACS 72% vs GPT 56% vs Gemini 52%；drift 0.000；排除反转 100% vs 20% vs 0%；约束累积 100% vs 60% vs 40%。
- Ablation：移除 session state 使多轮 Pass@5 从 72% 降到 52%；移除 SQL 约束使品牌合规从 1.000 降到 0.684。

最值得记住的一句话：将 LLM 的语言交互与确定性约束执行解耦，并让硬约束在会话中持久化，是固定目录对话推荐可靠性的关键。
