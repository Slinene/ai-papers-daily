---
title: 'Lara Mini Base: Language Diversity as a Resource, Not a Trade-off'
title_zh: Lara Mini Base：语言多样性是资源，而非权衡
authors:
- Translated
- Maria Pia Adinolfi
- Isabelle Andrieu
- Grazia Fiorella Anfuso
- Melania Annunziata
- Daniele Antonini
- Marta Arena
- Luca Barone
- Dana Barras Franco
- Francesca Basiricò
affiliations:
- Translated
arxiv_id: '2611.16956'
url: https://arxiv.org/abs/2611.16956
pdf_url: https://arxiv.org/pdf/2611.16956
published: '2026-11-12'
collected: '2026-11-13'
category: Training
direction: 多语言MoE预训练 · 容量竞争缓解
tags:
- MoE
- multilingual
- pretraining
- language diversity
- efficiency
- LLM
one_liner: 用0.6B激活参数的MoE在多语言训练中实现多语言能力领先，推理速度显著更快
practical_value: '- **多语言业务扩展可借鉴 MoE 架构**：跨境电商、多语言广告文案、多语言搜索 Query 理解等场景，用总参数大、激活参数小的
  MoE 模型，可在控制推理成本的同时获得多语言能力，避免为每种语言单独部署小模型。

  - **训练数据配比策略**：非英语数据在训练后期占比超过英语，说明小模型多语言训练可以逐步提高非主语言比例，不必一开始就平衡，这样能缓解语言间容量竞争。

  - **单卡推理效率优势明显**：0.6B 激活参数模型在单 GPU 无量化下比同分模型快至少 1.8 倍，适合对延迟敏感的推荐/Agent 系统，尤其需要多语言生成时，可用
  MoE 小激活模型替代稠密模型。

  - **T-HellaSwag 基准可直接用于评估**：发布的多语言常识推理基准覆盖 110 种语言变体，可用于评估电商场景下多语言商品描述、用户评论理解等任务的常识推理质量。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有通用 LLM 训练数据以英语为主（非英语占比≤12%），专门欧洲语言模型虽然语言覆盖多但同规模下表现显著落后；小模型中多语言常常相互竞争模型容量。

**方法关键点**：
- 从零训练 Lara Mini base，采用 MoE 架构（总参数 7.2B，激活 0.6B），训练语料 6T token，覆盖英语及 44 种语言（含欧盟 24 种官方语言）。
- 训练后期非英语语料占比超过英语，通过数据配比逐步提升多语言能力。
- MoE 专家分工降低语言间容量竞争，支持 128k 上下文。

**关键结果**：
- 在活跃参数≤2B 的开放基础模型中，英语、多语言、数学、代码四个领域平均分最高，超过训练 token 多 4-6 倍的模型。
- 多语言和数学基准优势最大。
- 无量化单 GPU 推理速度比平均分更高的模型至少快 1.8 倍。
- 发布权重（CC BY-NC-SA 4.0）及 T-HellaSwag 多语言常识推理基准。
