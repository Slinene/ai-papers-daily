---
title: 'Ribbon: Scalable Approximation and Robust Uncertainty Quantification'
title_zh: 'Ribbon: 可扩展近似与鲁棒不确定性量化'
authors:
- Graham Gibson
- John Tipton
- Kellin Rumsey
- Natalie Klein
arxiv_id: '2606.27269'
url: https://arxiv.org/abs/2606.27269
pdf_url: https://arxiv.org/pdf/2606.27269
published: '2026-06-25'
collected: '2026-06-27'
category: Eval
direction: 贝叶斯自举近似 · 影响函数线性化
tags:
- uncertainty quantification
- Bayesian bootstrap
- influence function
- calibration
- scalable approximation
- Dirichlet reweighting
one_liner: 用影响函数线性化近似狄利克雷加权自举，免去模型重训练，实现可扩展且校准良好的不确定性估计
practical_value: '- 在已训练好的点击率或转化率预估模型上，用 Ribbon 快速计算预测不确定性，无需重训练，可直接集成到在线探索策略（如 Thompson
  采样）中。

  - 依赖影响函数线性化，只需梯度或 Hessian 向量积，实现与 Laplace 近似同阶成本，但模型误设时恢复稳健三明治协方差，更适合动态变化的推荐环境。

  - 浓度参数 α 可在验证集上调优，相当于对不确定性尺度进行校准；可借鉴至推荐模型的校准流程，提升 ECE 等指标。

  - 对于搜索广告等大型模型，Ribbon 提供了一种后验采样近似，有助于模型监控、协变量漂移检测和风险评估，而不牺牲训练效率。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

动机：复杂高维模型（如深度神经网络）难以获得可靠预测不确定性，贝叶斯推断和自举重采样虽然原则性好，但需重复后验采样或重训练，计算代价过高。

方法关键点：
- Ribbon 用影响函数线性化近似狄利克雷加权自举，仅在单一拟合模型基础上进行后处理线性代数，保留贝叶斯自举的一阶数据重加权结构。
- 当似然模型正确时，Ribbon 渐近等价于平坦先验下的 Laplace 近似；在模型误设时，则还原稳健的 sandwich 协方差估计。
- 引入浓度参数 α，构成校准的 Dirichlet 重加权族，可在验证集上调优不确定性尺度。

结果：在合成回归、MNIST 分类和加州房价预测任务上，Ribbon 在避免重训练的同时，取得竞争力的预测表现，且在多个设置中改进了校准指标。
