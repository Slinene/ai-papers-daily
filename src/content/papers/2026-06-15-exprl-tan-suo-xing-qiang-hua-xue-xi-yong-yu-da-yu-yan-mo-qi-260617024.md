---
title: 'ExpRL: Exploratory RL for LLM Mid-Training'
title_zh: ExpRL：探索性强化学习用于大语言模型中期训练
authors:
- Violet Xiang
- Amrith Setlur
- Chase Blagden
- Nick Haber
- Aviral Kumar
affiliations:
- Stanford University
- Carnegie Mellon University
- OpenAI
arxiv_id: '2606.17024'
url: https://arxiv.org/abs/2606.17024
pdf_url: https://arxiv.org/pdf/2606.17024
published: '2026-06-15'
collected: '2026-06-16'
category: Training
direction: 强化学习中期训练增强推理覆盖率
tags:
- Reinforcement Learning
- Mid-Training
- LLM Reasoning
- Dense Reward
- Process Reward
- Coverage
one_liner: ExpRL 利用人类解答作为奖励脚手架，通过稠密过程奖励在中期 RL 中提升推理覆盖率，优于 SFT 与稀疏奖励，为后续 RL 提供更好初始化
practical_value: '- 用参考解答构建奖励脚手架，不暴露答案，让 LLM judge 对比过程给出稠密奖励，可自动化利用人工标注数据引导策略探索；在
  Agent 多步决策（如多轮对话、搜索推荐解释）中，用少量理想路径作为参考，通过过程奖励强化有效推理链。

  - 过程级奖励（ExpRL-Process）能对中间步骤反馈，适合长链路任务（如商品推荐中的多步推理），可设计类似 judge 机制对每一步给出信号，提升模型分解与自纠正能力。

  - 中期训练作为 RL 预热：先用 ExpRL 在标注数据上提升覆盖率，再进行稀疏奖励 RL，可提高训练效率和最终性能；适用于推荐系统用用户反馈做 RL 微调前，先获得更好初始策略。

  - 大量人工问答数据可不用于直接模仿，而作为奖励生成源，更充分利用数据；在电商客服、导购场景中，可收集人类对话构建奖励模型，训练更强的交互式 Agent。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：稀疏奖励 RL 提升 LLM 推理的关键在于基模型对解空间的覆盖，通常通过中期训练教授分解、验证等原语来准备，但这依赖人工指定且难覆盖更复杂的策略组合。

**方法**：提出 ExpRL（Exploratory RL），将人类编写的问答数据用作奖励脚手架：参考答案对策略隐藏，仅由 LLM judge 将其与策略生成的推理轨迹对比，给出结果级或过程级稠密奖励。策略从问题文本中采样，judge 依据与参考答案的一致性分配奖励，使 RL 能强化部分进展、有效归约和 productive 推理行为，而不仅仅是最终答案正确性。

**结果**：在困难数学推理任务（如 MATH）上，ExpRL 作为中期训练方法，优于 SFT、稀疏奖励 GRPO 和自蒸馏；ExpRL-Process 进一步超越 ExpRL-Outcome；ExpRL 提供的初始化使后续稀疏奖励 RL 收敛更快、最终性能更高。混合领域实验表明该方法可扩展到数学之外。
