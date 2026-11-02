---
title: 'CRoS: Causality Reward on Scrambled CoTs Improves Accuracy and Reasoning Faithfulness'
title_zh: CRoS：基于打乱思维链顺序的因果奖励提升推理准确性与忠实度
authors:
- Xiao Yu
- Justin Chih-Yao Chen
- Zaid Khan
- Hyunji Lee
- Mohit Bansal
affiliations:
- UNC Chapel Hill
arxiv_id: '2610.42054'
url: https://arxiv.org/abs/2610.42054
pdf_url: https://arxiv.org/pdf/2610.42054
published: '2026-10-30'
collected: '2026-11-02'
category: Training
direction: LLM 推理训练 · 因果奖励设计
tags:
- RLVR
- CoT Causality
- Reasoning Faithfulness
- Reward Design
- LLM Training
one_liner: 用打乱推理步骤顺序而非改变信息内容的因果奖励，缓解结果奖励无法保证 CoT 因果贡献的问题
practical_value: '- 在电商/Agent 场景做 LLM 强化学习时，若只用最终结果正确性做 reward，模型可能产出与答案无关的低质量推理。可借鉴
  CRoS 思路：对生成的多步推理/决策轨迹做**顺序打乱**，观察最终答案是否变化，作为因果性奖励信号。

  - 对搜索推荐里的 query 改写、推荐理由生成、Agent 工具调用轨迹等，可以先按步骤/换行/工具调用边界切分，然后随机 shuffle 几步，让模型重新给答案；若答案对顺序不敏感则说明推理缺乏因果链条，适合作为负样本或扣分项。

  - 相比删除步骤或注入错误，shuffle 不损失信息，能避免模型钻空子生成冗余、低信息量 CoT；在 reward 工程中可优先采用这种**破坏顺序而非内容**的因果性检验方式。

  - 实现成本不高：只需对已有 RLVR 流程增加一次打乱后前向推理和一致性打分，适合作为 LLM-based recommender / Agent 的辅助 reward
  或 offline 过滤指标。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：RLVR 通常只用最终答案正确性作为 reward，无法保证思维链（CoT）对答案有真实因果贡献。现有因果性评估通过删除步骤或注入错误等扰动 CoT，但这些扰动会改变步骤中的信息，导致高因果分可能反映的是对信息变化的敏感度，而不是真实因果性；若直接用作训练奖励，还会让模型生成信息量更低的 CoT，减少探索和自我修正。

**方法关键点**：提出 CRoS，一种只打乱推理步骤顺序、不改变步骤内容的 CoT 因果性指标。具体做法是先切分 CoT 步骤，做随机乱序，再让模型基于乱序 CoT 生成答案；若答案发生变化，说明原 CoT 的步骤顺序对最终结果有因果作用，否则说明推理链缺乏真实因果性。该指标可作为 RL reward 的一部分，训练时鼓励模型生成具有步骤顺序因果性的 CoT。

**关键结果**：在 Reasoning Gym 上，用 Gemma-3-4B 训练后，CRoS 在 5 个未见过的逻辑和游戏数据集上取得 46.8% 准确率，超过最强 baseline 43.8%；CoT 质量方面，CoT-Pass@K 从 K=1 到 128 平均为 43.4%，对比 baseline 41.4%；CoT 忠实度方面，hint acknowledgment 指标为 34.0%，明显高于 baseline 20.2%。
