---
title: 'Democratic ICAI: Debating Our Way to Steering Principles from Preferences'
title_zh: 民主化逆宪政AI：通过辩论从偏好中提炼引导原则
authors:
- Kevin Kingslin
- Anish Natekar
- Ashutosh Ranjan
- Vivek Srivastava
- Savita Bhat
- Shirish Karande
affiliations:
- TCS Research
arxiv_id: '2606.28294'
url: https://arxiv.org/abs/2606.28294
pdf_url: https://arxiv.org/pdf/2606.28294
published: '2026-06-26'
collected: '2026-06-29'
category: MultiAgent
direction: 多角色辩论推导偏好原则
tags:
- Democratic ICAI
- Preference Alignment
- Persona Debate
- Constitutional AI
- Explainability
one_liner: 提出Democratic ICAI，用多角色辩论从偏好对中提取多竞争理由，生成更全面的决策原则
practical_value: '- 借鉴多角色辩论机制，在用户偏好分析时让多个 LLM 代理扮演不同用户画像（如价格敏感、品质优先）进行辩论，挖掘隐式决策因子，用于推荐排序的特征生成或召回策略调试。

  - 在推荐系统的 A/B 实验中，用该方法从行为数据中提取用户决策原则，替代经验性规则，指导模型迭代方向。

  - 生成的决策树法官可解释性强，适合作为推荐系统的可解释模块，为关键推荐结果提供基于原则的推理说明，提升用户信任。

  - 方法虽有前景，但计算开销大，在实时推荐中难以直接应用，可优先用于离线数据集偏好结构分析或策略制定。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：现有偏好对齐方法仅利用对比标签，丢失了人类决策背后的多维推理过程。单次解释（如 ICAI）无法捕捉复杂决策中的细致考量，导致对齐信号片面。

**方法**：提出 **Democratic ICAI**，通过构造多个不同角色的 LLM 代理，对每条偏好对生成相互竞争的理由，并以结构化辩论形式汇总。从这些丰富的信号中，提炼出更清晰、全面的自然语言原则，用于后续决策建模。最终训练两种法官：基于 LLM 的法官和可解释的决策树法官。

**结果**：在创意偏好基准 MuCE-Pref 和 LiTBench 上，该方法在多个任务类别中更忠实地还原了偏好结构，平均预测准确率优于审慎提示和基于原则的基线模型，并且生成的宪法原则更受 LLM 标注者偏好。
