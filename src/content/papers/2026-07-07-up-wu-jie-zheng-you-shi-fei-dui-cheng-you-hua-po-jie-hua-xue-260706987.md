---
title: 'UP: Unbounded Positive Asymmetric Optimization for Breaking the Exploration-Stability
  Dilemma'
title_zh: UP：无界正优势非对称优化破解LLM强化学习的探索—稳定性困境
authors:
- Chongyu Fan
- Pengfei Liu
- Jingjia Huang
- Sijia Liu
- Yi Lin
affiliations:
- ByteDance Seed
- Michigan State University
arxiv_id: '2607.06987'
url: https://arxiv.org/abs/2607.06987
pdf_url: https://arxiv.org/pdf/2607.06987
published: '2026-07-07'
collected: '2026-07-10'
category: Training
direction: 强化学习训练优化·无界探索
tags:
- RL
- Importance Sampling
- LLM Reasoning
- Policy Optimization
- Asymmetric Optimization
one_liner: 通过stop-gradient自锚定比率取代重要性采样，对正向优势释放无界梯度以最大化探索，同时保留负向裁剪加固训练稳定性
practical_value: '- **非对称正负处理**：在业务RL训练（如对话策略、推荐排序）中，可对正确/正向动作去除裁剪，使用自锚定梯度释放探索；对错误动作保留裁剪约束，防止模型退化。

  - **stop-gradient 即插即用**：将 `π_θ / sg(π_θ)` 作为无界更新核心，实现简单，可直接嵌入现有 PPO/GRPO 代码，无需改动
  critic 或奖励函数。

  - **探索容量监控**：通过追踪策略熵和 KL 散度，诊断是否出现探索崩塌，借鉴 UP 的熵上升趋势判断训练是否健康。

  - **通用性证明**：该方法已验证对 Dense/MoE/多模态模型均有效，推荐系统或 Agent 中更换 backbone 时可放心复用，无需重新设计。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有 LLM 推理 RL（如 GRPO、DAPO）依赖重要性采样 + 裁剪平衡稳定与探索，但裁剪机制导致**概率容量（Cap）**受限于旧策略，使得低置信度但正确的推理路径更新过早截断，形成探索-稳定性困境。

### 方法关键点
- **形式化概率容量（Probability Capacity）**：刻画正向优势下 token 概率可增加的上限，揭示标准裁剪的线性依赖瓶颈。
- **无界正优势更新**：引入 stop-gradient 自锚定比率 `π_θ / sg(π_θ)`，其梯度等价于 REINFORCE，彻底消除旧策略的梯度爆炸根源，同时保持多步样本复用。
- **非对称目标设计**：对正优势（正确 rollout）使用无 clipping 的对数概率目标；对负优势（错误 rollout）保留 DAPO/GRPO 的裁剪及 KL 惩罚，作为稳定保障。
- **跨粒度统一**：该设计同时适用于 token 级（UP-DAPO、UP-GRPO）和序列级（UP-GSPO）优化，只需替换优势分支即可。

### 关键实验结果
- **UP-DAPO**在 Qwen3-14B-Base 上 AIME24 的 Avg@32 达 51.15（DAPO 47.71），Maj@32 60.88，Best@32 81.79；策略熵明显高于基线而不损失稳定性。
- **UP-GRPO**在 MATH 训练、5 类推理基准上平均 Pass@1 为 61.31%，超越 GSPO、ASPO 等 11 个基线；同时 KL 散度最低、熵持续上升。
- **UP-GSPO**在 MoE 架构（Qwen3-30B-A3B）上 Avg@32 达 55.73（提升 3.02 个点），KL 无异常。
- **多模态**：Qwen3-VL-8B-Instruct 在 Geometry3K 上 UP-GRPO 精度达 62.60%（GRPO 59.30%），KL 保持稳定。

### 核心一句话
**以 `sg(π_θ)` 取代 `π_old` 作为比率分母，非对称地让正样本无界探索、负样本仍受裁剪保护，从而在保证稳定性的前提下最大化推理探索空间。**
