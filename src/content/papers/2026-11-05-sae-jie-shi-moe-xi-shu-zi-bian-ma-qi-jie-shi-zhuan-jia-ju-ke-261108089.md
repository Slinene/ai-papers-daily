---
title: 'SAE Interprets MoE: Sparse AutoEncoders Reveal That MoE Experts Exhibit Human-Interpretable
  Fine-Grained Specialization'
title_zh: SAE 解释 MoE：稀疏自编码器揭示专家具有人类可解释的细粒度专业化
authors:
- Anyuan Zhuo
- Shaohua Zhang
- Yuan Lin
- Pinyan Lu
affiliations:
- ByteDance Seed
- Shanghai University of Finance and Economics
arxiv_id: '2611.08089'
url: https://arxiv.org/abs/2611.08089
pdf_url: https://arxiv.org/pdf/2611.08089
published: '2026-11-05'
collected: '2026-11-08'
category: LLM
direction: MoE 专家可解释性与行为分析
tags:
- MoE
- Sparse Autoencoder
- Interpretability
- Expert Specialization
- Mechanistic Interpretability
one_liner: 用 SAE 对 MoE 层输出做线性分解，发现专家贡献远比分路由更集中，且呈现细粒度可解释分工
practical_value: '- 对于采用 MoE 架构的推荐/搜索模型，可将 SAE 训练在 MoE 层输出上，通过分解每个 latent 的 pre-activation
  到各专家，定位哪些专家真正驱动哪些特征/行为，避免仅看 gating 频率的误导。

  - 该方法不依赖预定义领域标签，能在未标注的行为数据上自动发现细粒度分工，适合电商场景中复杂、跨域的用户行为（如同时包含多种商品类目、搜索意图）来诊断专家是否按更细的语义/行为维度分化。

  - 分析结果显示不同领域所需专家数量不均，可为 MoE 推荐模型的路由结构设计提供依据：对高频、细分的任务分配更多专家，而非均匀设置，从而提升参数效率。

  - 可借鉴其“主导 latent 集合”的度量方式，监控 MoE 推荐模型上线后的专家漂移或退化，辅助裁剪冗余专家或发现新增行为模式。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：MoE 模型通过路由将 token 分配给少量专家，但单个专家到底负责什么一直不清楚。以往方法基于领域标签统计专家选择频率，存在分类体系固定、粒度粗、只记录选择不记录贡献等不足。

方法：直接在 MoE 层输出上训练稀疏自编码器（SAE）。由于 MoE 输出是专家输出的路由加权和，且 SAE 编码器是仿射变换，每个 latent 的 pre-activation 可以精确分解到各专家的贡献。在语料库上聚合后，为每个专家得到一个它主要驱动的 latent 集合（主导集），从而分析分工。

关键结果：在 Qwen3-30B-A3B 的第 4、30、46 层上，专家基于贡献的特化程度远高于基于 gating 的选择频率；大多数 latent 只有 1-2 个主导专家；主导集之间的重叠集中在少数专家对上。自动解释这些主导集发现，分工比粗粒度领域更细：例如不同专家分别负责 Java 和前端 Web 代码，或分别负责几何与算术/多项式，且不同粗粒度领域占用的专家数量非常不均衡。代码和 SAE 已开源。
