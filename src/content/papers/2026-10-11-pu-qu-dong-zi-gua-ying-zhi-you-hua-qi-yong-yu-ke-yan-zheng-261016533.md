---
title: Spectral-Driven Adaptive-Rank Optimizer for Large Language Model Reinforcement
  Learning with Verifiable Rewards
title_zh: 谱驱动自适应秩优化器，用于可验证奖励的 LLM 强化学习
authors:
- Zhipeng Chen
- Wayne Xin Zhao
- Ji-Rong Wen
affiliations:
- Gaoling School of Artificial Intelligence, Renmin University of China
arxiv_id: '2610.16533'
url: https://arxiv.org/abs/2610.16533
pdf_url: https://arxiv.org/pdf/2610.16533
published: '2026-10-11'
collected: '2026-10-14'
category: Training
direction: LLM RLVR 优化器设计
tags:
- RLVR
- Low-rank optimization
- Spectral structure
- Adaptive rank
- LLM training
one_liner: 发现 RLVR 梯度能量向低秩子空间集中，提出自适应秩优化器 Ares，跨模型和任务提升准确率
practical_value: '- 在业务中用 RLVR 微调推荐/搜索 Agent 时，可借鉴 Ares 的自适应低秩优化：根据梯度能量占比动态选择更新秩，避免固定
  LoRA rank 的欠拟合/过拟合，同时降低显存与通信开销。

  - 监控梯度谱能量分布与有效秩下降趋势，可作为 RLVR 训练健康度的诊断指标；若梯度能量没有像预期那样向低秩集中，可能说明奖励信号或任务设计有问题，便于早停或调整。

  - 实现上，Ares 的能量阈值法（估计保留一定能量比例的最小秩）可以复用到现有多卡训练框架中，对优化器状态做低秩投影，提升训练吞吐，适合大规模电商搜索推理模型更新。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：RLVR 已成为训练 LLM 推理能力的核心，但优化器仍沿用监督训练（teacher-forcing）时代的 AdamW 等，可能不匹配 RLVR 独特的优化几何。

**方法关键点**：作者分析 LLM 梯度谱结构，发现 RLVR 下梯度能量持续集中到收缩的有效子空间；固定能量占比所需的秩随训练逐步下降。这一现象在 SFT 下不存在，将可验证奖励替换为随机奖励后也大幅消失，说明有效更新维度本身在动态演化。基于此提出 Ares（Adaptive Rank-Effective Spectral Optimization）：从梯度谱能量分布估计当前有效更新秩，跟踪其演化，并将每次更新的梯度信号限制在对应的低秩子空间内，而非外部预设秩。

**关键结果**：在不同规模 LLM 上，Ares 相比常用优化器提升准确率，并在多种 RLVR 算法与任务上表现出一致泛化性。结果提示，有效优化需要围绕训练过程的几何与动力学设计优化器，而不是简单继承监督训练的优化器。
