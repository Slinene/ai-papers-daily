---
title: 'Agon: Competitive Cross-Model RL with Implicit Rival Grading of Reasoning'
title_zh: 'Agon: 竞争式跨模型强化学习，隐式对手评分提升推理能力'
authors:
- Vladislav Beliaev
affiliations:
- Independent Researcher
- thinkdense.ai
arxiv_id: '2607.07690'
url: https://arxiv.org/abs/2607.07690
pdf_url: https://arxiv.org/pdf/2607.07690
published: '2026-07-08'
collected: '2026-07-09'
category: Agent
direction: Agent 竞争训练增强推理
tags:
- Agon
- GRPO
- Competitive RL
- Multi-Agent
- Reasoning
- Self-Improvement
one_liner: 让两个模型互为评分者，通过竞争性RL隐式判断推理质量，无需过程标签，大幅超越GRPO
practical_value: '- 多模型互为评分的训练范式可直接用于对话Agent或推荐解释生成：用一个模型生成，另一个模型评估，交替优化，无需人工标注过程质量。

  - 在搜索推荐场景，可让生成式推荐模型与排序模型互相竞争，前者生成item，后者判断合理性，奖励机制为是否比对方更准，潜在提升推理链的实用价值。

  - 训练时形成的两阶段级联可直接部署：推荐系统可让轻量模型快速草稿再由精排模型修正，兼顾效率与质量。

  - 竞争双方仅需相当实力且行为差异，无需完全对称，启发我们用不同架构或偏好模型进行对抗训练，避免单模型自举的偏差放大。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：现有GRPO等RL方法只评分最终答案，导致模型在难题上倾向堆砌冗长推理而非真正改进思考过程，缺乏对思维链本身的有效反馈。

**方法**：提出Agon，让两个模型解决同一问题，轮流充当草稿者和阅读者。草稿者写出解，阅读者在参考该草稿后作答，奖励基于准确率和速度的相对优势（谁优于对方）。训练时双方交替优化，没有显式的过程标签或奖励模型；对手能力动态提升，形成渐进增强的隐式评分机制。推理时采用训练时形成的两阶段级联。

**结果**：在DeepMath难题集上，基于Qwen3，Agon将GRPO的pass@1翻倍，增益约为未训练MoA方法的8倍；在编程推理和Qwen3.5、Gemma 4等不同模型族上均验证有效。下一步计划探索隐空间交互。
