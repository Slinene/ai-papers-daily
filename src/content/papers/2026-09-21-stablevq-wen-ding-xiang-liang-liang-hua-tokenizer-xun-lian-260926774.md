---
title: 'StableVQ: Practical Guidelines for Stable Vector-Quantized Tokenizer Training'
title_zh: StableVQ：稳定向量量化 tokenizer 训练实践指南
authors:
- Bao Tang
- Jiahao Guo
- Haoxiang Cao
- Wenyu Liu
- Changqian Yu
- Kun Gai
- Xinggang Wang
affiliations:
- Huazhong University of Science and Technology
- KlingAI Research
- South China Normal University
arxiv_id: '2609.26774'
url: https://arxiv.org/abs/2609.26774
pdf_url: https://arxiv.org/pdf/2609.26774
published: '2026-09-21'
collected: '2026-09-24'
category: Training
direction: VQ 视觉 tokenizer 训练稳定性
tags:
- Vector Quantization
- VQ-VAE
- Codebook Training
- Training Stability
- Image Tokenizer
- Discrete Representation
one_liner: 针对共享投影码本 VQ 训练不稳定，提出 Dynamic STE、Region VQ Loss、Decoupled Schedule 三项无参改进，稳定提升码本利用率与重建质量
practical_value: '- 若在生成式推荐中使用 VQ / Semantic ID 做物品量化，常遇到码本坍塌或利用率低：可借鉴 Region VQ Loss
  的思路，让码本独立学习完整覆盖编码器输出分布，而非依赖编码器梯度抖动激活，提升 ID 多样性。

  - Dynamic STE 修正了低码本利用率下直通估计器的梯度不稳定问题，适合推荐场景中离散 ID 生成（如 Gumbel-Softmax 或 ST-Gumbel）的梯度回传，避免因初期码本利用率低导致训练崩溃。

  - 多模块联合训练（如编码器-解码器 + 码本、生成器 + 判别器）常因收敛速度不匹配而不稳定：Decoupled Schedule 将不同模块使用独立学习率调度，可直接迁移到多任务推荐模型或
  Agent 策略与价值网络的联合训练。

  - 整体无额外可学习参数、轻量易插入，适合在现有推荐召回或特征量化模块上低成本验证。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现代自回归与掩码图像生成依赖离散视觉 tokenizer，共享投影码本方法虽提升了码本利用率，但训练稳定性仍是关键挑战。根因在于 Encoder-Decoder 与 Codebook 的训练目标相互纠缠：任一模块无法独立完成自身职责，只能依赖偶然协作，训练压力大时系统易崩溃。

**方法**：StableVQ 重新审视各模块的学习目标，提出三项无额外可学习参数的改进：
- Dynamic STE：修正编码器学习目标的不稳定性，在低码本利用率下也能稳健优化重建空间；
- Region VQ Loss：重构码本学习目标，使码本能独立完整跟踪编码器输出分布，不依赖编码器振荡来驱动激活；
- Decoupled Schedule：为 Encoder-Decoder 与 Codebook 分别设定独立学习率调度，匹配各自优化动态。

**结果**：在 ImageNet 上，跨不同码本尺寸与初始化设置，训练稳定性、码本利用率和重建质量均获得一致改善。
