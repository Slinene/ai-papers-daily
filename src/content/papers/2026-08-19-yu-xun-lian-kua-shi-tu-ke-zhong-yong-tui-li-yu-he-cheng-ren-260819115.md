---
title: Pretraining Reusable Inference Across Views with Synthetic Task Priors
title_zh: 预训练跨视图可重用推理与合成任务先验
authors:
- Jielong Lu
- Zhihao Wu
- Jiajun Yu
- Zhaoliang Chen
- Haishuai Wang
affiliations:
- Zhejiang University
- Hong Kong Baptist University
arxiv_id: '2608.19115'
url: https://arxiv.org/abs/2608.19115
pdf_url: https://arxiv.org/pdf/2608.19115
published: '2026-08-19'
collected: '2026-08-23'
category: Reasoning
direction: 多视图推理预训练 · 合成任务先验
tags:
- Multi-view Learning
- In-context Learning
- Synthetic Task Prior
- Transfer Learning
- Pretraining
one_liner: 用合成任务先验预训练多视图推理过程，冻结或轻量 adapter 即可跨任务复用
practical_value: '- 多视图/多模态推荐中，不同视图（用户行为、物品文本、图片、知识图谱）的融合策略通常每个任务重训；可借鉴把“视图融合推理”本身做成可迁移过程，在新任务上仅用少量
  support 样本（few-shot）条件化预测，大幅减少训练成本。

  - 合成任务先验的构建方式可迁移：在 embedding 空间生成多样化的 support-query episodes，模拟视图缺失、噪声、跨视图依赖、分布偏移等，用于预训练鲁棒的多视图融合
  backbone；电商场景中特征缺失、新场景冷启动频繁，可通过此类可控生成器增强模型泛化。

  - In-context learning 思路适合线上快速适配新活动或新类目：无需梯度更新，仅通过 few-shot labeled support 即可进行推理；结合轻量
  adapter 做任务特定校准，兼顾通用性与专用性，可参考共享 backbone + 轻量 adapter 的多任务架构。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

**动机**：现代预训练编码器让异构视图表示可复用，但“决定视图有用性并组合证据”的推理过程仍为每个下游任务重新学习，导致视图相关性、互补性、可靠性、缺失模式等知识被反复丢弃。论文将多视图学习重定义为学习可复用的、任务条件化的推理过程，而非固定融合函数。

**方法关键点**：提出 SIMPLE，一个 prior-fitted 多视图 in-context learner，通过少量 labeled support set 条件化预测 query 标签。由于真实数据集覆盖视图配置和任务结构有限，作者在 embedding 空间构建可控的合成任务先验，生成多样化的 support-query episodes，涵盖不同类别结构、共享与视图特有因子、表示几何、跨视图依赖、可靠性水平、缺失模式和分布偏移。层次化推理架构依次在视图内部、跨视图、以及 support-query 样本间进行推理。

**关键结果**：在 multi-view 和 multi-omics 基准上，冻结版 SIMPLE 在不更新推理 backbone 的情况下达到有竞争力的性能；轻量 adapter 校准则在多数数据集上取得领先性能。frozen、one-shot、missing-view 设置下的结果共同支持核心假设：多视图推理本身可以被预训练并跨任务复用，adapter 校准则在需要时提供任务特定对齐。
