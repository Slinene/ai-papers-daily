---
title: 'Matrix AdaGrad: Row-wise and Column-wise Adaptive Subgradient Methods'
title_zh: 矩阵 AdaGrad：行向与列向自适应次梯度方法
authors:
- Wenpeng Zhang
- Runsheng Yu
- Peilin Zhao
affiliations:
- Independent Researcher
- Shanghai Jiao Tong University
arxiv_id: '2609.21815'
url: https://arxiv.org/abs/2609.21815
pdf_url: https://arxiv.org/pdf/2609.21815
published: '2026-09-18'
collected: '2026-09-21'
category: Training
direction: 自适应优化器 · 矩阵结构
tags:
- AdaGrad
- Matrix Optimization
- Online Mirror Descent
- Regret Bound
- Adaptive Methods
- Deep Learning Training
one_liner: 提出行/列矩自适应 AdaGrad，用矩阵结构替代逐元素缩放，获得更紧后悔界
practical_value: '- 在推荐模型中 embedding 矩阵、attention 权重矩阵等大矩阵参数上，可尝试用 Row-AdaGrad 或 Column-AdaGrad
  替代逐元素 Adam，按行/列累积梯度范数做缩放，减少二阶矩状态存储，同时可能提升训练稳定性。

  - 对稀疏且结构分明的 embedding 表（如用户 ID × 隐向量维度），行维对应 ID，列维对应特征维度，可灵活选择行/列分组，避免逐元素噪声导致的错误缩放，适合稀疏梯度场景。

  - 如果业务中需要加大学习率以加速收敛，但发现训练不稳定，可借鉴其矩阵感知缩放思路，实验按行/列分组自适应学习率，观察是否能扩大可稳定训练的学习率范围。

  - 理论结果表明，在结构化梯度下矩阵感知 Adagrad 的 regret 界可严格紧于逐元素版本，这意味着在推荐/CTR 模型中若能识别矩阵结构梯度分布，用相应优化器可能获得更优收敛行为，值得在新模型原型阶段快速对比实验。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**
现有自适应优化器（AdaGrad、Adam）主要针对向量参数设计，逐元素缩放学习率，未显式利用矩阵结构。尽管已有矩阵感知优化器展示收益，但缺少类似 AdaGrad 的通用理论框架来推导矩阵感知自适应方法。

**方法关键点**
开发通用 Online Mirror Descent 框架，为矩阵参数引入自适应 proximal functions。通过定义行向和列向矩阵 proximal functions，并分析 regret 权衡，推导出 Row-AdaGrad 和 Column-AdaGrad。其自适应缩放由累积行/列梯度范数决定，而非逐元素梯度平方和。

**关键结果**
建立 regret 保证，证明在结构化梯度下这些矩阵感知上界可严格紧于 entry-wise AdaGrad。实验在矩阵分解和深度神经网络训练上验证，对齐矩阵结构与自适应缩放可提升优化稳定性，并能用更大学习率训练更深网络。
