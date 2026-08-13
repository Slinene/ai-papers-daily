---
title: 'AdvFD: Boosting Visual Generation via Adversarial Fr''echet Distance Loss'
title_zh: AdvFD：通过对抗 Fréchet 距离损失提升视觉生成
authors:
- Mingju Gao
- Jingkai Zhou
- Kun Gai
- Changqian Yu
- Hao Tang
affiliations:
- Peking University
- KlingAI Research
arxiv_id: '2608.11205'
url: https://arxiv.org/abs/2608.11205
pdf_url: https://arxiv.org/pdf/2608.11205
published: '2026-08-10'
collected: '2026-08-13'
category: Training
direction: 生成模型后训练损失改进
tags:
- Adversarial Training
- Fréchet Distance
- Diffusion Models
- Post-training
- Feature Whitening
one_liner: 提出对抗 Fréchet 距离损失（AdvFD），用可学习对抗表示与特征白化缓解 Fréchet hacking，提升视觉生成后训练
practical_value: '- 主要是学术贡献，业务可借鉴点有限。

  - 指标 hacking 值得警惕：推荐/广告中仅优化 AUC、NDCG 等静态离线指标可能类似 Fréchet hacking，可尝试引入一个可学习评估器或对抗表征来暴露被固定指标忽略的分布差异。

  - 特征白化（whitening）作为对抗训练稳定技巧，可借鉴到多目标/对抗式训练（如 GAN-style 生成式召回）中，防止一侧通过放大特征范数欺骗损失。

  - 生成式推荐/创意生成中，后训练阶段加入分布级对抗损失可能提升生成结果与真实分布的全局对齐，但需要进一步验证。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：Fréchet distance 作为分布级目标用于生成器后训练，比样本级损失更直接优化分布差异。但直接优化会导致 Fréchet hacking：目标 FID 等指标持续改善，视觉质量和其他特征空间的对齐停滞甚至恶化。原因在于现有损失依赖静态预训练特征空间，对真实/生成分布差异的视角固定且不完整。

**方法关键点**：AdvFD 引入一个可学习的对抗表示，与静态表示互补；对抗表示最大化真实与生成样本的 Fréchet 差异，生成器在同一自适应空间最小化差异。为防止对抗表示通过特征放大 trivial 地提升目标，加入 real-feature whitening，对尺度与协方差几何归一化，稳定 min-max 优化。

**关键结果**：在 JiT 和 pMF 两种 backbone、不同模型规模的一步生成器后训练中一致提升；论文未提供具体数值，但强调跨配置的稳定改善。
