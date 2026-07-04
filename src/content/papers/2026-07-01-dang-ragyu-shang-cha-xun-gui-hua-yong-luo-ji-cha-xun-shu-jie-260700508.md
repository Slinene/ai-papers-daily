---
title: 'When RAG Meets Query Planning: Logical Query Trees for Resolving Exploratory
  Reasoning Problems'
title_zh: 当RAG遇上查询规划：用逻辑查询树解决探索性推理问题
authors:
- Ganlin Xu
- Linghao Zhang
- Zhitao Yin
- Hongda Xi
- Chen Yang
- Jiaqing Liang
- Weijia Lu
- Sihang Jiang
- Yanghua Xiao
- Deqing Yang
affiliations:
- School of Data Science, Fudan University
- College of Computer Science and Artificial Intelligence, Fudan University
- United Automotive Electronic Systems
arxiv_id: '2607.00508'
url: https://arxiv.org/abs/2607.00508
pdf_url: https://arxiv.org/pdf/2607.00508
published: '2026-07-01'
collected: '2026-07-04'
category: RAG
direction: 复杂查询规划 · 逻辑查询树
tags:
- RAG
- Query Planning
- Logical Query Trees
- Exploratory Reasoning
- Cost Model
- Dynamic Programming
one_liner: 将探索性推理问题建模为逻辑查询树，通过动态规划与成本模型优化多步检索与推理
practical_value: '- 电商搜索中，用户意图模糊的复杂查询（如“适合敏感肌的平价抗老面霜”）可借鉴PlanRAG的分解与重组逻辑：将原始查询拆分为原子子查询（如“敏感肌适用”、“抗老”、“平价”），通过成本模型决定检索顺序与合并方式，减少无效检索。

  - 成本模型的多维评估（如相关性、覆盖度、语义连贯性）可直接迁移到推荐系统的多路召回融合阶段，替代简单加权，动态规划出最优融合计划。

  - 树状执行结构与并行节点处理机制适用于Agent工作流：不同子任务可并行检索知识库，再逐步聚合生成最终答案，低延迟场景下可开启多线程加速。

  - 动态改写中间结果（rewriting）的思路可用于对话式推荐：对中间检索到的商品列表进行总结与再查询，逐步精炼用户需求。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：现有RAG系统难以处理探索性推理问题（ERP）——这类查询存在高不确定性和模糊性，推理路径不明确，容易引入检索噪声并累积错误，且缺乏端到端的规划机制来生成有效的执行轨迹。

**方法**：提出PlanRAG，将ERP建模为逻辑查询树（LQT）。首先将自然语言查询分解为原子查询，再通过动态规划与多维成本模型（综合考虑语义相关性、覆盖度、连贯性等）将原子查询组织为一棵有向无环树。执行时采用迭代聚合、改写、检索、生成循环：并行处理树中节点，向上传播中间结果，并支持多线程并行加速。

**结果**：在新建数据集WikiWeb-ERP上，PlanRAG在答案准确性、推理充分性等指标上均优于两类主流RAG基线（迭代式和图式），验证了逻辑查询树规划对复杂推理的增益。
