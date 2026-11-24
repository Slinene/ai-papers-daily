---
title: 'DiLE: Discrimination-Aware Latent-Space Learning for Universal Multimodal
  Embeddings'
title_zh: 用于通用多模态嵌入的判别感知潜空间学习
authors:
- Ben Kang
- Junda Wang
- Yuxuan Yuan
- Hang Li
- Yuhan Liu
- Xin Chen
- Wanting Geng
- Tong Lin
- Pei Fu
- Dong Wang
affiliations:
- Dalian University of Technology
- Peking University
- Xiaomi Inc
- City University of Hong Kong
arxiv_id: '2611.25419'
url: https://arxiv.org/abs/2611.25419
pdf_url: https://arxiv.org/pdf/2611.25419
published: '2026-11-18'
collected: '2026-11-24'
category: Multimodal
direction: 多模态嵌入 · 对比学习 + 蒸馏
tags:
- multimodal embeddings
- retrieval
- hard-negative mining
- knowledge distillation
- latent space
- MLLM
one_liner: DiLE 结合任务引导与在线策略检索反馈，用 learnable queries、shared-private experts 和 on-policy
  难负样本蒸馏提升多模态检索判别力
practical_value: '- **更省参数的多任务统一嵌入**：用少量可学习 queries 代替全量微调，把任务信息压进紧凑潜空间，适合电商多模态商品库中多任务共用同一编码器，降低每任务额外显存和训练成本。

  - **shared-private expert 适配多任务共性与个性**：跨任务共享专家 + 任务私有专家的结构可直接套用到电商推荐中的多目标/多场景建模，比简单
  shared-bottom 更能保留场景特有特征，比每个任务独立模型更省资源。

  - **on-policy hard-negative distillation 值得迁移到召回/ANN 检索**：让学生模型自己检索出当前容易混淆的候选，再用教师模型对这些候选的细粒度相关性分布做
  reverse KL 蒸馏，并周期性刷新候选；能缓解静态负样本过时问题，特别适合商品召回、图文检索中难负样本挖掘。

  - **推理指令 + 辅助生成监督可提升 embedding 判别性**：在 LLM 做编码器的场景下，显式加入推理指令和答案生成任务，有助于让 embedding
  保留检索所需的空间/关系等证据，可尝试用于多模态商品搜索的 query 理解与向量召回。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：MLLM 虽提升了通用多模态嵌入输入理解能力，但嵌入可能丢失区分相关项与混淆替代项所需的证据，导致检索时空间/关系等关键信息被忽略。

**方法关键点**：DiLE 框架通过判别感知的潜空间学习解决该问题。
- 使用少量可学习 queries 把任务相关信息编码到紧凑潜空间；
- 引入推理指令和辅助答案生成监督，让表示同时支持任务理解与检索判别；
- 设计 shared-private expert adaptation，融合跨任务共享知识与任务特定表示学习；
- 提出 on-policy hard-negative distillation：学生模型自行检索容易混淆的候选，用 reverse KL 将学生基于嵌入的相似度分布对齐到教师在这些候选上的细粒度相关性分布；候选集周期性用更新后的学生快照刷新，使教师监督紧跟学生当前的检索行为与混淆模式。

**关键结果**：在 MMEB-v2、UVRB、MRMR 三个基准上，覆盖两种骨干代际的四类模型配置均达到 SOTA，验证了方法跨模态和跨任务的有效性。
