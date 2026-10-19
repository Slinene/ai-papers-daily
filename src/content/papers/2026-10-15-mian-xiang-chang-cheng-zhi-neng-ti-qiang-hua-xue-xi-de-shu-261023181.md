---
title: Tree-Aware Posterior Distillation for Long-Horizon Agentic Reinforcement Learning
title_zh: 面向长程智能体强化学习的树感知后验蒸馏
authors:
- Heming Zou
- Qi Wang
- Yixiu Mao
- Yun Qu
- Yuyi Guo
- Zeyuan Liu
- Chenglin Li
- Weijie Liu
- Saiyong Yang
- Xiangyang Ji
affiliations:
- Tsinghua University
- Tencent
arxiv_id: '2610.23181'
url: https://arxiv.org/abs/2610.23181
pdf_url: https://arxiv.org/pdf/2610.23181
published: '2026-10-15'
collected: '2026-10-19'
category: Training
direction: Agentic RL · 树回溯信用与后验蒸馏
tags:
- RLVR
- Agentic RL
- Tree Search
- Posterior Distillation
- Credit Assignment
- Off-Policy Correction
one_liner: 提出 TreeOPSD，用树回溯信用构建有限目标分布，以 Forward-KL 后验蒸馏替代固定策略梯度，无 critic 地稳定长程 Agent
  RL
practical_value: '- **多轮 Agent 训练的 rollout 预算优化**：initialize-then-expand 用 M 条完整轨迹
  + 每个轨迹 N 个前缀分支，在同样 token/工具调用预算下（M=4, N=2 约等于 8 条全 rollout）构造 rollout tree，获得 turn-level
  信用；电商导购、售后客服等长程 agent 可直接用这种采样方式，不用改 reward 标注。

  - **用有限目标替代固定 advantage 权重，缓解 sequential mini-batch 漂移**：把每轮信用映射成伯努利教师 q=1/2+V/τ，再用
  Forward-KL 匹配当前 policy 的 sigmoid 后验 p=σ(avg log ratio)；梯度会自动在目标处消失、过冲后反向，可以避免多轮更新中的
  policy staleness，适合在线更新频率高的推荐策略。

  - **点式 credit 比 listwise centering 更适合多臂/多子节点场景**：分支后的父节点下多个有用子节点都应上升，listwise 的
  V_c - V_i 会让它们互相抵消；在推荐/搜索的候选生成、多工具调用分支中，可以考虑把树 backup 后的 pointwise credit 直接作为监督信号。

  - **长序列 off-policy 更新的数值稳定 trick**：用 per-token 平均 log-likelihood ratio 构造 p=sigmoid(s)，避免整条
  turn 的 likelihood ratio 指数爆炸；这个做法可复用到长文本/多轮交互的 policy 优化或蒸馏中。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
长程 Agent RLVR 面临两个难题：终端奖励稀疏，导致 turn-level 信用分配高方差；固定 rollout batch 上做多个 sequential mini-batch 更新时，当前 policy 与行为 policy 漂移，policy staleness 难以控制。已有 critic、PRM、on-policy distillation 等方案要么需要价值网络/步骤标注/外部教师，要么仍只提供 ascent 方向而非有限收敛目标。

**方法关键点**
论文提出 TreeOPSD，一个 critic-free 的树感知后验自蒸馏框架：
- 用 initialize-then-expand 构造 rollout tree：行为 policy 先采样 M 条完整轨迹，再对每条轨迹的 N 个 anchor 前缀采样新 suffix；共享前缀合并后，对 K=M(N+1) 个终端奖励标准化，并按 behavior likelihood 递归回溯得到每个 turn 的 credit V_i。
- 目标构造：将 credit 映射为行为相对的伯努利教师 q_i = 1/2 + V_i/τ，目标似然比 r*_i=(τ+2V_i)/(τ-2V_i)；该仿射映射与树回溯可交换，保证父节点目标等于子节点目标的加权平均。
- 分布匹配：学生用 turn 内 per-token 平均 log-likelihood ratio 的 sigmoid 后验 p_θ,i=σ(s_θ,i) 表示；损失为 Forward KL τ D_KL(Q*_i || P_θ,i)，按 turn token 数加权。
- 关键性质：在行为 policy 处，该损失梯度精确恢复 tree policy gradient；后续 mini-batch 中，梯度权重 τ(p-q) 会在目标处消失、过冲后反向，形成有限目标的自纠正更新。

**关键实验**
在 Multi-Hop QA（HotpotQA 训练；2Wiki、MuSiQue、Bamboogle 评估）和 Deep Research（OpenResearcher 训练；BrowseComp-Plus、BrowseComp、GAIA、xbench 评估）上，对比 ReAct、GRPO、GSPO、TreePO。Qwen3-4B：Deep Research Avg 从 GRPO 12.18 / TreePO 13.07 提升到 15.45；Qwen3-30B-A3B：Deep Research Avg 从 GRPO 16.23 / TreePO 17.59 提升到 21.20，相对 GRPO 提高 4.97 点；Multi-Hop QA Avg 也分别提升至 44.13 和 45.93。

**最值得记住的一句话**
把树回溯 credit 变成有限的行为相对目标分布，再用 Forward-KL 匹配——既保留 on-policy 树策略梯度的方向，又给 sequential mini-batch 更新一个会停止和反向的终点，避免固定 advantage 的过冲。
