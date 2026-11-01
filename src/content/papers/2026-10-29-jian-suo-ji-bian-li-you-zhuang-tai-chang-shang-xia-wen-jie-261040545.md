---
title: 'Retrieval as Traversal: Value-Indexed Memory for Stateful Long-Context Agents'
title_zh: 检索即遍历：有状态长上下文Agent的价值索引记忆
authors:
- Daniel Strauß
- Zhenshan Bing
- Alois Knoll
affiliations:
- Technical University of Munich
- Nanjing University
arxiv_id: '2610.40545'
url: https://arxiv.org/abs/2610.40545
pdf_url: https://arxiv.org/pdf/2610.40545
published: '2026-10-29'
collected: '2026-11-01'
category: Agent
direction: 有状态长上下文Agent的记忆检索机制
tags:
- Stateful Retrieval
- Memory Indexing
- Value-Indexed Memory
- Long-Context Agents
- Traversal
one_liner: 提出价值索引记忆与局部遍历检索，分离内容与地址，验证有状态检索比无状态更易学习
practical_value: '- 在对话式推荐或 Agent 多轮任务中，可借鉴“局部遍历”思想：维护一个可移动的检索头/游标，利用相邻步骤记忆重叠，减少重复全局检索开销；工程上可将向量索引组织为图结构，让查询在图中局部游走而非每次全量
  ANN。

  - 分离“记忆内容”与“地址几何”的框架可用于商品/内容 embedding 索引优化：定义价值为内容信息增益，地址距离为访问成本，用带成本正则的索引目标自动布局，让高互补且高价值的
  item 在索引中靠近，冗余 item 自然分散，提升检索效率和多样性。

  - 论文证明有状态检索在简单任务上比无状态绝对寻址收敛更快（0.59M vs 0.94M/2M+ steps），提示在需要高频连续检索的推荐/搜索场景，引入检索状态可能降低学习难度，值得在召回模块做小规模实验验证。

  - 整体主要是学术贡献，业务可迁移性有限，上述思想可作为架构探索的参考，但需注意论文只测试了简单固定几何环境。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：长上下文模型每次前向都重新搜索相关记忆，循环压缩又过早丢弃信息，两者都忽略相邻检索步骤之间有用记忆的高度重叠。

**方法关键点**：将检索视为持久的局部遍历地址空间，分离记忆内容与地址。效用由内容的信息量决定，几何只决定访问成本。提出成本正则化索引目标：在局部邻域保留高价值信息，同时对每个可访问记忆收费。其边际价值形式带来吸引和排斥两种压力：互补记忆若额外价值超过检索成本则可共检索，冗余记忆即使单独有用也不应挤占同一检索集。

**关键结果**：仅在 MiniGrid Memory 上用最简单固定几何实例验证。持久局部遍历头用五 token 上下文在 0.59M 训练步达到 0.95 平均回报，而 Gaussian 绝对寻址需 0.94M，categorical 绝对寻址超过 2M 步。实验未测试学习几何或重复检索，但初步支持“有状态检索比无状态更容易学习”的假设。
