---
title: 'LeVJEPA: Efficient & Scalable Video Pretraining without the Heuristics'
title_zh: LeVJEPA：无需启发式的高效可扩展视频预训练
authors:
- Lukas Kuhn
- Lucas Maes
- Giuseppe Serra
- Quentin Le Lidec
- Yann LeCun
- Randall Balestriero
- Florian Buettner
affiliations:
- German Cancer Research Center
- Mila
- Université de Montréal
- Brown University
- Advanced Machine Intelligence (AMI Labs)
arxiv_id: '2608.27395'
url: https://arxiv.org/abs/2608.27395
pdf_url: https://arxiv.org/pdf/2608.27395
published: '2026-08-27'
collected: '2026-08-29'
category: Training
direction: 高效视频自监督预训练 · 无坍塌目标
tags:
- Video Pretraining
- Self-Supervised Learning
- Token Dropping
- Block-Causal Attention
- SIGReg
- Efficiency
one_liner: 首个在 LeJEPA 无坍塌目标下训练的视频编码器，用 token dropping 与 block-causal attention 大幅降低预训练算力
practical_value: '- uniform random token dropping 能同时降低注意力序列长度和提升下游指标，可直接迁移到电商短视频/直播内容或用户行为序列的预训练：在
  Transformer 输入前按固定比例随机丢弃 token，无需重要性采样，工程实现简单。

  - SIGReg 的 collapse-free 单分支目标替代 EMA target encoder + stop-gradient + predictor，可简化多模态/行为序列对比学习架构，减少显存与超参；若团队在用
  Two-tower 或 CLIP 式预训练，可尝试用带正则的 invariance loss 去掉动量编码器。

  - block-causal attention 让帧表示只依赖过去观测而几乎不损失精度，适合直播流式场景或推荐中的时序行为建模：使用块级 causal mask
  可避免未来信息泄漏，并使模型支持在线推理。

  - 若已有商品视频/直播数据，token dropping 后的视频预训练在匹配 FLOPs 下接近图像预训练的 appearance 指标，且 motion
  指标近乎翻倍，可考虑用视频底座替代静态图底座，增强对动态商品展示的理解。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：视频自监督预训练主流方法依赖 EMA target encoder、stop-gradient、predictor 或像素重建来防 collapse，架构复杂、计算开销大。

**方法关键点**：LeVJEPA 采用 LeJEPA 的 collapse-free 目标，仅需单编码器+投影器，配合 SIGReg 正则，有可证明的防坍塌保证。对 clip 的全局/局部视图做 invariance loss；训练成本由编码器观察 token 数决定，uniform random token dropping 大幅减少 token 并提升下游精度；因无需分支不对称，可改为 block-causal attention，使每帧表示只依赖过去观测，时间顺序内化为编码器属性。

**关键结果数字**：ViT-S/B/L 在相同数据/epoch 下匹配或超过 V-JEPA 2，预训练总算力降低 5.6–20.8×；匹配总 FLOPs 时 ImageNet-1K 超过最强视频基线 7.6 点，并在运动中心基准保持竞争力。与 compute-matched DINOv2 帧训练相比，appearance 指标接近，motion 指标近乎翻倍。
