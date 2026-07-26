---
title: 'KroQuant: Kronecker-Structured Block Transforms for Efficient Post-Training
  Quantization of Diffusion Transformers'
title_zh: KroQuant：基于Kronecker结构化块变换的扩散模型高效训练后量化
authors:
- Yann Bouquet
- Alireza Khodamoradi
- Kristof Denolf
- Mathieu Salzmann
arxiv_id: '2607.21446'
url: https://arxiv.org/abs/2607.21446
pdf_url: https://arxiv.org/pdf/2607.21446
published: '2026-07-23'
collected: '2026-07-26'
category: Training
direction: 扩散模型训练后量化：Kronecker块变换
tags:
- PTQ
- Quantization
- DiT
- Kronecker
- TensorCore
- LoRA
one_liner: 提出KroQuant，用学习的Kronecker结构化块变换对激活做32元素块量化，比SmoothQuant更快且精度更高
practical_value: '- 在推荐模型量化部署中，可借鉴KroQuant的块级Kronecker变换抑制激活异常值，参数少、在线开销低，适合实时推理。

  - 将量化变换设计为32元素块的小GEMM，直接利用GPU Tensor Core加速，延迟更低。

  - 离线LoRaQ权重校准可吸收量化后残差，提升精度，可作为PTQ流程的通用后处理步骤。

  - 局部块变换替代全矩阵变换的思路，在保持量化质量同时大幅降低计算成本，适合搜索推荐系统的高吞吐需求。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：扩散变换器（DiT）量化到W4A4时，激活中的异常值严重损害生成质量。现有方案中，SmoothQuant计算便宜但影响通道幅度，Hadamard变换需要大块尺寸导致高在线成本，学习全矩阵可逆变换则引入密集GEMM开销。

**方法**：KroQuant提出学习的Kronecker结构化可逆变换，对每个32元素激活块独立处理，参数比per-channel scaling少一半以上。块局部结构以小型张量核GEMM高效运行，在线量化内核在MI350上比SmoothQuant快14%。离线使用LoRaQ校准权重，吸收残差量化误差。

**结果**：在PixArt-Σ、SANA、FLUX.1-schnell上执行W4A4（MXFP4e2），生成的图像在MJHQ-30K和SDCI基准上比SVDQuant和LoRaQ更接近全精度参考，保持或改善图像质量。
