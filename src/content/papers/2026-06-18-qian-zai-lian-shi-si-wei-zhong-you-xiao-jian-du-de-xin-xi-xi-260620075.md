---
title: 'What Makes Effective Supervision in Latent Chain-of-Thought: An Information-Theoretic
  Analysis'
title_zh: 潜在链式思维中有效监督的信息论分析
authors:
- Xinghao Chen
- Chak Tou Leong
- Wenjin Guo
- Jian Wang
- Wenjie Li
- Xiaoyu Shen
affiliations:
- Ningbo Institute of Digital Twin, Eastern Institute of Technology
- Department of Computing, The Hong Kong Polytechnic University
arxiv_id: '2606.20075'
url: https://arxiv.org/abs/2606.20075
pdf_url: https://arxiv.org/pdf/2606.20075
published: '2026-06-18'
collected: '2026-06-19'
category: Reasoning
direction: 潜在链式推理的监督优化
tags:
- Latent CoT
- Information Theory
- Process Supervision
- Trajectory Supervision
- Space Supervision
- Mutual Information
one_liner: 信息论分析揭示潜在CoT双坍塌，提出轨迹与空间监督，发现生成式重建优于几何压缩，建立信息-性能绑定
practical_value: '- 在搜索推荐系统中若采用隐式CoT进行多步推理（如用户意图推断、推荐理由生成），不应仅依赖结果监督，应引入轨迹监督向中间隐状态注入步骤级信号，并利用空间监督保持隐空间语义结构，防止语义漂移。

  - 避免将隐状态强行对齐到离散符号（如MSE回归到思维token），该做法会压缩推理空间；改用生成式重建（自解码器生成推理步骤）作为更灵活的语义锚，可更好地保留信息容量，提升复杂推荐任务的推理质量。

  - 可借鉴统一潜在探针（ULP）的设计，通过测量隐轨迹与显式推理步骤的互信息，监控推荐模型中隐式推理过程的信息保真度，作为训练质量的评价指标，指导优化方向。

  - 论文证实推理准确率与隐链信息保真度强绑定，因此在需要多步逻辑推理的推荐场景（如用户兴趣演化建模）中，应优先优化隐状态与推理逻辑的互信息，而非仅关注最终推荐指标。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：潜在链式思维（Latent CoT）在连续隐状态中进行推理，虽省去显式生成，但纯结果监督导致信号微弱，隐轨迹易发生语义漂移，推理鲁棒性差。
**方法**：从信息论角度分析，将失败归因于双坍塌——优化路径上的梯度衰减和表示空间中的语义漂移。将过程监督分解为两个互补维度：**轨迹监督**，沿隐状态序列注入稠密的逐步推理信号；**空间监督**，维持隐流形的语义结构。对比发现，硬性几何压缩（如将隐状态对齐到离散思维token）会限制推理空间，而**生成式重建**（用解码器从隐状态重建推理步骤）作为语义锚点更灵活，能更好保留信息容量。为量化效果，提出**统一潜在探针（ULP）**，测量隐轨迹与显式推理步骤间的互信息，揭示出明确的**信息-性能绑定**：推理准确率依赖于隐链中保留的信息保真度。
**关键结果**：生成式空间监督显著优于几何压缩，验证了信息保真度与任务性能的强正相关。实验确立了以互信息最大化为导向的潜在推理监督原则框架。
