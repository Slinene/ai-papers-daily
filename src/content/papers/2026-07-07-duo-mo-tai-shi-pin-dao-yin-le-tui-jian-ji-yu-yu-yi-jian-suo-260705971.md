---
title: Multimodal Video-to-Music Recommendation via Semantic Retrieval and Temporal
  Reranking
title_zh: 多模态视频到音乐推荐：基于语义检索与时序重排序的两阶段框架
authors:
- Seungheon Doh
- Minhee Lee
- Sangmoon Lee
- Ben Sangbae Chon
- Juhan Nam
affiliations:
- Graduate School of Culture Technology, KAIST
- Gaudio Lab, Inc
arxiv_id: '2607.05971'
url: https://arxiv.org/abs/2607.05971
pdf_url: https://arxiv.org/pdf/2607.05971
published: '2026-07-07'
collected: '2026-07-11'
category: RecSys
direction: 视频到音乐推荐 · 多模态检索与重排
tags:
- video-to-music
- multimodal retrieval
- temporal reranking
- cross-modal embedding
- semantic compatibility
one_liner: 提出语义检索与时序重排序两阶段框架，在视频到音乐推荐中同时建模全局语义和细粒度时序对应
practical_value: '- 多模态融合思路可迁移：联合视觉、音频、文本信号构建联合表征，电商场景中可类似融合商品图像、描述文本、评论音频等多模态信息，提升语义匹配质量

  - 粗召回+细排两阶段架构效率与效果平衡：粗召回用全局嵌入快速筛选候选集，细排用时序注意力捕捉序列对齐，适合电商推荐中用户行为序列与候选项序列的精细匹配

  - 时序重排机制捕获动态对应：广告推荐中可借鉴对用户交互序列与广告创意序列进行细粒度时序对齐，提升点击率预估的时序合理性

  - 人类偏好评估补充离线指标：推荐系统除了离线A/B，可引入人类偏好对比，尤其在生成式推荐结果质量评估上更贴近实际体验'
score: 7
source: arxiv-cs.MM
depth: abstract
---

**动机**：视频创作者需要为视频搭配背景音乐，既要满足整体语义（情绪、风格）的兼容，又要考虑视觉动态与音乐节奏、情绪的时序对应。现有方法难以同时兼顾这两层需求。

**方法关键点**：提出VTMR两阶段框架。第一阶段利用多模态编码器将视频（视觉、音频、文本元数据）和音乐映射到联合表示空间，通过全局嵌入计算余弦相似度快速检索语义匹配的音乐候选集。第二阶段设计时序重排器，用交叉注意力机制对齐视频与音乐的时序序列，捕捉视觉变化与音乐元素（如节拍、力度）之间的细粒度对应，对候选列表重新排序。训练时结合对比学习与重排损失。

**关键结果**：在视频到音乐推荐任务上，语义检索阶段将R@10从最强基线的14.2提升至15.9，Median Rank从75降至58；加入时序重排后R@10进一步提升至18.3，Median Rank降至46，显示语义与时序信息的互补增益。人类偏好研究显示，VTMR整体偏好与商业基线持平，但音乐质量显著优于生成式基线。
