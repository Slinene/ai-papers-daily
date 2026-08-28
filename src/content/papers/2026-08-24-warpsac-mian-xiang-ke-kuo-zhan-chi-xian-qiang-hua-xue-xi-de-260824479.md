---
title: 'WarpSAC: Towards the Pinnacle of Scalable Off-policy RL by Rethinking Exploration
  and Exploitation'
title_zh: WarpSAC：面向可扩展离线强化学习的数据范式自适应算法
authors:
- Zihao Wu
- Hongyao Tang
- Yi Ma
- Huizhong Song
- Pengyi Li
- Yifu Yuan
- Fei Ni
- Jinyi Liu
- Wei Wei
- Jianrong Wang
affiliations:
- Tianjin University
- Shanxi University
- Imperial College London
arxiv_id: '2608.24479'
url: https://arxiv.org/abs/2608.24479
pdf_url: https://arxiv.org/pdf/2608.24479
published: '2026-08-24'
collected: '2026-08-28'
category: Other
direction: 离线强化学习规模化训练方法
tags:
- Off-policy RL
- Scalable RL
- Data Regime
- Sample Weight Decay
- GPU Parallel
- Stabilizers
one_liner: 提出数据范式感知的离线强化学习算法 WarpSAC，根据数据丰富度动态调整稳定器配置，大幅提升大规模并行训练性能
practical_value: '- 数据范式感知的稳定器配置：在在线学习/强化学习推荐中，当数据吞吐量大幅提升（如实时日志流、大规模并行仿真），可关闭参数归一化并简化
  critic 为 single-Q，减少计算瓶颈并提升价值拟合能力；在数据稀疏或覆盖度低时保留归一化与 clipped double-Q。

  - Sample Weight Decay 可借鉴为按样本年龄做衰减加权，赋予新样本更高权重，有助于模型快速适应分布漂移，适用于推荐系统、Agent 决策策略的在线更新。

  - 大规模并行训练中，传统稳定器（如归一化、double-Q）可能由优势变为制约，应根据数据覆盖度做消融实验而非沿用默认配置，这与大规模分布式训练中参数同步策略的选择有相似逻辑。

  - 对于 Agent 仿真到真实（sim-to-real）部署，参考 regime-aware 配置思路，根据仿真数据规模选择不同训练设置，可显著缩短 wall-time
  迭代周期。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：大规模并行模拟改变了离线强化学习的数据范式，传统稳定器（参数归一化、clipped double-Q、年龄偏置重放加权）最初为数据有限场景设计，在高吞吐多样数据下可能不再最优。

方法关键点：通过八个基准族的受控实验，揭示稳定器具有强数据范式依赖性：数据有限时参数归一化有助于，但数据丰富时限制了价值拟合；clipped double-Q 可在高吞吐操作中安全放宽；年龄偏置重放加权普遍提升学习效率，尤其在网络容量有限时。据此提出 WarpSAC，采用 Sample Weight Decay（样本权重衰减）实现高效利用，并提供两种预设变体：WarpSAC-L（开启归一化和 clipped double-Q）用于数据有限的 CPU 规模训练；WarpSAC-A（关闭归一化，single-Q）用于数据丰富的 GPU 并行训练。

关键结果：相比 FlashSAC，WarpSAC 在九个 CPU 环境上 normalized score-step AUC 提升 4.5%，在十四个 GPU 并行环境上提升 23.1%；将 UnitreeG1TransportBox-v1 成功率从 19.8% 提升至 96.4%，MuJoCo Playground 平均归一化 wall-time AUC 提升 19.1%，sim-to-real 部署 wall time 缩短 36.4%。
