---
title: A Gradient Perspective on RLVR Stability and Winner Advantage Policy Optimization
title_zh: RLVR稳定性梯度分析与赢家优势策略优化
authors:
- Prasanth YSS
- Zhichen Ren
- Rasa Hosseinzadeh
- Ilan Gofman
- Yuqi Chen
- Zhaoyan Liu
- Guangwei Yu
- Jesse C. Cresswell
- Satya Krishna Gorti
affiliations:
- Layer 6 AI
arxiv_id: '2606.16154'
url: https://arxiv.org/abs/2606.16154
pdf_url: https://arxiv.org/pdf/2606.16154
published: '2026-06-14'
collected: '2026-06-17'
category: Training
direction: RL训练稳定性分析与策略优化
tags:
- RLVR
- GRPO
- Policy Gradient
- Training Stability
- WAPO
- Reasoning
one_liner: 通过梯度分析揭示GRPO崩溃机制，提出仅对正优势序列更新的WAPO，提升训练稳定性与性能。
practical_value: '- 在RL微调推荐/Agent模型时，只对奖励高于平均的生成结果（正优势）进行策略更新，可避免负优势样本导致熵增和输出崩溃，是一种简单的实现
  trick。

  - 裁剪策略梯度更新幅度（类似 PPO 的 clipping），防止梯度爆炸，保持训练稳定，可直接集成到现有 RL 训练流程。

  - 论文提出的 token 级梯度分解与稳定性分类法可用于分析推荐模型的 RL 微调行为，诊断训练不稳定是由哪些 token 分布引起，指导超参调整。

  - 使用在线采样（on-policy）而非重用旧策略样本（off-policy），可减少策略漂移带来的问题，在推荐系统的多步 Agent 训练中值得尝试。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：GRPO 等 RLVR 方法在微调 LLM 推理时容易发生崩溃（输出高熵噪声或重复），但原因不明。本文从梯度层面分析该现象，旨在理解并解决不稳定性。

**方法关键点**：
1. 对 GRPO 的 token 级梯度进行分解，推导出一个分类法：根据当前 token 概率、优势符号以及是否被采样，预测更新后下一 token 概率和熵的变化方向。发现当负优势序列中出现低概率 token 时，梯度倾向于提升其概率，可能引发熵失控。
2. 基于此分析，提出 **WAPO（Winner Advantage Policy Optimization）**：一种在线的裁剪策略梯度算法，仅对正优势（赢家）的完成序列进行更新，并直接使用当前策略的采样结果（on-policy），避免 off-policy 漂移。
3. WAPO 通过 clip 控制更新幅度，消除负优势样本的影响，保持策略熵稳定。

**关键结果**：在数学推理（MATH、GSM8K）和多跳问答（HotpotQA）基准上，WAPO 在 SmolLM、Qwen 等多个模型家族上匹配或超越 GRPO、RLOO 等基线，且训练过程无崩溃，熵值平稳。
