---
title: 'TubiFM: Unified Item, Carousel, and Search Ranking for Streaming Discovery'
title_zh: TubiFM：统一物品、轮播与搜索排序的流媒体推荐模型
authors:
- Alexandre Salle
- Chenglei Niu
- Suchismit Mahapatra
- Xiaoxiao Chen
- Suvash Sedhain
- Yaqi Wang
- Shervin Shahryari
- Saurabh Agrawal
- Qiang Chen
- Michael Tamir
affiliations:
- Tubi
arxiv_id: '2605.23702'
url: https://arxiv.org/abs/2605.23702
pdf_url: https://arxiv.org/pdf/2605.23702
published: '2026-05-22'
collected: '2026-05-25'
category: RecSys
direction: 生成式推荐 · 多任务统一排序
tags:
- generative recommendation
- multi-task ranking
- LLM finetuning
- user story
- streaming
- unified model
one_liner: 将用户跨表面的行为序列化为“用户故事”，通过单一生成式模型统一物品、轮播和搜索排序，简化系统并提升多任务效果。
practical_value: '- **统一用户行为表示**：将搜索、观看、轮播曝光等异构信号序列化为“用户故事”，可作为电商场景中浏览、搜索、购买行为的统一输入格式，避免为不同任务维护多套特征工程。

  - **单一模型处理多任务**：通过不同提示词完成物品排序、容器排序、搜索排序，无需多任务头，可直接借鉴到电商首页推荐、频道排序和搜索排序的模型合并，降低系统复杂度。

  - **原子token与掩码训练**：使用原子item token而非Semantic ID，减少推理开销；训练时随机掩码carousel token，增强模型对容器无关排名的泛化能力，适合电商中跨场景打分。

  - **工程落地启示**：用1B LLM取代多阶段召回+排序流水线，p99延迟从500ms降至200ms，在搜索上TVT提升3.9%，证明生成式统一排序可在简化架构的同时保持或提升业务指标。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：流媒体个性化发现需同时处理物品排序、轮播排序和搜索排序，但这些任务常由独立模型完成，割裂了用户旅程中的互补信号（如搜索透出意图、观看反映偏好）。论文提出“用户故事”——一种跨表面的行为序列化表示，使单一生成式模型能够完成所有排序任务。

**方法关键点**
- **用户故事构造**：将用户属性、会话边界、观看事件（含表面、轮播上下文）、搜索事件按时间序序列化为token序列，形成固定语法的统一输入。
- **模型与训练**：基于Llama 3.2 1B，通过扩展词表加入领域token（如`<|id()|>`、`<|carousel()|>`），使用下一个token预测微调；训练集包含约2000万用户故事，辅助目录语料帮助领域token与预训练语义对齐。
- **多任务提示推理**：对不同任务，在故事末尾追加特定提示头（如预测物品、轮播或搜索结果），一次前向计算即可从全量词表logit中对候选打分。
- **关键设计**：原子item token（非多token Semantic ID）减少推理开销；训练时随机掩码轮播token（概率0.1）及少量item token，提升容器无关排序和冷启动适应能力。

**实验结果**
- 离线评估：在2000万用户样本上，统一TubiFM在物品排序（HR@8 0.5817 vs HSTU 0.4121）、轮播排序（HR@8 0.8343 vs HSTU 0.7724）、搜索排序（HR@8 0.5673 vs BM25 0.4637）上全面超越专有基线，且超过任务特化TubiFM变体。
- 在线A/B：搜索总观看时长TVT提升3.9%，轮播TVT提升0.30%，物品排序TVT持平（+0.14%）但系统简化、p99延迟从500ms降至200ms。

**一句话**：将用户旅程序列化为统一故事，用单一生成式模型跨任务排序，可在简化生产系统的同时显著提升搜索和推荐效果。
