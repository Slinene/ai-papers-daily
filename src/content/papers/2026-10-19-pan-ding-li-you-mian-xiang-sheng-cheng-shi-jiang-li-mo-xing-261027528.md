---
title: 'Judging the Justification: Decision Certificate Supervision for Generative
  Reward Models'
title_zh: 判定理由：面向生成式奖励模型的决策证书监督
authors:
- Guiquan Sun
- Bing Bai
- Martin Renqiang Min
- Dongjin Song
affiliations:
- University of Connecticut
- NEC Labs America
arxiv_id: '2610.27528'
url: https://arxiv.org/abs/2610.27528
pdf_url: https://arxiv.org/pdf/2610.27528
published: '2026-10-19'
collected: '2026-10-27'
category: Training
direction: 生成式奖励模型训练与理由质量监督
tags:
- Generative Reward Models
- Decision Certificate
- Preference Optimization
- Rationale Supervision
- Positional Bias
- LLM Judge
one_liner: 提出 DeCert 框架，用决策证书评估 rationale 有效性与一致性，构造偏好对训练生成式奖励模型
practical_value: '- 在电商/广告中若用 LLM 生成推荐理由或广告解释，不要仅用最终点击/转化标签微调，可采样多个解释，用自动设计的 certificate（validity
  + verdict consistency）打分，构造偏好对进行 DPO 训练，让模型区分解释质量。

  - 无需人工标注 rationale 参考，节省成本；可对线上 LLM-as-a-judge 的评估结果自动构造 rationale 偏好数据，提升判断一致性。

  - DeCert 显著缓解 position bias，可将训练后的 judge 用于搜索结果、推荐列表的 pairwise 评估，减少位置对判断的干扰，提升评估可信度。

  - 对于生成式推荐（如直接生成商品描述/推荐理由），可将 verdict 正确性与 justification 质量解耦监督，避免“蒙对结论但给错理由”，提高用户信任和转化。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机：** 生成式奖励模型（GenRMs）生成自然语言 rationale 来支持偏好判断，但正确 verdict 不保证 justification 合理。现有工作常依赖参考解释监督 rationale，获取成本高且未直接保证 rationale 支持 verdict。需一种无需参考解释即可监督 rationale 质量的方法。

**方法关键点：** 提出 DeCert（Decision-Certificate Supervision）。核心是自动评估生成 rationale 的 validity（有效性）和 verdict consistency（与最终判断一致性），生成决策证书。利用证书评估结果构造偏好监督：当多个采样判断共享相同正确 verdict 时，依据证书质量差异构造 rationale 偏好对，区分更强与更弱的 justification。该偏好信号同时考虑 verdict 正确性和 justification 质量，可结合偏好优化训练 GenRM。

**结果：** 在两个模型家族、多个 in/out-of-distribution benchmark 上，DeCert 持续优于强生成式 judge 基线，且提升 rationale 质量；有效缓解位置偏见，position-consistent accuracy 最高提升 14.8 个百分点。表明监督“如何判断”与“判断是否正确”同样重要。
