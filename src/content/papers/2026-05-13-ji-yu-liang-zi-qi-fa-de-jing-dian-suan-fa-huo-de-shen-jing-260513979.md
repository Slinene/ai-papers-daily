---
title: Winning Lottery Tickets in Neural Networks via a Quantum-Inspired Classical
  Algorithm
title_zh: 基于量子启发的经典算法获得神经网络中奖彩票
authors:
- Natsuto Isogai
- Hayata Yamasaki
- Sho Sonoda
- Mio Murao
affiliations:
- The University of Tokyo
- RIKEN AIP
- CyberAgent
arxiv_id: '2605.13979'
url: https://arxiv.org/abs/2605.13979
pdf_url: https://arxiv.org/pdf/2605.13979
published: '2026-05-13'
collected: '2026-05-18'
category: Training
direction: 去量子化彩票采样算法
tags:
- lottery ticket hypothesis
- sparse subnetwork
- quantum-inspired
- dequantization
- ridgelet transform
- sampling
one_liner: 提出量子启发的多项式时间经典算法，高效采样稀疏子网络，性能媲美精确采样
practical_value: '- 对于推荐系统大模型，可借鉴该采样方法快速选取可训练子网络，降低训练成本；利用脊波变换优化的概率分布，比随机剪枝更可靠。

  - 算法复杂度与数据维度多项式相关，可在经典硬件上实现，适合工业界直接部署，无需量子硬件。

  - 去量子化思路提示：某些量子加速算法可能存在高效的经典对应，可尝试类似思路简化现有采样或搜索模块。

  - 该方法在浅层网络上验证有效，可实验迁移至深层网络或Transformer结构，用于Embedding层或Attention头的稀疏化。'
score: 6
source: arxiv-stat.ML
depth: abstract
---

**动机**：量子机器学习算法能高效从大神经网络中采样稀疏子网络，但经典实现面临指数复杂度，实际无法应用。本文旨在构建多项式时间的经典替代算法，去除对量子硬件的依赖。

**方法**：受量子算法启发，构建了基于脊波变换（ridgelet transform）的经典采样算法。该算法不直接处理指数多的候选隐藏节点，而是通过脊波变换定义优化概率分布，然后采用经典随机过程（如带重启的随机游走）在O(poly(D))时间内完成采样，其中D为数据维度。算法关键点包括：利用脊波变换将网络函数表示为积分形式，进而导出节点采样概率；通过去量子化技巧将量子采样过程转为经典多项式过程。

**结果**：数值实验表明，该经典采样器取得的经验风险与精确采样相当，显著优于未优化的均匀采样；运行时间相比经典暴力实现呈指数级加速，且随数据维度D多项式增长，验证了经典多项式算法可完全实现量子算法的采样效果。
