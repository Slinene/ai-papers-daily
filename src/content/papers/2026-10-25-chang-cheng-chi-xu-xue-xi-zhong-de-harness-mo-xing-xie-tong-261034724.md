---
title: Harness-Model Collaboration for Long-Horizon Continual Learning
title_zh: 长程持续学习中的 Harness-模型协同框架
authors:
- Zhen Bi
- Zhizhi Peng
- Yan Wang
- Xueshu Chen
- Haofei Zhang
- Yaobo Zhang
- Zeyu Yang
- Qing Shen
- Jungang Lou
affiliations:
- Huzhou Normal University
- Alibaba Group
- Zhejiang University
- Ningxia University
arxiv_id: '2610.34724'
url: https://arxiv.org/abs/2610.34724
pdf_url: https://arxiv.org/pdf/2610.34724
published: '2026-10-25'
collected: '2026-10-29'
category: Agent
direction: Agent 持续学习 · 经验检索与参数更新协同
tags:
- Continual Learning
- Web Agents
- Procedural Knowledge
- Retrieval
- Experience Replay
- Harness-Model Collaboration
one_liner: HaMo 将轨迹蒸馏为策略经验卡供即时检索，并以经验条件持续学习目标实现快慢协同，提升长程 Agent 的保留与迁移能力。
practical_value: '- 在电商/Web agent 中，把成功购物、搜索、交易等多步轨迹压缩成策略级经验卡（目标、前置条件、操作步骤、适用上下文），检索时按当前任务上下文召回，而不是直接存原始
  log，可降低噪声并提升跨任务复用。

  - 采用快慢结合：线上先走非参数记忆即时复用，离线用检索覆盖度筛选「紧凑且互补」的少样本轨迹做参数更新，避免频繁全量训练和遗忘；该思路可直接迁移到推荐系统的持续学习/增量训练。

  - 经验条件训练目标可迁移到 RAG-style agent：不仅把检索到的策略拼进 prompt，还要用专门目标让模型学会读懂检索结果、判断其是否适用、并按策略执行，这比单纯加外部
  memory 更稳定。

  - 若做导购、push 文案、搜索 query 生成等长程任务，可建立跨 session 流程经验库，按场景召回候选策略，再用小模型微调内化，兼顾线上 latency
  与跨域泛化。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：长程 agent（尤其 Web agent）反复执行信息查找、商品搜索、交易等多步工作流，会不断产生可复用流程知识；但现有系统要么只做模型参数适应、要么只靠外部记忆，难以兼顾持久学习与快速复用。

方法关键点：HaMo 采用 Harness-模型协同框架，将快慢两种学习路径结合。一方面把历史轨迹蒸馏为策略级经验卡（strategy-level experience cards），供即时非参数检索；另一方面引入经验条件的持续学习目标，训练模型在不同上下文中理解、接地并执行检索到的策略。此外，基于检索覆盖度的选择机制会筛选紧凑且互补的轨迹用于参数更新，减少冗余和遗忘。

关键结果：在域内和跨域分布偏移下，HaMo 均优于仅 harness 和仅模型适应的基线，同时改善知识保留与任务适应能力。
