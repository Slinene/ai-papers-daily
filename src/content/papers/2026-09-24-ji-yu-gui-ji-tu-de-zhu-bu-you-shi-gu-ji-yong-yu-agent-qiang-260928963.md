---
title: 'Back to the Definition: Estimating Step-Level Advantages via Trajectory Graphs
  for Agentic Reinforcement Learning'
title_zh: 基于轨迹图的逐步优势估计用于 Agent 强化学习
authors:
- Xincheng Yao
- Haobo Fu
- Weiming Liu
- Chongyang Zhang
affiliations:
- Shanghai Jiao Tong University
- Tencent AI Platform Department
arxiv_id: '2609.28963'
url: https://arxiv.org/abs/2609.28963
pdf_url: https://arxiv.org/pdf/2609.28963
published: '2026-09-24'
collected: '2026-09-25'
category: Training
direction: Agentic RL 的 step-level 信用分配
tags:
- GRAFT
- step-level advantage
- trajectory graph
- Bellman iteration
- GRPO
- agentic RL
one_liner: 用轨迹图合并多条 rollout，以 Bellman 迭代反传稀疏奖励估计状态价值，得到符合 RL 定义的 step-level advantage
practical_value: '- **无 PRM 的步骤级信用分配**：把同一 prompt 下的多条 rollout 按状态合并成有向图，用终端奖励做 Bellman
  反向迭代估计节点价值，得到 step advantage。适合多轮对话/任务型 agent 只有结局奖励（成功/失败）的场景，不需要额外 step reward
  标注或 critic 模型。

  - **状态 canonicalization 可复用**：对 LLM 生成的中间状态用 exact matching 或 embedding 相似度聚类，解决语义相同但文本不同的问题。电商搜索
  agent、多轮推荐对话中，可以把用户状态和系统动作序列映射为图节点，聚合跨轨迹的相似状态。

  - **Graph GAE + on-state group norm 稳定训练**：用图上的 GAE 加权多跳 TD residual 降低 value estimation
  bias；按同一源节点的出边做 group normalization。这两个 trick 对稀疏奖励下的策略梯度方差控制有直接借鉴价值，可嵌入现有 GRPO
  类训练框架。

  - **步骤级重要性比匹配优势粒度**：GRPO-C 用 step 级（或序列级）geometric mean importance ratio 替代 token
  级分配，避免 response-level advantage 被错误均匀分配给每个 token。若你在做多轮交互的策略优化，建议把 action 定义为“一步回复/一次工具调用”而不是
  token，更新时用步骤级 likelihood ratio。'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

## 动机
GRPO 在单轮任务中的 response-level advantage 估计符合 RL 定义：同一 prompt 下采样多个完整回答，组均值是 V(q) 的无偏估计。但多轮 agent 任务中，把它直接扩展到 step level 会出现系统偏差——同一 step index 的中间状态各不相同，用组归一化估计 V(s_t) 实际上是跨状态聚合动作。结果失败轨迹里有价值的步骤被惩罚，成功轨迹里的冗余/错误步骤被错误奖励。训练 PRM 需要昂贵标注且易 reward hacking，而逐状态补采样 N-1 条 continuation 的 Monte Carlo 方案成本 O(N^2 T) 不可接受。

## 方法关键点
- **轨迹图构建**：将同一 prompt 的 N 条 rollout 合并为有向图，节点是 canonicalized state，边是执行的动作。状态 canonicalization 支持 exact matching 和 embedding similarity（cosine > τ）两种模式。终端状态作为 sink node 赋 outcome reward（0/1）。
- **Bellman 迭代估计节点价值**：对非 sink 节点按 action-level 聚合方程 V(u) = Σ_a π(a|u) Σ_v P(v|u,a)·γV(v) 做 Gauss-Seidel 迭代，reverse-BFS 排序加速收敛。稀疏奖励下该过程是标准 value function 的经验近似。
- **步骤级 advantage**：At = γV(s_{t+1}) - V(s_t)，在确定性转移且中间奖励为 0 时严格等于 A(s,a)=Q(s,a)-V(s)。
- **Graph GAE**：对每个 transition，加上后续 k-hop TD residual 的加权和，λ 控制 bias-variance trade-off，降低状态价值估计偏差影响。
- **On-state group norm + GRPO-C**：按同一源节点的出边做 advantage 归一化；用 step 级 importance ratio（geometric mean）替代 token 级分配，使优化粒度与 advantage 一致。

## 实验结果
在 ALFWorld、WebShop、SearchQA 三个多轮 agent 基准上，基于 Qwen2.5-1.5B/3B/7B 训练。ALFWorld 上 1.5B 和 7B 相比 GRPO 平均成功率分别提升 24.6% 和 20.8%；WebShop 成功率提升 25.5% 和 16.7%。同时超过 GiGPO 和 GraphGPO：ALFWorld 高 10.7%/17.3%，WebShop 高 4.7%/3.6%。SearchQA 上 7B 平均成功率 48.6%，优于 Search-R1、StepSearch、GiGPO、GraphGPO。额外开销仅占训练时间 0.43%，无额外 GPU 内存。Ablation 显示 advantage normalization 和 Graph GAE 对最终性能至关重要，去掉 normalization 后 ALFWorld 成功率从 96.10 掉到 71.33。

## 最值得记住的一句话
把 rollout 轨迹接成图，用 Bellman 迭代从稀疏终端奖励反推出每个状态的价值，再做一步 TD residual，就能在不需要 PRM 的情况下得到理论忠实的步骤级信用分配。
