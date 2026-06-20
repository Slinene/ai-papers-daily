---
title: 'Beyond Uniform Forgetting: A Study of Sequential Direct Preference Optimization
  Across Preference Settings'
title_zh: 超越均匀遗忘：顺序直接偏好优化的跨设置研究
authors:
- Pranav Bhandari
- Nicolas Fay
- Amitava Datta
- Usman Naseem
- Mehwish Nasim
affiliations:
- University of Western Australia
- Macquarie University
arxiv_id: '2606.19744'
url: https://arxiv.org/abs/2606.19744
pdf_url: https://arxiv.org/pdf/2606.19744
published: '2026-06-18'
collected: '2026-06-20'
category: LLM
direction: 多目标顺序对齐中的遗忘分析
tags:
- Sequential DPO
- Catastrophic Forgetting
- Alignment
- LoRA
- Multi-objective
- Preference Optimization
one_liner: 顺序DPO的遗忘模式非均匀，取决于目标关系、信号强度与训练顺序，可退化、稳定或正迁移
practical_value: '- **多目标顺序微调时的风险意识**：在电商推荐中，若对LLM使用顺序DPO注入多个偏好（如点击率、转化率、多样性），后续目标可能削弱前期偏好，但削弱程度取决于目标间冲突程度。可提前评估目标兼容性，将冲突强的目标并行训练，或把重要目标放在后期。

  - **监控不能只看聚合指标**：像本文一样做 pair-level 和置信度分层的分析，否则整体 win-rate 可能掩盖高置信度样本的退化。在推荐模型中，对关键用户群体的偏好变化应单独追踪。

  - **梯度正交性揭示遗忘并非直接干扰**：文章发现后期更新方向与前期目标近乎正交，说明简单的梯度冲突缓解可能无效。可尝试通过少量回放前期偏好数据或约束表示空间，而不必依赖梯度正交化来防遗忘。

  - **信号强度决定稳定性**：强安全信号容易在后续训练中保持，弱信号易被覆盖。在推荐系统中，重要的底线目标（如安全、品牌安全）应使用强信号优先训练，或增大其损失权重。'
score: 7
source: arxiv-cs.HC
depth: abstract
---

**动机**：语言模型对齐通常需要优化多个行为目标，顺序直接偏好优化（DPO）是一种实用策略，但后续训练是否会均匀遗忘早期偏好尚不明确。本文旨在探究顺序DPO中的遗忘规律是否与目标间关系有关。

**方法**：在四类偏好设置上（分布冲突、多属性交互、强安全信号、兼容响应质量）进行两阶段顺序DPO实验，使用 Llama-3.1-8B-Instruct + LoRA适配器，每阶段后评估所有目标，并固定基模型参考。分析涵盖聚合指标（win-rate）、长度归一化策略边际的 pair-level 变化、四分位数分解，以及梯度/更新向量的余弦相似度诊断。

**关键结果**：
- 遗忘并非均匀发生：部分退化、稳定性、pair-level再分布、甚至正迁移四种模式并存，取决于目标关系、信号强度和顺序。
- Pair-level 分析显示，高置信度样本可能退化也可能改进，聚合指标会掩盖这种异质性。
- 梯度诊断发现，第二阶段梯度与前一目标近乎正交（余弦相似度接近0），直接梯度对立不是遗忘主因。
- 强安全信号在后续训练中保持稳定，弱信号易被覆盖。

**结论**：顺序对齐需考虑目标兼容性和信号强度，不应假设后续训练统一影响前期偏好。
