---
title: 'Take a Step Back: A Dual-Granularity Raw Feature Empowered Intermediate Fusion
  Graph Convolutional Network for Multimodal Recommendation'
title_zh: 退一步看：双粒度原始特征增强的中间融合图卷积多模态推荐网络
authors:
- Jinfeng Xu
- Zheyu Chen
- Shuo Yang
- Jinze Li
- Wenhao Yuan
- Ziyue Peng
- Puzhen Wu
- Shujie Li
- Jian Chen
- Zheng Lin
affiliations:
- The University of British Columbia
- The Hong Kong Polytechnic University
- The University of Hong Kong
- The Hong Kong University of Science and Technology
- University of Luxembourg
arxiv_id: '2611.19974'
url: https://arxiv.org/abs/2611.19974
pdf_url: https://arxiv.org/pdf/2611.19974
published: '2026-11-15'
collected: '2026-11-17'
category: RecSys
direction: 多模态推荐 · 图卷积融合
tags:
- Multimodal Recommendation
- Graph Convolutional Network
- LLM Feature Engineering
- Modality Fusion
- Cold Start
one_liner: 用 LLM 构建双粒度原始特征，并以中间融合 GCN 和动态跨模态权重修正替代纯对齐式融合，提升多模态推荐
practical_value: '- LLM 直接生成物品/内容的双粒度 raw features（粗粒度：类别/主题；细粒度：属性/卖点），可沉淀为新物品冷启动特征层，减少对交互日志和
  ID embedding 的依赖，适合电商新品与长尾商品。

  - 中间融合 GCN 的 dynamic cross-modality weight correction 不强行把各模态 align 到同一空间，而是在图上做跨模态消息传递并动态修正融合权重，能保留
  modal-specific 信息；可借鉴到多模态召回/排序中的 late fusion 改造成图传播融合。

  - 方法对数据稀疏和冷启动有专门分析，工程上可先用 LLM 生成结构化文本特征，再接入 GNN，比单纯训练多模态 embedding 更稳。

  - 架构与额外 contrastive alignment 兼容，冷启动阶段可只启用 raw feature + 中间融合，后期数据丰富后再追加对齐任务，适合渐进式上线。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：现有多模态推荐存在两大问题：表示学习质量受推荐数据稀疏制约，难以训练多粒度表示；融合常靠 contrastive learning 对齐不同模态，但 pure alignment 会过度压缩模态特有信息。

**方法关键点**：作者提出 DIGCN。它利用 LLM 的多模态理解能力直接生成 item 的双粒度原始特征：粗粒度特征提供全局语义，细粒度特征保留局部细节，避免因行为稀疏导致表示学习困难。融合侧设计 intermediate fusion graph convolutional network，在 user-item 交互图上引入跨模态消息传递，并加入 dynamic cross-modality weight correction 动态修正不同模态的融合权重，使模型能保留 modal-specific 信息而非只做对齐。

**关键结果**：在四个真实多模态推荐数据集上，DIGCN 稳定超过多种强基线；在数据稀疏和冷启动场景下优势更明显。分析还表明 DIGCN 具有高扩展性，可与额外 contrastive alignment 任务叠加并进一步受益。
