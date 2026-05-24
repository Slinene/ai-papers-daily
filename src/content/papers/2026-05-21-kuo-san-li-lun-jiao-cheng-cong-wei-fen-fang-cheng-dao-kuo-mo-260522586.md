---
title: 'A Tutorial on Diffusion Theory: From Differential Equations to Diffusion Models'
title_zh: 扩散理论教程：从微分方程到扩散模型
authors:
- Jiayi Fu
- Yuxia Wang
affiliations:
- INSAIT
- Sofia University "St. Kliment Ohridski"
arxiv_id: '2605.22586'
url: https://arxiv.org/abs/2605.22586
pdf_url: https://arxiv.org/pdf/2605.22586
published: '2026-05-21'
collected: '2026-05-24'
category: Training
direction: 扩散模型理论统一框架
tags:
- diffusion models
- SDE
- ODE
- score matching
- DDPM
- DDIM
one_liner: 用微分方程统一推导扩散模型的前向/反向过程，阐明训练目标与采样方法的关系
practical_value: '- 理解DDPM与DDIM的采样本质（反向SDE vs 反向ODE），在生成式推荐中可根据速度与质量需求选择合适的采样器。

  - 分类器指导和无分类器指导的推导可用于条件生成（如基于用户属性的商品图片生成），直接提升生成内容的相关性。

  - DPM-Solver等快速采样方法可加速扩散模型的推理，降低线上延迟。

  - 训练目标的等价性（噪声预测=分数匹配）允许灵活选择损失函数，简化实现。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

动机：扩散模型缺乏从微分方程视角的统一数学推导，使得训练和采样之间的联系不够清晰。本文从条件高斯前向过程出发，逐步导出完整的扩散理论框架。

方法：首先定义条件前向路径，给出对应的ODE和SDE表示；通过数据分布平均得到边缘前向过程，它同样可由ODE或SDE生成。然后推导反向过程，得出反向SDE和概率流ODE，两者均依赖于边际分数函数。训练目标即为分数匹配，与常见的噪声预测损失等价。采样方面，介绍了离散化的反向SDE（DDPM）、反向ODE（DDIM）以及高阶求解器DPM-Solver，并讨论分类器指导和无分类器指导的数学形式。

关键结果：证明了DDPM和DDIM共享同一训练目标，但DDPM采样对应离散反向SDE，DDIM对应离散反向ODE，因此DDIM可更少步数生成。提供了完整的理论脉络，将主流方法纳入统一框架。
