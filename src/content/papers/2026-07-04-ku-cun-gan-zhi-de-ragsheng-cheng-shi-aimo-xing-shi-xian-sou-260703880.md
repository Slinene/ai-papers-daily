---
title: 'Next-Gen Sponsored Search: Crafting the Perfect Query with Inventory-Aware
  RAG (InvAwr-RAG) Based GenAI'
title_zh: 库存感知的RAG生成式AI模型实现搜索广告查询改写
authors:
- Md Omar Faruk Rokon
- Weizhi Du
- Zhaodong Wang
- Musen Wen
affiliations:
- Walmart AdTech
arxiv_id: '2607.03880'
url: https://arxiv.org/abs/2607.03880
pdf_url: https://arxiv.org/pdf/2607.03880
published: '2026-07-04'
collected: '2026-07-07'
category: QueryRec
direction: 查询改写与广告库存对齐
tags:
- Query Rewriting
- RAG
- Inventory-Aware
- Sponsored Search
- LLM
- LoRA
one_liner: 通过实时库存感知的RAG+LLM查询改写，将无广告填充的搜索比例从13%大幅降低，填充率提升68%
practical_value: '- **零填充查询改写策略**：可借鉴「识别→检索→改写→混合」流程，先通过规则分类器识别低效查询，再基于库存感知的RAG生成候选改写，最后混合历史高点击查询，直接复用至电商广告系统的查询召回阶段。

  - **两塔BERT + LoRA LLM 的架构组合**：用双塔模型做语义检索得到 Top-N 商品，将其属性拼入 prompt 作为上下文，再用 LoRA
  微调的 Llama2 生成改写查询，这种轻量微调方式适合业务快速迭代。

  - **离线评测设计**：刻意选取历史零填充查询作为测试集，直接衡量改写模型的填补能力，同时用 NDCG@8 评估相关性，可作为广告改写效果的兜底指标。

  - **动态库存感知的即时性**：实时检索向量数据库中的可用广告库存并考虑预算，生成与可投放商品绑定的查询，避免改写后仍然无广告可投的尴尬。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

## 动机

电商搜索广告中约 13% 的用户查询无法召回任何广告（零填充），造成巨大收入损失。根本原因在于传统 IR 或 NLG 方法未考虑实时广告库存和竞价预算，导致改写查询虽有语义匹配却无广告可投。需要一套能动态感知可用商品并将查询改写与库存对齐的系统。

## 方法关键点

- **数据准备**：收集用户查询与商品标题的配对并人工标注相关性，训练两塔 BERT；从搜索日志抽取点击≥500次的高互动查询，人工筛选作为改写样本。
- **两塔 BERT 语义检索**：查询塔与商品塔独立编码，通过余弦相似度从向量库中召回 Top N（N=20）个符合预算的库存商品。
- **LoRA 微调 Llama2 7B**：低秩适配器高效微调，使模型能根据原始查询和召回商品属性生成 5 条多元改写查询。
- **RAG 流程**：1) 规则分类器识别低效查询；2) 向量检索实时库存项；3) 将查询与商品描述组装成 prompt；4) LLM 生成改写查询；5) 并入历史流行查询作为混合候选；6) 用交叉编码器 BERT 评估相关性并筛选达到阈值的广告。
- **混合查询池**：动态生成的改写查询与历史上带来高广告展示的成功查询融合，兼顾新鲜度与稳定性。

## 关键实验

- **数据集**：历史零填充的 10,000 条查询。
- **对比基线**：原始查询（0% 填充率）、GPT-4 改写。
- **核心结果**：InvAwr-RAG 填充率 68%，NDCG@8 为 0.6847；GPT-4 填充率 53%，NDCG@8 为 0.6458。

## 一句话要点

将实时库存数据注入 RAG 的 LLM 查询改写，解决了广告系统“有语义匹配却无库存可投”的零填充问题。
