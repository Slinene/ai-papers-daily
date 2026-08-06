---
title: 'MALT: Lightweight Curvature-Aware Muon via Diagonal Preconditioning'
title_zh: MALT：通过对角线预处理实现轻量级曲率感知的Muon优化器
authors:
- Tongle Wu
- Huanyu Dong
- Ying Sun
- Ziye Ma
affiliations:
- The Pennsylvania State University
- City University of Hong Kong
arxiv_id: '2608.05088'
url: https://arxiv.org/abs/2608.05088
pdf_url: https://arxiv.org/pdf/2608.05088
published: '2026-08-05'
collected: '2026-08-06'
category: Training
direction: Muon优化器的曲率感知对角线预处理
tags:
- Muon
- Curvature Preconditioning
- Diagonal Preconditioning
- LLM Pretraining
- Optimizer
- Stochastic Optimization
one_liner: 在Muon正交化前加入行/列对角预处理，以极小开销缓解曲率各向异性，配合噪声自适应步长显著提升LLM预训练性能
practical_value: '- 在推荐模型的矩阵参数（如Embedding、MLP权重）上可直接替换Muon为MALT，在不增加显存和时间的前提下获得更优收敛，尤其适合需要降低训练成本的工业场景。

  - 噪声自适应步长MALTER可稳定分布式推荐训练中常见的梯度噪声，避免手动调参，提升训练鲁棒性。

  - 对角线预处理与正交化结合的思想可迁移到其他矩阵感知优化器（如Shampoo变体），为结构化参数提供轻量曲率适应。

  - 对于曲率各向异性明显的Transformer层（如FFN或Attention投影），建议优先使用MALT，在保持Muon原有优势的同时进一步加速收敛。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**  
Muon优化器通过正交化动量矩阵减少梯度各向异性，但并未显式考虑损失地形的曲率各向异性，导致在病态Hessian下收敛缓慢。现有工作如Shampoo、FISMO等虽然引入曲率信息，但需要存储稠密因子或进行矩阵求逆/特征分解，开销巨大。本文旨在以极低开销弥补Muon的这一短板。

**方法关键点**  
- 基于局部二次近似构建预处理空间：将正定曲率代理的对角线平方根作为线性变换，在该空间中正交化以同时处理曲率各向异性和梯度各向异性。  
- 轻量级对角线预处理：对每个矩阵参数，维护行/列梯度平方范数的EMA，分别取-1/8次幂形成左、右对角预处理矩阵 \(L_t, R_t\)，动量经 \(L_t M_t R_t\) 变换后再正交化。存储开销仅为 \(O(m+n)\)，无密集运算。  
- 范数嫁接（norm grafting）：用正交化方向的F范数作为更新幅度，避免预处理导致步长过激。  
- MALTER自适应变体：在预处理空间用Adam风格的标量二阶矩估计调整步长，以抵抗随机梯度噪声，仅引入一个标量状态。  
- 收敛性分析：在非凸随机优化框架下证明MALT收敛，复杂度为 \(O(\delta^{-4})\)。

**关键实验**  
在OpenWebText上预训练GPT-2 Small（124M）、Medium（355M）、Large（774M），对比AdamW、Muon。MALT在所有规模上验证损失均低于Muon，而MALTER进一步降低，例如在Small上比Muon低0.0241，Medium低0.0277，Large低0.0164。内存和每步墙钟时间几乎与Muon相同（Medium模型MALTER仅比Muon多约1ms/步）。此外，对角线预处理矩阵的条件数随训练动态变化，表明其非平凡。

**核心洞见**  
“对角线预处理与正交化互补，以极小开销解决了Muon对曲率各向异性的敏感问题，配合噪声自适应步长可获得显著提升。”
