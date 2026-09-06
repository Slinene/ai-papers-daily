---
title: 'DSAQuant: Denoising-Stage-Aligned Quantization-Aware Training for Video Generation'
title_zh: DSAQuant：面向视频生成的对齐去噪阶段的量化感知训练
authors:
- Shuaiting Li
- Zelin Gao
- Haibin Shen
- Yujun Shen
- Haotong Qin
- Yinghao Xu
affiliations:
- Robbyant
- ZJU
- PolyU
- HKUST
arxiv_id: '2609.04031'
url: https://arxiv.org/abs/2609.04031
pdf_url: https://arxiv.org/pdf/2609.04031
published: '2026-09-03'
collected: '2026-09-06'
category: Other
direction: 视频生成扩散模型量化训练
tags:
- Video Diffusion Models
- Quantization-Aware Training
- Denoising Stages
- W4A4
- VBench
- CFG
one_liner: 提出按去噪阶段对齐的量化训练框架，在 W3A3 下 VBench 平均最高提升 6.60
practical_value: '- 若业务部署视频生成模型（如电商广告素材自动生成），可借鉴分阶段量化：在扩散去噪的早期保留全精度教师监督，后期切换到量化目标，能显著降低低比特细节损失。

  - 推理时在最后若干步禁用 CFG 是低成本 trick：可减少量化误差放大、避免高频伪影，对图像/视频生成模型均有参考意义。

  - 量化训练不要统一处理所有 timestep；按去噪阶段角色分配监督信号，是比单纯减小量化误差更有效的架构选择。

  - 实验显示 W3A3 下 VBench 提升 6.60，激进压缩可行且无推理额外开销，适合边缘侧部署。'
score: 6
source: arxiv-cs.CV
depth: abstract
---

**动机**：视频扩散模型（VDM）推理成本高，量化感知训练（QAT）是可行的压缩路径，但现有方法在低比特（W4A4/W3A3）下严重损失视觉细节、纹理与清晰度，仅保留语义和粗略运动。

**方法关键点**：定位问题为传统量化管线 timestep-agnostic，忽略视频去噪的阶段功能。DSAQuant 包含两个阶段对齐设计：
1. 训练阶段 Denoising-Stage Oriented Supervision：早期去噪步保留教师蒸馏以稳定全局结构与运动规划；中后期转向目标驱动优化，强化细节重建。
2. 推理阶段 Denoising-Stage Gated Guidance：在最后若干去噪步禁用 classifier-free guidance（CFG），防止 CFG 放大量化误差为高频伪影。

**关键结果**：在 Wan 和 CogVideoX 系列模型上，W4A4 与 W3A3 设置下，DSAQuant 持续超过 SOTA QAT 基线；VBench 平均分在 W3A3 下最高提升 6.60，同时保持强文本-视频对齐。
