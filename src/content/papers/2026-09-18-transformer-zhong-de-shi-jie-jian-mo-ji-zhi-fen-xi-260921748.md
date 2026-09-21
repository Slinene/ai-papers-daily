---
title: World Modeling in Transformers
title_zh: Transformer 中的世界建模：机制分析
authors:
- Pierre Beckmann
- Matthieu Queloz
- Andre Freitas
affiliations:
- EPFL
- IDIAP Research Institute
- MATS
- University of Bern
- University of Manchester
arxiv_id: '2609.21748'
url: https://arxiv.org/abs/2609.21748
pdf_url: https://arxiv.org/pdf/2609.21748
published: '2026-09-18'
collected: '2026-09-21'
category: LLM
direction: 机制可解释性 · 世界模型
tags:
- mechanistic interpretability
- world model
- transformers
- feature superposition
- navigation
- causal intervention
one_liner: 通过机制分析与因果干预揭示 TaxiGPT 内部存在一致地图与导航能力，行为失败源于叠加特征干扰
practical_value: '- 评估 LLM/Agent 能力时，不应只看行为指标（如推荐 CTR、合法动作率），可结合探针或因果干预检查中间表示是否编码关键实体与关系；行为失败可能是特征干扰而非能力缺失。

  - 对 embedding 或序列模型，可按相同动作/属性的实体做分组表示（类似 affordance packing），降低叠加特征干扰，提升导航/决策鲁棒性；可迁移到商品/query
  表示中按可替代行为聚类。

  - 用机制指标追踪模型训练过程中能力的涌现阶段，指导训练轮数、模型规模选择或继续训练，避免依赖单一评估集。

  - 当线上模型出现异常行为时，可先定位是感知/表示层错乱还是策略层决策错误，再针对性修复，减少无效重训。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：行为失败可能让 Transformer 看似缺乏世界模型，即使它已学到环境的忠实表示。TaxiGPT 在曼哈顿随机游走上训练，虽 99% 输出合法转弯，但重建地图呈“意大利面状”，被解读为内部地图不连贯。

**方法**：通过机制分析与因果干预，分解模型对交叉口、街道的表示，定位位置跟踪和目标罗盘的使用；隔离叠加交叉口特征引起的干扰；引入 affordance packing，将合法动作相同的交叉口表示分组；提出机制指标比较不同模型。

**关键结果**：模型确实表示交叉口和街道，追踪自身位置，并使用目标罗盘导航；失败主要源于叠加交叉口特征干扰定位，而非缺失世界模型；affordance packing 能限制错误后果；不同训练阶段的世界建模能力具有不同涌现顺序。
