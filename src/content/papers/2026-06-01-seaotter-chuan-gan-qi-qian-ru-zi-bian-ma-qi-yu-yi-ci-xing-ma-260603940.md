---
title: 'SEAOTTER: Sensor Embedded Autoencoding with One-Time Transcode for Efficient
  Reconstruction'
title_zh: SEAOTTER：传感器嵌入自编码器与一次性转码的高效云机器人图像压缩框架
authors:
- Dan Jacobellis
- Neeraja J. Yadwadkar
affiliations:
- The University of Texas at Austin
arxiv_id: '2606.03940'
url: https://arxiv.org/abs/2606.03940
pdf_url: https://arxiv.org/pdf/2606.03940
published: '2026-06-01'
collected: '2026-06-07'
category: Other
direction: 云机器人图像压缩与任务感知表示
tags:
- image compression
- autoencoder
- cloud robotics
- JPEG compatibility
- learned quantization
one_liner: 结合学习型潜在表示与 JPEG 兼容性，在极端带宽下实现快速编解码与高任务精度
practical_value: '- 若业务中有端侧低功耗图像采集与云端处理链路，可借鉴“非对称自编码器 + 标准格式兼容”思路：传感器端用轻量编码器生成紧凑潜在表示，云端一次性转码为
  JPEG，兼顾带宽与下游生态兼容。

  - 可学习 JPEG 色彩与量化变换（learnable color & quantization transform）是一种保留标准解码器下提升任务精度的 trick，类似思路可用于对既有
  JPEG 管线做任务感知后处理，而不改动解码端。

  - 任务感知转码（task-aware transcoding）设计可迁移到推荐系统的多模态特征压缩：为不同下游任务（如分类、VLM）训练不同转码头，共享冻结的编码器，降低整体训练成本。

  - 对于视觉特征存储与传输场景，采用冻结编码器 + 可训练转码的策略，可以在不重新训练上游模型的前提下适配压缩率与任务精度权衡，减少重复训练开销。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：云机器人场景中，传感器端算力与带宽极度受限，传统编码器（JPEG/AVIF）要么编码开销过大，要么不兼容现有设施；非对称自编码器虽压缩高效但解码沉重且格式私有。亟需一种兼顾端侧低功耗、高压缩率、标准解码兼容性的方案。

**方法**：提出 SEAOTTER 框架，由传感器嵌入自编码器与一次性转码模块组成。传感器端用预训练、冻结的编码器将原始图像压缩成紧凑潜在表示；云端将该潜在表示转码为标准 JPEG 文件，供后续人类或机器感知任务使用。核心创新包括：1）可学习的 JPEG 色彩与量化变换，通过端到端训练优化量化表与色彩变换，使得转码后的 JPEG 在任务精度上接近原生潜在表示；2）支持通用与任务感知两种转码流水线，可在固定编码器下针对分类、密集预测、VLM 等多种下游任务调优。

**结果**：在 200:1 压缩比下，与 AVIF 相比，编码速度提升 7 倍、解码速度提升 3.5 倍，ImageNet Top-1 分类准确率提高 8%，同时完全兼容 JPEG 生态系统。
