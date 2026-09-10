---
title: Revisiting Complete Reasoning Traces for Post-Training
title_zh: 重新审视完整推理轨迹在后训练中的作用
authors:
- Jaehui Hwang
- Sangdoo Yun
- Byeongho Heo
- Dongyoon Han
affiliations:
- NAVER AI Lab
arxiv_id: '2609.07103'
url: https://arxiv.org/abs/2609.07103
pdf_url: https://arxiv.org/pdf/2609.07103
published: '2026-09-06'
collected: '2026-09-10'
category: Training
direction: LLM 推理后训练 · 轨迹截断
tags:
- reasoning traces
- post-training
- SFT
- token redundancy
- RL
- distillation
one_liner: 完整推理轨迹对SFT收益有限，仅用端点训练更高效且可迁移到RL和蒸馏
practical_value: '- 在训练 LLM 生成推荐理由、商品卖点、搜索 query 改写等推理链时，可只保留结论或关键步骤，不必收集完整思维链；中间冗余
  token 会分散学习，截断后模型可借助内部知识补齐缺失步骤。

  - 使用端点（如最终答案/推荐结果）作为 SFT 目标，能提高样本利用效率，降低 token 长度与训练成本，尤其适合大规模商品语料和长推理场景。

  - 对基于 RL 或 on-policy distillation 的 Agent 策略优化，可考虑用部分轨迹或关键状态对替代全轨迹，减少冗余更新和奖励 hacking，保持推理行为稳定。

  - 在构建电商问答/搜索推荐 Agent 的训练数据时，优先定义任务端点和关键中间约束，而非依赖完整长文本；该发现支持用更简洁的监督信号。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM 通常在海量预收集的推理轨迹上进行后训练，以提升推理能力。但这些轨迹往往冗长且包含弯路，目前尚不清楚模型是否真的需要学习完整轨迹。

**方法关键点**：通过 pilot study 发现，完整轨迹对 SFT 收益有限，而部分轨迹甚至在重度截断下仍有效。利用注意力分析和受控 token 删除实验表明，中间 token 对最终推理质量的贡献很小。进一步提出仅使用轨迹端点进行训练，让模型依靠内部知识自行推断缺失步骤，从而避免冗余信息。该方法也可扩展到强化学习（RL）和 on-policy distillation。

**关键结果**：完整轨迹收益有限；部分轨迹或仅端点训练在多种后训练范式下均表现有效，且能稳定改变模型推理行为。
