---
title: 'ReRound: Reconstructive Rounding to Resolve Midpoint Ambiguity in Calibration-Free
  LLM Quantization'
title_zh: ReRound：重构舍入解决免校准 LLM 量化中的中点歧义
authors:
- He-Yen Hsieh
- H. T. Kung
affiliations:
- Harvard University
arxiv_id: '2608.11045'
url: https://arxiv.org/abs/2608.11045
pdf_url: https://arxiv.org/pdf/2608.11045
published: '2026-08-10'
collected: '2026-08-14'
category: Training
direction: LLM 低比特量化 · 校准自由 PTQ
tags:
- LLM quantization
- post-training quantization
- diffusion model
- round-to-nearest
- calibration-free
- low-bit inference
one_liner: 用条件扩散模型重建权重作为舍入方向指导，混合 RTN 与重构舍入，提升小模型 3/4-bit 免校准量化精度
practical_value: '- 对广告/推荐场景中部署的小模型（如轻量排序塔、CTR 特征提取器）可尝试校准自由 PTQ：ReRound 不依赖线上数据分布，奇异值匹配选择矩阵避免维护校准集，适合快速迭代压缩。

  - 容忍度参数只对歧义区间权重做特殊舍入，可作为量化后处理的“局部修正”思路：在工程上对量化误差敏感的层或权重矩阵单独做扩散重建，其余层用 RTN，控制上线成本。

  - 扩散模型生成重建权重这种“以生成做去噪/补全”的思路，可以迁移到 embedding 量化、低秩近似中，针对小模型权重分布做条件生成，提升量化后表示质量。

  - 方案完全离线、推理零额外开销，对延迟敏感的排序/召回服务是重要优势；若现有压缩工具链中精度不够，可替换 rounding 模块而不改变推理图。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：标准 RTN 在权重接近量化区间中点时舍入方向不明确，导致低比特量化精度损失，小 LLM 尤为明显。

方法：ReRound 训练一个条件扩散模型以重构低比特权重，作为消除中点歧义的指导信号；引入容忍度度量权重与中点的距离，中点附近权重用扩散重构进行量化，靠近量化边界的权重仍用 RTN。通过扫描容忍度生成多个候选量化矩阵，选取去量化后 leading singular values 与原始全精度权重最匹配的候选。过程完全离线，推理时无额外开销。

结果：在多种小模型上，3-bit、4-bit 权重量化效果一致优于标准 RTN，超过大量校准无关方法，并与校准依赖方法接近。
