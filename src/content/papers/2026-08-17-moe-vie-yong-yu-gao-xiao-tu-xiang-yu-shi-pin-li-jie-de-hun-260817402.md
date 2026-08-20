---
title: 'MoE-ViE: Mixture of Experts Vision Encoder for Efficient Image and Video Understanding'
title_zh: MoE-ViE：用于高效图像与视频理解的混合专家视觉编码器
authors:
- Bonan Zhang
- Shiyu Dong
- Quan Hung Tran
- Katharina Gschwind
- Shuqi Yang
- Sijia Chen
- Adel Ahmadyan
- Seungwhan Moon
- Lu Zhang
- Ahmed Kirmani
affiliations:
- Meta
arxiv_id: '2608.17402'
url: https://arxiv.org/abs/2608.17402
pdf_url: https://arxiv.org/pdf/2608.17402
published: '2026-08-17'
collected: '2026-08-20'
category: Multimodal
direction: 视觉编码器 MoE 高效扩展
tags:
- MoE
- Vision Encoder
- CLIP
- Video Distillation
- Efficient Inference
one_liner: 系统研究 CLIP 视觉编码器的 MoE 设计，以细粒度拓扑与无辅助损失均衡实现高效扩展并超越稠密模型
practical_value: '- 电商多模态召回/排序依赖 CLIP 式视觉编码器，可替换为 MoE-ViE 类细粒度 MoE 编码器，在商品图片/视频特征提取中获得更高吞吐、更低延迟；其专用
  MoE kernel 可直接借鉴到线上推理优化。

  - 细粒度 MoE 拓扑与无辅助损失均衡方法可迁移到多模态特征塔或用户行为序列编码器，减少专家负载不均衡和训练不稳定，提升模型容量扩展效率。

  - 视频理解中的帧级蒸馏与冻结机制适合电商直播/短视频场景：在已有图像编码器基础上增量扩展视频能力，避免灾难性遗忘，无需从头预训练视频模型。

  - 对于多模态 Agent（如商品问答、视觉搜索），视觉编码器是延迟瓶颈之一，采用 MoE-ViE 可在保持精度下降低端到端延迟，适合交互式场景。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：视觉编码器是 VLM 关键组件，扩展容量可提升性能，但稠密扩展带来计算和推理延迟增长，高分辨率图像和长视频更严重。MoE 在 LLM 中实现高效扩展，但 CLIP 风格视觉编码器的 MoE 设计空间缺乏系统研究。

方法：系统研究 MoE 设计，发现细粒度 MoE 拓扑相比稠密和标准 MoE 有显著增益；提出无辅助损失均衡变体，改善专家利用率；设计专用 MoE kernel 减少推理延迟；为增强视频能力同时保留图像知识，引入帧级蒸馏与新型冻结机制。

结果：预训练一系列 MoE-ViE，所有模型一致优于稠密对应；最大模型零样本性能匹配 1.7 倍规模的 SOTA 编码器，延迟仅为其 76%；与 LLM 对齐后，在图像和视频基准上超过所有对比编码器，包括激活参数高达 5 倍的模型。
