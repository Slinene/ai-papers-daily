---
title: Does Synthetic Layered Design Data Benefit Layered Design Decomposition?
title_zh: 合成图层设计数据是否有利于图层设计分解？
authors:
- Kam Man Wu
- Haolin Yang
- Qingyu Chen
- Yihu Tang
- Jingye Chen
- Qifeng Chen
affiliations:
- Hong Kong University of Science and Technology
- WeBank
arxiv_id: '2605.15167'
url: https://arxiv.org/abs/2605.15167
pdf_url: https://arxiv.org/pdf/2605.15167
published: '2026-05-13'
collected: '2026-05-18'
category: Multimodal
direction: 图形设计图层分解 · 合成数据增强
tags:
- synthetic data
- layered design
- image editing
- data-centric
- VLM
- graphic design
one_liner: 纯合成数据训练在图形图层分解任务上超越真实数据集，且可扩展至数万样本。
practical_value: '- 电商商品图分层编辑：可直接用纯合成数据训练图层分解模型，摆脱对难以获取的专有分层 PSD 文件的依赖，降低数据成本。

  - 自动化标注流程：结合 VLM 自动预测图层边界框并生成文本描述，实现训练样本的自动化构造，提升迭代效率。

  - 数据分布控制：合成数据可灵活调整图层数量分布，避免真实数据长尾问题，提升模型对不同复杂度设计的泛化能力。

  - 训练规模参考：实验表明约 5 万张合成图像即可达到性能饱和，为实际部署时的数据预算提供直接参考。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有图像生成模型输出的扁平图像难以灵活编辑，图层分解是打通“最后一公里”编辑的关键。然而，训练数据依赖稀缺的专业分层资产（如 PSD 文件），可扩展性差。本文探索纯合成数据能否替代真实数据，驱动图层分解模型。

**方法**：基于 SOTA 图层分解框架 CLD，构建纯合成数据集 SynLayers，利用视觉语言模型（VLM）自动生成文本监督并预测物体边界框作为推理输入，全流程无需人工标注。

**关键结果**：
- 纯合成数据训练的模型在图形设计分解任务上，性能超越基于真实数据集 PrismLayersPro 的方案，证明合成数据的有效性和可扩展性。
- 性能随训练数据量增加而提升，约 5 万样本时趋于饱和，指明实用规模上限。
- 合成数据能平衡图层数量分布，克服真实数据中严重的图层计数长尾问题，提升模型对多图层设计的鲁棒性。
