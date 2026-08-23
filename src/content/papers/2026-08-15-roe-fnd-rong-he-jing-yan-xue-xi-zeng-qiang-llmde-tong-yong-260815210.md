---
title: 'RoE-FND: Synergizing LLMs with Experiential Learning for Effective and Generalizable
  Evidence-Based Fake News Detection'
title_zh: RoE-FND：融合经验学习增强LLM的通用证据型假新闻检测
authors:
- Yuzhou Yang
- Qichao Ying
- Sheng Li
- Zhiyin Zhu
- Zhenxing Qian
- Xinpeng Zhang
affiliations:
- Fudan University
- Hohai University
arxiv_id: '2608.15210'
url: https://arxiv.org/abs/2608.15210
pdf_url: https://arxiv.org/pdf/2608.15210
published: '2026-08-15'
collected: '2026-08-23'
category: RAG
direction: LLM 推理增强 · 经验检索
tags:
- Fake News Detection
- LLM Reasoning
- Retrieval Augmented
- Experiential Learning
- Self-Reflection
- Cross-Dataset Generalization
one_liner: 构建可复用推理经验库并通过检索经验裁决对立论证，提升LLM假新闻检测与跨域泛化能力
practical_value: '- 经验库构建方法：在电商内容审核（如虚假评论、商品描述真实性）中，可让 LLM 同时生成无约束判断与给定真实标签后的条件判断，将两者分歧提炼为可复用的审核规则/经验条目，沉淀成行业/品类专属经验库。

  - 双论证对抗裁决：对高风险 case，不要单次 LLM 判断，而是给出两个相反伪标签分别生成论证，再检索类似历史经验对关键分歧点做裁决；可迁移到客服纠纷判责、商家资质审核等需要证据链推理的业务。

  - 无需微调的跨域迁移：适合电商多品类、多平台快速冷启动，避免频繁训练模型；只需维护经验库与检索器，即可在新类目复用推理能力。

  - 与现有 RAG 结合：把经验库当作比事实片段更高阶的"推理模式索引"，修正 LLM 易被表面说服的倾向，可增强 Agent 在复杂决策中的鲁棒性。'
score: 7
source: arxiv-cs.MM
depth: abstract
---

**动机**：现有假新闻检测要么依赖标注数据训练，迁移性差；要么依赖 LLM 推理，但易被有说服力却有缺陷的论证带偏，缺乏系统经验和纠错机制。

**方法关键点**：提出 RoE-FND。经验构建阶段，用 ground-truth 标签作为 posterior supervision，对比无约束分析和标签条件分析，总结关键分歧成可复用推理 guideline，存入经验库。推理阶段，用翻转伪标签生成正反两个论证，检索最相关经验解决分歧，选择论据更强的一方作为最终预测。整个过程无需优化 LLM 参数。

**关键结果**：在 CHEF、Snopes、PolitiFact 三个纯文本以及 FakeTT、FakeSV 两个多模态基准上，超越强基线，并展现出强跨数据集泛化能力。
