---
title: 'SPIRAL: Learning to Search and Aggregate'
title_zh: SPIRAL：序列-并行-聚合强化学习统一推理计算扩展框架
authors:
- Jubayer Ibn Hamid
- Ifdita Hasan Orney
- Michael Y. Li
- Omar Shaikh
- Yoonho Lee
- Dorsa Sadigh
- Chelsea Finn
- Noah Goodman
affiliations:
- Stanford University
arxiv_id: '2606.23595'
url: https://arxiv.org/abs/2606.23595
pdf_url: https://arxiv.org/pdf/2606.23595
published: '2026-06-22'
collected: '2026-06-23'
category: Reasoning
direction: 推理计算扩展 · 序列-并行-聚合训练
tags:
- RLHF
- inference-time scaling
- parallel reasoning
- set RL
- aggregation
- test-time compute
one_liner: SPIRAL端到端训练语言模型同时进行并行多条推理链采样与聚合，实现推理计算扩展效率大幅提升
practical_value: '- **并行推理链聚合**：在推荐解释、Agent规划等需要深度推理的任务中，可借鉴SPIRAL并行采样多条候选路径再聚合的思路，用较小模型获得更优输出

  - **Set RL训练方法**：训练模型生成一组多样且互补的推理链，直接优化集合对最终聚合结果的贡献，可用于对话策略学习、多臂老虎机创意优选等场景

  - **推理计算扩展效率**：相比单纯增加单条链长度，并行+聚合可线性提升性能，适合电商场景中控制延迟的同时提高推理质量

  - **端到端联合优化**：将搜索（生成多条路径）与聚合一起训练，避免分阶段调优的不一致，可直接用于训练Agentic Search系统'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：现有测试时扩展仅放大单条推理链的串行计算，模型常将计算预算浪费在琐碎步骤上，面对复杂推理任务性能停滞。需要同时利用并行轨迹采样与聚合来更高效地利用推理计算。

**方法**：提出SPIRAL框架，在训练阶段让模型学习三种原语：生成多条并行推理链（搜索）、每条链内串行推理、基于所有链聚合生成最终答案。使用集合强化学习（set RL）训练搜索策略，使生成的轨迹集合对聚合器最有用；使用标准RL训练聚合器，使最终输出质量最优。整个系统端到端联合优化，奖励信号来自最终聚合答案的准确性。

**结果**：在多个推理任务上，SPIRAL显著优于仅扩展串行推理的GRPO方法，推理计算扩展效率最高提升11倍，在同时扩展三种原语时绝对性能高15%。
