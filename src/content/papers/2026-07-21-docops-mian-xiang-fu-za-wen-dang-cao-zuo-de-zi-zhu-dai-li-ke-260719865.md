---
title: 'DocOps: A Verifiable Benchmark for Autonomous Agents in Complex Document Operations'
title_zh: DocOps：面向复杂文档操作的自主代理可验证基准
authors:
- Jiazhen Jiang
- Boxi Cao
- Lingyong Yan
- Yaojie Lu
- Hongyu Lin
- Shuaiqiang Wang
- Dawei Yin
- Xianpei Han
- Le Sun
affiliations:
- Chinese Academy of Sciences
- University of Chinese Academy of Sciences
- Baidu Inc.
arxiv_id: '2607.19865'
url: https://arxiv.org/abs/2607.19865
pdf_url: https://arxiv.org/pdf/2607.19865
published: '2026-07-21'
collected: '2026-07-24'
category: Agent
direction: Agent 评估基准 · 文档操作
tags:
- Agent
- Benchmark
- Document Operations
- Verifiable Evaluation
- Long-range Tasks
- Failure Analysis
one_liner: 构建可确定性验证的文档操作基准，揭示前沿代理在长程耦合任务中状态跟踪崩溃、浅层验证等关键失效模式
practical_value: '- 评估框架的设计思路（层次化任务分解、确定性验证）可迁移至电商搜索/推荐 Agent 的自动化评测，避免人工标注成本，确保可复现性

  - 识别出的三种失败模式对构建面向长流程任务（如多步查询改写、动态过滤条件组合）的 Agent 有直接警示：需加强长程状态追踪、深层次语义校验、避免破坏性操作

  - 文档操作中的“全局一致性维护”问题类似推荐系统中多轮对话或交叉操作下的状态管理，借鉴其分析维度可设计更鲁棒的交互式 RecBot

  - 若业务涉及报告自动化、表格数据净化等 Agent 编排，该基准的层级分类可直接作为能力分级和测试用例设计的模板'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有 Agent 在模拟现实文档工作流（表格、幻灯片、PDF 等）时缺乏可靠评估，尤其长程、强耦合任务下的能力边界不明。

**方法**：构建 DocOps 基准，采用层次化分类法，将真实世界的文档操作拆解为原子能力维度和递增复杂度的工作流，并设计确定性验证机制（不需人工评判）。基于该框架，系统评估了多种闭源/开源模型及 Agent 框架。

**关键结果**：即使最先进的前沿配置，在处理高度耦合的长程任务时仍存在显著局限。细粒度分析揭示了三大典型失效模式：
- **长程状态跟踪崩溃**：Agent 在连续操作中丢失对文档全局状态的追踪；
- **浅层语义校验**：仅匹配表面格式而忽略语义一致性；
- **结构元数据破坏性编辑**：不经意地损坏文档结构信息。

这些发现指出了当前 Agent 在维护全局文档一致性上的能力天花板，为设计非破坏性、鲁棒的智能助手提供了方向。
