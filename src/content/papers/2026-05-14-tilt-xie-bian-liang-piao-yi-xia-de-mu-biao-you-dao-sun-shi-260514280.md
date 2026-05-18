---
title: 'TILT: Target-induced loss tilting under covariate shift'
title_zh: TILT：协变量漂移下的目标诱导损失倾斜
authors:
- Kakei Yamamoto
- Martin J. Wainwright
affiliations:
- Massachusetts Institute of Technology
arxiv_id: '2605.14280'
url: https://arxiv.org/abs/2605.14280
pdf_url: https://arxiv.org/pdf/2605.14280
published: '2026-05-14'
collected: '2026-05-18'
category: Training
direction: 无监督域适应 · 重要性加权 · 协变量漂移
tags:
- domain adaptation
- covariate shift
- importance weighting
- loss penalty
- empirical risk minimization
- unsupervised learning
one_liner: 通过分解源预测器为 f+b 并在目标无标签数据上惩罚 b，实现无需密度比估计的隐式重要性加权域适应
practical_value: '- 在电商推荐中，训练集与线上分布不符时，可将推荐模型分解为共享主体（f）和域偏置（b），用目标域无标签曝光数据惩罚 b 来矫正分布差异，部署时仅使用
  f，避免密度比估计的不稳定。

  - 该方法对正则化超参数不敏感，实验中在一个宽范围内表现稳定，适合工业场景调参困难的问题。

  - 理论保证了即使源目标域支持不相交，b 的范数仍一致有界，避免极端偏移下的失效，可应用于用户群体差异巨大的跨市场推荐。

  - 实现简单：只需在原损失中增加目标侧对 b 的惩罚项，支持任何梯度下降框架，可快速集成到现有模型中。'
score: 6
source: arxiv-stat.ML
depth: abstract
---

动机：预测模型从源域训练后部署到分布不同的目标域（协变量漂移），直接源训练会偏向源分布，而标准重要性加权需要估计密度比，在高维或支持不重叠时失败。

方法关键点：提出 TILT，将源模型表示为 $f+b$，在带标签源数据上拟合 $f+b$，同时在无标签目标数据上惩罚辅助函数 $b$ 的某种范数。最终只使用 $f$ 作为目标预测器。这种目标侧惩罚在总体上隐式诱导了重要性加权，但权重通过自局部化的 $b^*_f$ 确定，对任意源-目标对保持有界。理论给出了有限样本超额风险 oracle 不等式，并对稀疏 ReLU 网络给出端到端保证。

关键结果：在可控回归任务和 shifted CIFAR-100 蒸馏上，TILT 均优于纯源训练、精确重要性加权及相对密度比基线，且性能对正则化参数取值不敏感，展示了实用鲁棒性。
