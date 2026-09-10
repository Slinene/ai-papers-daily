---
title: 'Building Multilingual Bridges: Data Mixing as the Pillar of Generalization
  for In-Language Reasoning'
title_zh: 构建多语言桥梁：数据混合作为语言内推理泛化的支柱
authors:
- Mehrnaz Mofakhami
- Ananya Sahu
- Alejandro R. Salamanca
- Daniel D'souza
- Alexandre Berard
- Thomas Euyang
- Marzieh Fadaee
- Julia Kreutzer
affiliations:
- Cohere Labs
- Cohere
arxiv_id: '2609.10445'
url: https://arxiv.org/abs/2609.10445
pdf_url: https://arxiv.org/pdf/2609.10445
published: '2026-09-09'
collected: '2026-09-10'
category: Reasoning
direction: 多语种语言内推理 · 数据混合训练
tags:
- Multilingual
- Reasoning
- Data Mixing
- SFT
- Language Consistency
- LLM
one_liner: 通过数据混合与调度优化，3.35B模型在60种语言上实现93%以上语言内推理率，证明推理行为可跨语言迁移。
practical_value: '- **数据混合降本**：跨境业务的多语言场景下，只需英文推理标注数据 + 目标语言的通用语料，即可让小模型获得目标语言上的推理能力，避免为每种语言单独标注推理数据。可用于多语言商品推荐解释、售后问答等。

  - **推理语言一致性**：将“语言内推理率”作为核心评估指标，监控模型在用户使用语言上的推理占比，避免模型在非英语语言下切换回英文，提升本地化体验和用户信任。

  - **小模型可行性**：3.35B参数即可达到高语言内推理率，说明中小规模模型结合高质量数据混合策略可以在有限算力下覆盖多语言推理场景，适合需要低延迟、低成本的多语言搜索/推荐助手。

  - **调度策略借鉴**：SFT中数据调度对推理泛化有重要影响，可尝试“先英文推理数据建立骨干，再混合多语言非推理数据”的课程式训练，在训练过程中动态调整语言配比以稳定能力迁移。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有推理模型以英语为中心，即使用户用非英语提问，模型也主要用英语推理，导致非英语用户可及性差、丢失原问题意图、错失目标语言知识。论文提出 L2 reasoning——让模型在用户提示语言上持续推理，搭建提示与答案之间的语言内桥梁。

**方法关键点**：从数据为中心角度，系统探索 SFT 中数据组成与调度对推理泛化的影响。构建 3.35B 的 Tiny Aya L2-Thinker，研究如何通过数据混合将推理能力迁移到多种语言。关键发现：向未见过语言泛化 L2 推理需要三条路径：更广的语言覆盖、现成的多语言非推理数据、以及足够的英语推理骨干。推理被视为语言无关行为，可通过精心设计的数据混合跨类型多样的语言迁移，无需为每个目标语言提供推理监督。

**关键结果**：在 60 种语言、6 个基准（数学、常识推理、指令跟随、开放生成、文化推理）上，L2 推理率超过 93%，同时保持性能强劲。模型权重与多语言推理数据已发布。
