---
title: Stochastic Gradient Optimization with Model-Assisted Sampling
title_zh: 基于模型辅助采样的随机梯度优化
authors:
- Jonne Pohjankukka
- Jukka Heikkonen
affiliations:
- University of Turku, Department of Computing
arxiv_id: '2606.27171'
url: https://arxiv.org/abs/2606.27171
pdf_url: https://arxiv.org/pdf/2606.27171
published: '2026-06-25'
collected: '2026-06-27'
category: Training
direction: 训练优化 · 梯度估计方差削减
tags:
- variance reduction
- gradient estimation
- model-assisted sampling
- stochastic optimization
- survey sampling
- AdamW
one_liner: 将调查抽样中的模型辅助估计引入小批量梯度计算，构造更低方差的梯度估计器，可无缝嵌入现有优化器
practical_value: '- 训练推荐模型（如 CTR/CVR 预估）时，可用该方法替代默认的均匀小批量采样，降低梯度方差，加速收敛，尤其适于中等维度特征空间场景。

  - 与 AdamW 等带动量的优化器组合时，能在约一半训练轮次达到同等或更好泛化，适合大规模工业模型缩短训练周期。

  - 实现简单：只需在数据加载器中替换采样逻辑，并维护一个轻量辅助模型（如一个小型预测网络），不改变优化器内部更新规则，工程侵入性低。

  - 可借鉴其“辅助信息”思路：在搜索/推荐系统中，利用曝光偏差、用户活跃度等先验知识构建采样权重，进一步降低在线学习中的梯度估计误差。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：深度学习常用小批量随机梯度下降，梯度估计的噪声影响收敛稳定性和泛化。现有方差削减方法（如 SVRG）往往增加额外计算开销或改变优化动态。

**方法关键点**：将训练集视为有限总体，梯度视为基于样本的估计，引入调查抽样理论中的**模型辅助采样**。核心是构造一个辅助梯度预测模型（如一个轻量网络），利用它和当前样本梯度共同修正批量估计，得到更低方差的梯度估计量。均匀随机采样是该框架在无辅助信息时的特例。该方法与任何优化器（SGD、AdamW等）兼容，只需在构建批量时按设计采样或加权，不干扰优化器内部步骤。

**关键结果**：在合成数据和6个基准数据集上，71-86% 的实验配置取得性能提升。尤其带动量的优化器（如 AdamW）获益明显：在约一半训练 epoch 时即达到或超越基线完整训练后的泛化水平，表明加速收敛且噪声抑制有效。方法对于中等规模输入维度效果最突出。
