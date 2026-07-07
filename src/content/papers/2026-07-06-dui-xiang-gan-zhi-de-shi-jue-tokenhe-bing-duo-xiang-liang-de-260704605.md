---
title: Do All Visual Tokens Matter Equally? Object-Evidence Preserving Token Merging
  for Vision-Language Retrieval
title_zh: 对象感知的视觉token合并：多向量VL检索的高效压缩
authors:
- Suhyeong Park
- Junha Jung
- Jungwoo Park
- Jaewoo Kang
affiliations:
- The Catholic University of Korea
- Korea University
- AIGEN Sciences Inc.
arxiv_id: '2607.04605'
url: https://arxiv.org/abs/2607.04605
pdf_url: https://arxiv.org/pdf/2607.04605
published: '2026-07-06'
collected: '2026-07-07'
category: Multimodal
direction: 多向量视觉-语言检索中的对象感知token压缩
tags:
- token merging
- late interaction
- vision-language retrieval
- ColPali
- object evidence
- storage efficiency
one_liner: 提出对象感知token合并框架SaMer，在MaxSim下将视觉token压缩至K个质心，减少16.09×存储并提升R@1
practical_value: '- **可迁移到电商多模态搜索索引压缩**：商品图片的 ColPali 表示通常 token 量极大，SaMer 的对象感知合并能保留关键物体证据，缩减索引存储
  16 倍, 适合大规模商品库的轻量化多向量检索。

  - **训练时仅需对象标注，推理时零开销**：借鉴其合并先验设计，可在商品多模态模型训练阶段利用目标检测或分割标注指导 token 合并，推理阶段无需检测器，直接端到端压缩，实现低成本部署。

  - **MaxSim 友好压缩策略**：SaMer 通过聚类形成语义质心而非直接丢弃 token，确保每个质心覆盖不同对象区域，使查询仍能匹配到细粒度证据，这比传统剪枝/池化更适合电商搜索中属性或区域敏感的匹配（如
  logo、文本区域）。

  - **可与现有双塔架构兼容**：只需微调共享投影层，冻结视觉与文本主干，改动量极小，适合在已有的 ColPali/ColQwen 商品检索服务中插入，快速获得压缩与精度收益。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：多向量视觉-语言检索（如 ColPali）通过 MaxSim 保留细粒度视觉证据，但密集的图像侧 token 导致存储和评分开销极大。现有 token 压缩方法（剪枝、特征池化）可能删除或坍缩对象/区域级证据，损害未来查询 token 的选择能力。如何在不丢失查询可选对象证据的前提下高效压缩 token 是关键。

**方法**：提出 SaMer，一个对象感知的 token 合并框架。它在训练时利用物体标注作为先验，通过二分图匹配将图像投影后的 token 合并为 K 个质心，同时惩罚跨实例混合，迫使质心保持对象完整性。推理时无需任何检测器或边界框，仅用学习到的合并策略，且只微调共享投影层，视觉与文本骨干完全冻结。最终保留原始 MaxSim 接口，每个质心代表一个区域块，压缩比可达 93% 以上（K=64）。

**结果**：在 K=64 时，SaMer 将 ColPali 存储降低 16.09 倍，并在 Flickr30K 和 MSCOCO 上 R@1 均有提升（优于剪枝、特征池化等基线）。更重要的是，对象感知合并保留了可被查询选中的物体证据，在短语级定位任务上也表现出更强的对齐能力，证明高效多向量检索不仅依赖 token 数量减少，更依赖保留未来查询所需的证据。
