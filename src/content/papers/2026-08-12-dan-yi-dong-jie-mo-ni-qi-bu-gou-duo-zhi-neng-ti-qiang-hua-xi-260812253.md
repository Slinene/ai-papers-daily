---
title: 'One Frozen Simulator Is Not Enough: Simulator Collapse in Multi-Agent RL'
title_zh: 单一冻结模拟器不够：多智能体强化学习中的模拟器坍缩
authors:
- Simon Yu
- Nicholas Tomlin
- Marwa Abdulhai
- Ximing Lu
- Derek Chong
- Abe Hou
- Dilara Soylu
- Sergey Levine
- Christopher D. Manning
- Weiyan Shi
affiliations:
- Northeastern University
- New York University
- UC Berkeley
- University of Washington
- Stanford University
arxiv_id: '2608.12253'
url: https://arxiv.org/abs/2608.12253
pdf_url: https://arxiv.org/pdf/2608.12253
published: '2026-08-12'
collected: '2026-08-13'
category: MultiAgent
direction: 多智能体强化学习 · 用户模拟器坍缩
tags:
- Multi-Agent RL
- Simulator Collapse
- LLM User Simulator
- Co-Training
- Verbalized Sampling
- Policy Entropy
one_liner: 识别单冻结 LLM 用户模拟器导致的 simulator collapse，并提出 Verbalized Sampling 与 Co-Training
  两种解法
practical_value: '- **训练对话/Agent 策略时不要只信单一 frozen LLM 用户模拟器**：如果训练 reward 持续上升、held-out
  或真实用户指标先升后跌、策略 entropy 趋零，基本就是 simulator collapse。可以在电商客服、导购对话、多轮搜索 agent 训练中加一个
  held-out simulator panel 或真实日志回放，监控这条曲线。

  - **用 Verbalized Sampling 做低成本的 inference-time 增强**：rollout 时让模拟器显式列出多个可能用户回复及概率，再采样，而不是
  greedy 生成。这能覆盖接受、追问、拒绝、投诉等不同用户反应，避免策略学成固定脚本；不重训、不增加模型更新成本，适合快速在现有 user simulator
  上打补丁。

  - **把用户模拟器也 trainable，并做成 checkpoint pool**：策略和模拟器同 rollout 联合更新，或从近期 simulator
  checkpoint 池中采样，让训练环境成为 moving target。工程上对应电商场景：用户行为模型随策略一起迭代，防止策略只学会讨好某一批“好说话”的模拟用户。

  - **模拟器 reward 要保留 informative variation**：二进制任务下让 simulator 训练目标接近 success rate
  ≈ 0.5，保持 batch 内 variance 最大；不要让模拟器只学成一个新的固定 mode。否则 Co-Training 也会重新坍缩。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**
多轮人机交互 RL 通常用单个冻结 LLM 模拟用户，以降低真实用户训练成本。但这种做法会系统性泛化失败：aligned LLM 模拟器本身 mode-collapsed，策略训练时只能看到其主导模式，学到利用该模式的窄策略；训练 reward 继续上升，held-out 与真实用户性能却先升后跌，策略 entropy 也趋零。问题不在算法，而在训练环境多样性不足。

**方法关键点**
- 将多轮对话建模为 POMDP，用户模拟器决定策略访问的状态与梯度信号。
- 定义 simulator collapse 为训练 rollout 访问的 simulator turns 上概率质量高度集中；证明策略梯度偏向对确定性 mode-user 的优化，组相对优势只剩 agent-side contrast，策略按几何速率集中到 mode-exploit set。
- **Verbalized Sampling**：inference-time 方案，每次 simulator turn 让模拟器生成带概率的多个候选回复并采样，恢复 within-simulator 多样性，不重训。
- **Co-Training / Population Co-Training**：training-time 方案，策略与可训练模拟器在同一 rollout 上联合更新；population 版本从近期 simulator checkpoint 池采样，使 mode 不断移动。

**关键实验**
在 Persuasion for Good、τ²-bench、CooperBench 三个多轮 benchmark 上验证。Qwen3-4B-Instruct 上，τ²-Retail：RL (Single) 46.1，Verbalized Sampling 55.5，Co-Training 60.5，Population Co-Training 62.2；τ²-Airline：29.8 → 36.9 → 44.4 → 45.7；P4G reward：0.275 → 0.484 → 0.438 → 0.508。策略 entropy 在 single-simulator RL 中崩溃到接近零，两种方法均能恢复。人类研究中，Co-Training 在 τ²-bench task outcome 达 0.70，VS 达 0.63，均显著高于 RL (Single) 的 0.43；P4G 捐款额与自然度也明显提升。CooperBench 上 population self-play 在 9B 模型达 33.6，高于 frozen-partner cross-play 的 28.8。

**最值得记住的一句话**：训练环境的多样性，而不只是策略多样性，决定了多轮 RL 能否泛化到真实用户。
