---
title: 'From Code Review to Code Critique: Intent, Drift, and Spotlight for AI-Generated
  Diffs at Scale'
title_zh: 从代码审查到代码评论：面向大规模 AI 生成差异的意图、漂移与聚光灯
authors:
- Chandra Maddila
- Mashrur Rashik
- Euna Mehnaz Khan
- Smriti Jha
- James Saindon
- Nachi Nagappan
- Peter C. Rigby
affiliations:
- Meta, USA
- Concordia University, Montreal, Canada
arxiv_id: '2607.29516'
url: https://arxiv.org/abs/2607.29516
pdf_url: https://arxiv.org/pdf/2607.29516
published: '2026-07-31'
collected: '2026-08-03'
category: Agent
direction: AI 编码 Agent 审查 · 意图理解与漂移检测
tags:
- code review
- LLM
- intent prediction
- drift detection
- code spotlight
- AI coding agents
one_liner: 提出意图预测、漂移检测和代码聚光灯三大机制，革新 AI 编码代理的代码审查流程
practical_value: '- **意图预测用于生成式推荐**：利用用户会话日志、历史行为等元数据推断搜索意图，动态调整推荐策略，提升生成内容的针对性。

  - **漂移检测作为线上监控**：通过回译（backtranslation）测量最终推荐结果与原始意图的语义偏移，设定阈值告警，防止模型“自由发挥”导致体验恶化。

  - **聚光灯机制优化资源分配**：对大量生成候选项进行重要性排序，仅对人眼或高成本模型暴露高优先级条目，大幅降低 token 消耗与人工审核成本。

  - **主题分类体系迁移**：参考论文的六主题分类（正确性、安全性等），构建推荐系统的质量评估框架，细粒度监控生成内容的多维度风险。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：AI 编码代理产出超出传统人工审查承受力，现有 AI 审查工具过度关注代码风格等低价值建议，忽略正确性、安全性等人类最重视的方面。

**方法**：构建 ARCTIC 系统，基于 18,000 次代码审查归纳六主题分类体系，并实现三大核心能力：
1. **意图预测**：从会话日志和元数据推断变更的真实原因；
2. **漂移检测**：通过回译技术量化开发者意图与代理生成代码之间的语义差异；
3. **代码聚光灯**：对 diff 区域排序，标识最需人工审查的片段。

**结果**：离线评估中，意图预测 F1=0.86，漂移检测与人类标注的加权 Kappa 系数高达 0.907，代码聚光灯在质量估计上以 1/5 的 token 消耗超越基线 2.4 倍；实验推出后，漂移得分降低代码不对齐 5.76 分（p=0.026），意图预测获 90.2% 认可，且上线以来自审 diff 零缺陷。
