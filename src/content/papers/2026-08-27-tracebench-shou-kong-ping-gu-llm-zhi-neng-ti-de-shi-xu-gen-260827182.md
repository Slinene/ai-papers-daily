---
title: 'TraceBench: Controlled Evaluation of LLM Agents for Time-Series Root-Cause
  Attribution'
title_zh: TraceBench：受控评估 LLM 智能体的时序根因归因
authors:
- Tommaso Bendinelli
- Artur Dox
- Christian Holz
affiliations:
- ETH Zürich
- CSEM SA
- Independent Researcher
arxiv_id: '2608.27182'
url: https://arxiv.org/abs/2608.27182
pdf_url: https://arxiv.org/pdf/2608.27182
published: '2026-08-27'
collected: '2026-08-30'
category: Eval
direction: LLM Agent 时序根因归因评测
tags:
- LLM agents
- time series
- root-cause attribution
- benchmark
- evaluation
one_liner: 提出 TraceBench 仿真基准，系统评估 LLM agent 在受控机械系统时序数据上的根因归因能力
practical_value: '- 构建诊断/归因类 agent（如广告投放异常、推荐效果波动归因）时，显式提供系统或业务领域上下文能显著提升归因效果，应把领域知识入口作为核心设计。

  - 让 agent 优先通过结构化数值/表格输出探索数据，而非依赖可视化；在工具接口上优先提供数值 console 输出，更符合 LLM 的使用习惯。

  - 评估归因/诊断能力时，可用仿真或可控生成的数据集构造“参数是否变化+定位哪个参数”的判别式任务，量化根因归因性能。

  - 避免强制 agent 生成 Python 脚本来输出标签，直接允许提交预测结果在多数场景下性能更好；若需脚本模式，应单独评估该环节的损失。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

动机：LLM agent 越来越多用于真实系统时序异常检测和根因分析，但缺乏受控评估。TraceBench 通过模拟物理动态系统生成可控根因归因任务，系统评估 agent 在时间序列观测上判断参数是否变化并定位具体参数的能力。

方法关键点：从三个可解释机械系统生成任务，给 agent 提供时间序列观测，让其判断是否有参数被改变及具体哪个参数；比较 4 个 LLM agent；实验条件包括是否提供领域上下文、输出形式（直接预测 vs 生成 Python 脚本映射样本到标签）；观察数据探索方式（数值 console 输出 vs 可视化）。

关键结果：agent 获得领域上下文后性能显著提升；主要使用数值 console 输出而非可视化来探索数据；强制生成 Python 脚本会降低性能，直接提交预测表现更好。发布数据集、agent 轨迹、实验结果和 leaderboard。
