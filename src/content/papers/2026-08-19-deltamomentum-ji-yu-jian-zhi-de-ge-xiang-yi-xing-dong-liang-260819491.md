---
title: 'DeltaMomentum: A Key-Value based Anisotropic Momentum Update via Delta Rule'
title_zh: DeltaMomentum：基于键值的各向异性动量更新
authors:
- Euijin Hong
- Guannan Qu
affiliations:
- Electrical and Computer Engineering, Carnegie Mellon University
arxiv_id: '2608.19491'
url: https://arxiv.org/abs/2608.19491
pdf_url: https://arxiv.org/pdf/2608.19491
published: '2026-08-19'
collected: '2026-08-21'
category: Training
direction: 优化器动量更新 · Delta Rule
tags:
- Optimizer
- Momentum
- Delta Rule
- Training
- LLM Pretraining
- Anisotropic
one_liner: 把线性层梯度拆成 key-value，用 delta rule 做方向感知动量更新来加速训练收敛
practical_value: '- 推荐系统特征通常极度稀疏/长尾，例如 user/item id、类目等输入方向的频率高度不均。DeltaMomentum 可直接替换现有优化器的动量
  buffer，对高频方向自动降低遗忘、低频方向加快遗忘，特别适合 embedding 层和 wide 部分；无额外持久内存，可在排序/召回模型训练中验证步数节省。

  - 若业务在用 LLM 做生成式推荐或领域模型预训练，可在 AdamW 上启用 DeltaMomentum，论文在 67M/370M 语言模型上分别减少 46%/22%
  达到同验证损失的步数，对固定算力预算下扩大模型或数据量有直接价值。

  - 工程实现注意：额外计算约为 gated-MLP 线性层成本的 22-25%，无 persistent memory；但方法基于线性层 key-value 结构，对
  attention 等非简单线性部分需适配，建议先在 MLP/embedding 层替换。

  - 调参经验：系数在 μP 下可跨宽度迁移，若业务使用 μP 训练超大规模模型，能用小模型调的系数直接放大，降低调参成本。'
score: 7
source: arxiv-stat.ML
depth: abstract
---

**动机**：现有优化器的动量是对历史梯度的 EMA，所有方向以同一速率遗忘；但深度网络训练输入高度各向异性，少数方向频繁出现、大量方向罕见，固定遗忘速率不利于稀疏/长尾方向的学习。

**方法关键点**：对线性层梯度做 key-value 分解：输入 x 为 key，输出误差 e 为 value。将动量 buffer 视为可写的键值存储，用 canonical delta rule 更新，使每个方向的遗忘率由该方向出现频率决定；等价于 input-side curvature correction，但无需矩阵求逆。证明其为有效动量，且在固定/漂移最优下比 EMA 更快清除过期方向。可作为任意优化器动量 buffer 的 drop-in replacement，额外计算为 gated-MLP 线性成本的 22.2%-25%，无 persistent memory。

**关键结果数字**：FineWeb-Edu 预训练中，DeltaAdamW 达到 AdamW 同验证损失所需步数减少 46.39±4.32%（67M）和 22.12±0.80%（370M），1B Chinchilla-optimal 下收益保持；在 SGD、ResNet-18、ViT-Tiny/CIFAR-10 上也有效。注意 Muon 基线在同协议下仍高于 DeltaAdamW。
