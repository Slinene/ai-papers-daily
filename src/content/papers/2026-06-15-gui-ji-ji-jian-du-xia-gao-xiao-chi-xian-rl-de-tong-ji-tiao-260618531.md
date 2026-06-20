---
title: When Does Trajectory-Level Supervision Permit Efficient Offline Reinforcement
  Learning?
title_zh: 轨迹级监督下高效离线 RL 的统计条件
authors:
- Xuanfei Ren
- Tengyang Xie
affiliations:
- University of Wisconsin-Madison
arxiv_id: '2606.18531'
url: https://arxiv.org/abs/2606.18531
pdf_url: https://arxiv.org/pdf/2606.18531
published: '2026-06-15'
collected: '2026-06-20'
category: Other
direction: 离线强化学习 · 轨迹级反馈理论
tags:
- offline RL
- trajectory-level supervision
- pessimism
- sample complexity
- reward learning
- preference feedback
one_liner: 提出 OPAC 算法，证明仅用轨迹级标量标签可实现样本高效离线策略优化，并刻画泛化结果监督的可处理条件
practical_value: '- 在序列推荐或对话 Agent 中，若只有会话结束时的整体转化/点击等标量标签，可借鉴 OPAC 的悲观演员-评论家框架：先学习潜在步奖励模型，再用悲观值函数优化策略，避免盲目分配奖励导致的分布偏移恶化。

  - 论文定义的泛化结果监督场景（如偏好、全成功目标）与推荐系统从会话级指标（如转化率、净推荐值）逆向学习策略高度对应，可通过结构系数 κ_μ(σ) 和 χ_μ(σ)
  评估任务的信息损失，指导选择可处理的奖励聚合形式。

  - 离线策略优化的悲观原则（Pessimism）在业务中已有应用，本文的理论保证（O(H^2√(C_sa/n))）为使用轨迹级反馈替代过程奖励提供了样本复杂度的量化依据，可在实验设计时预估所需数据量。

  - 当结果标签与优化目标不一致时（如用点击率作为代理目标学习收益最大的策略），警惕指数级样本需求（Ω(2^H)）的陷阱，需通过线性近似或引入过程信号避免不可学习问题。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：离线 RL 通常要求过程级奖励，但许多顺序决策数据仅记录轨迹级标量结果（如总回报、偏好）。从这类弱监督中离线学习策略的理论依据尚不明确。  
**方法关键点**：1) 基本设定：目标仍为期望累积奖励，但每条轨迹只给标量标签，其条件均值为总回报。提出 OPAC（Pessimistic Actor-Critic），先学潜在奖励模型，再用悲观值函数进行策略优化。2) 理论保证：证明高概率界 ˜O(H^2√(C_{sa}(π^⋆)/n))，并给出匹配下界，刻画了用单个轨迹级标签替代过程奖励的统计代价。3) 扩展：将结果应用于偏好反馈，保持领头阶项和 concentrability 依赖，仅增加偏好模型常数。4) 泛化结果监督：目标和监督都是轨迹级非线性聚合量。指出一般不可学习（全成功目标下需 Ω(2^H) 轨迹），然后通过结构系数 κ_μ(σ) 和 χ_μ(σ) 量化信息损失，在其有界时广义 OPAC 达到多项式样本复杂度。  
**关键结果**：基本设定下，只要 concentrability 系数 C_{sa} 有限，OPAC 能以 ˜O(H^2/√n) 速率收敛到最优策略；泛化结果下，样本复杂度由 κ 和 χ 控制，否则可指数级恶化。
