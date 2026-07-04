---
title: Representation Distribution Matching for One-Step Visual Generation
title_zh: 表征分布匹配实现一步视觉生成
authors:
- Lan Feng
- Wuyang Li
- Eloi Zablocki
- Matthieu Cord
- Alexandre Alahi
affiliations:
- EPFL
- Valeo.ai
- Sorbonne Université
arxiv_id: '2607.02375'
url: https://arxiv.org/abs/2607.02375
pdf_url: https://arxiv.org/pdf/2607.02375
published: '2026-07-01'
collected: '2026-07-04'
category: Training
direction: 生成模型训练与一步蒸馏
tags:
- One-Step Generation
- Distribution Matching
- MMD
- Diffusion Distillation
- Representation Learning
one_liner: 用修正的MMD、超大批次和平衡编码器组抗投机，将多步扩散模型蒸馏为一步生成器
practical_value: '- 推荐生成式模型蒸馏：可借鉴 RDM 范式，用预训练的用户/物品编码器计算表征分布距离（如 MMD），替代传统扩散损失，将多步扩散推荐模型蒸馏为一步生成器，降低推理延迟。

  - 抗投机评估：单一编码器的分布距离可能被“游戏”，推荐系统在做离线评估时，应采用多个独立预训练编码器的组合指标（如类似 SW_r14 的切片瓦瑟斯坦距离），确保生成质量真实提升。

  - 超大批次训练：MMD 估计需要大 batch size（>2048）来稳定梯度，推荐场景中在使用分布匹配损失时，应设计足够大的负采样或跨 batch 缓存机制，否则训练效果会显著下降。

  - 训练效率：iRDM 仅 90 H200 GPU 小时就能将四步 FLUX.2 蒸馏为一步模型，且指标超越原版，该高效蒸馏方案可推广至推荐系统的文本/图像生成模块，快速实现低成本部署。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：扩散模型需要多步去噪，推理慢；现有一步生成方法通常依赖对抗训练或复杂蒸馏。本文重新审视表征分布匹配（RDM），旨在用简单、可扩展的目标训练一步生成器。

**方法**：利用冻结预训练编码器的特征分布距离作为训练损失，核心是最大平均差异（MMD）。关键发现：
1.  以往 MMD 失效是因估计方式有偏，采用无偏估计并修正统计特性后，MMD 成为强大且可扩展的目标。
2.  生成 batch size 对分布匹配至关重要，最优值超过 2048，远超常规设置。
3.  单一编码器易被“游戏”：生成器可让该指标极低但图像仍失真，故需匹配多个精心选择的编码器组合，抵抗投机。
4.  为独立评估，提出 SW_r14，基于 14 个编码器的切片瓦瑟斯坦距离，不依赖训练损失，更难被欺骗。

**结果**：
- 结合上述策略的 iRDM 在 ImageNet 上取得一步生成 SOTA，SW_r14 1.30，PickScore 偏好度达 71.2%（未优化 PickScore）。
- 将四步 FLUX.2 后训练为一步模型，GenEval 从 0.794 提升至 0.826，PickScore 从 22.58 提升至 22.76，仅需 90 H200 GPU 小时。
