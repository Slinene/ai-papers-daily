---
title: 'Generalized Agent Iteration: One Formal Framework for Iterative Policy Improvement
  and Recursive Self-Improvement'
title_zh: 广义智能体迭代：统一迭代策略改进与递归自改进的形式框架
authors:
- Hongyao Tang
- Yi Ma
- Pengyi Li
- Yifu Yuan
affiliations:
- Tianjin University
- Shanxi University
arxiv_id: '2609.13406'
url: https://arxiv.org/abs/2609.13406
pdf_url: https://arxiv.org/pdf/2609.13406
published: '2026-09-10'
collected: '2026-09-18'
category: Agent
direction: Agent 迭代学习的形式化框架
tags:
- Generalized Agent Iteration
- Recursive Self-Improvement
- Generalized Policy Iteration
- Agent Learning
- Formal Framework
one_liner: 提出 GAI 框架，用两个维度统一经典 GPI 与递归自改进，并给出目标漂移与自指缺陷的形式化刻画
practical_value: '- 在电商/推荐的 LLM Agent 自改进链路（如 self-refine、Reflexion）中，可用论文的两个旋钮做架构审查：改进机制是否在
  Agent 内、评估标准是否外部接地；优先采用 anchored 配置，把奖励模型或业务指标作为独立外部评估器，避免同模型自评导致 goal drift。

  - 多轮自训练或 self-play 策略迭代时，若候选生成与评估标签都由同一模型产生，系统会滑向 fully self-referential；工程上应引入独立线上业务指标、人工标注或固定测试集作为外部锚点，并设置漂移监控。

  - 可将改进机制显式外置为独立组件（如单独 prompt、规则或小模型），使系统具备 GPI 式可分析性；等外部评估稳定后再逐步将改进机制内化为 Agent 的一部分，降低不可控递归风险。

  - 论文偏理论，无实验或可复用算法；主要价值是提供诊断自改进系统缺陷的坐标语言，适合作为设计评审的思维框架。'
score: 6
source: huggingface-daily
depth: abstract
---

动机上，递归自我改进（RSI）在不同尺度被广泛宣称，但缺少统一形式化；经典广义策略迭代（GPI）只覆盖更新原则与评估基准都在智能体外部的情形。GAI 框架把智能体定义为系统内可修改组件配置，将学习过程建模为 agent evaluation 与 agent improvement 的循环。两个关键旋钮区分实例：改进机制是否属于智能体；评估标准是否外部接地。前者划定 GPI 与 RSI 边界，后者把系统分为 anchored、goal drift、fully self-referential 三类。用这两个坐标可把现有系统放在同一轴上比较，并让 RSI 的缺陷逐个条件陈述。论文无实验，主要是形式化与分类工具，为分析和设计新的自改进系统提供基础。
