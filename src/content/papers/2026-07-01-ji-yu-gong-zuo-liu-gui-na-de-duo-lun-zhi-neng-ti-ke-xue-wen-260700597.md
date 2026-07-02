---
title: Multi-Turn Agentic Scientific Literature Search via Workflow Induction
title_zh: 基于工作流归纳的多轮智能体科学文献搜索
authors:
- Jisen Li
- Bingxuan Li
- Nanyi Jiang
- Xuying Ning
- Xiyao Wang
- Yifan Shen
- Heng Wang
- Yuqing Jian
- Xiaoxia Wu
- Ben Athiwaratkun
affiliations:
- University of Illinois Urbana-Champaign
- Together AI
- University of Pennsylvania
- Stanford University
arxiv_id: '2607.00597'
url: https://arxiv.org/abs/2607.00597
pdf_url: https://arxiv.org/pdf/2607.00597
published: '2026-07-01'
collected: '2026-07-02'
category: Agent
direction: Agent 工作流生成 · 多轮搜索
tags:
- Agentic Search
- Workflow Induction
- Multi-turn Interaction
- Preference Optimization
- DAG
- Scientific Literature
one_liner: PaperPilot将多轮文献搜索构建为可执行、可编辑的DAG工作流，结合用户反馈实现高效可控的搜索对齐
practical_value: '- 将搜索过程显式化为可编辑的DAG工作流（关键词搜索→引用扩展→过滤→重排序→证据提取），可为电商搜索/推荐Agent提供可解释、可调控的交互式搜索链路，便于开发者调试与用户定制。

  - 利用用户反馈调整工作流结构（如增加查询扩展或调节评分权重）的思路，可迁移到电商多轮查询改写与召回路自适应，例如基于前一轮推荐结果的隐式反馈动态插入过滤或重排序模块。

  - 训练采用监督工作流模仿（从人工工作流中学习）与偏好优化（对生成的工作流进行可控破坏并学习偏好）的组合方式，可借鉴到电商工具调用Agent的训练中，提升工作流生成的准确性和执行稳定性。

  - 工作流执行错误率从9.5%降至0%，表明显式结构化调用比纯推理更可靠；在电商客服、导购助手等场景中，可设计类似的结构化操作链，降低非法操作风险，提升系统鲁棒性。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：科学文献搜索需要多轮交互来澄清模糊意图并融合用户偏好，但现有搜索智能体依赖固定流程或隐式推理，策略不可控、难以修正。
**方法**：提出PaperPilot，将多轮搜索建模为**工作流归纳（Workflow Induction）**。给定锚定论文和用户查询，智能体生成一个可执行的**DAG**，其中的节点包括关键词搜索、引用扩展、过滤、打分、重排序、证据提取等原子操作。用户反馈用于同时精化查询和修改工作流结构。训练分两阶段：先用人工构建的`(用户, 锚定论文, 目标论文)`三元组进行**监督工作流模仿**；再对生成的工作流进行可控破坏（如随机删节步骤），通过**偏好优化**使模型偏好正确版本。
**结果**：PaperPilot-9B在多轮交互中Hit@5从58.0→**77.0**，MRR从47.5→**59.4**，nDCG@10从26.8→**32.5**，工作流执行错误率从9.5%→**0%**。显式可编辑的工作流成为对齐复杂搜索意图的有效接口。
