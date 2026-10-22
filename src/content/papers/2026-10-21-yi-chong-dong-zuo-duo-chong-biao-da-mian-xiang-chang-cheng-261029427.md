---
title: 'One Act, Many Masks: Effect-Marginal Policy Optimization for Long-Horizon
  Agents'
title_zh: 一种动作多种表达：面向长程智能体的效应边际策略优化
authors:
- Shaojin Ma
- Ruitao Wang
- Pengyi Li
- Jie Yang
- Liangyu Chen
- Gangyi Zhao
- Hongyao Tang
- Yan Zheng
- Jianye Hao
affiliations:
- Tianjin University
- Fudan University
- Renmin University of China
arxiv_id: '2610.29427'
url: https://arxiv.org/abs/2610.29427
pdf_url: https://arxiv.org/pdf/2610.29427
published: '2026-10-21'
collected: '2026-10-22'
category: Agent
direction: Agent 强化学习策略优化
tags:
- LLM Agent
- RL
- Credit Assignment
- Policy Optimization
- GRPO
- Long-Horizon
one_liner: 提出 EMPO，对执行等价响应共享长度归一化策略比率，消除信用-更新错位，提升 GRPO/GiGPO 长程任务效果和效率
practical_value: '- 在结构化动作的 Agent 训练里（工具调用、搜索词改写、推荐解释生成），可以把执行等价但文本多样的响应分组成 effect
  cell，共享长度归一化的 likelihood ratio，减少文本措辞差异对策略梯度更新的干扰；GRPO/GiGPO 可直接加这个 ratio sharing，无需额外
  critic/rollout。

  - 长度归一化要保留：跨不同生成长度的响应直接聚合 full-sequence ratio 会让长响应主导 shared ratio；用 exp(1/T Σ log
  r_t) 能校准 token 级尺度和 PPO clip。

  - 与 credit assignment 解耦：EMPO 只用原始 advantage，不在 advantage 侧做聚合，方便叠加 SALT/GraphGPO
  等更精细 credit estimator；clip 下 ratio-sharing 比 advantage-aggregation 更稳，WebShop GiGPO
  提升更明显。

  - 若线上动作空间是自然语言 query/推荐文案，需要先有 canonical effect parser；无结构化 parser 时 coverage 会低，建议先从可枚举
  action 的 agent 场景验证。'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

**动机**
长程 LLM agent RL 中 credit assignment 逐步改进，但 policy update 仍按 response-specific probability ratio。执行等价的不同文本（如不同 reasoning/措辞但相同工具调用）因后续结果被赋予不同 advantage，却保留各自的文本梯度，造成 credit-update misalignment。作者用分解 G_ind = 均值项 + covariance(Advantage, score) 刻画这种错位。

**方法关键点**
- 定义 executable effect e = ψ(c,y)，把同 context、同 canonical effect 的响应建为 effect cell K。
- EMPO 对 cell 内响应计算 token-level ratio r_{i,t}，按长度归一化 q_i = exp(1/T_i Σ log r_{i,t})，并聚合为共享比率 q̄_K。
- 仅将 q̄_K 替换原 token ratio（cell size≥2），advantage 保持原样，无额外 critic/rollout；PPO clip 下仍保留非零更新，区别于 advantage 平均。
- 适用于 GRPO（trajectory-level credit）和 GiGPO（step-level credit）。

**关键结果**
- ALFWorld 上 Qwen2.5-1.5B：EMPO-G 整体 SR 69.5→83.3，EMPO-GiG 90.1→94.0；7B 上总体也提升。
- WebShop 1.5B：EMPO-G 62.8→70.3 SR，EMPO-GiG 73.8→77.3；7B 上 EMPO-GiG 72.1→79.7。
- Sokoban：EMPO-G 72.7→84.4，EMPO-GiG 75.0→81.3。
- TTT60 在 8 个 setting 中均下降，最大减少 36.5%。
- 消融显示 length normalization、ratio sharing、effect-based grouping 三者都关键。

**最值得记住的一句话**：policy update 阶段按 executable effect 而非文本 realization 对齐，是低成本、可叠加的稳定化改进，尤其适合结构化 action 的长程 agent RL。
