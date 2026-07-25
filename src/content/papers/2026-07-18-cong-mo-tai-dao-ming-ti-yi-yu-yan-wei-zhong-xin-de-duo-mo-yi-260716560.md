---
title: 'From Modalities to Propositions: A Language-Centric Framework for Multimodal
  Intelligence'
title_zh: 从模态到命题：以语言为中心的多模态统一框架
authors:
- Nadine Chang
- Maying Shen
- Shizhe Diao
- Jialiang Wang
- Jingde Chen
- Thomas Breuel
- Pavlo Molchanov
- Rafid Mahmood
- Jose M. Alvarez
affiliations:
- NVIDIA
- University of Ottawa
arxiv_id: '2607.16560'
url: https://arxiv.org/abs/2607.16560
pdf_url: https://arxiv.org/pdf/2607.16560
published: '2026-07-18'
collected: '2026-07-25'
category: Multimodal
direction: 语言中心的多模态语义表示框架
tags:
- multimodal
- semantic representation
- propositional reasoning
- interpretability
- cross-modal retrieval
one_liner: 提出将任意模态数据表示为原子命题集合，通过全局语义码本实现可解释、可组合的跨模态理解与检索
practical_value: '- **商品语义原子化**：将商品的多模态信息（图文、视频）拆解为“材质:纯棉”“风格:通勤”“场景:办公室”等原子命题，构建可解释的商品语义空间，替代纯Embedding匹配，提升冷启动和可解释推荐。

  - **结构化跨模态检索**：在电商搜索中，用户自然语言查询可映射为原子命题集合，与商品的多模态命题袋进行精确匹配，支持“带兜风帽的羽绒服”类组合条件检索，解决传统向量检索难以处理的组合属性问题。

  - **组合式推荐与解释**：利用命题的布尔组合特性，进行复杂推荐逻辑（如“买过A+B的人还需要C”），并直接生成自然语言解释，适合作为推荐Agent的推理底座。

  - **数据增强与冷启动**：通过语义码本自动生成大量虚拟样本的命题表示，可用于新品类/缺样本场景的召回，避免对交互数据的强依赖。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

**动机**：当前多模态模型（如CLIP、MLLM）将语义信息分散在高维隐空间中，缺乏可解释性和组合推理能力。现实场景理解需要实体、属性、动作、关系等原子语义的组合，单一向量表示难以支撑结构化检索与推理。

**方法**：提出**原子命题袋（Bag of Atomic Propositions, BoAP）** 表示法。构建一个全局语义码本（codebook），包含标准化的原子命题（如“human holding cup”）。对于任意模态的观测（图像、视频、文本），通过模态特定的编码器将其映射为该码本上的稀疏或多热向量，即一个命题集合。所有模态的表示被统一到同一可解释的命题空间，天然支持组合、比较与推理，无需额外对齐。

**结果**：在自动驾驶和开放世界数据上验证了跨模态理解、可解释推理和结构化检索。命题表示能清晰揭示场景中的细粒度语义，支持组合查询与概念组合，例如从“parked car”和“beside building”组合出复杂场景描述，提升检索精度和推理透明度。
