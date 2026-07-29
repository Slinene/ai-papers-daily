---
title: LLM-as-a-Judge for Evaluating System Responses in Conversational Music Recommendation
title_zh: 对话式音乐推荐中LLM-as-a-Judge评估系统响应可靠性研究
authors:
- Seungheon Doh
- Bruno Sguerra
- Sergio Oramas
- Elena V. Epure
- Juhan Nam
affiliations:
- KAIST
- Deezer Research
- SiriusXM
- Idiap Research Institute
arxiv_id: '2607.25640'
url: https://arxiv.org/abs/2607.25640
pdf_url: https://arxiv.org/pdf/2607.25640
published: '2026-07-28'
collected: '2026-07-29'
category: Eval
direction: 对话推荐系统评估 · LLM-as-a-Judge
tags:
- LLM-as-a-Judge
- Conversational Recommendation
- Human Alignment
- Bootstrapped Correlation
- Evaluation
- Personalization
one_liner: 首次实证验证LLM评判者与人类在对话推荐响应评估中的对齐度，发现中等正相关且优于参考基线
practical_value: '- **低成本自动评估对话推荐响应**：在电商客服Bot或导购Agent中，可直接复用LLM-as-a-Judge方案，从个性化和解释质量两个维度打分，替代昂贵的人工评估。

  - **提升评判可靠性的工程技巧**：使用更大规模的LLM（如GPT-4）并输入完整对话历史，能显著提升与人工评分的相关性。建议在链路上注入用户画像和上下文，而非仅看单轮响应。

  - **评估标准可迁移**：个性化和解释质量这两个维度可直接用于商品推荐的对话评估，只需将评测Prompt中的物品描述替换为商品属性。

  - **相关性分析方法**：Bootstrap相关性分析能稳健衡量评判器与人类的一致性，可作为搭建内部自动评估体系的统计框架。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：对话推荐系统（CRS）在推荐物品的同时需生成自然语言响应，评估响应质量一直是难题。人工评估虽是金标准，但成本高、难以扩展，LLM-as-a-Judge成为潜在代理，但其在CRS场景下与人类判断的一致性尚不明确。

方法关键点：①从20个多轮音乐推荐对话中采样，使用4种指令微调的LLM（如GPT-3.5、GPT-4等）生成不同质量的系统响应；②招募20名领域专家，对每个响应在“个性化质量”和“解释质量”两个维度上打分（共400条）；③采用Bootstrap相关性分析（Spearman、Kendall’s Tau），衡量LLM评判者与人工评分的一致程度，并与基于参考的自动指标对比；④分析评判模型规模和条件信息（如对话历史、用户画像）对表现的影响。

关键结果：LLM评判者与人类评估呈中等正相关（Spearman’s rho约0.6），显著优于BLEU、ROUGE等参考指标。更大的评判模型（GPT-4）和充分的上下文信息带来更高对齐度，为实际部署提供明确指导。
