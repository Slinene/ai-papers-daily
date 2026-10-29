---
title: Multiscale Policy Optimization for Long-Horizon LLM Agents
title_zh: 长程 LLM Agent 的多尺度策略优化
authors:
- Tao Ren
- Hui Yang
- Jia Deng
- Tingyang Chen
- Qiyao Wang
- Shuo Tang
- Ziyang Zeng
- Yuhua Jiang
- Guanghao Li
- Huatong Song
affiliations:
- Peking University
- IQuest Research
- Tsinghua University
- Renmin University of China
- The University of Hong Kong
arxiv_id: '2610.35013'
url: https://arxiv.org/abs/2610.35013
pdf_url: https://arxiv.org/pdf/2610.35013
published: '2026-10-25'
collected: '2026-10-29'
category: Agent
direction: Agent RL · 多尺度信用分配与策略更新
tags:
- Agent RL
- Multi-turn
- Advantage Estimation
- PPO
- Long-horizon
- Importance Sampling
one_liner: 提出 MPO，组合 turn 级 GAE 与均值保持的 token 级信用分配，并用 turn 级重要性采样更新策略，在搜索/工具/自动化任务上全面超越
  PPO/VAPO/SAO
practical_value: '- 在对话式电商/购物 Agent 的多轮 RL 中，把一次完整的 assistant turn（搜索词、工具调用、加购决策、最终回复）作为宏动作，用
  turn 级 GAE 传播终局奖励（下单、成交、任务完成），而不是直接在 token 序列上做 GAE。论文统计显示 turn 间方差占 critic 价值方差的
  89.5%，说明 reward 信用主要在轮次尺度，token 级只需做均值保持的局部修正。

  - 策略更新时使用 complete-turn importance ratio，并对其他 token 的 ratio 做 stop-gradient，只让当前
  token 的 score gradient 保留 token-specific advantage。这个实现可以方便地接入现有 PPO/VAPO 训练框架，避免
  token 级 ratio 带来的 within-turn distribution shift，适合 LLM 生成内容较长、但交互边界更重要的电商 Agent
  场景。

  - 超参上把跨轮衰减 λ 和轮内衰减 λ_intra 分开调，推荐 λ≈0.8、λ_intra≈0.95、β≈1.0。原因是一个 turn 包含大量 token，两者的时间尺度不同；业务里如果直接用相同衰减，要么跨轮信用太短，要么轮内
  token 信号稀释。

  - 该方法只增加一个 critic 和一个均值约束投影，计算开销低；若你的搜索/推荐 agent 已有 PPO 类训练栈，可以先替换 advantage 计算与
  ratio 构造，不必重构环境或 reward。'
score: 8
source: huggingface-daily
depth: full_pdf
---

动机：长程 LLM agent 通过完整 assistant turns 与环境交互，但策略是按 token 生成的。现有 RL 方法存在尺度错配：GRPO/GSPO 等 group-relative 方法给整条序列一个共享 advantage，无法区分不同轮次和 token；PPO/VAPO/SAO 等 critic-based 方法把每个 token 当动作，虽提供细粒度信用，但没有显式分离 turn 级环境交互和 turn 内生成。论文从 critic 价值结构观察到，turn 均值差异解释了 89.5% 的 token 加权价值方差，93.8% 的轨迹中 turn 间方差大于 turn 内方差，说明 long-horizon agent 的信用应主要在 turn 尺度传播，同时保留 token 内差异。

方法关键点：
- 提出 MPO，包含 MAE 与 turn 级重要性加权。
- MAE：先在 turn 轴线上做 GAE，得到 turn-level advantage A_turn；再在当前 turn 内部用 λ_intra 计算局部 token GAE，得到 A_intra；通过约束最小二乘投影把 token 信用设为 A_MAE = A_turn + β(A_intra - mean(A_intra))，保持该 turn 的均值等于 A_turn，仅保留 token 间相对差异。
- 更新目标：用 complete-turn importance ratio ρ_t = ∏ρ_t,i 作为前向权重，但对其他 token 的 ratio 做 stop-gradient，使每个 token 的梯度仍由其自身 MAE advantage 控制，从而避免 token-level surrogate 的 within-turn distribution shift。

关键实验结果：在 Qwen3-4B-Thinking 和 Qwen3-30B-A3B-Instruct 上，覆盖 Search（BrowseComp-Plus、GAIA、HLE）、Claw-Eval 和 Automation Bench，与 GRPO、GSPO、PPO、VAPO、SAO 对比。在 9 个指标上 MPO 全部最高：4B 上 BrowseComp-Plus pass@1 48.08（vs SAO 43.75、PPO 40.85），GAIA pass@1 39.47（vs PPO 31.71），HLE pass@1 9.92；30B 上 BrowseComp-Plus pass@1 50.32，Automation Bench pass@1 15.00。消融显示去掉 turn 级 ratio 会掉 2-3 个点，β=0 时掉约 6.28/5.27/2.04 个点（三个 Search 基准）。测试时采样扩展 pass@32 也持续领先 GRPO/PPO。

值得记住的一句话：在长程 agent 中，信用分配与重要性加权的尺度要对齐到完整交互 turn，而不是 token；token 级信号只应做均值保持的局部修正。
