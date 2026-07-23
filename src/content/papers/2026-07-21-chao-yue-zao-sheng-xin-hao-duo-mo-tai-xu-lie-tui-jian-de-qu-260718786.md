---
title: 'Beyond Noisy Signals: Dual-Level Denoising for Multi-modal Sequential Recommendation'
title_zh: 超越噪声信号：多模态序列推荐的双层去噪框架
authors:
- Jie Luo
- Qi Jin
- Xinming Zhang
affiliations:
- University of Science and Technology of China
arxiv_id: '2607.18786'
url: https://arxiv.org/abs/2607.18786
pdf_url: https://arxiv.org/pdf/2607.18786
published: '2026-07-21'
collected: '2026-07-23'
category: RecSys
direction: 多模态序列推荐 · 双层图频域去噪
tags:
- Multi-modal
- Sequential Recommendation
- Denoising
- Graph Low-pass Filter
- FFT
- Contrastive Alignment
one_liner: 提出图低通滤波和频域自适应滤波的双层去噪，联合清洗多模态特征与序列行为噪声，显著提升推荐鲁棒性
practical_value: '### 可以借鉴到电商推荐工作中

  - **特征层面图低通滤波去噪**：利用物品语义图上的拉普拉斯平滑作为低通滤波器，能有效抑制预训练视觉/文本特征中与推荐意图无关的高频噪声。在构造电商场景的商品多模态特征（如商品图、描述）时，可直接复用此轻量模块，无需引入复杂注意力，计算开销小。

  - **序列层面的频域去噪**：通过 FFT 将用户交互序列变换到频域，用可学习的频率滤波器自适应增强良性信号、衰减异常点击等随机噪声。对于电商/广告场景中常见的误触、短暂兴趣等噪声行为，该模块能显著增强序列建模的稳定性，可插入现有
  Transformer 或 SASRec 类骨干结构。

  - **多模态对比对齐目标**：引入跨模态对比损失，强制视觉与文本表征在语义上一致，能弥补模态间语义鸿沟。在构建商品多模态特征库时，可用此约束训练更好的对齐编码器，或直接在召回模型中加入该辅助损失。

  - **整体架构即插即用**：DDMSR 的 denoising 组件均可独立拆解，作为现有推荐模型的增强插件。对于已有序列模型（如 BST、DIEN），只需要在特征输入层和序列编码层分别接入图滤波与频域滤波，实验显示在多个公开数据集上稳定提升
  3–8%，适合快速 A/B 测试验证。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
多模态序列推荐利用图文等辅助信息，然而面临双重噪声困境：1) **特征冗余**：通用预训练表征与推荐意图存在语义鸿沟，高频噪声掩盖有效信号；2) **序列随机性**：误点击、偶发行为等让交互序列含虚假关联，干扰兴趣建模。现有方法缺乏对特征和序列两个层次噪声的协同处理。

### 方法
提出 **DDMSR**，从“特征-拓扑”和“序列-频域”两个视角系统去噪：
- **图特征去噪模块**：基于物品语义图，用拉普拉斯平滑作为结构低通滤波器，抑制高频语义噪声，保留显著特征。
- **频域序列去噪模块**：对交互序列做 FFT，用可学习的频率滤波器自适应调制频谱，衰减异常行为对应的高频分量。
- **多模态对比对齐**：跨模态对比损失强制图文表征语义一致，弥合异质鸿沟。

### 关键结果
在4个公开基准（如Amazon、Movielens）上，DDMSR 较最先进基线（SASRec、MMSSL等），HR@10 和 NDCG@10 平均提升 3%-8%，并在噪声强度增大时鲁棒性优势更显著；消融验证了双层去噪与对比对齐的协同增益。
