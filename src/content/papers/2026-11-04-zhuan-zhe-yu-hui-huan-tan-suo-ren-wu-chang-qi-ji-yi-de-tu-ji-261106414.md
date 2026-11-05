---
title: 'Twists and Turns: A Graph-Based Benchmark and Framework for Long-Term Memory
  in Exploration Tasks'
title_zh: 转折与回环：探索任务长期记忆的图基准与框架
authors:
- Chongyuan Dai
- Yaling Shen
- Zirui Song
- Junfeng Liao
- Jinpeng Hu
- Xiuying Chen
affiliations:
- Mohamed bin Zayed University of Artificial Intelligence (MBZUAI)
- Monash University
- Hefei University of Technology
arxiv_id: '2611.06414'
url: https://arxiv.org/abs/2611.06414
pdf_url: https://arxiv.org/pdf/2611.06414
published: '2026-11-04'
collected: '2026-11-05'
category: LLM
direction: 长期记忆 · 图结构化探索
tags:
- Long-term memory
- Graph-based memory
- Benchmark
- Exploration tasks
- Retrieval
- LLM agents
one_liner: 提出图引导基准 LExMem 与图记忆框架 LExGraph，将探索过程组织为图并显著超越现有检索记忆系统
practical_value: '- 将用户长期交互/会话建模为图而非扁平总结：节点可以是 query/商品/反馈/尝试结果，边是“修订/重试/对比/复用”关系，让推荐或客服
  Agent 在用户重新回到旧意图时能恢复完整决策路径，避免记忆丢失。

  - 检索增强可采用混合检索 + 邻居扩展：先用向量/关键词召回锚点节点，再沿图的入边/出边扩展相关历史节点，能提升长对话中证据召回率，适合需要追溯多次试错的推荐解释、售前咨询场景。

  - 基准设计可借鉴“图结构生成 QA”的思路：用演化机制构造分支、修订、复活等复杂探索图，再从图中生成问题，评测模型对过程性长期记忆的掌握，比只测事实更贴近真实业务中的多轮决策。

  - 框架强调增量式构建记忆节点，可在线落地：每轮对话结束后提取节点并建立边，不依赖事后批量整理，适合实时 Agent 在电商导购中持续积累用户偏好和决策历史。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

动机：长期问题解决（如科研、软件开发）是围绕目标不断试错、修订、复活的非线性过程，但现有长期记忆研究主要关注事实回忆与更新，忽视了探索过程中方法、中间结果、早期尝试之间的互联关系。

方法关键点：作者观察到探索过程天然形成图结构——分支方案通过“修订”和“重新考虑”相互连接。基于此提出：1）LExMem 基准：将探索过程建模为图，并引入演化机制增加结构复杂性，最终生成 224 段对话和 2,018 个基于图结构的 QA 实例；2）LExGraph 记忆框架：增量式把对话组织为互连的记忆节点，检索阶段采用混合检索（如向量+关键词）并沿邻居关系扩展证据。

关键结果：实验显示 LExMem 对现有 retrieval-based 和 memory-based 系统构成显著挑战；LExGraph 在 LExMem 上取得更优表现，并能有效泛化到外部长期记忆基准。
