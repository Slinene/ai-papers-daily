---
title: 'Before You Say It: Anticipating Verbal Behavior from Longitudinal Everyday
  Conversations with LLMs'
title_zh: 开口之前：利用 LLM 从长期日常对话预测言语行为
authors:
- Yasith Samaradivakara
- Valdemar Danry
- Paul Liang
- Pattie Maes
affiliations:
- Massachusetts Institute of Technology
arxiv_id: '2608.13454'
url: https://arxiv.org/abs/2608.13454
pdf_url: https://arxiv.org/pdf/2608.13454
published: '2026-08-13'
collected: '2026-08-17'
category: LLM
direction: LLM 用户行为预测 · 长期对话
tags:
- LLM
- Behavior Prediction
- Longitudinal Conversations
- User Modeling
- Proactive AI
- Personalization
one_liner: 用 LLM 从 1000+ 小时长期自然对话中预测个人言语行为，探索主动式个性化 AI 可能性
practical_value: '- **可借鉴思路：把长期用户会话/行为序列变成“个人行为预测器”。** 电商/客服场景中的用户对话、点击、订单序列，可用 LLM
  做长期 pattern mining，识别重复的高风险/高价值行为模式（如冲动下单、流失前兆、价格敏感表达），用于早期干预。

  - **工程上可落地为“情境相似度召回 + LLM 预测”**：将当前会话/上下文与用户历史行为模式做相似度匹配，再让 LLM 预测用户下一步意图/反应；输出可作为召回/排序特征，也可作为
  Agent 是否触发主动服务的条件。

  - **面向 Agent 的干预时机与形式**：论文强调“在行为展开前提醒”。业务中可设计 push/文案/优惠券的 just-in-time 触发，但需结合用户访谈结论——用户关心透明度和控制权，主动干预要可解释、可关闭，否则可能引起反感。

  - 业务可借鉴点有限处：论文使用 wearable 采集自然对话，成本高、规模小（14人/1000小时），直接照搬难；但用现有日志替代可降低门槛。'
score: 7
source: arxiv-cs.HC
depth: abstract
---

**动机**：现有交互系统大多只能做短期个性化，难以预测用户在未来情境中的语言/行为反应；这类预测是主动式、前瞻式 AI 的前提。  
**方法关键点**：
- 用可穿戴智能手表采集 14 名参与者超过 1000 小时自然对话，构建纵向数据集；
- 提出基于 LLM 的预测行为模型，从个人长期对话中挖掘行为模式，预测其在特定日常会话情境下可能说的话/反应；
- 用 ground truth 行为评估预测效果，并通过半结构化访谈了解参与者对行为预测的感知及未来行为支持形式的期望。  
**关键结果**：验证了从长期对话数据可以预测特定个人的言语行为，且该预测具有 person-specific 特征；访谈揭示了用户对预测的复杂态度，为上下文感知、主动式、个性化 AI 系统提供了实证基础。
