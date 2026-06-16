---
title: Understanding the Behaviors of Environment-aware Information Retrieval
title_zh: 理解环境感知信息检索的行为
authors:
- Ruifeng Yuan
- Chaohao Yuan
- David Dai
- Yu Rong
- Hong Cheng
- Hou Pong Chan
- Chenghao Xiao
affiliations:
- Fudan University
- Alibaba DAMO Academy
- Chinese University of Hong Kong
- Stanford University
- Shanghai University of Finance and Economics
arxiv_id: '2606.16817'
url: https://arxiv.org/abs/2606.16817
pdf_url: https://arxiv.org/pdf/2606.16817
published: '2026-06-15'
collected: '2026-06-16'
category: QueryRec
direction: RL驱动的查询改写自适应检索器
tags:
- RAG
- Query Reformulation
- Reinforcement Learning
- GRPO
- Retriever-Aware
- Information Retrieval
one_liner: 首次用强化学习使LLM学会为不同检索器自适应生成查询风格，并揭示各检索器最优查询风格差异显著
practical_value: '- 电商搜索常混合使用倒排索引与向量检索器，可借鉴 RL 训练查询改写模型，使其根据后台检索器类型动态调整 query 风格（如对
  BM25 生成关键词式，对向量检索器生成描述性文本），提升召回相关性。

  - 多步检索场景中，可利用论文提出的分支 rollout 技术稳定训练改写策略，避免长轨迹的奖励震荡，适用于需要多轮交互的 Agent 搜索链。

  - 揭示的检索器偏好差异（Contriever 偏好文档段落式查询，BM25 偏好精确关键词）可直接指导搜索系统的预处理或 prompt 设计：根据检索器类型设定不同的改写模板或约束。

  - 引入检索器特有的人类先验作为辅助奖励，可加速 RL 训练并注入业务知识，类似推荐系统中利用人工规则冷启动生成式模型。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：现有 RAG 系统常忽略一个关键问题——不同检索器（如 BM25、Contriever）对查询表述有截然不同的偏好，固定改写策略难以在所有检索器上取得最优效果。论文旨在探究 LLM 能否通过强化学习学会针对特定检索器生成最优查询。

**方法**：将查询改写建模为 RL 任务，使用 GRPO 优化 LLM，奖励为检索器返回结果的准确率。引入**分支 rollout** 技术，在多步检索轨迹中同时探索多个分支，提升训练稳定性。实验覆盖 BM25、Contriever、GTR 等多种检索器，并在训练中融入检索器特定的人工指导作为额外奖励信号。

**关键结果**：
- RL 训练后，LLM 能自动学习到不同检索器的最优查询风格：对 Contriever 生成**文档段落式**长查询，对 BM25 生成**精简关键词**查询，风格差异显著且非平凡。
- 未适配时，同一改写策略在不同检索器上性能差距达 20%+；RL 适配后整体召回准确率提升 10-15%，且模型规模扩展带来进一步增益。
- 分支 rollout 有效缓解了多步奖励信号的高方差问题，使训练更稳定。
- 额外的人工指导奖励可加速收敛并小幅提升最终性能。
