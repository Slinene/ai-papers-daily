---
title: 'CORE: Improving Compositional Reasoning in MLLM Embedding via Reranker Distillation'
title_zh: 通过重排器蒸馏提升 MLLM 嵌入的组合推理能力
authors:
- Tingyu Song
- Mingxin Li
- Yanzhao Zhang
- Dingkun Long
- Chu Liu
- Pengjun Xie
- Yilun Zhao
- Shu Wu
affiliations:
- CASIA
- Alibaba Group
- University of Chinese Academy of Sciences
- Yale University
arxiv_id: '2609.04083'
url: https://arxiv.org/abs/2609.04083
pdf_url: https://arxiv.org/pdf/2609.04083
published: '2026-09-02'
collected: '2026-09-05'
category: Multimodal
direction: 多模态嵌入蒸馏 · 组合推理检索
tags:
- MLLM Embedding
- Reranker Distillation
- Rank-KL
- Compositional Reasoning
- Cross-modal Retrieval
- Listwise Training
one_liner: 将重排器的跨注意力组合判断蒸馏为 Rank-KL listwise 目标，显著提升多模态嵌入的组合检索与细粒度区分
practical_value: '- 双塔召回或 embedding 模型训练时，用 reranker 作为 teacher 做 listwise 蒸馏，Rank-KL
  目标比传统 contrastive/pairwise 更能传递细粒度排序结构；电商图文相关性、属性绑定问题可直接复用。

  - 五级匹配粒度（完全匹配/部分出现/属性错/对象错/全错）适合挖掘商品主图与 query 的难负样本：例如“红色条纹衬衫”与“蓝色条纹衬衫”应作为属性错误而非随机负样本，提升
  embedding 对属性-对象组合的判别。

  - 评估上不建议只看 Recall@K，可以按 L1-L5 错误类型分级统计，定位模型在绑定关系上的盲区；搜索/推荐中可迁移到 query-主图/标题-属性一致性评测。

  - 工程上 teacher reranker 只在训练阶段蒸馏，推理仍用双塔 embedding，不增加线上 latency；注意需要统一数据构造和调优预算才能公平对比不同训练目标。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：现有 MLLM embedding 在组合检索上较弱，常分不清相同概念但属性-对象绑定不同的场景；但同一 backbone 做 cross-attentive reranker 时能区分，因此把 reranker 的组合判断蒸馏给 embedding。

方法：CORE 为一张图合成五级候选列表（L5 完全匹配、L4 部分出现、L3 属性错误、L2 对象错误、L1 完全错误），提出 Rank-KL listwise 目标，让学生 embedding 复现 teacher reranker 的细粒度排序；同时构建分级评测协议，并在相同数据和调优预算下对比 contrastive learning、pairwise CoSENT、listwise Rank-KL。

结果：CoSENT 和 Rank-KL 比 contrastive 更有效利用多级监督，Rank-KL 最强。CORE-RERANKER-8B 在 COLA、SUGARCREPE++、NEGBENCH 三项 benchmark 上 total average 达 82.7%，超过 Jina-Reranker 10.7 分；CORE-EMBED-8B 在所有评估 embedding 模型中取得最佳 total average 0.666。同时迁移到 MCMR 不损害 COCO/Flickr30K 检索表现。
