---
title: Auditing Cross-Lingual Fairness in Language Model Watermarking
title_zh: 审计语言模型水印的跨语言公平性
authors:
- Alexander Nemecek
- Osama Zafar
- Debargha Ganguly
- Vikash Singh
- Vipin Chaudhary
- Erman Ayday
affiliations:
- Case Western Reserve University
arxiv_id: '2608.20047'
url: https://arxiv.org/abs/2608.20047
pdf_url: https://arxiv.org/pdf/2608.20047
published: '2026-08-20'
collected: '2026-08-22'
category: Eval
direction: LLM 文本水印跨语言公平性评估
tags:
- watermarking
- cross-lingual fairness
- evaluation framework
- typological disparity
- LLM
one_liner: 提出四组件跨语言评估框架，揭示LLM水印在多语言场景下的结构性公平性差距
practical_value: '- 多语言业务中部署生成式文本水印或检测时，不要沿用英文场景的固定检测阈值；应像论文一样按语言/文字/类型学家族分别做经验校准，否则会因校准失败误判检测能力。

  - 评估生成质量时不要只用一个指标，可以借鉴其三种不重叠范式：分布层（与参考分布距离）、语义配对（同义改写一致性）、参考困惑度，三者分离能暴露单指标掩盖的跨语言质量下降。

  - 跨语言差异可以用广义熵按语言类型学家族分解，区分“家族间结构性差距”和“语言个体噪声”，这适合多语言电商文案、翻译、query 生成等场景做公平性审计。

  - 对多语言生成任务（如广告文案本地化、客服消息）做模型评估时，显式按文字系统/语系分层报告指标，避免平均分掩盖低资源语言或小众文字的失败模式。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：LLM 文本水印的评估几乎只在英文上进行，使用各方案自带的检测阈值和单一质量指标。多语言部署时，英文场景下无关紧要的评估设计选择会直接改变跨语言结论。

**方法关键点**：提出四组件评估框架：
1. 检测阈值按部署上下文经验校准；
2. 引入阈值无关的伴随测量，区分“校准失败”与“检测失败”；
3. 三种不重叠的质量测量范式：分布层、配对语义、参考困惑度；
4. 基于语言类型学家族划分，用广义熵分解跨语言差异。

**关键结果**：在 6 种水印方案、3 个开源模型、11 种语言（4 种文字、8 个类型学家族）、基座与指令微调两种模式下，框架揭示了单语言单范式评估无法暴露的失败模式。检测与质量上的差异主要来自类型学家族之间，说明跨语言公平性差距是语言属性的结构性问题，而非特定语言的特异表现。
