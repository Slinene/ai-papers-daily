---
title: 'You Only Need Minimal RLVR Training: Extrapolating LLMs via Rank-1 Trajectories'
title_zh: 仅需极少量 RLVR 训练：通过秩-1 轨迹外推 LLM
authors:
- Zhepei Wei
- Xinyu Zhu
- Wei-Lin Chen
- Chengsong Huang
- Jiaxin Huang
- Yu Meng
affiliations:
- University of Virginia
- Washington University in St. Louis
arxiv_id: '2605.21468'
url: https://arxiv.org/abs/2605.21468
pdf_url: https://arxiv.org/pdf/2605.21468
published: '2026-05-19'
collected: '2026-05-22'
category: Training
direction: RLVR 训练效率优化 · 参数轨迹外推
tags:
- RLVR
- low-rank
- extrapolation
- checkpoints
- denoising
- training efficiency
one_liner: 发现 RLVR 参数轨迹是低秩且线性的，提出 RELEX 只需 15% 训练步数即可外推高质量 checkpoint
practical_value: '- **在线学习/RL 调优的早期停止**：在电商推荐、Agent 策略的 RL 微调中，监控参数更新矩阵的秩，若观察到类似秩-1
  结构，可大幅压缩训练步数，直接外推后续 checkpoint，节省算力。

  - **低资源快速实验**：仅需短窗口（如 15% 步数）和简单 SVD+线性回归，无需额外训练即可获得完整训练的近似模型，适合快速迭代验证想法。

  - **模型合并与聚合中的去噪**：秩-1 投影可滤除随机优化噪声，这一思想可迁移到联邦学习的参数聚合或多臂老虎机策略合并，提高鲁棒性。

  - **长期性能预测**：在无法完整训练的场景（如在线 A/B 测试需快速决策），用少量步数的参数变化线性外推长期趋势，提前终止劣化方向。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：RLVR 虽能提升 LLM 推理能力，但需大量计算步数，其参数更新的几何特性未被探索。本工作揭示 RLVR 参数轨迹是极低秩且高度可预测的，旨在用极简方式降低训练成本。

**方法关键点**：
- 实证发现 RLVR 训练中参数增量（ΔW）主要由秩-1 子空间主导，其投影模长随步数近乎线性增长。
- 提出 RELEX：从训练前 15% 步数的 checkpoint 序列，通过 SVD 估计秩-1 主方向，再对模长进行线性回归，外推生成任意后续步数的模型参数，无需重新训练。
- 秩-1 投影天然滤除随机优化噪声（“去噪”效应），避免噪声累积损害外推性能。

**关键结果**：
- 在 Qwen2.5-Math-1.5B、Qwen3-4B/8B 上，RELEX 仅用 15% 完整训练步数（如观测前 50 步外推至 1000 步），在域内和外推基准上匹配或超越完整 RLVR 性能。
- 外推因子可达 10~20× 观察窗口，且性能随步数继续改善，无上限迹象。
- 消融证实增加子空间秩或非线性建模不带来额外增益，方法具极简充分性。
