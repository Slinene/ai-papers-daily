---
title: 'PDMR: Passage-Driven Multi-ID Document Retrieval'
title_zh: 段落驱动的多标识符文档检索
authors:
- Smail Oussaidene
- Mohand Boughanem
affiliations:
- Institut de Recherche en Informatique de Toulouse (IRIT)
arxiv_id: '2609.08762'
url: https://arxiv.org/abs/2609.08762
pdf_url: https://arxiv.org/pdf/2609.08762
published: '2026-09-08'
collected: '2026-09-09'
category: Other
direction: 生成式文档检索 · 多 passage ID
tags:
- Generative Retrieval
- Multi-ID
- Passage-Level
- DocID Design
- Multi-Target Learning
one_liner: 用多个 passage 级标识符替代单一文档 ID，结合多目标训练与 query-段落对齐，提升生成式文档检索的 R@1 与 MRR
practical_value: '- 在电商/内容生成式检索或推荐中，不要为长详情页/多卖点商品只建一个 Semantic ID；可先做段落/卖点切分，为每个语义单元建“文档/商品标题+段落标题”式层级
  ID，提供多个生成入口，用 max 概率聚合回父级 item。

  - 多目标加权损失可落地：当 query 命中商品多个属性/卖点时，给最相关属性（如 BM25 最高分卖点）更高权重（如 0.6），其余均分，避免单一监督信号过强。若类目内容同质，可尝试
  all-passages 标签；内容异构大时用 best-passage。

  - 原始训练 query 增强很关键：仅用合成 query 会弱化真实 query 分布；可将真实 query 通过 BM25 对齐到最佳段落，或根据数据均匀度选择
  all passages，能带来显著 R@1 提升。

  - 标识符顺序有讲究：Doc→Pass 前缀结构更适合 autoregressive 解码，能先缩小到正确文档再选段，可复用到层级式 ID 设计中。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：生成式检索将 query 直接映射到文档标识符，但大多数方法假设每个文档只有一个 ID，压缩多面文档为单一序列会导致表示损失，查询变化时鲁棒性差。尤其长文档/网页包含多个语义块，单一访问路径难以对齐不同意图。

**方法关键点**：
- 两阶段 LLM 将文档切分成若干段，每段带标题；第二阶段去重筛选，得到 compact 语义单元。
- 为每个段构建标识符，探索随机数字 RNID、段标题 PT-ID、文档标题+段标题 TC-ID（Doc→Pass 与 Pass→Doc 两种顺序）。
- 训练集混合从段落生成的合成 query（DocT5Query）与原始训练 query；原始 query 对齐到段落采用“全部段落”或“BM25 最佳段落”两种策略。
- 多目标加权 NLL 训练：primary 段权重 0.6，其余段均分，使概率质量覆盖多个有效 ID。
- 推理时 constrained beam search 生成段 ID，文档得分取该文档所有段 ID 最大似然。

**关键结果**：
- NQ320K 上 R@1 67.6、MRR@100 74.4，超过 DSI-QG/NCI/MINDER；MINDER R@1 62.7。
- MS MARCO Doc 上 R@1 37.71、MRR@10 48.66，为报告方法中最佳；R@10 71.49 有竞争力。
- 消融：单一文档 ID→段落 ID 在 NQ R@1 40.54→45.62；TC-ID Doc→Pass 最优；原始 query 增强在 NQ 用 all-passages 好，在 MSM 用 best-passage 好；多目标训练进一步提升。

**最值得记住的一句话**：把单一文档 ID 拆成多个段落级 ID，相当于为生成式检索增加多个语义入口，能显著提高首中率和排序质量，但 query 到段落的对齐策略需要按数据异构程度选择。
