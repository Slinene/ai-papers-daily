---
title: 'HYDRA-X: Native Unified Multimodal Models with Holistic Visual Tokenizers'
title_zh: HYDRA-X：以整体视觉分词器实现原生统一多模态模型
authors:
- Guozhen Zhang
- Xuerui Qiu
- Yutao Cui
- Tianhui Song
- Changlin Li
- Junzhe Li
- Tao Huang
- Xiao Zhang
- Yang Li
- Jianbing Wu
affiliations:
- Nanjing University
- CASIA
- Tencent Hunyuan
- Zhongguancun Academy
- Shanghai AI Lab
arxiv_id: '2606.13289'
url: https://arxiv.org/abs/2606.13289
pdf_url: https://arxiv.org/pdf/2606.13289
published: '2026-06-10'
collected: '2026-06-13'
category: Multimodal
direction: 统一视觉分词与多模态理解/生成
tags:
- Visual Tokenizer
- Unified Multimodal
- ViT
- Video Understanding
- Image Generation
- Latent Space
one_liner: 首个以单一ViT统一图像与视频分词的原生视觉分词器，通过分层时间压缩与潜在级语义注入提升重建与编辑一致性
practical_value: '- 对电商商品多模态处理：统一分词器可直接编码商品图片和视频至同一潜在空间，简化多模态商品表征流水线，减少编解码器数量。

  - 视频内容压缩借鉴：分层时间压缩策略（优于单步压缩）与轻量解压器设计，可迁移至短视频商品描述或虚拟试穿场景，在保持语义的同时降低序列长度。

  - 编辑任务中的交互层级选择：论文发现将源-目标交互放在分词器潜在层（而非LLM语义层）能显著提升编辑一致性和收敛速度，该 insight 可应用于多模态对话式商品编辑或海报生成。

  - 训练策略启示：联合图像-视频教师监督可增强潜在空间语义结构，类似原理可用于多任务商品理解模型，联合商品图片和视频标签进行预训练。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：统一多模态模型（UMM）需要将图像和视频等多种视觉输入映射到统一表示空间，但现有方案要么采用分离式图像/视频编码器，要么难以同时保证重建质量和语义丰富度。本工作旨在构建首个在单一 ViT 内同时处理图像和视频的整体视觉分词器。

**方法关键点**：首先，通过大量消融实验发现：(1) 帧级因果时间注意力足以实现视觉重建，全时空注意力反而有害；(2) 分层时间压缩（逐帧降维）显著优于单步压缩。基于此，提出在原生 ViT 中插入轻量级时间层与分层压缩模块。其次，为在紧凑潜在空间中注入图像和视频级语义，设计了一个轻量解压器，在联合图像-视频教师监督下上采样时间压缩特征，迫使潜在表示携带互补语义结构。此外，提出编辑流程改进：将源-目标内容交互从 LLM 语义层下移至分词器潜在层，有效提升编辑一致性和训练收敛速度。

**关键结果**：在 7B 稠密模型上，HYDRA-X 在图像和视频理解与生成任务上取得强性能，尤其在视频重建和编辑任务上表现突出，验证了整体分词器设计的有效性，并为未来统一分词器 UMM 铺平道路。
