---
title: 'Learning from Your Own Mistakes: Constructing Learnable Micro-Reflective Trajectories
  for Self-Distillation'
title_zh: 从自身错误中学习：构建可学习的微反思轨迹用于自我蒸馏
authors:
- Zhilin Huang
- Hang Gao
- Ziqiang Dong
- Yuan Chen
- Yifeng Luo
- Chujun Qin
- Jingyi Wang
- Yang Yang
- Guanjun Jiang
affiliations:
- Qwen Business Unit of Alibaba
- Tsinghua University
- Peking University
arxiv_id: '2606.18844'
url: https://arxiv.org/abs/2606.18844
pdf_url: https://arxiv.org/pdf/2606.18844
published: '2026-06-16'
collected: '2026-06-23'
category: Training
direction: LLM 自我蒸馏 · 轨迹增强
tags:
- Self-Distillation
- Reinforcement Learning
- Trajectory Construction
- LLM Reasoning
- GRPO
- Error Correction
one_liner: 通过修正模型自身的错误轨迹并插入自然语言诊断，将自我蒸馏从分布对齐升级为显式轨迹构造。
practical_value: '- 电商/广告场景中若用 LLM 生成推荐理由或解释，可借鉴 TAPO 对比式轨迹构建：收集模型自身的正确与错误回复，在失败点插入反思诊断，形成新的微调样本，提升解释准确性与错误恢复能力。

  - 对于搜索意图理解等推理链路长且容易出错的任务，可利用难度感知筛选，只在高能力边界的样本上构造反思轨迹，避免简单样本浪费训练资源，并保持 on-policy
  分布。

  - 解耦优势估计的技巧可迁移至多策略混合训练中，防止不同难度或不同来源轨迹间的梯度互相干扰，改善训练的稳定性。

  - 工程实现上，TAPO 无需外部更强模型参与，完全依赖模型自身的采样群组，适合在闭环推荐系统中持续自我优化，降低人工标注与模型蒸馏成本。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有 LLM 自我蒸馏通常对齐输出分布（最小化 KL 散度），但监督信号来自无控采样，缺乏对具体错误模式的诊断与矫正，模型只能盲目模仿，无法获得细粒度的推理纠错。

**方法关键点**：TAPO 将自我蒸馏从隐式分布对齐升级为显式轨迹构造。RL 训练中，同一 query 同时采样正确与错误 rollout，利用对比结构构建“微反思矫正”轨迹：保留错误前缀直至失败处，插入一段自然语言诊断（指明错误原因），随后引导正确推理。这种轨迹锚定在模型自身的 on-policy 前缀上，比以往按位置对齐的 KL 方法更能维持策略分布。为稳定训练，引入两个机制：(1) 难度感知的候选选择，仅在模型能力边界附近采样高价值轨迹；(2) 解耦优势估计，分离正确与反思轨迹的优势计算，避免梯度污染。

**关键结果**：在 AIME 2024、AIME 2025 和 HMMT 2025 数学推理基准上，相同训练步数下 TAPO 相对 GRPO 取得一致显著提升；分析表明模型在首次推理和纠错两方面能力均增强。
