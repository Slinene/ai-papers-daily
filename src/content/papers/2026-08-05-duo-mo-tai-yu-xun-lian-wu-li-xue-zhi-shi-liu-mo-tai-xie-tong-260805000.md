---
title: 'Towards Physics of Multimodal Pretraining: Knowledge Flow, Modality Synergy,
  Early Unification, and Recipes'
title_zh: 多模态预训练物理学：知识流、模态协同、早期统一与配方
authors:
- Junlin Han
- Shengbang Tong
- David Fan
- Minghao Chen
- Philip Torr
- Filippos Kokkinos
- Mike Lewis
affiliations:
- FAIR, Meta
- Reality Labs, Meta
- University of Oxford
arxiv_id: '2608.05000'
url: https://arxiv.org/abs/2608.05000
pdf_url: https://arxiv.org/pdf/2608.05000
published: '2026-08-05'
collected: '2026-08-09'
category: Multimodal
direction: 多模态预训练机制与训练效率优化
tags:
- Multimodal Pretraining
- Knowledge Flow
- Modality Synergy
- Early Unification
- MoE
- Training Efficiency
one_liner: 系统揭示多模态预训练中知识非对称流动、模态协同依赖任务复杂度、早期统一优于晚对齐，并给出高效配方
practical_value: '- **模态协同架构设计**：在多模态推荐模型（如结合商品图文）中，采用共享注意力与层归一化，但解耦模态特定的 FFN，可促进协同并缓解竞争。

  - **早期联合训练**：从训练之初就统一多模态特征，而非分阶段预训练后对齐，能避免视觉惰性，使模型同时学习跨模态理解，对需要同时理解文本查询和商品图像的场景有益。

  - **知识流动不对称性**：语言先验可强驱动视觉生成，可利用文本生成增强商品图像描述或虚拟试穿模型的训练策略。

  - **高效训练配方**：通过 MoE 架构与训练策略压缩计算至原 5% 仍能保持强生成能力，直接适用于资源受限的电商多模态模型预训练。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

**动机**：多模态预训练成为基础模型的关键方向，但模态间交互机制和设计空间缺乏系统理解。  
**方法**：在合成和真实大规模数据集上进行受控实验，解耦模态知识迁移、模态协同条件、统一时机和训练效率。  
**关键结果**：  
- **知识流**：语言和视觉理解向视觉生成的知识迁移呈非对称，前两者是强先验驱动生成。  
- **模态协同**：任务复杂度决定模态是否协同；架构上共享注意力和归一化，但使用模态特定 FFN 可提升协同、减弱竞争，且这一发现对不同视觉 tokenizer 通用。  
- **早期统一**：从最早期联合训练模态比晚期对齐或顺序训练更有效，延迟集成会导致模型依赖语言先验，出现“视觉惰性”。  
- **高效配方**：仅用 5% 计算预算即可达到强生成性能，通过训练多个 13.5B MoE（在 2T tokens 上）验证了这些发现。
