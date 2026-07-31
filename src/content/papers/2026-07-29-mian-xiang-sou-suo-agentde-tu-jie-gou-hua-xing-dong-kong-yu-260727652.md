---
title: 'Harness-G: A Graph-Structured Harness for Search Agents'
title_zh: 面向搜索Agent的图结构化行动空间与信用分配框架
authors:
- Yanning Hou
- Haoyuan Chen
- Sihang Zhou
- Xiaoshu Chen
- Xirui Liu
- Duanyang Yuan
- Lingyuan Meng
- Quan Liu
- Jian Huang
affiliations:
- National University of Defense Technology
arxiv_id: '2607.27652'
url: https://arxiv.org/abs/2607.27652
pdf_url: https://arxiv.org/pdf/2607.27652
published: '2026-07-29'
collected: '2026-07-31'
category: Agent
direction: 结构化搜索Agent · 行动空间重塑
tags:
- search agent
- action menu
- credit assignment
- graph retrieval
- RL
- multi-hop QA
one_liner: 用有限动作菜单替代自由形式查询，消除检索等价崩溃，并在同一状态下进行结构化信用分配，训练更稳定的RL搜索Agent
practical_value: '- 将自由文本检索转换为离散菜单选择（如词条、属性、类目），可避免策略优化中的检索等价崩溃，适用于电商搜索推荐中的多步推理agent。

  - 利用图形结构（实体-句子图）提供可预览的动作替代方案，实现局部对比信用（frontier-relative advantage），无需额外采样就能获得同状态下动作相对价值，可用于推荐系统的多步决策。

  - 启用信用传播通过依赖图回溯，将下游收益分配给早前的桥接动作，能有效处理多跳推荐/对话中的延迟奖励问题，且计算开销低（仅增加9~11%），适合工业部署。

  - 整体框架（菜单+SNC）与RL算法无关，可灵活集成到现有PPO/GRPO训练流程中，且图构建完全程序化（零LLM成本），为工业级搜索/推荐agent优化提供了高效方案。'
score: 9
source: huggingface-daily
depth: full_pdf
---

**动机**：现有RL搜索Agent使用自由文本查询，但语言表面多样性并不带来检索结果的多样性，大量查询最终收敛到几乎相同的证据集合，形成“检索等价崩溃”。这使得基于组内优势的GRPO优化失效，因为轨迹间的回报差异无法反映检索决策的优劣。该问题根源在于检索接口本身，而非奖励信号。

**方法关键点**：
- 将检索重新定义为在段落‑句子‑实体图上的有限动作选择（Select、Lookup、Answer），环境根据图结构构建确定性查询并过滤重复，策略仅需输出菜单ID，消除语言混叠。
- 动作菜单提供可预览的替代方案，使得在同一决策状态下可以直接比较不同信息获取动作的价值，为结构化信用分配奠定基础。
- 提出结构化非短视信用（SNC）：①前端-相对优势，利用冻结的答案评分器，计算选中动作相对于菜单中备选动作的边际增益差异；②启用信用，沿依赖图将下游步骤的信息增益回溯分配给上游桥接动作，解决延迟奖励问题。
- SNC步级信用与GRPO结局奖励相加，仅对策略生成token进行优化，无需额外采样。

**关键结果**：
- 在2Wiki、HotpotQA、MuSiQue等六个QA基准上，Qwen2.5-1.5B平均F1达50.83（超Graph-R1 10.74），3B达55.24（超3.98）；多跳数据集提升尤为显著。
- 对比相同环境下，动作菜单将零优势组比例从Search‑R1的80%以上降至23%左右，且训练后期主要为全对组（成功收敛）。
- SNC消融：移除任一信用成分均导致F1下降2‑4个点。训练稳定，无晚期崩溃，可迁移至多种backbone和RL算法。
- 图构建全程序化，零API成本；SNC仅增加9%~11%的每步时间。

**一句话**：检索动作空间的结构化重构与信用分配设计同等重要，有限动作菜单能从根本上恢复组内优化所需的检索对比度。
