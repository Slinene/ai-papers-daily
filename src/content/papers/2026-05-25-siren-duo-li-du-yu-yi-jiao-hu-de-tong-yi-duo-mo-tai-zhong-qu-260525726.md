---
title: 'SIREN: Unified Multi-Granularity Semantic Interaction for Multi-Modal Lifelong
  User Interest Modeling'
title_zh: SIREN：多粒度语义交互的统一多模态终身兴趣建模
authors:
- Yaqian Zhang
- Ruyi Yu
- Tianyi Li
- Bohan Liu
- Maoquan Ye
- Ke Wang
- Shifeng Wen
- Junwei Pan
- Lijie Wang
- Qi Zhou
affiliations:
- Tencent Inc.
- Xiamen University
arxiv_id: '2605.25726'
url: https://arxiv.org/abs/2605.25726
pdf_url: https://arxiv.org/pdf/2605.25726
published: '2026-05-25'
collected: '2026-05-26'
category: RecSys
direction: 多模态终身兴趣建模 · 语义ID
tags:
- Multi-modal
- Semantic ID
- Lifelong Sequence
- Target Attention
- RQ-VAE
- Industrial Recommendation
one_liner: 在工业推荐的两阶段框架中，通过语义ID和相似度桶实现多模态信号的早期融合，兼顾效果与部署效率。
practical_value: '- **语义ID生成与使用**：利用RQ-VAE将多模态embedding离散化为分层语义ID，并通过前缀编码保留层级语义，可作为item的稳定通用token，既用于GSU的硬检索（倒排索引，降低90%以上在线成本），又作为ESU中细粒度特征，可迁移至电商商品的生成式推荐或冷启表征。

  - **早期融合代替晚期融合**：将相似度桶和语义ID直接拼入item表征，与ID特征一起进入target-conditioned Transformer进行统一序列建模，而不是在序列聚合后再融合。这让多模态信号参与注意力权重和兴趣表征的联合学习，可应用于短视频、广告等场景的多模态长期行为建模。

  - **相似度桶化与语义ID的互补设计**：相似度桶提供粗粒度的目标相关度，语义ID捕获细粒度的物品语义和协同异质性。分析表明二者互补，且单纯增加桶数无法弥补细粒度缺失。在电商场景中可借鉴该组合特征方式，提升老客与新品的匹配精度。

  - **冷启动增益**：多模态信号显著提升低活用户和新广告的效果（GMV增益可达整体平均的1.4~3.6倍），对于电商新品冷启、小语种用户等场景有直接参考价值。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：工业推荐系统普遍采用两阶段（GSU-ESU）架构处理终身行为序列，但引入多模态内容特征时，现有方法多采用序列分别建模后晚期融合，导致多模态信号与协同信号交互不足，且仅依赖相似度会掩盖协同异质性。

**方法要点**：
- **多模态特征构建**：用RQ-VAE对预训练多模态embedding量化生成分层语义ID（SemID），并采用前缀编码，同时将目标-行为相似度离散化为桶嵌入。
- **GSU阶段**：提供两种检索策略——基于相似度的软检索（效果优先）和基于顶层SemID的硬检索（效率优先，利用倒排索引，在线成本降低>90%）。
- **ESU阶段**：将物品ID特征、前缀SemID嵌入、相似度桶嵌入拼接为统一表征，输入target-conditioned Transformer，并进行元素级目标交互，实现多粒度信号的早期融合与联合学习。

**关键结果**：
- 在Taobao-MM数据集上，GAUC达0.6155，相对最佳基线MUSE提升0.11%（+2.48% vs ID-only）；消融显示相似度桶和SemID互补，目标交互增强表示判别力。
- 腾讯微信广告线上A/B：朋友圈GMV+2.28%、公众号+3.87%、视频号+1.61%，低活用户和冷启广告增益更显著。

**核心洞见**：粗粒度相似度桶与细粒度语义ID的组合，以item-level早期融合方式统一学习多模态与协同信号，是终身兴趣建模效果与效率平衡的关键。
