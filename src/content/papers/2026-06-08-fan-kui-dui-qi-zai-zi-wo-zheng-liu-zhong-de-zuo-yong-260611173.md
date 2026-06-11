---
title: The Role of Feedback Alignment in Self-Distillation
title_zh: 反馈对齐在自我蒸馏中的作用
authors:
- Semih Kara
- Oğuzhan Ersoy
affiliations:
- Gensyn
arxiv_id: '2606.11173'
url: https://arxiv.org/abs/2606.11173
pdf_url: https://arxiv.org/pdf/2606.11173
published: '2026-06-08'
collected: '2026-06-11'
category: Training
direction: LLM自我蒸馏的反馈设计
tags:
- self-distillation
- feedback alignment
- step-aligned critique
- GRPO
- token-level supervision
one_liner: 逐步对齐求解器推理的反馈在自我蒸馏中效果最佳，能精确修正错误并保留正确步骤。
practical_value: '- 在训练多步推理智能体（如对话推荐）时，可生成与模型自身推理轨迹对齐的逐步评语作为自我蒸馏信号，只修正错误步骤，避免正确部分被扰动，相比整体奖励或参考解方式提升更显著。

  - 将细粒度反馈（如每步批评）融入强化学习或蒸馏流程，适用于电商客服、商品推荐解释等需要长推理链的场景；可利用用户反馈或规则自动生成 step-aligned
  critique。

  - 该方法揭示了反馈“结构对齐”的重要性：设计奖励或蒸馏目标时，应尽量与策略自身行为对齐，防止过度纠正。可迁移至 GRPO 等 RL 训练中的优势函数塑形。

  - 在生成式推荐中，若要模型在无辅助信息时仍产出高质量推理，可采用自我蒸馏框架，但注意用逐步对齐的批评替代简单答案奖励，以提升推理稳定性。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：语言模型在额外上下文（如反馈）下表现提升，自我蒸馏旨在让模型脱离该上下文时仍保持增益，但上下文设计尚未被充分探索。

**方法**：使用冻结 critic 提供反馈，训练 solver 进行自我蒸馏。比较三种上下文：二元奖励（GRPO）、参考解、与 solver 推理轨迹逐步对齐的评语（step-aligned critique）。自我蒸馏中，学生仅见问题，自教师见问题+反馈，匹配两者输出分布。

**关键结果**：逐步对齐评语取得最大增益，在 Avg@12 指标上比 GRPO 高 16.11 分，比参考解条件高 5.27 分。逐 token 优势分析表明，逐步对齐反馈仅针对推理失败的 token 施加压力，保留正确步骤；而参考解迫使求解器在每一步改变行为，即使正确部分也被干扰，因为替代解必然在措辞和路径上不同。这表明反馈与求解器推理间的结构对齐是自我蒸馏有效性的关键。
