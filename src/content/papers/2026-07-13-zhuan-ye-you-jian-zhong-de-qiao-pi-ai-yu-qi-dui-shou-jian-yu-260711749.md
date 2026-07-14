---
title: 'Playful AI in Professional Email: A Field Experiment on Tone and Recipient
  Engagement'
title_zh: 专业邮件中的俏皮 AI：语气对收件人参与度的现场实验
authors:
- Ziv Ben-Zion
- Teddy Lazebnik
affiliations:
- University of Haifa
- Yale School of Medicine
- Jönköping University
arxiv_id: '2607.11749'
url: https://arxiv.org/abs/2607.11749
pdf_url: https://arxiv.org/pdf/2607.11749
published: '2026-07-13'
collected: '2026-07-14'
category: Other
direction: LLM 辅助沟通效果与中介机制研究
tags:
- LLM
- Email Communication
- Tone
- A-B Testing
- Mediation Analysis
- Emotional Positivity
one_liner: AI改写邮件语气不直接影响打开/回复，而是通过提升情感积极性间接驱动参与行为。
practical_value: '- **Agent/消息推送的语气设计**：情感积极性（emotional positivity）是驱动用户打开和回复的关键中介，俏皮语气相比专业语气更能间接提升参与，推送文案、客服消息可优先做高积极性改写，无需过度追求“专业感”。

  - **A/B 实验的中介分析**：实验若发现 UI/文案变更无直接效果，应检查情感极性等中介变量；本研究的间接效应框架可直接复用，避免误判优化方向。

  - **工程落地**：接入 LLM 改写消息时，可对生成文本做情感极性评分（如 positive score），将评分作为排序或过滤信号，确保推送内容具备足够情绪动能。

  - **行为指标的间接驱动**：打开率和回复率的提升往往不是工具本身带来的，而是工具产出的内容特征所致，监控指标应同时覆盖内容质量和行为结果。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：企业普遍假设用 AI 润色邮件能提升收件人打开和回复，但缺乏真实工作场景下的行为证据，且作用渠道未知。

**方法**：在 6 家公司进行随机交叉现场实验，121 名员工在 3 周内发送邮件时经历三种条件：无 AI 帮助、GPT-5 俏皮语气改写、GPT-5 专业语气改写，共收集 16,880 封邮件的行为数据。用线性混合模型估计语气对情感极性的影响，再用逻辑回归和 Cox 回归检验情感极性对打开、回复和响应时间的预测作用，并做中介分析。

**关键结果**：俏皮改写显著提升邮件的情绪积极性（+0.068，p<0.001），专业改写则降低（-0.041，p<0.001）。但两种 AI 条件对打开率、回复率、响应时间均无直接效应。发件人的情感积极性却强力预测打开（OR=2.05）和回复（OR=3.32，p<0.001），形成显著的间接路径。AI 改写完全通过改变邮件的情感语气来间接影响收件人行为，并无“使用 AI”的直接光环。
