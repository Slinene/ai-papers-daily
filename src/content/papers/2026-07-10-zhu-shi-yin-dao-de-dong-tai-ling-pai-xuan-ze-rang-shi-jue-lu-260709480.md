---
title: Foveation-Guided Dynamic Token Selection for Robust and Efficient Vision Transformers
title_zh: 注视引导的动态令牌选择让视觉 Transformer 更鲁棒高效
authors:
- Ibrahim Batuhan Akkaya
- Kishaan Jeeveswaran
- Bahram Zonooz
- Elahe Arani
affiliations:
- Advanced Research Lab, NavInfo Europe
- Eindhoven University of Technology
arxiv_id: '2607.09480'
url: https://arxiv.org/abs/2607.09480
pdf_url: https://arxiv.org/pdf/2607.09480
published: '2026-07-10'
collected: '2026-07-13'
category: Other
direction: 高效视觉Transformer · 动态令牌选择
tags:
- Dynamic Token Selection
- Vision Transformer
- Foveation
- Adversarial Robustness
- Efficient Inference
- Human Visual System
one_liner: 模拟人眼中央凹视觉，动态选择重要 token 并融合多尺度信息，在 50% 预算下超越 DeiT-S 且计算量降低 34.57%
practical_value: '- 论文属于计算机视觉领域，与推荐系统、对话 Agent 等无直接关联，业务可借鉴的模块和方法有限。

  - 动态 token 选择的思想可类比于用户行为序列处理：在计算资源受限时，通过简单前馈模块（类似 fixation）丢弃不重要的行为 token，保留关键交互，可提升效率且潜在增强鲁棒性。

  - 多尺度“中央凹”嵌入生成方式（foveation）可启发商品图像编码：对商品图的不同区域按显著性分配注意力分辨率，在图像搜索或推荐缩略图生成中平衡精度与算力。

  - 无额外对抗训练即获得鲁棒性的特性，提示在推荐模型部署时可通过结构设计（而非仅依赖数据增强）改善对噪声特征或异常行为的容忍度。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：人类视觉系统通过中央凹采样和眼动实现高效感知，天然兼具计算效率和鲁棒性。现有视觉 Transformer（ViT）高计算量且易受噪声和对抗攻击，亟需一种结构层面兼顾二者的方案。

**方法关键点**：提出注视动态 Transformer（FDT），在标准 ViT 中引入两个模块：**fixation** 模块在单次前传中评估 token 重要性，按给定预算选择注视点，丢弃无关 token；**foveation** 模块围绕注视点生成多尺度嵌入，模拟中央凹周围分辨率递减的特性，使注意力操作能利用多粒度上下文。两个模块均轻量、可端到端学习，无需额外监督。

**关键结果**：在 ImageNet 分类任务上，50% 的 token 预算下，FDT 达到 81.9% 的 top-1 准确率，超过 DeiT-S 的 80.9%，同时 MACs 减少 34.57%；面对多种高斯噪声、椒盐噪声以及 FGSM、PGD 等对抗攻击，无针对性训练的 FDT 均表现出比 DeiT-S 更强的鲁棒性。论文展示了在准确率和效率权衡曲线上的优势，证明受生物启发的动态 token 选择可以同时提升推理效率和固有鲁棒性。
