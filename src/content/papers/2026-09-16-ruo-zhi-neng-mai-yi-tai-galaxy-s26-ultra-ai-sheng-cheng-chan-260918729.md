---
title: '"If I Had to Buy Just ONE: Galaxy S26 Ultra": Auditing AI-Generated Product
  Recommendations'
title_zh: 若只能买一台 Galaxy S26 Ultra：AI 生成产品推荐审计
authors:
- Lucas G. Uberti-Bona Marin
- Thales Bertaglia
- Giovanni Astante
- Bram Rijsbosch
- Gijs van Dijck
- Anikó Hannák
- Gerasimos Spanakis
- Konrad Kollnig
affiliations:
- Law & Tech Lab, Maastricht University
- Utrecht University
- Social Computing Group, Department of Informatics, University of Zurich
arxiv_id: '2609.18729'
url: https://arxiv.org/abs/2609.18729
pdf_url: https://arxiv.org/pdf/2609.18729
published: '2026-09-16'
collected: '2026-09-17'
category: Eval
direction: LLM 生成式推荐系统审计
tags:
- AI audit
- product recommendation
- LLM
- bias
- source attribution
- ConsumerQ
one_liner: 审计 ChatGPT、Gemini 与 Google AI Overviews 的产品推荐，揭示第一人称偏好、重复不一致和来源差异
practical_value: '- 评估生成式推荐时不能只看单次输出或 API，需模拟消费者端界面并多次重复请求，否则会低估产品推荐变化与来源差异；可引入第一人称偏好率、产品一致性、来源重叠等审计指标。

  - 若在电商中使用 LLM 做商品推荐，注意模型会高频使用「我会选」等主观表述（ChatGPT 达 79%），可能带来偏袒或误导风险；可通过 prompt 约束或后处理抑制第一人称表达，保持中立语气。

  - API 与消费者界面表现差异显著（来源重叠仅 12–15%），说明实验结论不能直接外推到生产环境；若做线上 LLM 推荐，需对实际部署界面和 API 分别做回归测试与监控。

  - 来源展示不稳定且跨模型重叠极低，会增加用户信任与合规风险；建议在推荐结果中显式记录并展示证据来源，建立可追溯链路，便于审计和争议处理。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：消费者越来越多依赖 AI 聊天机器人获取购买建议，而 OpenAI、Google 等通过广告变现，引发对推荐偏见与公正性的担忧。

**方法关键点**：构建 2,528 条真实商业咨询查询数据集 ConsumerQ，评估来自 ChatGPT（聊天机器人/API）、Google Gemini（聊天机器人/API）和 Google Search AI Overviews 的 1,536 条产品查询回复；分析第一人称产品偏好、重复请求间推荐变化、来源展示差异，以及 API 与对应界面的行为差距。

**关键结果数字**：ChatGPT 在 79% 的产品推荐回复中表达第一人称偏好，Gemini 为 7%，AI Overviews 仅 2%；产品推荐在重复请求中经常变化；相同查询下 ChatGPT 与 Gemini 界面平均仅共享 5.4% 域名，76.7% 比较无共同域名；API 与对应界面来源重叠均值分别为 12.0%（ChatGPT）和 14.8%（Gemini），且暴露的信息类型与层次不同。结论：孤立响应或 API 观察不能代表消费者实际遇到的商业建议，独立审计必须考虑重复响应、消费者端条件和来源层差异。
