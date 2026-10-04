---
title: 'Multimodal Flow: Unified Flow Modeling of Language and Vision in Embedding
  Spaces'
title_zh: 多模态流：嵌入空间中语言与视觉的统一流建模
authors:
- Hongyuan Tao
- Xinggang Wang
- Lianghui Zhu
- Yongkang Li
- Yunchao Wei
- Bin Feng
- Shaoyu Chen
- Qian Zhang
- Chang Huang
- Kai Yu
affiliations:
- Huazhong University of Science and Technology
- Beijing Jiaotong University
- Horizon Robotics
arxiv_id: '2609.40362'
url: https://arxiv.org/abs/2609.40362
pdf_url: https://arxiv.org/pdf/2609.40362
published: '2026-09-29'
collected: '2026-10-04'
category: Multimodal
direction: 多模态统一连续生成 · Flow Matching
tags:
- Multimodal
- Flow Matching
- Unified Model
- Continuous Embedding
- Vision-Language
- Generative Model
one_liner: 提出全连续多模态生成模型，用流匹配在连续嵌入空间统一语言和视觉，避免离散量化瓶颈
practical_value: '- 连续 embedding 流建模可以替代离散 token，用于商品多模态统一表征，减少视觉量化损失；在生成式推荐中可尝试用连续流匹配生成
  item embedding 或 Semantic ID 的替代表示。

  - chunk-causal 骨干同时保留文本顺序和图像空间结构，适合电商商品标题、详情图等混合模态的联合建模；训练时并行预测多 target chunks，推理顺序生成
  hyperchunks，可加速序列化商品描述生成。

  - 共享联合注意力 + 模态特定 FFN 的架构，可作为商品图文融合模块：不同模态保持专门前馈处理，同时通过注意力做跨模态交互，比简单拼接更灵活。

  - 在小数据预算下持续预训练仍能提升多模态能力，说明该连续建模范式的数据效率较高，对业务中数据量有限的场景有参考价值。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：统一多模态模型通常要么把语言和量化图像都当离散 token，要么混合离散语言预测与连续图像生成；前者受视觉量化瓶颈制约，后者需模态依赖的目标和采样过程。全连续建模可避免这些折衷，但在多模态预训练中尚未被充分探索。

**方法关键点**：Multimodal Flow 采用统一连续架构，将文本块和图像组织为有序的连续 hyperchunks，保留文本 token 顺序和视觉空间结构。共享 chunk-causal flow backbone 通过 Flow Matching 学习单一向量场，联合注意力实现跨模态交互，模态特定前馈网络分别处理各模态。训练时并行预测多个 target chunks，推理时顺序生成 hyperchunks。实例 MF-1 进行多模态预训练。

**关键结果**：在 0.6B、1.2B、1.6B 参数规模下，持续预训练一致改善多模态建模。仅用 150B 预训练 tokens，MF-1 在 GenEval 和 DPG-Bench 上平均 82.8，在 VQAv2、MMBench、POPE 上平均 75.3，与使用更多数据训练的统一模型持平。在匹配数据、优化和参数预算下，Multimodal Flow 超过代表性混合与离散模型。
