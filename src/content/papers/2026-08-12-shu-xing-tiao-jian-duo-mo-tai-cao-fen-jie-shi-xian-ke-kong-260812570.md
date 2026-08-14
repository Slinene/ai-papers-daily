---
title: Attribute-Conditioned Multimodal Slot Factorization for Controllable Fashion
  Retrieval
title_zh: 属性条件多模态槽分解实现可控时尚检索
authors:
- Najmeh Forouzandehmehr
- Topojoy Biswas
- Evren Korpeoglu
- Kannan Achan
affiliations:
- Walmart Global Tech
arxiv_id: '2608.12570'
url: https://arxiv.org/abs/2608.12570
pdf_url: https://arxiv.org/pdf/2608.12570
published: '2026-08-12'
collected: '2026-08-14'
category: RecSys
direction: 多模态可控检索 · 属性槽分解
tags:
- Multimodal Retrieval
- Attribute Factorization
- Fashion-CLIP
- Controllable Retrieval
- Text-Image Gating
- Slot Attention
one_liner: 将 Fashion-CLIP 多模态嵌入分解为四个命名属性槽并学习各自的 text-image gate，显著提升约束满足率
practical_value: '- 商品检索/推荐中，可把单一商品 embedding 拆成多个命名属性槽（类目、颜色、图案、人群等），每个槽独立表示，避免不同属性信号相互干扰，实现更细粒度的可控召回。

  - 借鉴 text-image gate 机制：视觉属性（颜色、图案）自动偏向图像证据，类目等结构化属性偏向文本证据。电商多模态商品表示可以根据属性类型分配模态权重，无需人工指定。

  - 属性槽量化后的 slot code 支持定向干预（如颜色提升 15.3x），可用于线上检索诊断、属性级重排或人工干预策略，比全局 embedding 或 item-level
  semantic ID 更可解释、可操作。

  - 使用「槽相似度 + 槽 logit 得分」组合评分，相比简单等权多模态融合提升约束满足率，该 scoring trick 可直接迁移到多属性约束的商品检索场景。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**
时尚检索常需同时满足多个属性（类目、颜色、图案、人群），单一 embedding 把所有信号混在一起，难以在检索时做属性级控制；现有 semantic ID 方法提供离散 item code，但未暴露可独立控制的命名属性槽。

**方法关键点**
提出 MM-slotgate：把 Fashion-CLIP 的文本和图像嵌入分解为四个命名属性槽（category、color、pattern、demographic）。每个槽学习独立的 text-image gate，使视觉强属性（颜色、图案）更多依赖图像证据，分类强属性（类目、人群）更偏文本驱动。训练不使用模态监督，但 gate 可解释：颜色 57.4% 权重给图像，类目偏文本；线性 probe 显示没有超出标签相关性的额外泄漏。槽码量化后支持定向干预。

**关键结果数字**
在 H&M 数据集上，采用槽相似度 + 槽 logit 的检索得分，MM-slotgate 达到 0.7566 macro ConstraintSatisfied@10，优于等权多模态融合的 0.7142 和 fCLIP 纯文本检索的 0.4755。颜色属性提升最显著，从 0.321 升至 0.889（+0.568 绝对提升）；颜色 gate 给图像 57.4% 权重。量化槽码支持定向干预，颜色提升 15.3x。
