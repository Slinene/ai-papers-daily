---
title: 'Overcoming Dynamics-Blindness: Training-Free Pace-and-Path Correction for
  VLA Models'
title_zh: 克服动态盲区：面向VLA模型的免训练步速与路径校正
authors:
- Yanyan Zhang
- Chaoda Song
- Vikash Singh
- Xinpeng Li
- Kai Ye
- Zhe Hu
- Zhongzhu Pu
- Yu Yin
- Vipin Chaudhary
affiliations:
- Case Western Reserve University
- The Hong Kong Polytechnic University
- Tsinghua University
- InspireOmni AI
arxiv_id: '2605.11459'
url: https://arxiv.org/abs/2605.11459
pdf_url: https://arxiv.org/pdf/2605.11459
published: '2026-05-13'
collected: '2026-05-17'
category: Agent
direction: 具身智能 · 动作块时域校正
tags:
- VLA
- Dynamics-Blindness
- Training-Free
- Action Chunking
- Temporal Consistency
- Robotics
one_liner: 提出训练无关的步速与路径校正模块，以闭式解统一修正VLA动作块在动态场景下的时域不一致性
practical_value: '- 动作块预测与时域动态不匹配的问题在推荐系统的序列决策中同样存在（如用户兴趣漂移），pace-path 分解的思路可以启发将预测序列校
  正解耦为“强度调整”和“方向微调”，提升模型在非平稳环境下的鲁棒性。

  - 免训练的推理时校正算子可以作为即插即用的外挂模块，适配现有模型而不需重训，在线上快速修正预测偏差，降低工程落地成本。

  - 将动态环境的影响抽象为两个正交分量的闭式解，这一设计可借鉴到 Agent 多步规划的在线修正，在状态变化时实时微调动作序列，避免完全重规划。

  - 在电商推荐中，类似动态环境的用户行为变化，可利用该思想对生成的推荐序列进行在线校准，平衡探索与执行效率。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：现有 VLA 模型通常基于单帧观测预测固定长度动作块，对时域动态先天盲视，导致在非稳态环境（如传送带、外部扰动）中成功率大幅下降。已有方案要么需要昂贵的重训，要么引入延迟和块间一致性差。

方法：提出 Pace-and-Path Correction，一个免训练、闭式的推理时算子，可包裹任意块动作 VLA。通过单一二次代价函数的联合优化，解耦为两个正交通道：**pace 通道**沿原规划方向压缩或拉伸执行速度，**path 通道**施加正交空间偏移，共同吸收感知到的环境动态。该算子即插即用，无需额外训练或微调。

结果：在专门构建的 MoveBench 基准（仅控制运动变量以分离动态影响）上，该方法在纯动态环境将基础 VLA 成功率绝对提升最多 28.8%，在动-静态混合环境提升 25.9%，显著超越现有免训练 wrapper 和动态自适应方法。
