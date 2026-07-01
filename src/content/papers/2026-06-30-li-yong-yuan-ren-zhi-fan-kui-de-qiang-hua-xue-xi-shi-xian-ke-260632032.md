---
title: Reinforcement Learning with Metacognitive Feedback Elicits Faithful Uncertainty
  Expression in LLMs
title_zh: 利用元认知反馈的强化学习实现 LLM 可信不确定表达
authors:
- Gabrielle Kaili-May Liu
- Avi Caciularu
- Gal Yona
- Idan Szpektor
- Arman Cohan
affiliations:
- Yale University
- Google Research
arxiv_id: '2606.32032'
url: https://arxiv.org/abs/2606.32032
pdf_url: https://arxiv.org/pdf/2606.32032
published: '2026-06-30'
collected: '2026-07-01'
category: Eval
direction: LLM 校准 · 元认知反馈
tags:
- uncertainty calibration
- metacognition
- RLMF
- preference optimization
- active learning
- LLMs
one_liner: 提出 RLMF 范式，以模型自我评判质量作为奖励来优化偏好排序，显著提升 LLM 的不确定度校准与边界认知能力。
practical_value: '- **生成式推荐解释的可信度增强**：在电商搜索推荐中，若 LLM 生成推荐理由或商品评测，可利用 RLMF 校准模型输出的置信度，使语言表达的不确定性（如“可能适合”“强烈推荐”）更符合真实准确率，提升用户信任。

  - **偏好优化的奖励信号设计**：RLMF 将自我评判质量（如校准误差）作为奖励项融入偏好优化，可借鉴到生成式推荐模型的排序对齐中，使模型在生成物品描述、理由选择时具备更好的自我评估与保守表达能力。

  - **高价值训练样本筛选**：元认知数据选择基于模型自我评估挑选高价值样本，可应用于点击率预估、用户意图识别等任务的主动学习流程，减少标注成本并提升样本效率。

  - **两阶段解耦式校准**：先校准数值置信度，再通过编辑映射到自然语言，这种解耦方法可直接用于推荐解释的生成后处理，在不重训模型的情况下提高解释的可靠性。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM 在表达不确定性时常常高自信地犯错、不能识别知识边界，损害可信任度。元认知（监测并调控自身认知）是解决该问题的核心能力。作者希望利用模型对自身表现的判断质量来驱动优化，从而同时提升校准准确度和任务表现。

**方法关键点**：
- 提出 RLMF（强化学习+元认知反馈）范式：在偏好优化过程中，基于模型自我评判质量的奖励来重新排序所生成的答案，使模型内在地倾向于生成更可校准的置信度。
- 提出元认知数据选择：利用自我评估的分数识别高价值训练样本，替代传统主动学习，更高效地提升微调效果。
- 采用两阶段解耦架构：首先用上述方法训练模型输出精确的数字置信度分数（校准阶段）；然后通过目标编辑将分数映射为自然语言的不确定性表达，如“我不确定”“很可能错误”。

**关键结果**：
- RLMF 在多种任务上实现了最先进的置信度校准（FC），且保留了模型准确率。
- 相比标准 RL 方法，RLMF 的校准指标提升高达 63%，并显著增强模型评估和表达自身能力边界的能力。
- 元认知数据选择在所有测试设置中均优于基准主动学习策略。
