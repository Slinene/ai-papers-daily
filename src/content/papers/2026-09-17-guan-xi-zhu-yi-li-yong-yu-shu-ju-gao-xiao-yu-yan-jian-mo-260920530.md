---
title: Relational Attention for Data-Efficient Language Modeling
title_zh: 关系注意力用于数据高效语言建模
authors:
- Adrian Brasoveanu
- Ece Takmaz
- Jakub Dotlačil
affiliations:
- UC Santa Cruz
- Utrecht University
arxiv_id: '2609.20530'
url: https://arxiv.org/abs/2609.20530
pdf_url: https://arxiv.org/pdf/2609.20530
published: '2026-09-17'
collected: '2026-09-19'
category: LLM
direction: 语言模型 · 关系注意力与数据效率
tags:
- Relational Attention
- BabyLM
- Dual Attention Transformer
- Data Efficiency
- NextLat
- RoPE
one_liner: 在 BabyLM 低数据场景下，用双注意力 Transformer 分离关系注意力与自注意力，提升数据效率和结构泛化
practical_value: '- 用户行为序列建模可借鉴双路注意力：将物品的内容特征（类目、品牌等）与关系/转移结构分离，减少特征纠缠，可能改善长尾和冷启动泛化。

  - 数据受限场景（冷启动、小业务）优先优化架构（如引入关系注意力、符号检索）比叠加训练目标更有效；论文显示架构是主导因素。

  - 无参数 RoPE-based 符号检索可替代学习型符号嵌入，减少参数和过拟合，适用于 item ID、类目等离散符号的表示。

  - NextLat 预测目标鼓励隐状态增量压缩历史，可用于用户状态表示，提升在线推理效率。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

动机：标准 Transformer 在 BabyLM 低数据训练下，自注意力将关系信息与高维对象特征纠缠，限制了数据效率和结构泛化。关系注意力（RA）在纯关系任务上表现出高数据效率，但语言建模需要整合对象与关系信息，相关探索较少。

方法关键点：采用 Dual Attention Transformer（DAT）将对象级特征与关系/结构信息分离路由；引入 NextLat 训练目标，鼓励隐状态增量压缩历史为稠密信念状态；提出基于 RoPE 的无参数符号检索机制，替代学习符号库。在 BabyLM 2026 挑战的 100M 词严格赛道评估。

关键结果数字：架构是结构泛化的主导因素，训练目标次要但显著；在 10M 词时三种关系注意力变体（RA、RCA、DisRCA）基本等价，100M 词时完整 RA 优势显现；最佳模型在 55 个提交中总排名第 6，NLP 任务子集排名第 3，两个最强模型在多数基准上超过 GPT-2 基线，其中一个取得严格赛道最高 EWoK 分数。
