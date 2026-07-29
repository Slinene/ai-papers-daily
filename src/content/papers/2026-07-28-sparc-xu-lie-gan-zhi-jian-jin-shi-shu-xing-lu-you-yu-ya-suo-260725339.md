---
title: 'SPARC: Sequence-aware Progressive Attribute Routing and Compression Framework
  for Generative Recommendation'
title_zh: SPARC：序列感知渐进式属性路由与压缩框架
authors:
- Chang Liu
- Changfa Wu
- Hui Qian
- Binbin Cao
- Jian Wu
- Yuliang Yan
- Han Zhu
- Bo Zheng
affiliations:
- Alibaba Group
arxiv_id: '2607.25339'
url: https://arxiv.org/abs/2607.25339
pdf_url: https://arxiv.org/pdf/2607.25339
published: '2026-07-28'
collected: '2026-07-29'
category: GenRec
direction: 生成式推荐 · 多字段压缩与上下文路由
tags:
- Generative Recommendation
- Semantic ID
- Multi-field Compression
- Context-aware Routing
- Sequence Modeling
- Lightweight Front-end
one_liner: 在生成推荐中，先对多字段行为历史做上下文建模再压缩，使每个交互仅占一个 token 且不损失关键信息
practical_value: '- **可插拔的轻量级历史压缩模块**：SPARC 作为生成式推荐骨干的前端，不改变训练目标与 SID，可直接插入现有模型（如
  RankGR、TIGER），在保持推理成本不变的前提下提升历史交互的表达能力。

  - **上下文感知路由机制**：CAR 通过将字段划分为身份（SID）与侧信息，并用上下文条件动态路由侧信息到有限槽位，这种设计可借鉴到电商推荐中的多字段行为建模——例如按行为类型、商品属性、时间衰减等动态决定哪些侧信息更具信息量，避免静态聚合的过早信息丢失。

  - **“先上下文，再压缩”的原则**：先按字段类型构成长序列（Field-wise Context Modeling）捕捉时序演化，再跨字段压缩；工程实现中可以为每个字段维护一条独立的序列
  Tranformer 或轻量编码器，成本远低于直接插入全字段 token 序列。这种方法对广告点击历史、多行为序列等场景均可复用。

  - **槽位分工的可解释性与可控性**：CAR 的路由权重自然形成了不同槽位对不同类型侧信息的偏好（例如一个槽专注行为类型与新鲜度，另一个专注卖家/品牌），可为后续人工规则或约束提供参考，有利于在线调优与特征筛选。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
在工业级生成式推荐中，每条用户历史交互包含多种异构字段（商品 SID、类目、品牌、价格、行为类型、时间衰减等）。全量展开为多 token 输入会极大增加生成骨干的序列长度，导致训练与推理开销急剧上升；而静态聚合为单个表示又可能丢失与当前上下文相关的关键信息（例如同一品牌连续浏览时品牌更重要，价格与行为类型在购买意愿变化时更重要）。因此，需要在固定 token 预算下实现上下文感知的、可保留互补信息的历史压缩。

### 方法
SPARC 是一个轻量级前端模块，对多字段历史进行三步渐进式压缩，最终每个交互只生成一个 token 输入骨干：
- **Field-wise Context Modeling (FCM)**：将同一字段类型沿用户历史组成序列，用轻量序列编码器捕捉字段级时序演化，得到上下文感知的字段表示。
- **Context-aware Attribute Routing (CAR)**：保留 SID 字段作为身份 token；对侧字段，结合原始表示、上下文表示与字段嵌入计算路由权重，将侧信息动态分配到固定数量的可学习侧槽位中，形成中间 token 集（身份 + 侧槽）。
- **Sequence-level Token Consolidation (STC)**：将所有交互的中间 token 展平成细粒度序列，通过轻量 Transformer 进行跨交互建模，再经残差门控融合身份与侧信息，压缩为单 token 序列。

### 实验
在工业数据集 TaoBao（21M 用户、260M 商品、26B 交互）和公开数据集 Amazon Beauty/Toys 上评测。对比 YouTubeDNN、SASRec、BERT4Rec、TIGER、RankGR 等传统与生成式基线。SPARC 在 RankGR 基础上进一步提升：TaoBao HR_click@20: 0.1568→0.1669，HR_click@1000: 0.5777→0.5883；Beauty HR@20: 0.0466→0.0794，HR@500: 0.2289→0.3571。消融实验表明静态压缩变体（MLP、QFormer 等）带来的提升有限，验证了上下文条件压缩的关键作用。路由分析显示槽位产生明确分工（一个槽关注行为类型 / 时间衰减，另一个关注卖家 / 品牌），且同一物品在不同用户历史下的路由权重显著变化，证明上下文感知路由的有效性。

### 核心结论
**“先序列上下文交互，再压缩”的原则，能以极低成本让历史 token 承载动态侧信息，是生成推荐中平衡效率与信息量的有效路径。**
