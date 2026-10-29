---
title: 'Collective Dynamics of Self-Reinforcement: How Cross-Task Coupling Drives
  Policy Collapse in Unsupervised RLVR'
title_zh: 自强化集体动力学：无监督RLVR中跨任务耦合如何驱动策略崩塌
authors:
- Peize Ding
affiliations:
- Columbia University
arxiv_id: '2610.37553'
url: https://arxiv.org/abs/2610.37553
pdf_url: https://arxiv.org/pdf/2610.37553
published: '2026-10-27'
collected: '2026-10-29'
category: Training
direction: RLVR自强化训练崩塌机制
tags:
- RLVR
- policy collapse
- self-reinforcement
- collective dynamics
- majority vote
- LLM training
one_liner: 揭示无监督RLVR多数投票自奖励的集体不稳定性，解释训练任务数增加导致模型答案趋同崩塌
practical_value: '- 在电商/推荐场景用自一致性投票或 LLM 自评做无监督 RLVR 时，跨任务共享参数会导致策略崩塌到统一输出；应按 task
  或 category 拆分 head/梯度，或显式移除共享方向，避免模型对所有 query 给出相同改写/推荐。

  - 任务数越多越容易崩塌。多品类、多目标 RLVR 训练时监控自评 reward 与真实 accuracy 的背离，设置验证集早停；任务规模大时可加大 per-task
  sharpening 的隔离（如 LoRA per task）降低共享耦合 λ。

  - 初始模型置信度低时崩塌风险高。业务冷启动做 RLVR 前先让 LLM 在监督数据上收敛到较自信策略，或用 KL/熵正则项（marginal-entropy
  bonus）稳定 uniform collective mode，防止退化。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：Label-free RLVR 用多数投票自评分数训练语言模型，初期提升 reasoning，但训练任务数增多后自评分数趋近 1、真实准确率下降，甚至对所有问题输出同一答案。论文解释这种 dataset-size 依赖的崩塌来自集体不稳定性。

**方法关键点**：构造多问题共享参数的可解模型，每个问题偏好的答案不同。共享扰动会被放大，只要单问题自强化漂移 F 的群体平均斜率 ⟨F′⟩ 为正（问题仍不确定答案时成立）。单问题锐化速率 ∝1/N，共享模式增长率 ∝λ²（λ 为共享耦合强度），与 N 无关。由此得到临界任务数 N_c≃ln(1/δ)/(λ²G)，δ 为共享模式种子噪声，G 随初始置信度降低。核版本理论还发现保护性耦合（锐化的泛化）和 marginal-entropy bonus 能稳定 uniform collective mode。

**关键结果数字**：随机仿真确认 sharp transition，N_c∝λ^{-2}（带对数修正），统一临界放大系数 λ²NG 跨耦合、置信度分布与训练变体成立，batch size 仅呈对数依赖；高置信初始模型不崩塌。小 Transformer 的 label-free RL 实验中，移除共享方向完全阻止崩塌，恢复共享方向则出现崩塌，且崩塌随训练集规模和 base-model entropy 增大而加剧。
