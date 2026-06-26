---
title: 'ViQ: Text-Aligned Visual Quantized Representations at Any Resolution'
title_zh: ViQ：任意分辨率下文本对齐的视觉量化表示
authors:
- Xumin Yu
- Zuyan Liu
- Zhenyu Yang
- Yuhao Dong
- Shengsheng Qian
- Jiwen Lu
- Han Hu
- Yongming Rao
affiliations:
- Tencent HY Vision Team
- Tsinghua University
- Nanyang Technological University
- Chinese Academy of Sciences
arxiv_id: '2606.27313'
url: https://arxiv.org/abs/2606.27313
pdf_url: https://arxiv.org/pdf/2606.27313
published: '2026-06-24'
collected: '2026-06-26'
category: Multimodal
direction: 多模态离散表示与高效训练
tags:
- Visual Tokenization
- Vector Quantization
- Multimodal Learning
- Discrete Representation
- Native Resolution
- Training Efficiency
one_liner: 通过文本对齐预训练与头量化，将图像编码为保留细节和语义的离散 token，多模态训练加速 20-70%
practical_value: '- 商品图像通过 ViQ 量化为离散 token，可与文本 token 统一送入 LLM，实现多模态生成式推荐，大幅降低计算和存储开销。

  - 两阶段训练策略（先 CLIP 式文本对齐，再近端离散化）保证语义和细节，适合电商场景中既需属性识别又需图像质量的需求。

  - 原生分辨率处理能力，可直接输入各种尺寸的商品图，避免统一 resize 造成的细节丢失或变形。

  - 量化特征在 LLM 微调时训练加速 20-70%，可将该方案用于大规模多模态推荐模型的训练与推理加速。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：统一文本和视觉的离散表示是多模态大模型高效训练的追求，但现有视觉离散表示难以同时保留低级细节与高级语义，且大多固定分辨率，造成信息损失。

**方法**：提出 ViQ，将视觉量化学习分为两阶段：（1）**文本对齐预训练**：利用预训练语言模型（如 CLIP 文本塔）对视觉编码器进行语义监督，使其学习语义丰富的连续特征，同时保持原生分辨率输入能力；（2）**特征离散化**：通过近端表示学习策略逐步压缩特征空间，使离散码本更易优化；设计位置感知的头量化机制，对每个注意力头独立量化，灵活支持任意分辨率的图像输入，输出紧凑的离散 token 序列。

**结果**：在多个多模态基准上，ViQ 以远低于连续特征的维度（如 16 维离散 token）取得与最新连续视觉编码器可比或更优的性能，同时在图像重建上保持高保真度。将 ViQ 的离散 token 用于多模态 LLM 训练，在不同 LLM 基座和训练配方下获得 20-70% 的训练加速。
