---
title: 'EDIT: Evidence-Diagnosed Intervention Training for Rule-Faithful LLM Grading'
title_zh: 证据诊断干预训练：实现LLM规则遵循评分的两阶段框架
authors:
- Zhihao Wu
- Linhai Zhang
- Taiyi Wang
- Runcong Zhao
- Peter Andrews
- Cesare Aloisi
- Yulan He
affiliations:
- King’s College London
- University of Cambridge
- AQA
- The Alan Turing Institute
arxiv_id: '2606.06350'
url: https://arxiv.org/abs/2606.06350
pdf_url: https://arxiv.org/pdf/2606.06350
published: '2026-06-04'
collected: '2026-06-05'
category: Training
direction: LLM推理过程诊断与干预训练
tags:
- LLM Grading
- Rubric Faithfulness
- Intervention Training
- Belief-Shaped RL
- Internal-State Diagnostics
- Credit Assignment
one_liner: 通过内部信号诊断推理步骤并局部干预，结合信念引导的奖励塑形，提升LLM评分的规则遵循性
practical_value: '- **内部信号驱动的错误定位**：使用模型对最终评分的 posterior belief 及输入 grounding 分数自动定位推理链中的问题步骤，这种方法可迁移到电商商品审核、合规文案检查等需要多步推理的场景，避免人工标注步骤级错误。

  - **局部干预而非全盘重训**：仅针对诊断出的问题步骤进行修正，且引入 rubric checklist 作为外部知识，可借鉴至需要严格遵循规则的 Agent
  流程，如客服话术合理性判断，只修正违规局部而保留整体流畅性。

  - **信念引导的奖励塑形**：在 RL 阶段通过 belief drift 惩罚有害的信念偏移，同时允许有益探索，这种细粒度的奖励设计可用于训练更可靠的对话
  Agent，防止其偏离原始承诺或规则。

  - **两阶段训练策略可复用到复杂决策**：先通过 SFT 定位并修正错误，再以 RL 校准整体行为，这种组合对电商场景中的多智体协作策略优化（如议价、售后协商）具有参考价值，先纠正局部不合理策略，再全局对齐。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM 自动评分不仅要准确，每个评分步骤必须严格依据评分标准（rubric）和学生答案中的证据。现有方法多针对数学推理等自包含任务，无法定位评分推理中哪一步出错、模型对最终分数的信念如何变化，导致评分缺乏规则遵循性。

**方法**：提出 EDIT 框架，分两阶段训练。第一阶段 EDIT-SFT，利用模型内部信号——对最终分数的 posterior belief 分布和输入 grounding 分数——自动诊断出推理链中的问题步骤，仅对这些步骤进行局部修正，修正时参考 rubric checklist 以保证证据导向。第二阶段 EDIT-RL，以 belief-guided reward shaping 进行强化学习校准，惩罚有害的信念偏移，同时允许能提升正确性的探索。

**结果**：在两个真实多学科评分基准上，EDIT 在域内和域外测试上均稳定超越强 SFT 和 RL 基线，消融实验证实内部状态诊断是性能提升的关键。
