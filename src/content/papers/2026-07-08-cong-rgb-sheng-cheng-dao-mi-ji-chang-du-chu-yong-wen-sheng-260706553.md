---
title: 'From RGB Generation to Dense Field Readout: Pixel-Space Dense Prediction with
  Text-to-Image Models'
title_zh: 从 RGB 生成到密集场读出：用文生图模型做像素空间密集预测
authors:
- Zanyi Wang
- Xin Lin
- Haodong Li
- Dengyang Jiang
- Yijiang Li
affiliations:
- UCSD
- HKUST
arxiv_id: '2607.06553'
url: https://arxiv.org/abs/2607.06553
pdf_url: https://arxiv.org/pdf/2607.06553
published: '2026-07-08'
collected: '2026-07-13'
category: Other
direction: 利用文生图 DiT 直接读出密集预测场
tags:
- Dense Prediction
- DiT
- LoRA
- Text-to-Image
- Readout
- Flux
one_liner: 冻结 DiT 并加 LoRA，直接从 patch token 线性读出深度/法线等密集场，避免生成 RGB 再解码
practical_value: '- **冻结大模型 + 线性读出**：用预训练生成模型作为编码器后，直接接任务线性头输出密集数值，避免生成中间媒介，简化推理 pipeline。推荐系统中可将
  LLM 编码的用户/物品表示直接读出 CTR 或评分，省去文本解码步骤。

  - **LoRA 适配低成本复用**：仅训练 LoRA 参数和极轻量线性头（约 33K 参数），适合业务中快速利用不同预训练基座适应新任务，如点击率预估、兴趣强度预测。

  - **保持输入分布，换输出接口**：保留 VAE 编码器维持模型输入一致性，只替换目标侧解码，这对在原有推荐模型框架上嫁接新预测目标有参考意义——保持上游不变，只改下游头。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有方法将深度、法线、抠图等密集预测任务转换为 RGB 目标生成，再通过 VAE 解码获得结果，这继承了不必要的生成接口。密集预测真正需要的是在输入图像平面上输出像素对齐的任务原生场，而不是渲染新的 RGB 内容。

**方法关键点**：提出 ReChannel，抛弃目标侧 VAE 解码。保留 VAE 编码器以维持 DiT 输入分布；冻结 DiT 并添加任务 LoRA；每个输出 token 通过一个共享的 token-local 线性头直接映射回 p×p×K_t 的像素 patch，无空间混合，总适配参数仅约 33K。

**关键结果**：在六个密集预测任务、十余个基准上验证，trimap-free matting、KITTI 深度估计和指代分割达到新 SOTA；表面法线、显著性、人体姿态估计保持竞争力。4B 参数规模下，比编辑+潜空间解码方案精度更高且推理速度快 2.48 倍。
