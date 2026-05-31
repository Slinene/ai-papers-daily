---
title: 'Beyond 3D VQAs: Injecting 3D Spatial Priors into Vision-Language Models for
  Enhanced Geometric Reasoning'
title_zh: 超越3D VQA：向VLM注入3D空间先验以增强几何推理
authors:
- Chun-Hsiao Yeh
- Shengyi Qian
- Manchen Wang
- Yi Ma
- Joseph Tighe
- Fanyi Xiao
affiliations:
- FAIR at Meta
- UC Berkeley
- HKU
arxiv_id: '2605.30231'
url: https://arxiv.org/abs/2605.30231
pdf_url: https://arxiv.org/pdf/2605.30231
published: '2026-05-27'
collected: '2026-05-31'
category: Other
direction: 多模态大模型3D空间推理增强
tags:
- 3D spatial reasoning
- vision-language model
- geometric prior
- correspondence learning
- depth consistency
- self-supervised
one_liner: 通过深度监督的对应头和双重几何损失，将2D/3D先验注入LLM层，无需3D VQA数据即大幅提升空间推理
practical_value: '- **内部几何对应诊断**：可借鉴对模型各层进行几何对应精度诊断的思路，分析电商多模态推荐模型中视觉分支何时建立实例不变性，用于指导蒸馏或层间损失设计。

  - **多视角一致性训练**：利用多视角图像的几何对应作为自监督信号，提升商品图像表征的3D不变性，有助于在商品搜索中跨角度匹配同一物品。

  - **深度一致性损失**：通过深度监督约束解决2D视图歧义，可拓展到推荐系统中的多模态对齐任务（如视频封面与标题），用3D信息隐式消除歧义。

  - **轻量对应头**：引入一个小的对应头作为各层的深层监督，不改变主干架构；该trick可迁移到多模态Agent的视觉编码器训练，用点对应任务增强中间特征的空间理解。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有VLM通过3D VQA微调来提升空间推理，但容易过拟合数据集偏差，且集成专用3D编码器不便。本文认为真正的空间理解应源自对基础几何先验的学习，而非高层VQA监督。

**方法**：提出GASP框架，直接在LLM的Transformer层中注入几何先验。一个小的对应头被施加到所有层作为深层监督信号。训练时利用大规模视频场景的逐帧几何真相，采用双重目标：对比损失在真实点对应上强化2D视角不变性；深度一致性监督通过预测深度与真实深度的对齐解决3D几何歧义。整个过程不依赖任何3D VQA数据。

**结果**：诊断显示标准VLM内部对应匹配精度极低（常低于5%），经GASP训练后，峰值层对应精度提升至70%以上，时序鲁棒性保持85%以上，而基线仍低于5%。在无3D VQA训练的情况下，下游空间基准测试表现大幅提升：All-Angles Bench +18.2%，VSI-Bench +29.0%，证明从基础几何先验学习是通向可靠3D空间理解的通用路径。
