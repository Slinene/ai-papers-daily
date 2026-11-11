---
title: 'From Counterfactual Edits to Human Narratives: LLM-Driven Interpretations
  for Recommender System Explanations'
title_zh: 从反事实编辑到人类叙事：LLM驱动的推荐系统解释
authors:
- Vojtech Cahlik
- Amir Reza Mohammadi
- Rodrigo Alves
- Pavel Kordik
- Eva Zangerle
affiliations:
- Faculty of Information Technology, Czech Technical University in Prague
- Department of Computer Science, University of Innsbruck
arxiv_id: '2611.13914'
url: https://arxiv.org/abs/2611.13914
pdf_url: https://arxiv.org/pdf/2611.13914
published: '2026-11-10'
collected: '2026-11-11'
category: RecSys
direction: 反事实解释的LLM摘要
tags:
- Counterfactual Explanations
- LLM
- Recommender Systems
- Preference Optimization
- Explainability
- DPO
one_liner: 用LLM将反事实编辑列表提炼成用户可理解的自然语言解释，并通过DPO提升语义正确性
practical_value: '- 电商推荐场景中，可先用CFX生成影响推荐结果的关键行为编辑，再交给LLM总结为自然语言理由（如“因为你最近浏览了户外装备”），替代直接展示编辑列表，降低用户认知负荷。

  - 评估解释质量时，除编辑距离外应同时报告语义与语言质量指标，可基于人类标注数据校准自动评估，避免只追求低编辑数而牺牲可读性。

  - 采用DPO训练轻量LLM作为解释生成器：构建（好解释，差解释）偏好对，优化后小模型也能接近大模型语义质量，适合线上低延迟要求。

  - 注意CFX方法的成功率对最终解释语义影响大，应优先部署成功率高的CFX方法（如ACCENT、SPINRec），否则LLM可能基于无效编辑生成错误偏好模式。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：反事实解释（CFX）能指出哪些历史交互改变会改变推荐，但通常需要大量编辑，产生冗长低层列表，用户难以理解；现有评估侧重编辑数量，忽视可读性与可操作性。方法：引入LLM作为中介，将原始CFX交互编辑列表总结为自然语言解释，描述更高层次的偏好模式；通过偏好优化（如DPO）优化正确性、信息量和语言质量；并使用基于独立人类标注数据校准的指标进行评价。结果：在MovieLens-1M上，跨多个CFX生成器和语言模型，摘要语言质量总体较高；语义指标最强的是高成功率CFX方法（ACCENT、SPINRec）；DPO在几乎所有设置下提升了语义指标。
