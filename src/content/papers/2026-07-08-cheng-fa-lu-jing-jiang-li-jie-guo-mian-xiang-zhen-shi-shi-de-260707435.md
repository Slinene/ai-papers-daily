---
title: 'RLVP: Penalize the Path, Reward the Outcome'
title_zh: 惩罚路径，奖励结果：面向真实世界 Agent 的高效在线学习
authors:
- Bojie Li
- Noah Shi
affiliations:
- Pine AI
- University of Washington
arxiv_id: '2607.07435'
url: https://arxiv.org/abs/2607.07435
pdf_url: https://arxiv.org/pdf/2607.07435
published: '2026-07-08'
collected: '2026-07-09'
category: Agent
direction: Agent 路径约束与高效在线学习
tags:
- RLVP
- Path Penalty
- Outcome Reward
- Agent Deployment
- Online Learning
- Constraint Satisfaction
one_liner: 用可验证的路径惩罚补充结果奖励，在极少交互下同时达成高成功率和近零违规
practical_value: '- **将业务规则转化为可验证惩罚**：在面向用户的推荐或客服 Agent 中，把“不频繁打扰”“遵守工作时间”等硬约束定义为一步即可检测的惩罚，与结果奖励叠加训练，可大幅降低违规率。

  - **用惩罚注入方差，提高样本效率**：当多个 episode 的结果全为失败时，仅靠结果奖励的 GRPO 等算法会因组内优势为零而浪费昂贵 rollout；对路径施加惩罚能产生可用的组内方差，使学习信号更密集，在推送策略、搜索对话等在线场景中快速收敛。

  - **避免纯惩罚导致不作为陷阱**：论文总结出四条惩罚设计规则，尤其提到不能只用惩罚而抛弃结果奖励，否则 Agent 会学会“不做任何动作”来逃避惩罚；在推荐
  Agent 中设计负向信号时需保持正向结果激励。

  - **利用路径惩罚提升无违规率可作为业务上线指标**：提出“可部署率（violation-free rate）”指标，可用于评估推荐 Agent 在真实环境中的合规表现，作为上线前的
  hard gate。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：现实世界 Agent（如电话呼叫、工单处理）必须通过昂贵且不可逆的在线交互学习，既要追求任务成功又必须遵守过程约束（如不反复骚扰用户）。传统的从可验证奖励中强化学习（RLVR）只优化最终结果，对中间违规视而不见，且在失败 episode 群组中因缺乏方差而浪费珍贵的学习机会。

**方法**：提出“惩罚路径，奖励结果”（RLVP）。核心洞察：可验证的路径惩罚能提供结果奖励所缺失的组内方差，从而为所有-失败群组提供有效学习信号。具体方法是在 GRPO 等算法中，为路径中违反约束的动作施加可计算的负奖励，同时保留最终结果的正奖励。论文给出了四条惩罚设计原则，尤其警示“不作为陷阱”——若单独使用惩罚，Agent 会学会静止以避免惩罚，必须与结果奖励配合。

**关键结果**：在需要遵守业务规则的任务中，RLVP 将无违规率从纯结果训练的近乎 0% 提升至接近 100%，同时仅需更少的 rollout 次数即可达到高任务成功率。实验证明路径惩罚能稳定注入方差，解决了纯结果奖励在失败群组中优势崩溃的问题。
