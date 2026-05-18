---
title: Skew-adaptive conformal prediction
title_zh: 偏度自适应共形预测
authors:
- Paulo C. Marques F.
- Helton Graziadei
affiliations:
- Insper Institute of Education and Research
- Federal University of São Carlos
arxiv_id: '2605.16145'
url: https://arxiv.org/abs/2605.16145
pdf_url: https://arxiv.org/pdf/2605.16145
published: '2026-05-15'
collected: '2026-05-18'
category: Other
direction: 局部偏度自适应的共形预测区间
tags:
- conformal prediction
- prediction intervals
- local skewness
- asymmetric intervals
- uncertainty quantification
- regression
one_liner: 提出偏度自适应共形预测方法，通过不对称区间和逆双曲正弦变换学习局部偏度，提升预测区间效率。
practical_value: '- 电商销量、转化率等回归目标常呈偏态分布，利用局部偏度建模可构建更紧的预测区间，提升业务决策可靠性。

  - 逆双曲正弦变换处理带符号残差，作为额外模型训练目标，巧妙提取偏度信息，可复用到类似的不确定性量化任务。

  - 提出的校准样本宽度比估计量能在离线评估时预估线上区间宽度改善，无需测试集，适合线上模型迭代。

  - 方法基于拆分共形预测，保持有限样本边际有效性，可与任意点预测模型组合，工程实现简单，适合高灵活性的ML系统。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：经典共形预测方法（如局部尺度分数）能产生自适应宽度的预测区间，但忽略了残差的局部偏度，导致区间效率不足，尤其在偏态分布下。

**方法**：从基于点预测的不对称区间族出发，用gauge方法导出相应的一致性分数。关键创新是将带符号尺度化残差经过逆双曲正弦变换（asinh），作为额外预测模型的训练目标，让模型学习特征空间中的局部偏度。最终区间通过不对称扩展常规对称区间得到，保持拆分共形预测的有限样本边际有效性。

**结果**：在多个数据集上，偏度自适应区间相比scaled-score和conformalized quantile regression宽度更窄，同时保持标称覆盖率；提出的校准样本宽度比估计量能准确逼近测试集上的平均宽度比，无需测试数据即可预估效率增益。
