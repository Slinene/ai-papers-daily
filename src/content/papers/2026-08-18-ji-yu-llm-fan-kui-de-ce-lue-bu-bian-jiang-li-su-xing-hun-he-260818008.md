---
title: 'Policy-Invariant Reward Shaping from LLM Feedback: A Framework for Hybrid
  RL Agents'
title_zh: 基于 LLM 反馈的策略不变奖励塑形：混合 RL Agent 框架
authors:
- Christophe D. Hounwanou
- John Emeka Eze
- Yaé U. Gaba
affiliations:
- African Institute for Mathematical Sciences, Rwanda
- AI Research and Innovation Nexus for Africa (AIRINA Labs), AI.Technipreneurs, Bénin
- Sefako Makgatho Health Sciences University (SMU), South Africa
- African Center for Advanced Studies (ACAS), Cameroon
arxiv_id: '2608.18008'
url: https://arxiv.org/abs/2608.18008
pdf_url: https://arxiv.org/pdf/2608.18008
published: '2026-08-18'
collected: '2026-08-20'
category: LLM
direction: LLM 反馈的奖励塑形理论保证
tags:
- LLM
- RL
- Reward Shaping
- Hybrid Agent
- Policy Invariance
- Potential-based
one_liner: 证明 LLM 进度分作为有界势函数做奖励塑形不改变最优策略，即使评分不准
practical_value: '- 若在搜索/推荐 Agent 中用 LLM 生成稠密进度奖励（如多跳查询完成度、任务分步得分），建议写成 potential-based
  shaping：`r + γΦ(s'') - Φ(s)`，并把 Φ 限制在有界范围；这样即使 LLM 打分有偏，理论上不会改变真实业务目标下的最优策略，可安全加速训练。

  - LLM 适合做 planner 输出子目标，RL/底层策略负责动作执行；可将 planner 的解析率、子目标覆盖率等指标单独离线评估，避免直接耦合训练导致难调试。

  - 关注 LLM 输出词表与环境动作/oracle 的 mismatch：例如 autocomplete 或 query 改写中，LLM 生成的 action/slot
  值若无法被执行环境解析，会造成虚假失败/奖励污染；需在 parser 层做规范化和映射。

  - 理论保证只适用于 shaping 项，不应替换核心业务奖励（点击、转化、GMV 等），建议仅作为辅助信号引入。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：LLM 与 RL 结合时，LLM 生成的奖励信号通常缺乏理论地位；Text2Reward、Eureka 等 LLM-as-reward 方法可能改变最优策略。
**方法**：将混合 LLM-planner + RL-controller 架构形式化为 Goal-Augmented MDP（GA-MDP）。把 LLM 对每个状态的进度打分作为有界势函数 Φ(s)，形成 Ng-Harada-Russell 奖励塑形项 F(s,s')=γΦ(s')−Φ(s)。证明：无论 LLM 打分在单点有多错误，该塑形项都不改变增广 MDP 的最优策略集合。给出完整推理算法和参考实现；用本地 Qwen-2.5:14b 在 20 个 MiniGrid 任务评估 planner，解析率 100%，真值覆盖率 54.8%；在 MiniGrid-DoorKey-6x6 上做 pipeline 验证，确认框架可运行，并诊断出 Done-oracle 词汇不匹配。
**结果**：理论上提供比一般 LLM-as-reward 更强的策略不变性保证；小型 MDP 数值实验在四种势函数配置（含 20 倍基奖励对抗配置）验证不变性。
