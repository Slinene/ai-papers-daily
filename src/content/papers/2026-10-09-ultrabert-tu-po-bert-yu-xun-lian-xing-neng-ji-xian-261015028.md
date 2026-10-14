---
title: 'UltraBERT: Beyond the Limit of BERT Pre-Training'
title_zh: 'UltraBERT: 突破 BERT 预训练性能极限'
authors:
- Jungwoo Park
- Taewhoo Lee
- Jaewoo Kang
affiliations:
- Korea University
- AIGEN Sciences
- Amazon
arxiv_id: '2610.15028'
url: https://arxiv.org/abs/2610.15028
pdf_url: https://arxiv.org/pdf/2610.15028
published: '2026-10-09'
collected: '2026-10-14'
category: Training
direction: 双向编码器预训练优化
tags:
- BERT
- pre-training
- masking ratio
- distillation
- encoder
- retrieval
one_liner: 提出双头掩码率预训练策略，首次同时达到分类与检索 SOTA
practical_value: '- 在电商搜索/推荐中，文本编码器常用于 query 理解、商品标题分类、相关性计算。可借鉴双头策略：一个 encoder 同时输出分类友好的低掩码率表示和检索友好的高掩码率表示，用不同
  LM head 解耦任务冲突，避免多模型部署成本。

  - 预训练算力投入有边际递减：超过几万亿 token 后 encoder 在下游任务饱和，业务侧做 domain-adaptive pretraining 时不必盲目扩大数据，应把资源转向任务适配或蒸馏。

  - 蒸馏和剪枝要谨慎与掩码率搭配：低掩码率下蒸馏可提升分类但高掩码率下损害检索；如果业务中既要分类又要检索，蒸馏目标应只绑定低掩码率分支，避免损害检索表征。

  - 实现上，可在同一个 batch 内混入不同掩码率样本，共用 backbone，减少工程复杂度。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：双向编码器在 RAG、数据过滤、奖励建模等非生成场景不可或缺，但预训练配方沿用旧式小规模做法，分类与检索难以兼顾。

**方法**：作者重新审视三项核心设计：训练 token 量、掩码率、蒸馏与剪枝。发现：1) 模型在几万亿 token 后饱和；2) 低掩码率利于分类，高掩码率利于检索，与之前研究相反；3) 蒸馏+剪枝低掩码率提升分类，高掩码率损害检索。据此提出 UltraBERT：在单个 batch 内设置低和高两种掩码率，用两个独立 LM head 分别处理，并将蒸馏目标限制在低掩码率上。

**结果**：UltraBERT 首个在分类和检索任务同时达到 SOTA，GLUE 91.0，BEIR 47.7。表明 encoder 性能仍可挖掘，并提供计算分配、掩码率设计与知识迁移的原则性依据。
