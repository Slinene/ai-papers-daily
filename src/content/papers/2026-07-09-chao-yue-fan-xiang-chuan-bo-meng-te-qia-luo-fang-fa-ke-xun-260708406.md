---
title: 'Beyond Backpropagation: Monte Carlo Method Can Train Deep Neural Networks'
title_zh: 超越反向传播：蒙特卡洛方法可训练深度神经网络
authors:
- Hong Zhao
affiliations:
- Department of Physics, Xiamen University
- Lanzhou Center for Theoretical Physics, Lanzhou University
arxiv_id: '2607.08406'
url: https://arxiv.org/abs/2607.08406
pdf_url: https://arxiv.org/pdf/2607.08406
published: '2026-07-09'
collected: '2026-07-13'
category: Training
direction: 蒙特卡洛无梯度训练方法
tags:
- Monte Carlo training
- gradient-free optimization
- deep neural networks
- pruning
- discrete weights
- unconventional transfer functions
one_liner: 用最简单的随机突变-保留蒙特卡洛算法在单GPU上训练深层网络，无需梯度、归一化或残差连接
practical_value: '- **离散权重训练**：可直接训练低比特量化模型，适合需要极端压缩的端侧推荐模型，避免量化后微调。

  - **纯剪枝训练**：在训练过程中维持稀疏连接，省去传统“训练-剪枝-重训”流程，可集成到推荐模型压缩 pipeline 中。

  - **不可微目标优化**：当损失函数不可微或硬件不支持高效 BP 时，提供备选方案，例如基于规则或模拟环境的推荐策略学习。

  - **主要学术贡献**：收敛速度极慢，目前不适合工业级大规模推荐在线训练，但可关注后续加速变体在小样本离线调优中的应用。'
score: 7
source: arxiv-stat.ML
depth: abstract
---

**动机**：反向传播依赖梯度，带来梯度消失和爆炸问题；探索替代方案一直是 AI 的目标。  
**方法**：提出一种极度简化的蒙特卡洛算法——随机扰动一个参数，若损失下降则保留，否则重试。该无梯度方法在单 GPU 上实现，可直接训练深层网络，无需批量归一化或残差连接。其灵活性还体现在：支持纯剪枝训练（直接学习稀疏网络）、离散权重、非标准传递函数（如高斯函数），并揭示了深度网络的冗余性。  
**结果**：在超过 20 层的深度网络、单隐层宽达 16384 神经元的网络及简单 Transformer 上验证，完成 MNIST 图像分类和 Tiny Shakespeare 字符级语言建模，证明该方法可行。
