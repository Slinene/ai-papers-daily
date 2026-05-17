---
title: Aligning Latent Geometry for Spherical Flow Matching in Image Generation
title_zh: 对齐潜空间几何以实现球面流匹配图像生成
authors:
- Tuna Han Salih Meral
- Kaan Oktay
- Hidir Yesiltepe
- Adil Kaan Akan
- Pinar Yanardag
arxiv_id: '2605.15193'
url: https://arxiv.org/abs/2605.15193
pdf_url: https://arxiv.org/pdf/2605.15193
published: '2026-05-13'
collected: '2026-05-17'
category: Training
direction: 球面潜在流匹配优化生成质量
tags:
- spherical flow matching
- latent space geometry
- image generation
- VAE
- geodesic paths
- diffusion models
one_liner: 将扩散模型潜空间的线性插值改为球面线性插值，仅微调解码器即可提升生成质量
practical_value: '- 对于电商中的商品图生成等视觉任务，直接将扩散模型潜空间的线性插值替换为球面插值（slerp），并配合固定半径投影与解码器微调，可在不改动主干网络的前提下提升FID，工程改动小，效果稳健。

  - 方向分量主导语义的洞察可迁移到推荐系统的表示学习：将用户/物品embedding归一化到固定球面，分离语义（方向）与强度（半径），有助于提升表示对齐和相似度计算的稳定性。

  - 冻结编码器、只微调解码器的策略，是一种低成本的分布适配技巧，适用于其他需要将高斯先验对齐到特定几何结构的生成式模型场景。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：流匹配（Flow Matching）在图像生成的潜空间中通常使用欧氏线性路径连接高斯噪声与VAE潜变量，但两端点实际分布在半径不同的薄球壳上，线性路径会偏离球面，可能导致生成伪影。方法关键点：将潜变量分解为径向与角度分量，通过分量互换实验发现，解码后的感知与语义内容主要由方向承载，半径贡献微弱。据此，将数据潜变量投影到固定半径球面，使用高斯噪声的径向投影作为球面先验，冻结编码器，仅微调解码器以适应固定半径的分布，并将线性插值替换为球面线性插值（slerp）。得到的测地线路径全程驻留在球面上，速度目标也变为纯角度量。结果：在类别条件ImageNet-256生成任务中，该方法在多种图像令牌化器下均取得更优的FID，不改变扩散架构，无需辅助编码器或表示对齐目标。
