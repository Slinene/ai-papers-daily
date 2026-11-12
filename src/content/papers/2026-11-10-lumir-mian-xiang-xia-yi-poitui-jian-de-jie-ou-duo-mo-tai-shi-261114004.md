---
title: 'LUMIR: Decoupled Multimodal Representation Learning from Heterogeneous Data
  for Next-POI Recommendation'
title_zh: LUMIR：面向下一POI推荐的解耦多模态表示学习
authors:
- Zehui Wang
- Wolfram Höpken
- Dietmar Jannach
affiliations:
- University of Applied Sciences Ravensburg-Weingarten
- University of Klagenfurt
arxiv_id: '2611.14004'
url: https://arxiv.org/abs/2611.14004
pdf_url: https://arxiv.org/pdf/2611.14004
published: '2026-11-10'
collected: '2026-11-12'
category: RecSys
direction: 多模态表示学习 · 下一POI推荐
tags:
- Multimodal
- Representation Learning
- POI Recommendation
- Contrastive Learning
- LLM
- Decoupled
one_liner: 用LLM统一多模态语义，通过对比学习与交互感知融合学习可复用表示，在下一POI推荐中超越现有融合基线
practical_value: '- 借鉴「表示学习与下游任务解耦」的思路：在电商商品多模态（图、文、属性）场景，用 LLM 先统一语义到文本空间，构建通用的 item
  表示，可同时服务召回、排序、语义 ID 生成等多种下游任务，避免每个模型重复做融合。

  - 交互感知融合 + 序列结构约束的对比学习范式，可迁移到用户行为序列建模：将曝光序列作为 structural constraint 注入 item 表示预训练，提升表示对时序上下文的敏感度。

  - 工程实现上，多模态表示预训练可作为离线批处理任务，线上直接查表或轻量编码，降低实时推理复杂度和异构数据对齐成本。

  - 若业务中已有 LLM 服务，可借鉴其「任意模态转文本」的统一入口，快速接入商品图、描述、属性等多源信息，无需为每种模态单独设计特征工程。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：POI 推荐中的多模态信息来自异构数据源，现有方法将多模态融合与下游模型架构和优化目标紧耦合，导致所学表示通用性和复用性受限。

**方法关键点**：LUMIR 采用解耦式多模态表示学习框架。首先用 LLM 将来自不同数据源的多模态信息统一到共享文本表示空间；然后设计 interaction-aware fusion 机制建模跨模态交互；同时将序列信号作为结构约束，通过对比学习训练表示，使 item 表示尽可能与下游任务无关。

**关键结果**：在多模态 POI 数据集上，以 next-POI recommendation 为下游任务，将所学表示接入多个序列推荐 backbone，LUMIR 在准确率导向（如 Recall@k、NDCG@k）和超越准确率指标（如多样性、覆盖率等）上均一致优于现有多模态融合基线，验证了解耦式表示学习对可复用性的提升。
