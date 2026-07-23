---
title: Topology-Aware Tokenization for Generative Recommendation
title_zh: 面向生成式推荐的拓扑感知词元化方法
authors:
- Yaokun Liu
- Yifan Liu
- Zhenrui Yue
- Gyuseok Lee
- Zelin Li
- Ruichen Yao
- Dong Wang
affiliations:
- University of Illinois Urbana-Champaign
arxiv_id: '2607.18600'
url: https://arxiv.org/abs/2607.18600
pdf_url: https://arxiv.org/pdf/2607.18600
published: '2026-07-21'
collected: '2026-07-23'
category: GenRec
direction: 生成式推荐 · 拓扑保持词元化
tags:
- Generative Recommendation
- Item Tokenization
- Topology Preservation
- Knowledge Distillation
- Sequential Recommendation
one_liner: 提出多级蒸馏框架 TopoTok，在量化过程中保留项目拓扑结构，缓解失真，召回率最高提升 9.42%
practical_value: '- 生成式推荐中项目嵌入量化为 token 时常破坏物品间邻近关系，可借鉴 TopoTok 的多级蒸馏框架来训练电商中商品 tokenizer，使相似商品的
  token 表征也接近，提升下一项预测准确率。

  - 组间/组内/项目间三级蒸馏可逐步恢复粗到细的拓扑，在业务中可对商品进行层次聚类，用预训练商品嵌入通过类似目标微调量化器，维持层级相似性，尤其有益于长尾商品和冷启动。

  - TopoTok 作为即插即用的 tokenizer 增强，不需改动现有生成式推荐主干模型，工程改造成本低，可直接串联在 TIGER 等框架中。

  - 实验证实 Recall@5 最高有 9.42% 的绝对提升，说明拓扑保持对推荐精度有直接且显著的价值，可迁移到电商的搜索联想、推荐补全、交叉销售等自回归生成场景。'
score: 10
source: arxiv-cs.IR
depth: abstract
---

**动机**：生成式推荐将序列推荐建模为自回归生成，但项目被量化成离散 token 时，其在预训练语义空间中的邻接关系遭到严重破坏（拓扑失真），导致模型错误感知项目相似度，限制推荐精度。

**方法关键点**：提出拓扑感知词元化框架 TopoTok，通过多级蒸馏在量化层级中保留项目关系结构。具体设计三级蒸馏：
1. 组间蒸馏：在语义簇之间保持全局关系；
2. 组内蒸馏：在簇内恢复局部结构；
3. 项目间蒸馏：对齐细粒度个体项目表征。
三者渐进从粗到细恢复拓扑，指导量化器训练，减少失真。

**结果**：在 Amazon、Yelp 等三个基准数据集上，TopoTok 有效缓解拓扑失真，与其他先进 tokenizer（如 VQ-Rec、RQ-VAE）相比，Recall@5 提升最高 9.42%，且在不同生成模型架构上表现一致鲁棒。
