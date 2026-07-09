---
title: Single-Rollout Asynchronous Optimization for Agentic Reinforcement Learning
title_zh: 单次 rollout 异步优化：让 Agent 强化学习训练更稳更强
authors:
- Zhenyu Hou
- Yujiang Li
- Jie Tang
- Yuxiao Dong
affiliations:
- Tsinghua University
- Z.AI
arxiv_id: '2607.07508'
url: https://arxiv.org/abs/2607.07508
pdf_url: https://arxiv.org/pdf/2607.07508
published: '2026-07-08'
collected: '2026-07-09'
category: Training
direction: 异步强化学习训练稳定化
tags:
- Asynchronous RL
- GRPO
- Agentic RL
- Importance Sampling
- Value Model
- LLM
one_liner: 提出单次 rollout 异步 RL 策略 SAO，以 token 级双面裁剪和更快价值更新稳定训练，在智能体推理与编码任务上显著超越 GRPO
practical_value: '- **单次 rollout 替代组采样适用于在线推荐/Agent 场景**：线上只能获得单条反馈时，可以用训练好的价值模型做基线，而非依赖组内相对奖励。这直接解决了
  GRPO 在实时环境中的部署困难。

  - **直接使用 rollout log-probabilities 做重要性采样，简化异步训练架构**：不需要维护策略的历史快照链，大幅降低工程复杂度，对推荐模型异步在线学习特别友好。

  - **价值模型的冻结注意力训练策略**：只在 MoE 层更新，注意力层冻结，能显著稳定 critic 训练并降低梯度范数。这对需要快速收敛的在线价值估计（如
  bandit 或 contextual bandit）有参考意义。

  - **Skip-Observation GAE 处理 agent 轨迹**：计算优势时跳过环境反馈 token，将价值估计限定在模型动作上，消除环境噪声。对于涉及工具调用或多轮对话的推荐
  agent（如对话式推荐），可借鉴该方式只对模型可控部分进行信用分配。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

## 动机
大型语言模型后训练越来越多采用强化学习，但现有 RL 流水线多为同步、组内采样（如 GRPO），在智能体长周期任务中效率低且受 straggler 影响。异步 RL 虽可提高利用率，却引入严重的 off-policy 漂移和训练不稳定，尤其是组采样天然与异步训练不兼容，且无法用于仅返回单条轨迹的在线环境。

## 方法关键点
- **单次 rollout 异步优化 (SAO)**：每个 prompt 只生成一条轨迹，完成后立刻送入训练，彻底消除组内等待。
- **直接双面重要性采样 (DIS)**：放弃维护旧的旧策略，直接用 rollout 引擎记录的 log-probs 计算概率比 r_t(θ) = π_θ / π_rollout，并通过严格的双面 token 级裁剪 (f(x) 在 [1-ε_l, 1+ε_h] 外直接置 0) 稳定训练。
- **更快价值更新 (Critic 更新频率 > Actor)**：每步策略更新前先进行 2 次价值模型更新，使基线更快跟踪分布变化。
- **冻结注意力训练价值模型**：只优化 MoE 层，冻结注意力参数，大幅降低 critic 梯度范数，提升训练稳定性。
- **跳过观察的 token 级 GAE (Skip-Observation GAE)**：针对 agent 轨迹交织环境反馈的特点，在计算优势时跨过观察 token，将价值估计集中在模型生成的动作上，避免环境噪声传播。
- **大规模价值模型预训练**：用大量数据预训练 value model，解决冷启动问题。

## 关键实验
- 以 Qwen3-30B-A3B 为基础模型，在 AIME2025、BeyondAIME、HMMT Nov 2025、IMOAnswerBench 四个数学推理基准以及 SWE-Bench Verified 编码任务上评估。
- SAO 稳定训练约 1000 步，而普通 GRPO 约 160 步即崩溃。SAO 在所有基准上均显著优于 GRPO：AIME2025 从 84.2 提升到 97.3，BeyondAIME 从 54.8 到 74.8，SWE-Bench Verified 从 27.0 到 29.8。
- 在线学习模拟中，SAO 应对风格偏好切换时快速恢复，而基于滑动平均的 baseline 明显滞后。

## 最值得记住的一句话
用单条 rollout 的 log-probs 直接做严格 token 级裁剪，配合更快更新的冻结注意力 critic，可以让异步 RL 在智能体任务上又稳又强。
