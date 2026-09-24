---
title: 'PACT: From Credit Assignment to Critic Alignment'
title_zh: PACT：从信用分配到 Critic 对齐
authors:
- Jiayan Fu
- Hang Xu
- Yong Zhang
- Zhaokai Luo
- Yao Hu
- Dongyan Zhao
- Mu Chuan
affiliations:
- Peking University
- Xiaohongshu
arxiv_id: '2609.26355'
url: https://arxiv.org/abs/2609.26355
pdf_url: https://arxiv.org/pdf/2609.26355
published: '2026-09-21'
collected: '2026-09-24'
category: Training
direction: LLM 强化学习的信用分配与 Actor-Critic 训练
tags:
- Credit Assignment
- RLHF
- Actor-Critic
- PPO
- Importance Sampling
- LLM
one_liner: 证明 token 级信用唯一等于条件奖励差分，提出 Actor-then-Critic 加重要性采样的 PACT，在数学与编码基准显著超越 PPO/GRPO/SAO
practical_value: '- **RL 微调推荐/搜索 Agent 时，用 Actor-then-Critic 顺序并对 critic 目标做 importance
  sampling 校正**：先更新 actor，再用更新后 actor 与旧 rollout 的重要性比修正 critic 的 value target，避免
  PPO 中 critic 始终落后一个 policy 版本的问题；适合点击/转化/任务成功等 0-1 或归一化 reward。

  - **Value/critic 训练用 BCE 替代 MSE**：在 reward ∈ [0,1] 条件下两者最优解相同，但 BCE 收敛更快、正负样本 value
  separation 更大；对稀疏奖励、长轨迹的搜索/推荐 Agent 训练尤其实用，可直接替换现有 critic loss。

  - **长 horizon outcome-only reward 场景优先使用 GAE λ=1**：论文证明 λ<1 会保留中间 critic 误差，且 token
  credit 近似稀疏时误差可能主导信号；业务中如果只有最终转化/成交 reward，建议 λ=1 或直接使用 RLOO/GRPO 的 response-level
  baseline，避免细粒度 critic 噪声。

  - **响应级 baseline 与 token 级 credit 在期望梯度上等价**：RLOO/GRPO 不必强行改造成 token-level advantage；如无高精度
  critic，保持 response-level 信号在期望上是安全的，但若要利用长程结构化信息，应优先提升 critic 对齐度和估计准确性。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
RL 已是 LLM 后训练核心，但 token 级信用分配长期缺乏公认数学定义，导致 OPD、RLOO、GAE 等算法中的信号与真实奖励贡献关系不清。论文希望给出统一刻画，并据此改进 Actor-Critic 训练。

## 方法关键点
- 定义三个正则条件：**Completeness**（信用总和等于奖励偏差）、**Prefix Consistency**（前缀信用只依赖已见信息）、**Neutrality**（下一步信用条件期望为 0）。
- 证明唯一 token 级信用为 `Ci = Vi - Vi-1 = E[R|Fi] - E[R|Fi-1]`，即条件奖励预测差分，构成 martingale difference。
- 用该视角解释：理想 OPD teacher 是隐式 critic，梯度与 token credit 成比例；RLOO response-level baseline 在期望梯度上与 token credit 等价；GAE λ=1 可消除中间 critic 误差，λ<1 在 credit 稀疏时误差可能主导。
- 提出 **PACT**：采用 Actor-then-Critic 更新顺序，actor 更新后对同一 rollout 做前向，用 continuation importance ratio 修正 critic 训练目标，使 critic 对齐更新后 policy；critic 目标用 BCE 而非 MSE；实际用当前 token detached importance ratio 并裁剪区间 [ρmin, ρmax]。

## 关键实验
- 数学推理：Qwen3.5-4B + OpenCode，在 DAPO-Math-17k 子集训练，评估 AIME 2025/2026、BeyondAIME、HMMT Nov 2025，Avg@16。
- 编码 Agent：Qwen3.6-35B-A3B + Codex，OpenSWE 训练，评估 SWE-bench Verified pass@1。
- 结果：数学平均 **72.87%**，比 GRPO 高 8.80 个百分点、比 PPO λ=1 高 13.16 个百分点；SWE-bench Verified **67.4%**，比 PPO/GRPO/SAO 分别高 2.4/2.0/3.8 个百分点。
- 消融：BCE critic 在固定 policy 下比 MSE 收敛更快、value separation 更大；去掉 importance correction 后数学平均降至 67.74%。

## 最值得记住的一句话
Token 级信用本质上就是条件奖励预测的差分 `Vi - Vi-1`，而 critic 与当前 policy 的对齐程度决定这一信号能否被可靠恢复；PACT 通过 Actor-then-Critic + importance sampling + BCE critic 把这套逻辑落地。
