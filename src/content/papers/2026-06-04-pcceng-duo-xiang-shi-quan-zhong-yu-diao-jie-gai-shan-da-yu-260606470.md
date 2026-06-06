---
title: 'PC Layer: Polynomial Weight Preconditioning for Improving LLM Pre-Training'
title_zh: PC层：多项式权重预调节改善大语言模型预训练
authors:
- Senmiao Wang
- Tiantian Fang
- Haoran Zhang
- Yushun Zhang
- Kunxiang Zhao
- Alex Schwing
- Ruoyu Sun
affiliations:
- The Chinese University of Hong Kong, Shenzhen
- Google LLC
- University of Illinois at Urbana-Champaign
- Shenzhen International Center for Industrial and Applied Mathematics, Shenzhen Research
  Institute of Big Data
arxiv_id: '2606.06470'
url: https://arxiv.org/abs/2606.06470
pdf_url: https://arxiv.org/pdf/2606.06470
published: '2026-06-04'
collected: '2026-06-06'
category: Training
direction: 大模型训练优化 · 权重预调节
tags:
- Preconditioning
- Weight Normalization
- LLM Pre-training
- Singular Value Spectrum
- Training Stability
one_liner: 提出可插入Transformer的PC层，通过多项式预调节重塑权重奇异值谱，训练后吸收无推理开销，提升LLM预训练稳定性
practical_value: '- 在电商、Agent等场景的Transformer（如行为序列模型、对话模型）预训练中，若出现训练不稳定或梯度范数异常，可尝试插入PC层作为轻量权重正则化，训练后无推理成本。

  - 结合Muon优化器使用时，PC层有额外增益；工业界若评估切换到Muon以获得更优收敛，可同时引入PC层。

  - PC层可视为一种即插即用的权重谱整形工具，与现有RMSNorm等输出归一化兼容，可叠加使用以进一步稳定训练。

  - 对于预训练后需部署的生产模型，PC层的可合并特性意味着零推理改动，适合 A/B 测试或逐步上线。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：大语言模型预训练不稳定，现有归一化方法（如 RMSNorm）主要作用于层输出，权重矩阵本身的奇异值谱可能严重退化，导致优化困难。

**方法**：提出多项式预调节层（PC Layer），在权重矩阵上应用低阶多项式变换，直接重塑其奇异值分布，使得训练过程中每层权重条件数保持健康且均匀。理论上，对于线性深层网络，若每层奇异值有界，则梯度下降能几何收敛到全局最优，这为谱控制提供了依据。

**结果**：在 Llama-1B 规模预训练中，使用 AdamW 和 Muon 两种优化器，PC 层均稳定优于标准 Transformer，验证损失显著降低。训练完成后，PC 层的多项式变换可数学合并回权重，模型还原为原始架构，推理零额外开销。该方法证明了权重空间谱整形对提升大规模训练稳定性的有效性。
