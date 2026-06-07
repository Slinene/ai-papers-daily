---
title: LLMs Can Leak Training Data But Do They Want To? A Propensity-Aware Evaluation
  of Memorization in LLMs
title_zh: LLM会泄露训练数据但这是它们的意愿吗？倾向感知的记忆评估
authors:
- Gianluca Barmina
- Peter Schneider-Kamp
- Lukas Galke Poech
affiliations:
- University of Southern Denmark
arxiv_id: '2606.06286'
url: https://arxiv.org/abs/2606.06286
pdf_url: https://arxiv.org/pdf/2606.06286
published: '2026-06-03'
collected: '2026-06-07'
category: Eval
direction: LLM记忆评估·倾向性度量
tags:
- Memorization
- Propensity
- LLM Safety
- Data Leakage
- Evaluation
one_liner: 提出倾向性感知框架，区分能力与倾向，发现LLM在普通使用下很少主动泄露训练数据。
practical_value: '- **区分能力与倾向性**：评估推荐/Agent系统中生成模型的数据泄露风险时，不应仅依赖前缀攻击等对抗性方法，需引入倾向性度量，模拟真实用户查询场景，避免高估风险。

  - **轻量级溯源管道**：SimpleTrace 利用 infini-gram 快速回溯生成文本至训练语料，可复用于电商搜索或推荐文案的版权/隐私审核，实现
  verbatim/near-verbatim 检测。

  - **持续预训练降低记忆**：DFM Decoder 表明，用新数据持续训练可降低对旧数据的记忆，对于需要定期更新且关注隐私的推荐模型，该结论支持数据滚动训练策略。

  - **双维度审计**：在部署生成式推荐前，应同时报告最坏可提取率与普通倾向性，为合规和风险控制提供更全面视图。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有LLM记忆评估主要依赖对抗性攻击（如前缀攻击），测量的是模型被强制提取训练数据的能力，而非正常使用下的自发泄露倾向，导致对实际风险的误判。

**方法**：提出 PropMe 框架，通过度量转换将现有记忆度量改造为倾向性度量，区分“能力”与“倾向”。引入 SimpleTrace，基于 infini-gram 的轻量级管道，将模型生成内容归因到大规模训练语料，计算 verbatim、near-verbatim 及倾向性转换后的记忆分数。实验在两个完全开放的模型（Comma 与 DFM Decoder，后者由 Comma 持续预训练得来）和两个数据集（Common Pile、Dynaword，涵盖两种语言）上进行，对比前缀攻击、通用提示和数据集特定提示下的记忆表现。

**关键结果**：前缀攻击激发的记忆信号显著强于通用或数据集特定提示，倾向性得分始终处于低位。DFM Decoder 对 Common Pile 的记忆显著低于 Comma，证明持续预训练若侧重不同数据，可降低对旧数据的记忆。研究建议记忆审计应同时报告最坏情况可提取性和正常使用倾向性。
