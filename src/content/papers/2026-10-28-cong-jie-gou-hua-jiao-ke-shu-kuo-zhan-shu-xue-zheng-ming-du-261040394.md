---
title: Scaling Mathematical Proof Supervision from Structured Textbooks
title_zh: 从结构化教科书扩展数学证明监督
authors:
- Youqing Fang
- Zhouqi Hua
- Yinhao Tang
- Yuzhe Gu
- Lingkai Kong
- Bin Liu
- Weiming Zhang
- Kai Chen
- Yanan Sun
- Wenwei Zhang
affiliations:
- University of Science and Technology of China
- Fudan University
- Shanghai AI Laboratory
- Shanghai Jiao Tong University
arxiv_id: '2610.40394'
url: https://arxiv.org/abs/2610.40394
pdf_url: https://arxiv.org/pdf/2610.40394
published: '2026-10-28'
collected: '2026-11-12'
category: Training
direction: 数学证明监督 · 结构化课程学习
tags:
- Mathematical Reasoning
- Structured Supervision
- Curriculum Learning
- SFT Data
- Textbook Corpus
one_liner: 构建保留教材章节与证明链的38万条数学监督语料，结构化教材监督比传统QA微调提升16.7个百分点
practical_value: '- 把领域知识/规则文档按原有层级（目录、章节、条目间依赖）保留并构造训练数据，比压平成孤立 QA 更有助于 Agent 多步推理与规划；可迁移到电商导购、客服
  SOP、价格/营销政策等场景。

  - Gap QA 思路可借鉴：在关键中间步骤挖空，强迫模型补全依赖链条，适合训练商品属性关联、优惠叠加规则、搜索意图补全等需隐式推理的任务。

  - 用课程学习时，不必依赖固定数据顺序，可沿用类目/难度/结果链的自然序；同时覆盖更多子域（来源广度）比单一域堆量更划算。

  - 主要学术贡献在数学推理，但对电商/推荐 Agent 而言，更值得复用其数据组织与结构化监督构造 pipeline，而非数学语料本身。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：传统数学 SFT 把教材压平成孤立问题-答案对，丢失课程顺序、命题-证明链接、依赖引用和来源信息，难以研究数据组织对数学推理的影响。

**方法**：构建 TOME-Math，将 2,118 本大学数学教材转为约 380K 结构化证明监督记录，保留章节顺序、命题-证明链接、依赖引用和来源。构造两类数据：Gap QA 挖去证明中间步骤，要求模型补全依赖链；Proof QA 则给完整证明。基于章节顺序进行多学科课程学习，并分析监督量和来源广度的 scaling 规律。

**结果**：全量微调后在 held-out 评测与公开数学基准上的未加权平均分较基座模型提升 16.7 个百分点，并超过三个公开 instruction-data 基线。证明结构化教材是可扩展的数学监督来源，也为数据组织与推理能力关系提供了实证框架。
