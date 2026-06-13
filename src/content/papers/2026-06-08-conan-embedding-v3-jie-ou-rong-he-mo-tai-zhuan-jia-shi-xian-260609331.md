---
title: 'Conan-embedding-v3: Fusing Modality-Specific Models for Omni-Modal Embedding'
title_zh: 'Conan-embedding-v3: 解耦融合模态专家实现全模态嵌入'
authors:
- Shiyu Li
- Zhiyuan Hu
- Yifan Wang
- Peiming Li
- Zheng Wei
- Yang Tang
affiliations:
- Tencent
- Tsinghua University
arxiv_id: '2606.09331'
url: https://arxiv.org/abs/2606.09331
pdf_url: https://arxiv.org/pdf/2606.09331
published: '2026-06-08'
collected: '2026-06-13'
category: Multimodal
direction: 全模态嵌入 · 解耦融合训练框架
tags:
- omni-modal retrieval
- embedding model
- model fusion
- projector drift
- multi-modal
one_liner: 提出解耦-融合-恢复框架，解决多模态模型融合中的Projector Drift问题，实现单骨干统一检索
practical_value: '- 若已独立训练好文本、图像、音频等模态专家，可直接用任务向量融合合成统一模型，无需昂贵联合预训练，适合快速落地多模态搜索。

  - 对带有独立编码器和投影器的模态（如音频、视频），融合后必须留意 **Projector Drift**：即使参数不变，骨干偏移也会导致投影器失效；可采用 **冻结骨干、全参数微调投影器**
  的策略低成本恢复性能。

  - **平衡多模态重放** 能有效缓解融合后的灾难性遗忘，实践中可按等比例或等采样策略混入各模态数据做轻量微调。

  - 在电商场景下，商品描述、图片、视频、直播音频等模态差异大，该方法为构建统一检索模型提供了清晰路径，可实现一键搜索所有“货”模态。'
score: 7
source: arxiv-cs.MM
depth: abstract
---

**动机**：全模态检索要求在单一嵌入空间中处理文本、图像、视频、文档、音频等多种模态，但不同模态在数据分布、模型架构和优化动态上差异巨大，直接联合训练困难。

**方法**：提出Conan-embedding-v3，采用“解耦—融合—恢复”三阶段框架。① 解耦：独立训练各模态专家模型。② 融合：将专家的任务向量（task vectors）合并到同一个骨干网络，实现视觉、视频、文档等能力的组合。但融合后发现基于投影器的音频模态出现严重性能退化，即**投影器漂移（Projector Drift）**——骨干参数改变后，原来为音频专家校准的投影器不再适用，导致音频检索准确率骤降。③ 恢复：通过**冻结骨干、全参数微调投影器**（Projector Recovery）修复漂移，再进行平衡多模态重放（balanced multi-modal rehearsal）稳定整体性能。

**结果**：最终模型在单一骨干上同时支持多种检索通路，在MMEB综合基准上达到74.9分，MAEB音频30任务套件得分55.61，有效解决了融合后的音频检索衰退问题。
