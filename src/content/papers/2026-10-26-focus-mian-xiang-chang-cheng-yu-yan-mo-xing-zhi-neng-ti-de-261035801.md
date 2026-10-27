---
title: 'FOCUS: Active Critic Learning for Long-Horizon Language Model Agents'
title_zh: FOCUS：面向长程语言模型智能体的主动 Critic 学习
authors:
- Zhengping Jiang
- William Jurayj
- Liaoyaqi Wang
- Chunsheng Zuo
- Anqi Liu
- Benjamin Van Durme
affiliations:
- Johns Hopkins University
arxiv_id: '2610.35801'
url: https://arxiv.org/abs/2610.35801
pdf_url: https://arxiv.org/pdf/2610.35801
published: '2026-10-26'
collected: '2026-10-27'
category: Agent
direction: 长程 Agent 强化学习 · 主动 Critic 学习
tags:
- RLVR
- Long-Horizon Agent
- Active Learning
- Critic
- Rollout Allocation
- Credit Assignment
one_liner: 把中途状态价值细化建模为主动学习：优先在预期最大减小 Critic 估计误差的状态分支采样，并用压缩边界做长程信用分配
practical_value: '- 在电商/搜索的 multi-step Agent（如导购助手、商品搜索 agent、售后 agent）做 RLVR 时，可以把
  context compaction / 工具调用边界作为可恢复状态，计算 segment 级 TD advantage 而不是轨迹级 group advantage；能缓解
  GRPO 训练后期“草率 submit/提前结束”的 collapse。

  - 如果已有 critic/value model，可借鉴 FOCUS 的主动采样公式：用 expected error reduction g(c)=[2κ²b̂e²+(N−κ)σ̂²]/(κ+N)³
  选择从哪些中间状态继续 rollout，避免均匀分支浪费 token；工程上可先在小规模 offline 诊断里验证 critic MSE 与 random/residual
  的差距。

  - 把 critic 预测当作 pseudo-observation 与 rollout 均值按 κ/(κ+n) 融合，递归 bottom-up 备份；这种轻量
  Bayesian blending 比直接用 MC 均值或 raw critic 更稳，适合预算受限的在线分配。

  - 模块化把 rollout allocator、context manager、credit assignment 解耦，便于替换 compaction 协议（in-context
  vs memory workspace）而不影响训练主流程；业务中可先接入现有 session 摘要/记忆模块。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

## 动机
长程 LLM agent 的 RLVR 面临两大困难：单一最终 reward 无法把功劳分到早期动作；学习 critic 能提供中间价值，但 critic 不准，用重复 continuation 采样估计价值又很贵。FOCUS 把“从哪里分支采样 continuation”当作 critic 的主动学习问题。

## 方法关键点
- 以工具调用/上下文压缩（compaction）边界作为可恢复状态，把轨迹切成 step/segment，构造 segment 级 TD advantage 与 critic 训练目标。
- 用 rollout tree 组织轨迹；对每个状态，结合 critic 预测和已采样 continuation 的均值做 posterior 混合：μ_obs = (κv + NḠ)/(κ+N)，并估计 critic MSE。
- 分支预算分配：选择 acquisition function g(c) = [2κ²b̂e² + (N−κ)σ̂²]/(κ+N)³ 最大的状态，即预期边际 MSE 减少最大的状态；支持异步 pending continuation。
- Critic 用递归 backup 的 Ḡ 训练；actor 用每段 TD residual 作为 advantage 做 PPO clip 更新；context management 与 rollout allocation 解耦。

## 关键结果
在 Qwen3.5-9B 上，匹配每步生成预算时：
- BrowseComp-Plus：55.4 vs GRPO 48.2（+7.2）
- DeonticBench overall：56.5 vs 52.4（+4.1）
- LocBench：File@1 72.4 vs 70.1，File@5 81.6 vs 80.5
- 27B 上 DeonticBench 仍领先：76.3 vs 74.3/74.9。
- 训练动态显示 FOCUS 避免 GRPO 后期 tool call 数量塌缩；消融表明主动 refinement rollouts 是关键，且不同 compaction 实现均可适配。

## 最值得记住
把 rollout 预算当作 critic 的主动学习预算，选择“最能降低价值估计误差”的状态分支，并以 compaction 边界作为长程信用分配的 step 切分点。
