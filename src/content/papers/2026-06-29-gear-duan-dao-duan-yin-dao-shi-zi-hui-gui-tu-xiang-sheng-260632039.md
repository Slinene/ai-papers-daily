---
title: 'GEAR: Guided End-to-End AutoRegression for Image Synthesis'
title_zh: GEAR：端到端引导式自回归图像生成
authors:
- Bin Lin
- Zheyuan Liu
- Chenguo Lin
- Sixiang Chen
- Yunyang Ge
- Yunlong Lin
- Jianwei Zhang
- Miles Yang
- Zhao Zhong
- Liefeng Bo
affiliations:
- 北京大学
- 腾讯混元
arxiv_id: '2606.32039'
url: https://arxiv.org/abs/2606.32039
pdf_url: https://arxiv.org/pdf/2606.32039
published: '2026-06-29'
collected: '2026-07-02'
category: Training
direction: 端到端联合训练与表示对齐
tags:
- End-to-End Training
- Vector Quantization
- Autoregressive Models
- Representation Alignment
- Image Synthesis
one_liner: 通过双路读出实现 VQ tokenizer 与 AR 生成器端到端联合训练，加速收敛并提升表示对齐
practical_value: '- **生成式推荐的 tokenizer 与生成器联合优化**：若用 VQ 将物品 ID 映射为离散 token 再自回归生成推荐列表，可借鉴双路读出（硬分支训生成器、软分支用表示对齐损失更新
  tokenizer），解决离散索引不可导问题，使 tokenizer 主动适配生成器。

  - **表示对齐损失的设计**：将 DINOv2 等预训练特征作为对齐目标，只用于 tokenizer 的软分支梯度回传，生成器本身并不直接接收对齐损失，这种非对称设计可迁移到推荐场景中，让物品
  tokenizer 学到更易被生成器预测的分布。

  - **收敛加速**：该方法在 ImageNet 上将 gFID 收敛速度提升最高 10 倍，对于推荐模型同样追求快速迭代，联合训练可能显著减少达到目标性能所需的训练步数，尤其适合需要频繁更新的工业级推荐系统。

  - **灵活适配不同量化器**：方法兼容 VQVAE、LFQ、IBQ 等多种量化方式，推荐系统中物品 ID 的离散化策略多样，此技术可降低替换量化模块的适配成本。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：传统视觉生成模型分两阶段训练——先训练并冻结 VQ tokenizer，再训练 AR 生成器，导致 tokenizer 无法感知生成器的建模偏好，生成的离散索引并非最优。

**方法**：GEAR 提出端到端联合训练框架，核心是双路读出的码本赋值。一条硬分支将 one-hot 索引输入 AR 模型做下一 token 预测，另一条可微分软分支计算与 DINOv2 表示的相似度分布，并引入表示对齐损失，该损失的梯度仅反向传播给 tokenizer，不干扰 AR 模型训练。生成器通过自己的学习信号间接引导 tokenizer 调整，使其索引分布更易预测。

**结果**：在 ImageNet 256×256 上，相同训练步数下 GEAR 的 gFID 相对强基线 LlamaGen-REPA 大幅降低，收敛速度提升最高 10 倍；模型越大收益越明显，XL 尺寸下 gFID 从 11.98 降至 4.08（无 CFG）。学习到的 patch 特征明显更优，线性探测精度提升 10%+，且空间一致性更强。方法在 VQVAE、LFQ、IBQ 三种量化器上均有效，并成功迁移到文本到图像生成。
