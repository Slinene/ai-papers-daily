---
title: POI Recommendation with LLM-Augmented Multi-Graph Learning and Contrastive
  Alignment
title_zh: LLM 增强多图学习与对比对齐的 POI 推荐
authors:
- Burak Tamer
- Wolfram Höpken
- Zehui Wang
affiliations:
- Institute for Digital Transformation - University of Applied Sciences Ravensburg-Weingarten,
  Germany
arxiv_id: '2608.16407'
url: https://arxiv.org/abs/2608.16407
pdf_url: https://arxiv.org/pdf/2608.16407
published: '2026-08-17'
collected: '2026-08-18'
category: RecSys
direction: 多图对比学习 · LLM 语义增强
tags:
- POI Recommendation
- Multi-Graph Learning
- Contrastive Learning
- LLM-Augmented
- Cold-start
- LightGCN
one_liner: 用 LLM 生成语义图和地理图扩展 LightGCN，通过跨视图对比对齐缓解 POI 冷启动
practical_value: '- **LLM 生成 item 语义图**：对 item 的多模态信息（图/文/元数据）用 LLM 生成 photo summary
  + keywords，再用 sentence transformer（如 all-MiniLM-L6-v2）编码后做 top-k 相似度建图。电商/本地生活可直接对商品标题、详情、图片生成摘要，构建商品语义邻接图，冷启动
  item 也能获得邻居信号。

  - **地理邻近性建模**：用 Haversine 距离 + top-k（k=10）构建地理 item-item 图，权重取 `1/(1+distance)`，与语义相似度权重同尺度，归一化后做
  LightGCN 传播。本地生活/门店推荐可直接复用，电商可扩展到配送范围、仓储邻近等空间关系。

  - **跨视图对比对齐很关键**：将 collaborative embedding 与 semantic/geographic embedding 做双向 InfoNCE，仅对
  batch 内正样本计算，τ=0.2，λ=0.05 作为正则化项。消融显示该对齐是主要收益来源，去掉后 Recall@20 下降 22.9%。建议在多路召回或表示融合场景中，用对比损失强制行为表示与内容/空间表示一致。

  - **工程实现简单有效**：所有视图共享 item embedding 矩阵，多图传播后直接 additive fusion 相加，不引入额外参数。这种轻量设计适合线上快速迭代，后续可替换为可学习加权融合。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：POI 推荐中基于 GNN 的协同过滤依赖用户-item 交互，面对新商户或低交互商户（冷启动）缺乏有效表示。但商户的语义信息（图片、文本、元数据）和地理位置信息不依赖交互，可直接补偿缺失的协同信号。本文试图用 LLM 生成的语义描述和地理距离构建辅助 item-item 图，通过多图传播与跨视图对比对齐，提升推荐并缓解冷启动。

**方法关键点**：
- 构建三张图：用户-item 交互图（带评分权重）、LLM 生成 photo summary + keywords 经 sentence transformer 编码后构建的语义 item-item 图（top-k=10 邻居）、基于 Haversine 距离构建的地理 item-item 图（top-k=10，权重 `1/(1+distance)`）。
- 模型以 LightGCN 为骨干，三条传播路径并行：collaborative 路径 3 层，语义和地理路径各 2 层；所有路径共享 item embedding 矩阵，最终 item 表示为三视图逐元素相加。
- 训练采用 BPR loss + 双向 InfoNCE 对比损失（λ=0.05）+ L2 正则；对比损失强制协作视图与语义/地理视图对同一 item 表示对齐，同时推开 batch 内其他 item。

**关键实验**：在 Yelp Multimodal Recommendation Dataset 上，对比 NGCF、NeuMF、GC-MC、LightGCN、MF-BPR、ItemKNN、UserKNN、SGL。LLM-MGCL 相比 LightGCN，Recall@20 提升 52.0%，NDCG@20 提升 64.8%；与最强基线 SGL 基本持平（Recall@20 0.1175 vs 0.1187，NDCG@20 0.0722 vs 0.0712）。消融显示移除对比对齐后 Recall@20 从 0.1175 降至 0.0906，而单独移除语义图或地理图仅轻微下降，说明对比对齐是主要驱动力。

**最值得记住的一句话**：外部 grounded 的 LLM 语义/空间信息通过多图传播 + 跨视图对比对齐，可以替代缺失的协同信号，有效缓解 item 冷启动。
