---
title: 'ScholarQuest: A Taxonomy-Guided Benchmark for Agentic Academic Paper Search
  in Open Literature Environments'
title_zh: ScholarQuest：基于分类法的智能体学术搜索评估基准
authors:
- Tingyue Pan
- Mingyue Cheng
- Daoyu Wang
- Yitong Zhou
- Jie Ouyang
- Qi Liu
- Enhong Chen
affiliations:
- State Key Lab of Cognitive Intelligence, University of Science and Technology of
  China
arxiv_id: '2606.20235'
url: https://arxiv.org/abs/2606.20235
pdf_url: https://arxiv.org/pdf/2606.20235
published: '2026-06-18'
collected: '2026-06-20'
category: Agent
direction: Agent 检索评估 · 分类法引导
tags:
- benchmark
- agent
- academic search
- LLM
- retrieval
- evaluation
one_liner: 提出 ScholarQuest 基准，系统评估智能体在开放文献环境中的迭代检索能力
practical_value: '- **意图分类法可迁移至电商搜索**：将查询意图细分为方法导向、场景锚定、对比型等，用于构建更丰富的搜索评测集或指导 Agent
  的意图识别。

  - **共享检索后端保证可复现性**：固定文献库 ScholarBase 的设计思路可直接用于搭建企业内部的搜索 Agent 评测平台，确保不同方法在相同语料上公平对比。

  - **多维评估信号**：同时关注召回、效率与不同意图下的鲁棒性，为推荐/搜索 Agent 提供更全面的诊断信息，避免单指标误导。

  - **基于引用图的可扩展答案构造**：利用引用关系自动扩张相关论文，类似在推荐中利用物品共现链扩展候选池，可启发生成式推荐的评测数据生成。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：现有基准难以在真实的开放文献环境中系统评估基于 LLM 的学术搜索 Agent，缺乏对多轮、意图驱动的检索能力的全面衡量。

**方法**：
- 构建 ScholarQuest，覆盖超过 1000 个计算机科学主题，定义四类研究意图：方法导向、场景锚定、对比型和范围控制查询。
- 通过引用图自动扩展相关论文生成大规模答案，确保可扩展性。
- 提供共享检索后端 ScholarBase，使不同 Agent 在同一语料库下公平比较，强调可复现性。

**关键结果**：
- Agent 方法显著优于单次检索基线，但最佳模型 Recall@100 仅 0.314，Recall@All 仅 0.355，表明仍有巨大提升空间。
- 进一步分析搜索效率、意图层面的鲁棒性及失败案例，证明该基准能提供多维度评估信号。
