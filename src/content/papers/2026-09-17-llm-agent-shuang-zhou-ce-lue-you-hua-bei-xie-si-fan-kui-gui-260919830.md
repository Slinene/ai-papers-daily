---
title: 'Dual-Axis Policy Optimization for LLM Agents: Bayesian Feedback Attribution
  and Trajectory Mass Normalization'
title_zh: LLM Agent 双轴策略优化：贝叶斯反馈归因与轨迹质量归一化
authors:
- Yingxuan Zhuang
- Binhe Yu
- Jingxiao Yang
- Ruopei Sun
- Ziting Li
- Cheng Tan
- Xuhong Zhang
- Jianwei Yin
- Jintao Chen
affiliations:
- Zhejiang University
- University of Science and Technology of China
- University of New South Wales
- Shanghai Artificial Intelligence Laboratory
arxiv_id: '2609.19830'
url: https://arxiv.org/abs/2609.19830
pdf_url: https://arxiv.org/pdf/2609.19830
published: '2026-09-17'
collected: '2026-09-18'
category: Agent
direction: Agent 强化学习训练优化
tags:
- LLM Agents
- Reinforcement Learning
- GRPO
- Feedback Attribution
- Trajectory Normalization
one_liner: 提出 BATON 框架，分离轨迹内反馈归因与轨迹间目标聚合，提升多轮 Agent RL 效果并降低推理长度
practical_value: '- 训练多轮购物导购/搜索 Agent 时，直接按 token 平均会被长失败轨迹主导，可先做 trajectory-level
  mean 再跨轨迹等权平均，只改 loss 聚合就能缓解长度偏差，易接入现有 GRPO/GiGPO 流水线。

  - BFA 的“反馈兼容性”思想适合只有 outcome reward 或稀疏环境反馈的场景：不替换 reward，而是用 old policy 对 observed
  feedback 的 likelihood 与 counterfactual action 比较，生成 step-level soft 权重；对检索增强问答、多轮选品对话尤其可复用。

  - 工程落地时可以先只上 TMN，几乎零额外开销（约 1.01-1.02 倍训练时间），能拿到一部分稳定收益；BFA 需要额外 forward 计算（总开销约
  1.10-1.17 倍），但可同时减少 eval 轨迹动作数和生成 token 数，有利于线上推理成本。

  - 长尾失败 session 常见于多跳搜索、电商导购等场景，可直接借用长度校准的几何证据归一化，避免长反馈文本 token 数对 likelihood 量级的影响。'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

**动机**
多轮 LLM agent 的 RL 训练存在两个被忽视的偏差：一是轨迹内对环境反馈利用不足，二是轨迹间 token 级平均让长失败轨迹主导梯度。ALFWorld 中最长 25% 轨迹占 60.3% 的聚合质量，WebShop 中占 42.2%。传统 GRPO/GiGPO 的全局 valid-token 平均混淆了这两个维度，导致长失败样本过度影响策略更新。

**方法关键点**
- 将目标分解为 L(θ)=Σ_i q_i · (1/N_i)Σ_{t,k} ω_{i,t} ℓ^A_{i,t,k}(θ)，分别控制轨迹间质量 q_i 和轨迹内分配 ω。
- Bayesian Feedback Attribution (BFA)：对每个决策 (h,a,o')，从 old policy 采样 counterfactual 动作，计算 observed feedback 的条件 likelihood，构造 pairwise 后验得到 evidence ratio e；按反馈 token 长度做几何平均并归一化为权重 ω，stop-gradient 加权到 host learner 的局部 loss。
- Trajectory Mass Normalization (TMN)：将轨迹级权重从 token-proportional q_flat_i=Ni/ΣNj 改为 q_TMN_i=1/B，每条完整轨迹等权，消除长轨迹 mass 偏差。
- 两者可独立使用，不改变 host learner 的 reward、advantage、clipping 和 rollout 流程，兼容 GRPO/GiGPO。

**关键实验**
在 ALFWorld、WebShop、SearchQA 上，用 Qwen2.5 1.5B/3B/7B，以 GRPO 和 GiGPO 为基线。ALFWorld 1.5B GRPO success 从 72.9% 升至 85.6%，GiGPO 从 86.8% 升至 94.1%；7B 同样提升。WebShop 1.5B GRPO success 从 57.1% 升至 68.2%，GiGPO 从 67.1% 升至 76.4%。SearchQA 平均 exact match 提升约 2-4 个点。Ablation 显示 BFA 与 TMN 各自独立有效且组合最优。推理行为上，GRPO 平均动作数从 21.5 降至 16.4，生成 token 数从 1734 降至 1301；训练额外开销约 1.10-1.17 倍，无额外环境交互。

**最值得记住的一句话**
把 token 级平均拆成“轨迹内反馈分配 + 轨迹间等权聚合”，只改 loss 聚合层就能让多轮 Agent RL 更稳、更强、更短。
