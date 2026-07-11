---
title: 'LongE2V: Long-Horizon Event-based Video Reconstruction, Prediction, and Frame
  Interpolation with Video Diffusion Models'
title_zh: 基于视频扩散模型的长时程事件视频重建、预测与插帧
authors:
- Cheng-De Fan
- Chun-Wei Tuan Mu
- Chen-Wei Chang
- Chin-Yang Lin
- Kun-Ru Wu
- Yu-Chee Tseng
- Yu-Lun Liu
affiliations:
- National Yang Ming Chiao Tung University
arxiv_id: '2607.08770'
url: https://arxiv.org/abs/2607.08770
pdf_url: https://arxiv.org/pdf/2607.08770
published: '2026-07-08'
collected: '2026-07-11'
category: Multimodal
direction: 事件相机视频生成 · 扩散模型
tags:
- event-based vision
- video diffusion models
- autoregressive unrolling
- frame interpolation
- zero-shot generalization
- sensor robustness
one_liner: 利用预训练视频扩散先验统一处理事件相机的视频重建、预测与插帧，引入自回归展开与自适应上下文切换抑制长期漂移
practical_value: '- 复用预训练生成式先验解决稀疏输入逆问题的范式，可迁移至推荐系统的多任务统一生成（如用户行为补全、缺失特征预测）。

  - 自回归展开与自适应上下文切换的控制策略，对长序列生成中的漂移问题有借鉴价值，可用于用户长期兴趣演化建模。

  - 事件体素密度增强应对异构传感器分辨率，类似数据增强思路可应用于多来源、多粒度行为数据的对齐与鲁棒训练。

  - 零样本泛化到帧插值任务的方法论，可启发推荐模型在未见业务场景下的快速冷启动适配。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：事件相机输出稀疏异步事件流，传统回归方法重建视频常模糊纹理，现有生成模型在长时程上稳定性差。亟需一种能同时处理重建、预测和插帧三个任务，且能保持长期时序一致性的统一框架。

**方法关键点**：
- 基于预训练视频扩散模型（SVD）微调，利用其强先验知识降低数据需求并提升感知质量。
- 针对长序列生成中的时间漂移，提出**自回归展开**（逐步生成未来帧并回收预测帧作为条件）与**自适应上下文切换**（动态选择起始帧或已生成帧作为条件域），保持全局一致性。
- 为帧插值任务设计**重编码对齐+交叉残差校正**，将事件流编码为双向光流并注入潜空间，确保首尾帧间的精确双向一致性。
- **事件体素密度增强**：训练时随机缩放事件密度，提升对异构传感器分辨率的鲁棒性。

**关键结果**：
- 在真实事件相机数据集上，重建、预测、插帧三个任务均超越现有最佳方法，PSNR 与 LPIPS 显著提升。
- 自回归策略下，长序列预测（>100 帧）的漂移显著降低。
- 插帧任务无需下游微调，即可零样本泛化到不同帧率与场景。
