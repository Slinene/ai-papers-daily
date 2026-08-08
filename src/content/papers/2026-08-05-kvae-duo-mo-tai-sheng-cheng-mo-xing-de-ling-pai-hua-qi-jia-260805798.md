---
title: 'KVAE: Family of Tokenizers for Multimodal Generative Models'
title_zh: KVAE：多模态生成模型的令牌化器家族
authors:
- Andrey Shutkin
- Denis Parkhomenko
- Ivan Kirillov
- Kirill Chernyshev
- Kirill Malakhov
- Ilia Vasiliev
- Ilia Trushkin
- Valeriya Kobenko
- David Chikovani
- Alexander Ivanov
affiliations:
- Kandinsky Lab
arxiv_id: '2608.05798'
url: https://arxiv.org/abs/2608.05798
pdf_url: https://arxiv.org/pdf/2608.05798
published: '2026-08-05'
collected: '2026-08-08'
category: Multimodal
direction: 多模态连续潜在tokenizer设计
tags:
- Tokenizer
- VAE
- Multimodal
- Latent Diffusion
- Audio
- Video
one_liner: 提出音频、图像、视频的连续潜在tokenizer，重建和生成质量匹敌前沿开源模型
practical_value: '- 主要是多模态生成的基础研究，对电商搜索推荐业务直接可借鉴点有限

  - 若涉及商品短视频/音频摘要或内容理解，可尝试用其压缩特征作为轻量表示，降低存储计算成本

  - 潜在空间设计理念（如低帧率、全频带）可启发多模态特征提取模块的压缩率选择

  - 推荐系统中的多模态内容生成（如广告创意）可将其作为潜在表示生成器的基础组件'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：潜在扩散模型（LDM）高度依赖 tokenizer 将信号压缩到潜在空间，影响学习速度和生成质量。现有开源 tokenizer 在音频、视频、图像上仍存在性能差距，且训练细节不透明。本文旨在推出一套面向文本条件生成的连续潜在 tokenizer 家族，覆盖多模态需求。

**方法关键点**：
- **KVAE-Audio**：48 kHz 全频带连续潜在音频 tokenizer，潜在帧率 50 Hz、64 通道，支持高质量音频重建与生成。
- **KVAE-3D**：因果视频 tokenizer，提供 4×16×16 和 4×8×8 两种压缩率，适应不同计算预算。
- **KVAE-2D**：图像 tokenizer，8 倍空间压缩，32 通道潜在表示。
- 公开完整训练细节、模型选择方法和消融实验，强调设计选择的影响。

**关键结果**：
- 重建指标（PSNR, LPIPS, PESQ 等）和生成指标（FD, CLIP score, CLAP score）在客观和主观评估中，匹配或超越 Wan-2.2、HunyuanVideo-1.5、FLUX.2、MovieGen、StableAudio、MMAudio 等前沿开源 tokenizer。
- 展示了连续潜在在生成任务上的有效性，代码开源可复现。
