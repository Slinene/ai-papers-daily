---
title: Reinforcement Learning without Ground-Truth Solutions can Improve LLMs
title_zh: 无需标准答案的强化学习提升LLM性能
authors:
- Yingyu Lin
- Qiyue Gao
- Nikki Lijing Kuang
- Xunpeng Huang
- Kun Zhou
- Tongtong Liang
- Zhewei Yao
- Yi-An Ma
- Yuxiong He
affiliations:
- University of California, San Diego
- Snowflake AI Research
arxiv_id: '2606.27369'
url: https://arxiv.org/abs/2606.27369
pdf_url: https://arxiv.org/pdf/2606.27369
published: '2026-06-25'
collected: '2026-06-27'
category: Training
direction: 无真值答案的RL训练 · 校准奖励
tags:
- RLVR
- reward_calibration
- score-based_optimization
- LLM_training
- group-relative_RL
- RiVER
one_liner: 通过排名诱导的可验证奖励框架，在无真值答案的得分任务上训练LLM并泛化至精确解基准
practical_value: '- 在推荐系统 RL 训练中，若奖励来自用户行为等连续值，不同用户或场景的奖励幅度差异会导致 **scale dominance**，可借鉴
  **实例级归一化** 或 **排名奖励**，而非使用原始绝对分数。

  - 于在线学习或探索场景，频繁出现的次优解可能淹没偶然的高质量样本（**frequency dominance**），可对每个 queries 组内解进行排名，仅对
  **top-k** 赋予显著正奖励，其余给予有界负反馈，稳定策略更新。

  - 利用 **得分型优化任务**（如离线的时长/收益预估）作为辅助训练环境，无需人工标注真值，通过校准的连续奖励提升模型通用能力，可能迁移至生成式推荐中的物品排序或文案生成。

  - 奖励塑造中保留对 **有效但非最优解** 的信息（如温和负奖励或 entropy 奖励），预防模型过度集中，保持探索性，类似推荐中的 diversity 考量。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：现有 RLVR 依赖标准答案（如数学题结果匹配）作为奖励信号，难以应用于无真值的得分型优化任务。本文探索仅用执行得分作为连续监督，训练 LLM 通用推理能力。

**方法关键点**：提出 RiVER 框架，采用确定性执行反馈作为连续奖励，并针对组相对 RL 中的两大挑战进行校准：
- **尺度主导（scale dominance）**：不同测试实例的得分幅度差异扭曲梯度更新。通过实例级比较，将绝对分数转为相对排名奖励，消除尺度影响。
- **频率主导（frequency dominance）**：采样反复出现的次优解可能压过偶然的强解。采用 top-k 强调策略，对排名顶部的解赋予高奖励，对有效但次优的解保留有界反馈。

整体奖励塑造为：对每个实例的采样组内排序，只突出最优解，并对其他合法解给予温和负奖励，维持探索信息。

**关键结果**：在 12 个 AtCoder 启发式竞赛任务上训练后，AID 评估：
- ALE-Bench 评分相对提升：Qwen3-8B 提升 8.9%，GLM-Z1-9B-0414 提升 9.4%。
- 在无真值训练的精确解基准 LiveCodeBench 和 USACO 上也意外提升，绝对平均提升 2.4% 和 3.5%。而用原始执行分数训练的基线仅提升 ALE，无迁移能力。

**结论**：经校准的得分型优化任务可作为通用训练环境，无需标准答案即可提升模型的精确求解能力。
