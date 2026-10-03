---
title: 'Trust the Direction, Search the Step: Zero-and-First-Order Methods for LLM
  Fine-Tuning'
title_zh: 信任方向，搜索步长：LLM微调的零阶与一阶方法
authors:
- Cristian McGee
- El Houcine Bergou
- Aritra Dutta
affiliations:
- University of Central Florida
- Mohammed VI Polytechnic University
arxiv_id: '2610.02190'
url: https://arxiv.org/abs/2610.02190
pdf_url: https://arxiv.org/pdf/2610.02190
published: '2026-10-01'
collected: '2026-10-03'
category: Training
direction: LLM微调优化 · 零阶一阶混合步长选择
tags:
- Zero-Order Optimization
- First-Order Optimization
- Step-size Selection
- LLM Fine-tuning
- Adaptive Optimization
one_liner: 提出ZFO框架，用一阶优化器定方向，沿一维子空间做零阶评估选步长，成本低于线搜索
practical_value: '- 在微调用于排序、召回或Agent决策的LLM时，可尝试ZFO自适应步长替代固定学习率或余弦退火，减少手动调参，训练后期或小数据集上可能提升稳定性。

  - ZFO仅额外增加两次前向传播（无额外反向），成本极低，可作为插件直接嵌入现有AdamW等训练流程，无需重写优化器。

  - 方法解耦方向与步长：保持一阶方向不变，仅动态调整沿该方向的移动距离，能应对损失地形变化，降低训练崩溃风险。

  - 实现时注意局部模型选择：论文表明不同目标偏好不同局部模型（如二次/三次），可对验证损失做快速搜索选择，无需复杂超参。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：步长选择是神经网络优化核心难题，保守步长收敛慢，激进步长易失稳。现有方法多依赖启发式或手动调参，缺乏自适应机制。

**方法关键点**：ZFO框架解耦方向与步长——使用可信的一阶优化器（如AdamW）确定更新方向，仅沿该一维子空间做两次额外目标函数评估（零阶），利用当前梯度信息和这两个函数值构建局部模型（二次或三次），在有限搜索区间内选择曲率感知的步长。相比完整线搜索，成本更低。

**理论保证**：证明共享样本评估能产生可靠的有限差分曲率估计；局部模型在搜索区间内选择近最优步长；ZFO收敛到稳定点邻域。

**关键结果**：在多种语言模型和数据集上，ZFO相比固定步长一阶基线经常改善优化过程和最终性能，提升幅度和最优局部模型形式取决于具体目标函数。
