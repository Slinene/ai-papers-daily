---
title: 'MakeupMirror: Improving Facial Attribute Preservation in Diffusion Models
  for Makeup Transfer'
title_zh: MakeupMirror：在妆容迁移扩散模型中提升面部属性保留
authors:
- Nefeli Andreou
- Angel Martínez-González
- Sabine Sternig
- Matthieu Guillaumin
- Epameinondas Antonakos
- Michael Opitz
affiliations:
- Amazon
arxiv_id: '2606.20094'
url: https://arxiv.org/abs/2606.20094
pdf_url: https://arxiv.org/pdf/2606.20094
published: '2026-06-18'
collected: '2026-06-20'
category: Other
direction: 虚拟试妆 · 扩散模型精细化控制
tags:
- Diffusion Models
- Makeup Transfer
- Facial Attribute Preservation
- ControlNet
- Virtual Try-On
one_liner: 通过面部几何控制、区域特定调制和肤色保持，将人脸识别相似度相对提升60%，肤色差异降低50%，推理仅0.7秒
practical_value: '- 电商虚拟试妆：引入 ControlNet 编码面部几何（如边缘、关键点），可在生成中保持人脸结构不变，适合直接移植到在线试妆服务

  - 区域特定调制：通过皮肤、眼唇等区域 mask 分别控制 makeup 强度和风格，避免溢出，提升妆容自然度，可迁移至商品图上局部修饰

  - 肤色保持模块：跨人妆容迁移时根据源肤色调整参考妆容色彩，防止肤色漂移，增强用户信任，这对生产级 VTO 至关重要

  - 加速采样：使用 Levenberg-Marquardt Langevin 采样器，将 50 步扩散降至 0.7s 推理，平衡质量与速度，适合移动端部署'
score: 6
source: arxiv-cs.MM
depth: abstract
---

**动机**：现有基于扩散的妆容迁移方法（如 Stable-Makeup）在真实感和妆容保真度上进步明显，但仍存在面部身份和肤色偏移问题，无法满足生产级虚拟试妆（VTO）要求。

**方法关键**：提出 MakeupMirror，在 Stable-Makeup 基础上创新四点：
1) 引入 ControlNet 注入人脸几何条件（面部边缘、关键点），增强身份结构保持；
2) 设计区域特定控制模块，将面部划分为皮肤、眼、唇等区域，分别控制妆容应用程度，避免跨区域溢出；
3) 肤色调制：在跨对象迁移时，根据源图像肤色对参考妆容进行色彩变换，防止肤色被意外改变；
4) 集成 Levenberg-Marquardt Langevin 采样器，大幅减少推理步数，同时保持生成质量。

**结果**：在 CPM-Real、Makeup Wild 及新收集的多样化数据集 MakeupSelfies 上，相比 Stable-Makeup，人脸识别相似度相对提升 60%，肤色差异相对降低 50%，推理延迟 0.7 秒，专家审核的核心身份保留标准接受率达 94%。
