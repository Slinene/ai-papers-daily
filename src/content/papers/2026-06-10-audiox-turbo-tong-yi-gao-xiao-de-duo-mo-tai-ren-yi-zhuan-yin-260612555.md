---
title: 'AudioX-Turbo: A Unified Framework for Efficient Anything-to-Audio Generation'
title_zh: AudioX-Turbo：统一高效的多模态任意转音频生成框架
authors:
- Zeyue Tian
- Lei Ke
- Zhaoyang Liu
- Ruibin Yuan
- Liumeng Xue
- Yujiu Yang
- Weijia Chen
- Xu Tan
- Qifeng Chen
- Wei Xue
affiliations:
- The Hong Kong University of Science and Technology
- Tsinghua University
- Noiz AI
- Independent Researcher
arxiv_id: '2606.12555'
url: https://arxiv.org/abs/2606.12555
pdf_url: https://arxiv.org/pdf/2606.12555
published: '2026-06-10'
collected: '2026-06-13'
category: Multimodal
direction: 多模态音频生成 · 扩散模型蒸馏
tags:
- Audio Generation
- Diffusion Distillation
- Multimodal
- Flow Matching
- Teacher-Student
one_liner: 通过蒸馏实现统一多模态任意转音频生成，仅4步采样即超越多步基线，速度提升约25倍
practical_value: '- **少步蒸馏方案可迁移**：所采用的分布匹配蒸馏（DMD）适配流匹配框架，通过判别器提升少步生成质量，这一思路可直接应用于推荐系统中扩散模型的加速（如物品嵌入生成、语义ID去噪），在保持质量的同时大幅降低推理成本。

  - **多模态自适应融合模块值得参考**：针对文本、视频、音频等多种条件信号设计的融合机制，可启发电商多模态推荐或Agent中多源输入的对齐与融合设计，提升条件控制的灵活性。

  - **数据构建流程可复用**：两阶段收集与标注的大规模数据集IF-caps-Pro（约920万样本）构建方法，为构建多模态训练数据提供了工程范式，尤其适用于需要对齐文本与其它模态的场景（如商品文案与图片/视频的配对数据）。

  - **判别器在蒸馏中的应用**：扩散模型蒸馏中引入扩散基判别器对抗训练，这一技巧可尝试用于生成式推荐中少步采样质量的保真，例如在序列推荐或对话式推荐中加速候选项生成。'
score: 7
source: arxiv-cs.MM
depth: abstract
---

**动机**：灵活的多模态控制音频生成面临三大挑战：统一的多模态建模框架、大规模高质量训练数据、以及多步扩散采样导致的高昂推理成本。

**方法**：提出AudioX-Turbo，采用教师-学生蒸馏范式。教师模型AudioX-Base基于多模态扩散Transformer，通过多模态自适应融合模块对齐文本、视频、音频等异构输入，实现高保真合成。学生模型AudioX-Turbo通过适配流匹配的分布匹配蒸馏（DMD）获得，仅需4步采样，并引入扩散基判别器提升少步生成质量。此外，构建了大规模高质量数据集IF-caps-Pro（约9.2M样本），通过两阶段收集与标注流程确保数据质量。

**结果**：在文本到音频、文本到音乐等多项基准上，AudioX-Turbo性能优于多步基线，函数评估次数（NFE）减少约25倍，实现了高效、灵活的多模态指令跟随生成。
