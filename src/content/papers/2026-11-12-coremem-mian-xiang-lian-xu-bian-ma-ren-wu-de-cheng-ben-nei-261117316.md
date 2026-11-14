---
title: 'CoReMem: Cost-Internalizing Memory for Successive Coding Tasks with Prospective
  Valuation'
title_zh: CoReMem：面向连续编码任务的成本内化记忆框架
authors:
- Peiwen Li
- Harshit Verma
- Sophia Zhou
- Haiwen Wang
- Ngoc Bui
- Heng Chang
- Fei Fei
- David van Dijk
- Rex Ying
affiliations:
- Yale University
- Tsinghua University
- Goodvision AI
arxiv_id: '2611.17316'
url: https://arxiv.org/abs/2611.17316
pdf_url: https://arxiv.org/pdf/2611.17316
published: '2026-11-12'
collected: '2026-11-14'
category: Agent
direction: Agent 记忆与成本内化
tags:
- Agent Memory
- Cost-Aware Memory
- Prospective Valuation
- Coding Agent
- LLM Agent
- RL
one_liner: 提出成本内化记忆框架，通过前瞻片段估值与锚点记忆将27B编码Agent解决率从21.0%提至25.7%，步数降17%
practical_value: '- 记忆选择成本内化：在电商Agent（如客服、推荐对话）维护跨会话记忆时，可对候选记忆片段做“未来任务收益 vs 写入/读取成本”的量化评估，只保留高边际价值片段，避免无脑全量存储。

  - 锚点式记忆表示：参考其“仓库位置 + 可执行检查”的锚点设计，在业务Agent中用“关键页面/接口 + 可执行校验规则”作为记忆单元，使记忆可验证、可定位，减少幻觉。

  - On-policy记忆价值训练：用 rollout group 有/无记忆对比来估计记忆价值，并设计 reward 优先解决率、惩罚步数；可迁移到推荐Agent的交互式决策训练，减少
  token 消耗和步数。

  - Provenance-gated credit：对使用记忆提供信息的步骤分配额外价值信用，其余步骤保留 outcome credit；在RL训练中能更精细地强化记忆使用行为，适合电商多轮对话策略优化。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：编码 Agent 在连续任务中需把记忆带到未知后续任务，但写读记忆和利用时机都有成本，难以平衡。

**方法**：CoReMem 提出前瞻片段估值，对同一继承仓库状态下，下一任务跑有/无某轨迹片段的对比，筛选紧凑记忆；记忆围绕锚点构建：仓库位置与可执行检查。Actor 适应则在有/无记忆的 rollout 组内估计 on-policy 记忆价值，奖励优先解决率并惩罚成功轨迹步数；Provenance-gated credit 把额外价值项分配给识别为使用记忆锚点的步骤，所有步骤保留 outcome credit。

**结果**：ChainSWE 上 27B actor 解决率从 21.0% 提升到 25.7%，步数减少 17%，总 cache-aware token 减少 11%（含记忆模块调用）。
