---
title: A Technique to Model Product Information and User Reviews (MPIUR)
title_zh: 一种建模产品信息与用户评论的技术（MPIUR）
authors:
- Emna Belguith
- Fajrian Yunus
- Talel Abdessalem
affiliations:
- Higher School of Communication of Tunis
- LTCI, Télécom Paris, IP Paris
arxiv_id: '2611.13361'
url: https://arxiv.org/abs/2611.13361
pdf_url: https://arxiv.org/pdf/2611.13361
published: '2026-11-09'
collected: '2026-11-11'
category: RecSys
direction: 多模态图推荐 · 评论与内容融合
tags:
- multimodal recommendation
- graph neural networks
- user reviews
- sparse items
- collaborative-semantic alignment
one_liner: MPIUR 提出多模态图推荐模型，融合商品文本、图像和用户评论，并按交互密度自适应融合协同与语义信号
practical_value: '- 可把用户评论作为额外节点/边引入 item 异构图，通过图卷积传递评论语义，缓解仅依赖 ID 协同信号或 item 文本/图像单一模态的冷启动问题，尤其适合长尾商品。

  - 用 item 交互密度自适应调节协同过滤信号与语义内容信号的融合权重：对热门商品更信任协同，对稀疏商品更多依赖多模态内容和评论；工程上可按曝光/点击分桶实现。

  - 图像和文本表示对齐是有效防噪手段，可在商品多模态 embedding 输出层加对比/对齐 loss，避免某模态缺失或噪声时影响整体表示。

  - 实验显示该方法在 Musical Instruments 和 Baby 两类目均取得最佳 nDCG@10/Recall@10，且稀疏 item 上提升明显；评估时可单独观察稀疏商品的指标，有助于验证冷启动收益。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：电商平台天然提供三类互补信息：商品文本描述、商品图片和用户评论。现有多模态推荐方法常忽略评论，或未在统一框架中融合三模态，导致长尾/稀疏商品推荐效果受限。

**方法关键点**：MPIUR 提出多模态图推荐模型。首先将用户评论编码进异构图，使评论文本成为连接用户与商品的额外语义路径；其次对齐图像和文本表示，形成更一致的商品多模态表征；第三，根据商品交互密度自适应调整协同信号与语义内容信号的融合程度，密度低的商品更依赖多模态和评论语义。

**关键结果**：在 Amazon Reviews 2023 的 Musical Instruments 和 Baby 两类目上，MPIUR 取得所有对比方法中最佳全局 nDCG@10 和 Recall@10；在稀疏商品子集上同样取得最佳 nDCG@10 和 Recall@10，表明联合利用评论和多模态商品内容在交互历史有限时特别有效。
