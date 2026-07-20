---
title: 'VideoRAE: Taming Video Foundation Models for Generative Modeling via Representation
  Autoencoders'
title_zh: VideoRAE：基于表示自编码器驯服视频基础模型的高效视频生成
authors:
- Zhihao Xie
- Junfeng Wu
- Xinting Hu
- Junchao Huang
- Li Jiang
affiliations:
- The Chinese University of Hong Kong, Shenzhen
- Huazhong University of Science and Technology
- Shenzhen Loop Area Institute
- University of Science and Technology of China
arxiv_id: '2607.14088'
url: https://arxiv.org/abs/2607.14088
pdf_url: https://arxiv.org/pdf/2607.14088
published: '2026-07-14'
collected: '2026-07-20'
category: Other
direction: 视频生成 · 潜空间自编码器
tags:
- video generation
- representation autoencoder
- foundation model
- discrete tokens
- alignment distillation
one_liner: 用冻结视频基础模型特征 + 轻量自编码器压缩为连续/离散潜变量，SOTA 生成且收敛快 5 倍
practical_value: '- **利用冻结基础模型特征做生成式推荐物品表示**：将预训练视频/图文模型的多尺度语义特征通过轻量投影网络压缩成紧凑潜变量，可类比把商品多模态内容编码为生成式检索的
  Semantic ID，省去从零训练 VAE 的成本。

  - **表示对齐目标替代 KL 正则化**：解码时引入局部/全局与冻结教师模型的对齐损失，能更好地保留语义信息，这种技巧可迁移到推荐系统中用户或物品编码器的蒸馏训练，避免
  KL 坍塌。

  - **多码本高维量化支持离散 token 生成**：VideoRAE 的多码本量化将连续特征离散化为 token 序列，适合自回归生成式推荐（如生成下一物品
  token），可参考其码本配置与训练策略。

  - **轻量架构实现快速收敛**：冻结主干 + 1D 自注意力投影的廉价设计使训练收敛加速约 5 倍，适合业务快速实验与低 GPU 预算场景。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有3D-VAE主要为像素重建优化，学到的潜空间缺乏语义和时空结构，限制了视频生成质量。视频基础模型（VFMs）具有强理解能力，但其冻结特征能否被压缩为紧凑、支持重建且生成友好的潜变量仍未知。

**方法**：提出VideoRAE，使用冻结VFM编码器的多尺度层次特征，经轻量1D自注意力投影头压缩为高效潜空间。连续版本直接供扩散 Transformer 使用；离散版本通过多码本高维量化得到 token，支持自回归生成器。解码时引入局部与全局表示对齐目标，以冻结VFM为教师进行蒸馏，无需KL正则化即可保留语义。

**关键结果**：在UCF-101类别到视频生成中，自回归和扩散生成器的gFVD分别达到40和93，均为SOTA；收敛速度比对比自编码器基线快约5倍。在2B参数的文本到视频实验中，替换LTX-VAE后用VideoRAE收敛更快，VBench指标更优。
