---
title: 'Learn What''s Left, Not What''s Mastered: Saturation Aware Advantage Reweighting
  for Multi-Reward Policy Optimization'
title_zh: 学习未掌握部分而非已掌握部分：多奖励策略优化的饱和感知优势重加权
authors:
- Yixuan Wang
- Yifei Chen
- Haichao Zhang
- Haozheng Luo
- Xander Wu
- Jie Ni
- Yun Fu
- Nuno Vasconcelos
- Yijiang Li
affiliations:
- University of Florida
- UC San Diego
- Northeastern University
- Northwestern University
- Stanford University
arxiv_id: '2608.16072'
url: https://arxiv.org/abs/2608.16072
pdf_url: https://arxiv.org/pdf/2608.16072
published: '2026-08-16'
collected: '2026-08-19'
category: Training
direction: LLM 后训练 · 多奖励 RL 优化
tags:
- RL
- multi-reward
- GRPO
- advantage reweighting
- LLM reasoning
- post-training
one_liner: 提出 SA-MRPO，独立标准化各奖励并按批次饱和度动态折扣优势，将优化重心转向未饱和目标，提升困难指标性能
practical_value: '- 多目标 RL 微调时，不要先固定加权求和再标准化优势；改为对每个奖励独立标准化，并在每个 batch 估计目标饱和度（如 batch
  平均奖励接近上限）来动态折扣其梯度贡献，可让模型自动将优化重心转向未达标目标，避免简单指标吸干预算。

  - 推荐系统多任务学习可借鉴“饱和度感知动态损失权重”：每隔若干 step 根据验证集或 batch 上各目标当前水平计算饱和度，自动降低已达标任务的损失权重，把容量留给困难目标（如转化率）。

  - 工程实现成本低：只需在 batch 内统计每个奖励的均值或分位数，设计递减函数（如 1 - 均值/上限）生成权重，无需额外超参或元学习，易嵌入现有 GRPO/PPO
  流程。

  - 多目标场景下应监控指标是否已达标，适时冻结或降低其训练信号，将 RL 信号导向更难提升的目标，符合“保持已满意水平而提升困难目标”的实践原则。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM 后训练常用 group-relative advantage (GRPO) 优化多奖励目标，但现有做法先将奖励向量固定加权求和再做组内标准化，导致两个问题：不同奖励分布的 rollouts 可能得到相同优势；所有目标以固定相对权重优化，忽视饱和度，已解决目标继续占用梯度预算。

**方法**：提出 SA-MRPO，独立标准化每个奖励目标，并根据批次级饱和度估计自适应折扣其优势贡献。具体地，对每个奖励计算 batch 内均值等饱和度指标，用递减函数生成折扣因子，动态将优化重心转向未饱和目标，同时保持已满足目标性能。还证明饱和感知重加权可反转更新符号，而非仅缩放幅度。

**结果**：在数学推理二目标和三目标组合上，SA-MRPO 在 15 个基准对比中 12 个超过 GDPO，困难正确性目标提升最高达 AIME24 上 5%。在自适应推理五个基准上准确率全部提高，平均 3.8%，最高 AMC23 上 9.2%；编码基准 pass rate 提升最高 2.3%，同时简单目标维持在已满足水平附近。
