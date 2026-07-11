---
title: Systematic Evaluation of Learning Rate Scheduling Strategies Across Heterogeneous
  Architectures
title_zh: 异构架构下学习率调度策略的系统评估
authors:
- Hafsa Mateen
- Radu Timofte
- Dmitry Ignatov
affiliations:
- Computer Vision Lab, CAIDAS & IFI, University of Würzburg, Germany
arxiv_id: '2607.08511'
url: https://arxiv.org/abs/2607.08511
pdf_url: https://arxiv.org/pdf/2607.08511
published: '2026-07-09'
collected: '2026-07-11'
category: Training
direction: 训练超参数：学习率调度策略评估
tags:
- Learning Rate Schedule
- Hyperparameter Optimization
- Training Strategies
- Cosine Annealing
- Cyclic LR
one_liner: 大规模实验表明 CosineAnnealingWarmRestarts 与 CyclicLR 普遍优于基础衰减，调度选择高度依赖架构
practical_value: '- 训练深度推荐模型（如 CTR 预估、双塔召回）时，可直接用 CosineAnnealingWarmRestarts 或 CyclicLR
  作为默认调度，替代阶梯衰减，以提升收敛速度与泛化能力

  - 调度器选择应与模型架构绑定：不同结构（DNN、Transformer、DeepFM）对调度敏感度差异大，建议针对具体架构做小规模网格搜索

  - 在大规模超参优化中，将学习率调度视为一级超参数，联合基础学习率与调度配置进行自动搜索，可能带来显著收益

  - 对于强化学习 Agent 训练，周期性重启学习率（如 CosineAnnealingWarmRestarts）有助于跳出局部最优，可尝试引入到策略梯度或 Q-learning
  训练中'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：学习率调度对训练收敛、最终精度和泛化影响巨大，但实践中常被当作次要超参数而随意固定。现有 AutoML 方法也常忽略调度空间的系统探索，缺乏跨架构的调度选择指导。

**方法**：利用 LEMUR 神经网络数据集中的 30 个代表性架构（覆盖卷积和 Transformer 家族），通过自动化源码注入，在 PyTorch 下测试了 9 大调度器家族的 25 种配置（包括 StepLR、ExponentialLR、CosineAnnealingLR、CosineAnnealingWarmRestarts、CyclicLR 等），在 CIFAR-10 上总计评估 3938 个模型变体。

**关键结果**：
- 最佳单次配置达到 86.45% top-1 准确率，237 个变体超过 80%。
- CosineAnnealingWarmRestarts 和 CyclicLR 在所有架构中稳定优于基础衰减策略。
- 调度器的最优选择高度依赖具体架构，不存在单一万能调度。
- 构建的准确率全景图已贡献给 LEMUR 数据集，可作为深度网络训练中原则性选择调度器的参考基准。
