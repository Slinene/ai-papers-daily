---
title: Dual-Stream MLP is All You Need for CTR Prediction
title_zh: 双流 MLP：CTR 预测的极简高效方案
authors:
- Kesha Ou
- Zhen Tian
- Wayne Xin Zhao
- Long Zhang
- Sheng Chen
- Ji-Rong Wen
affiliations:
- Gaoling School of Artificial Intelligence, Renmin University of China
- ByteDance
- Meituan
arxiv_id: '2606.04944'
url: https://arxiv.org/abs/2606.04944
pdf_url: https://arxiv.org/pdf/2606.04944
published: '2026-06-03'
collected: '2026-06-04'
category: RecSys
direction: CTR 预测 · 特征交互 · 知识蒸馏
tags:
- CTR Prediction
- Feature Interaction
- Knowledge Distillation
- Dual-Stream MLP
- Alignment Loss
one_liner: 用知识蒸馏将显式特征交互能力压缩至主 MLP，辅以并行隐式 MLP 并通过双重对齐训练，达到 SOTA 且部署简单。
practical_value: '- **轻量部署**：线上推理只使用一个简单 MLP，但知识蒸馏可以把复杂显式交互模型（如 DCN、xDeepFM）的能力注入其中，适合大规模推荐系统对延迟敏感的场景。

  - **双流互补设计**：保留一个并行的隐式交互 MLP 作为辅助训练分支，缓解显式模块可能过拟合或主导预测的问题，训练后丢弃，不影响推理成本。

  - **特征与 logit 双重对齐**：引入隐式/显式特征表示对齐损失和最终预测 logit 对齐损失，有效平衡两个分支，防止辅助分支退化或主分支被干扰，该对齐策略可迁移到多路模型融合。

  - **即插即用的蒸馏范式**：DS-MLP 可作为通用 CTR 模型的压缩框架，将任意复杂 teacher 的交互知识迁移到极简 MLP，适合在电商广告、推荐系统中进行模型轻量化。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**

CTR 预测的双流架构通常同时建模显式特征交互（如交叉网络）和隐式交互（如 DNN），但面临计算复杂度高、过拟合风险以及两路输出不平衡（往往一路主导最终预测）的问题。

**方法**

提出 DS-MLP，核心思路是用知识蒸馏将显式交互模块的能力“浓缩”进一个主 MLP 中，同时保留一个并行的辅助 MLP 捕捉隐式交互作为补充。训练阶段包含两个关键对齐：
- **特征对齐**：让辅助 MLP 的隐式交互表示向主 MLP 的蒸馏特征对齐；
- **logit 对齐**：约束两路的预测 logit 一致。
最终线上推理只保留被蒸馏过的主 MLP，从而在极简结构上保留显式交互能力并获得隐式信息的补偿。

**结果**

在 Criteo、Avazu、Taobao 三个公开基准上，DS-MLP 以原始 MLP 级的参数量和推理代价，超越了 DCNv2、xDeepFM、DeepFM 等复杂模型，达到 SOTA，同时训练稳定，收敛更快。
