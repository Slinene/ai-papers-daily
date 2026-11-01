---
title: 'rTaste: Do Research Agents Have Taste? Evaluating Early Stage Research Judgment'
title_zh: rTaste：研究智能体有品味吗？评估早期研究判断
authors:
- Art Kanke
affiliations:
- University of Minnesota
arxiv_id: '2610.40488'
url: https://arxiv.org/abs/2610.40488
pdf_url: https://arxiv.org/pdf/2610.40488
published: '2026-10-29'
collected: '2026-11-01'
category: Eval
direction: LLM 研究智能体早期判断评估
tags:
- LLM Agents
- Research Evaluation
- Forecasting
- Experiment Selection
- Multi-Agent
one_liner: 用 415 个最小可行实验评估六款前沿模型的研究判断，发现智能体的实验排序未能显著优于简单基线
practical_value: '- 在电商/广告/推荐业务中若用 Agent 做实验优先级排序或预算分配，不要默认其排序有价值：该研究发现 Agent 排序仅略优于随机，且未超越“选第一个写出实验”的基线。可先用简单规则或人工序作为对照，避免被
  Agent 自信输出误导。

  - 评估 Agent 的判断能力时，必须把所有候选实验都执行（包括排名最后的），再审计结果，否则会引入幸存者偏差。这篇论文的 harness 设计可复用：预注册通过阈值、执行全部
  MVE、用独立模型审计 sound/value/novelty。

  - 预测校准需要单独验证：文中 Agent 的通过率预测只略高于基础率，且不比只给论文+注册信息的新实例更准。业务中做 A/B 测试成功率预测或 query 表现预测时，应对比朴素基线，避免为了复杂
  Agent 流程付出额外成本。

  - 多 Agent 团队在这类判断任务上没有带来整体收益却增加成本。在推荐/搜索的 Agent 工作流中，若任务以排序和预测为主，先做单 Agent 基线，不要急于上多智能体协作。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM Agent 已能承担文献检索、实现、跑实验等研究工作，但前沿实验室尚未将研究议程和预算决策委托给 Agent。这种“哪些实验值得做”的早期判断恰是研究品味（taste）的核心。论文系统评估六款前沿模型作为研究 Agent 在真实 NLP 论文上的实验选择与预测能力。

**方法关键点**：给每个模型 7 篇近期 NLP 论文，让模型单独或组队提出最小可行实验（MVE），为每个实验设定通过阈值、预测是否通过并排序。随后由独立执行器尝试全部 415 个 MVE（包括排名最后的），三名模型审计员根据 sound、valuable、new、beyond seed paper、non-obvious 等标准评估结果。

**关键结果**：415 个 MVE 中 194 个被判定为 sound、valuable 且 new，但其中仅 73 个同时满足 beyond seed paper 和 non-obvious。Agent 的首选实验与审计员最看重实验的匹配度高于随机选择，但未证明优于直接选择第一个写出的实验；通过率预测仅略优于基础率，且不比只给论文和注册信息的新实例更准；多 Agent 团队成本更高但没有带来提案质量的整体提升。评估框架和数据集已开源。
