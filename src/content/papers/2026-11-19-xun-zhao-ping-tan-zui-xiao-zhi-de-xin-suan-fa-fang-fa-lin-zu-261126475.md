---
title: 'A new algorithmic approach for finding flat minima: critically damped Polyak
  stepsizes'
title_zh: 寻找平坦最小值的新算法方法：临界阻尼 Polyak 步长
authors:
- Francesco Caporali
- Jason M. Altschuler
- Boris Hanin
arxiv_id: '2611.26475'
url: https://arxiv.org/abs/2611.26475
pdf_url: https://arxiv.org/pdf/2611.26475
published: '2026-11-19'
collected: '2026-11-22'
category: Training
direction: 优化器设计 · 平坦最小化
tags:
- Flat Minima
- Adaptive Stepsize
- Polyak Stepsize
- Sharpness-Aware Minimization
- Optimization
- Generalization
one_liner: 提出 CDP 自适应步长规则，以有限学习率收敛到最小化锐度的平坦解，无需额外梯度计算
practical_value: '- 在训练深度推荐模型（如 DeepFM、DIN、多任务模型）时，可尝试用 CDP 步长替代 Adam/SGD：它提供类似 SAM
  的平坦性偏差但无需双倍梯度计算，适合大规模稀疏特征场景下的训练效率与泛化平衡。

  - 对于过参数化的召回/排序模型，CDP 的步长随距离最小流形收缩的特性有助于收敛到低锐度插值解，可减少线下过拟合、提升线上 A/B 稳定性。

  - LLM 微调（如用 LLM 做 query 理解、商品文案生成）中，论文显示 CDP 能降低 sharpness，可将其作为 AdamW 的补充或替换，在低资源微调下验证其对下游任务泛化的影响。

  - 工程实现上，CDP 只需基于损失和梯度计算自适应步长，改动成本低；可先在中小模型上扫步长范围，观察 loss landscape 平坦度与验证集指标的关系。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：过参数化模型存在大量全局最小，平坦最小通常对应更好泛化。现有平坦性方法如 SAM 需要额外梯度计算，normalized GD 虽有平坦性偏差但步长不收缩、收敛有限。目标是设计一个自适应步长规则，既能偏向平坦最小，又能以有限学习率收敛。

**方法关键点**：提出 critically damped Polyak (CDP) 步长，将经典 Polyak 规则乘以 4 和一个温和阻尼因子。因子 4 使迭代在最小值流形 M 附近产生等幅振荡，阻尼则驱动收敛到 M。当损失较小时，投影迭代沿 M 遵循关于最大特征值 log λ1(∇²L) 的梯度下降，产生平坦性偏差。与 normalized GD 不同，CDP 步长随到 M 的距离缩小，使得在有限学习率下收敛到局部最小化锐度的插值解。理论适用于具有局部二次 Morse-Bott 结构的非负损失，覆盖光滑过参数化神经网络的规则插值区域。

**关键结果**：建立了 sharpness 和 loss reduction 的 uniform-in-time 保证；实验显示 CDP 产生与 Sharpness-Aware Minimization (SAM) 类似的平坦化效果，在非线性 teacher-student 网络和预训练 LLM 微调中也能降低锐度。
