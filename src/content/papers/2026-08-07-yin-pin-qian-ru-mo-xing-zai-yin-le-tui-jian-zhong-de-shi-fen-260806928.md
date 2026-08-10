---
title: 'From Classification to Recommendation: Empirical Analysis of Audio Embedding
  Models Application for Content-Based Music Recommendation'
title_zh: 音频嵌入模型在音乐推荐中的实证分析：从分类到推荐
authors:
- Qingrui Li
- Haowei Lou
- Chengkai Huang
- Quan Z. Sheng
- Lina Yao
affiliations:
- University of New South Wales
- Macquarie University
arxiv_id: '2608.06928'
url: https://arxiv.org/abs/2608.06928
pdf_url: https://arxiv.org/pdf/2608.06928
published: '2026-08-07'
collected: '2026-08-10'
category: GenRec
direction: 音频表示 · 生成式推荐 · Semantic ID
tags:
- Audio Embedding
- Music Recommendation
- Generative Recommender
- Semantic ID
- Empirical Evaluation
one_liner: 系统评估6种音频编码器在内容推荐、序列推荐和生成式推荐中的效果，揭示预训练与微调下的表现差异及Semantic ID设计影响
practical_value: '- **内容特征选型**：分类任务优化的预训练模型不一定适合推荐，优先考虑对比学习或多模态对齐的表示（如CLAP），它们在直接使用嵌入几何时更有效。

  - **序列推荐作为强基线**：交互式序列训练（如SASRec）能大幅缩小不同编码器的性能差距，在资源有限时可直接用通用音频嵌入+微调，无需追求领域最优预训练模型。

  - **生成式推荐中的Semantic ID设计**：RQ-VAE量化时，码本宽度和深度需谨慎平衡，更大容量不一定提升效果且可能引入不稳定；少量共享底码的前缀（如1-2层）足以保留推荐信息，深层码本收益递减。

  - **评估范型迁移**：该评测框架可复用于电商商品图片/视频等多模态推荐场景，直接比较不同编码器在纯内容、序列和生成式范式下的表现，为模型选型提供依据。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：预训练音频嵌入在分类任务中表现优异，但音乐推荐需要捕捉主观、行为依赖的偏好，现有模型的目标（掩码预测、对比学习、音频-文本对齐）并不保证生成适合推荐的表示空间。生成式推荐范式兴起，但音频编码器在这一新兴范式下的效果尚不明朗。

**方法**：选取6个代表性音频编码器（包括通用大模型、音乐领域模型、音频-文本对齐模型），在三种推荐系统（内容基、序列、Semantic ID生成式）上系统评测。生成式推荐通过RQ-VAE将音频嵌入量化为Semantic ID序列，并探究码本宽度、量化深度、前缀保留等设计的影响。

**关键结果**：1) 直接使用预训练嵌入时，音频-文本对齐（如CLAP）和音乐领域模型明显优于通用音频模型；2) 经过交互式序列训练（如SASRec）后，不同编码器性能差距大幅缩小；3) 增大Semantic ID容量（更深量化或更宽码本）并未一致提升生成推荐效果，反而增加训练不稳定性和过拟合风险，深层码本对推荐信息保留帮助有限。
