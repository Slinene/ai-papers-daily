---
title: 'IDs That Mean Something: A Hands-On Tutorial on Semantic IDs for Recommender
  Systems'
title_zh: 有意义的ID：推荐系统语义ID实操教程
authors:
- Roger Zhe Li
- Aghiles Salah
- Mete Sertkan
- Changhong Jin
- Yingjie Niu
- Ruihai Dong
- Barry Smyth
affiliations:
- Huawei Ireland Research Center
- University College Dublin
arxiv_id: '2611.04140'
url: https://arxiv.org/abs/2611.04140
pdf_url: https://arxiv.org/pdf/2611.04140
published: '2026-11-03'
collected: '2026-11-04'
category: GenRec
direction: 语义ID与生成式推荐
tags:
- Semantic ID
- Generative Recommendation
- RQ-VAE
- Cross-Domain
- Tutorial
- Multimodal
one_liner: 系统梳理从原始ID到语义ID的演进，覆盖生成式与判别式应用并提供可动手的实践教程
practical_value: '- 用语义 ID 替代原始整数 ID，通过 RQ-KMeans/RQ-VAE 把商品内容量化成离散 token 序列，可直接作为生成式推荐的解码目标，大幅压缩
  item embedding 表，缓解 embedding 爆炸和冷启动。

  - 在判别式排序模型中加入语义 ID 作为结构化输入特征，可提升冷启动泛化和 embedding 稳定性；Google YouTube ranking、Kuaishou、Meta
  已有工业部署验证。

  - 多模态商品内容融合采用 early fusion 或 late fusion，需注意模态冗余；同时把协同信号通过量化、微调或对比学习注入语义 ID，平衡“语义有意义”和“推荐可感知”。

  - 跨域推荐无需显式源-目标对齐，共享语义结构从量化过程自然涌现，电商多国家/多站点场景下可直接复用语义 ID 做迁移。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

动机：推荐系统长期用任意整数 ID 标识物品，ID 本身无语义，模型只能从交互数据中学习表示；引入文本、图像等内容信息虽能缓解冷启动，但 embedding 表随 catalog 规模无限增长，且多模态架构复杂、跨域需显式对齐。语义 ID 将语义信息直接编码进物品身份，形成离散 token 序列，在保留原始 ID 查找与记忆能力的同时支持跨 item 泛化。

方法关键点：
- 语义 ID 构造：常用 RQ-VAE 或 RQ-KMeans 对物品内容 embedding 做残差量化，生成多层离散 token 序列；设计需权衡紧凑性、稳定性、语义一致性和下游可用性。
- 应用范式：生成式推荐中以语义 ID 为解码目标（如 TIGER）；判别式排序中作为结构化输入特征（如 YouTube ranking 模型、Kuaishou DAS、Meta semantic ID），提升冷启动和 embedding 稳定性。
- 多模态与协同信号：多模态内容融合分 early fusion 和 late fusion 两条路线，需处理模态冗余；协同信号可通过 collaborative embedding quantization、内容模型微调或对比训练注入语义 ID，实现“内容有意义 + 行为可感知”。
- 跨域迁移：语义共享结构从量化过程自然涌现，无需显式源-目标对齐，多域/多站点电商场景下可直接迁移。

关键实验/结果：作为教程提案，未报告具体实验数字；配套 hands-on 使用 Amazon Reviews 数据集，训练 RQ-KMeans 并对比原始 ID 基线，同时用 Cornac 框架做生成式推荐。工业部署案例包括 Google YouTube ranking、Kuaishou、Meta 等，验证了语义 ID 在生成式和判别式推荐中的可行性与规模化价值。

最值得记住的一句话：把物品身份从“无语义整数”换成“含内容与行为的离散语义 token 序列”，是推荐系统从检索走向生成、从单域走向跨域的关键抽象。
