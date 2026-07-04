---
title: 'OrbitQuant: Data-Agnostic Quantization for Image and Video Diffusion Transformers'
title_zh: OrbitQuant：图像与视频扩散 Transformer 的数据无关量化
authors:
- Donghyun Lee
- Jitesh Chavan
- Duy Nguyen
- Sam Huang
- Liming Jiang
- Priyadarshini Panda
- Timo Mertens
- Saurabh Shukla
affiliations:
- Cantina Labs
- University of Southern California
- University of Illinois Urbana-Champaign
arxiv_id: '2607.02461'
url: https://arxiv.org/abs/2607.02461
pdf_url: https://arxiv.org/pdf/2607.02461
published: '2026-07-02'
collected: '2026-07-04'
category: Other
direction: 扩散 Transformer PTQ · 数据无关旋转量化
tags:
- PTQ
- Quantization
- Diffusion Transformers
- Hadamard Rotation
- Lloyd-Max Codebook
- Data-Agnostic
one_liner: 在归一化旋转基上量化，用固定码本适应所有时间步和模态，无需数据重校正，将 DiT PTQ 推进到 W2A4。
practical_value: '- 对推荐系统中可能使用的 Transformer 或扩散生成模型，旋转基量化可消除校准集依赖，避免因用户行为分布漂移而反复重校。

  - 权重旋转离线吸收进线性层，推理时仅对激活做前向旋转，工程实现简洁高效，可直接参考其算子融合技巧。

  - 单一码本跨层复用，大幅降低推荐模型量化时的码本存储与设计复杂度，适合存储受限的线上环境。

  - W2A4 极低比特可成倍压缩推理带宽，在电商直播、短视频内容生成等需高吞吐的 GPU 受限场景具备直接落地价值。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：扩散 Transformer（DiT）在图像/视频生成中 SOTA，但多步采样与巨量参数导致推理昂贵。PTQ 是自然加速手段，然而 DiT 的激活值随时间步、提示词和引导分支剧烈偏移，已有方法须为每个新检查点和模态重采校准数据，难以工程化。

**方法关键点**：
- 提出数据无关的量化范式 OrbitQuant，不依赖任何校准数据。
- 核心是在归一化、随机排列块 Hadamard（RPBH）旋转的基底上量化，使每个坐标的分布集中于一个已知的固定边缘分布，从而一个预训练的 Lloyd-Max 码本可通用复用于所有时间步、提示和层（同维度）。
- 权重行同样离线在此旋转基下量化，并将旋转吸收进线性层权重，推理时仅需对激活做一次前向 RPBH 旋转，旋转在层内抵消，无额外开销。
- 同一套方案无需任何修改即可从图像迁移到视频。

**关键结果**：在 FLUX.1、Z-Image-Turbo、Wan 2.1、CogVideoX 上，OrbitQuant 在多种低比特设定（W4A4、W3A4、W3A3、W2A4）均达 SOTA PTQ 质量，并首次将图像扩散 Transformer 的 PTQ 推至 W2A4 仍保持可用生成效果，显著优于 QuaRot、ViDiT-Q 等依赖校准的方法。
