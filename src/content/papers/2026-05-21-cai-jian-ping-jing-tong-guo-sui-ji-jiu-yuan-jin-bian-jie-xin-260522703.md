---
title: 'Clipping Bottleneck: Stabilizing RLVR via Stochastic Recovery of Near-Boundary
  Signals'
title_zh: 裁剪瓶颈：通过随机救援近边界信号稳定RLVR
authors:
- Shuo Yang
- Jinda Lu
- Chiyu Ma
- Kexin Huang
- Haoming Meng
- Qihui Zhang
- Yuyang Liu
- Bolin Ding
- Guoyin Wang
- Li Yuan
affiliations:
- Alibaba Group
- Peking University
- Dartmouth College
- University of Toronto
arxiv_id: '2605.22703'
url: https://arxiv.org/abs/2605.22703
pdf_url: https://arxiv.org/pdf/2605.22703
published: '2026-05-21'
collected: '2026-05-22'
category: Training
direction: RLVR 训练稳定性优化 · 裁剪决策
tags:
- RLVR
- GRPO
- Clipping
- NSR
- Stochastic Rescue
- Training Stability
one_liner: 诊断硬裁剪决策是GRPO-style RLVR不稳定的关键瓶颈，提出随机救援边界信号的方法NSR，显著提升训练稳定性与性能。
practical_value: '- 诊断方法可迁移：通过解耦裁剪决策与梯度大小，精确定位训练瓶颈，适用于电商/Agent场景中基于PPO/GRPO的微调稳定性分析。

  - NSR实现简单：仅需在裁剪计算时对出界token按距离做一次随机保留判断，可直接嵌入现有DAPO/GSPO代码，无额外超参负担，适合快速实验验证。

  - 随机救援优于确定性衰减：业务中若需软化信任区域，优先使用概率化保留而非固定权重衰减，能获得更稳定训练与更低方差。

  - 支持token级与序列级裁剪：NSR在两种粒度上均有效，可复用于推荐对话生成或策略优化中的不同动作空间。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**：RLVR（如GRPO、DAPO）通过硬裁剪约束策略更新，但训练不稳定且收敛不佳。现有方法多通过调整梯度幅度改进，但本文通过因果干预发现，真正瓶颈在于硬裁剪的二元决策（keep/drop），它无差别地丢弃了略出信任区域的有效学习信号，尤其近边界处。

**方法关键点**：
- 提出Near-boundary Stochastic Rescue（NSR），不改算法核心，仅在计算裁剪时对出界token做一次随机救援：以概率保留其梯度（乘以均匀噪声，若落回内区就保留，否则继续裁剪）。
- 该机制在期望上等价于隐式软裁剪，梯度衰减约 O(1/r²)，但实验证明其随机性优于确定性衰减，因为它起到了边界局部滤波作用。
- 实现即插即用，适配token级（DAPO）与序列级（GSPO）裁剪。

**关键结果**：
- 在Qwen2.5-Math-7B、Qwen3-8B、Qwen3-30B-A3B（MoE）上，基于DAPO/GSPO，NSR在AIME24/25、AMC上全面超越基线，如7B Pass@1 提升+4.93，8B提升+6.36。
- 训练熵更稳定，平均响应长度平稳增长，表明救援信号促进深度推理。
- 消融证实仅救援区操作即可复现增益，而推边区无效；随机救援在跨运行稳定性上显著优于确定性衰减。

**一句话**：刚性裁剪决策是瓶颈，用简单随机救援恢复近边界信号，即可获得稳定且高性能的RLVR训练。
