---
title: 'SoftServe: A Scalable Quasi-Newton Method for Deep Learning'
title_zh: SoftServe：面向深度学习的可扩展拟牛顿法
authors:
- Joohwan Ko
- Tetiana Parshakova
- Diana Cai
- Robert M. Gower
affiliations:
- University of Massachusetts Amherst
- CCM, Flatiron Institute
- Cornell University
arxiv_id: '2610.02182'
url: https://arxiv.org/abs/2610.02182
pdf_url: https://arxiv.org/pdf/2610.02182
published: '2026-10-01'
collected: '2026-10-04'
category: Training
direction: 深度学习优化 · 拟牛顿法
tags:
- Quasi-Newton
- Optimization
- Second-order
- Deep Learning
- Newton-Schulz
- Kronecker-factored
one_liner: 提出无需线搜索和曲率修正的可扩展拟牛顿族 SoftServe，通过正定曲率估计与 Newton-Schulz 迭代训练大规模网络
practical_value: '- 推荐/广告模型常存在病态优化区域：长尾 item/user embedding 梯度方差大、多任务 loss 尺度差异显著。可尝试
  SoftServe 的 diagonal 曲率预处理，作为 Adam 的替代或 warmup 后切换，减少手调 epsilon/weight decay 的敏感性。

  - 工业级推荐模型参数巨大，Kronecker-factored 变体可对 layer-wise 曲率做结构化近似，类似 K-FAC 但保证正定，适合 Transformer/特征交互层；工程上用
  Newton–Schulz 迭代通过矩阵乘法实现，便于 GPU/TPU 加速。

  - 该方法强调无需 line search，减少分布式训练中的通信与超参搜索成本；在离线 CTR/CVR 或召回模型训练中，可先在病态子任务（如 autoencoder
  特征压缩、辅助 loss）上验证收敛速度与最终 loss。

  - 注意：论文主要面向通用深度学习优化，不是推荐/检索架构本身；落地前需评估其对稀疏 embedding、动态数据流和在线更新的兼容性，初期以离线对比实验为主。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：Quasi-Newton（QN）方法在大规模凸优化中很强，但深度学习的非凸性和海量参数阻碍其应用；现有二阶方法常依赖线搜索或临时曲率修正，难以扩展到大型网络。

**方法关键点**：SoftServe 从 Berglund et al. 的变分目标导出正定曲率估计，即使 Hessian 存在负曲率也能保证正定性；提出 diagonal 与 Kronecker-factored 两种参数化，天然保持正定并扩展到大规模神经网络；用稳定的 coupled Newton–Schulz 迭代完成矩阵运算，以 GPU 友好的矩阵乘法替代昂贵的矩阵分解；无需线搜索和 ad hoc 曲率修正。

**关键结果**：在严重病态问题上优于 Adam、Muon、SOAP，包括循环网络、深度自编码器、物理信息神经网络，以及 136M 参数的物理信息扩散模型，常取得更低损失。
