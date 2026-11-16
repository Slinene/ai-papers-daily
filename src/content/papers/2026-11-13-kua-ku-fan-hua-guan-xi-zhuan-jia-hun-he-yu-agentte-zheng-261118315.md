---
title: 'Experts Across Schemas: Agent-Guided Mixture-of-Relational-Experts for Cross-Database
  Generalization'
title_zh: 跨库泛化：关系专家混合与Agent特征增强
authors:
- Hiren Madhu
- Sukanta Ganguly
- Kiran Srinivasan
- Smita Krishnaswamy
- Rex Ying
affiliations:
- Yale University, USA
- NetApp, USA
arxiv_id: '2611.18315'
url: https://arxiv.org/abs/2611.18315
pdf_url: https://arxiv.org/pdf/2611.18315
published: '2026-11-13'
collected: '2026-11-16'
category: RecSys
direction: 关系基础模型 · 跨库泛化 + Agent 特征工程
tags:
- Mixture-of-Experts
- Graph Transformer
- Cross-Database
- Relational Learning
- LLM Agent
- Feature Engineering
one_liner: 用列元数据路由的关系专家图Transformer加上标签盲LLM Agent生成派生列，小预训练语料下跨库预测最优。
practical_value: '- MoE 按列元数据路由而非值路由：在跨国家/类目、多 schema 迁移时，避免模型过拟合特定值分布，可作为多业务统一用户/物品模型的路由策略。

  - LLM agent 从 schema+列统计盲标签生成单行派生特征：适合冷启动新表或快速特征工程，注意加入验证机制防止标签泄漏。

  - 行与单元格同时 token 化，并显式注入行 log-age 和外键关系名：用户行为建模中可把时间衰减与关系类型作为注意力偏置，提升对历史交互的利用。

  - 小语料跨库预训练 + 架构改进可逼近大语料模型：对没有海量跨平台数据的中小团队，优先优化结构而非堆数据更经济。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

动机：Web 平台用户/物品记录分散在不同 schema 的关系库中，跨库迁移预测模型困难；现有关系基础模型依赖大规模预训练语料，成本高。

方法：设计 MoREGT 图 Transformer，将行与单元格均作为 token；注意力显式加入行的 log-age 与外键关系名；用列元数据（非值）路由到关系专家。配套一个 label-blind LLM agent，读取目标库 schema 与列统计，生成并校验单行派生列，全程不接触标签与模型分数。

结果：在 21 个 RelBench 任务、6 库 leave-one-database-out 预训练下，MoREGT 较同数据预训练的 Relational Transformer 平均 AUROC 提升 2.25 点、nMAE 提升 5.83 点；加入 agent 特征后 AUROC 达 79.63、nMAE 降至 26.98，为对比方法中最高，优于用约 400 倍库预训练的 RT-J。
