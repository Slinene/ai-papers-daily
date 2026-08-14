---
title: Total Recall at What Cost? Benchmarking the Serving Cost of Agentic Memory
  Systems
title_zh: 全面回忆代价几何：智能体记忆系统服务成本基准测试
authors:
- Natchanon Pollertlam
- Witchayut Kornsuwannawit
affiliations:
- Bricks Technology, Thailand
arxiv_id: '2608.11879'
url: https://arxiv.org/abs/2608.11879
pdf_url: https://arxiv.org/pdf/2608.11879
published: '2026-08-12'
collected: '2026-08-14'
category: Eval
direction: Agent 记忆系统成本与精度基准
tags:
- Agentic Memory
- LLM Serving Cost
- Cost-Accuracy Trade-off
- Benchmark
- Conversational Agents
one_liner: 系统对比三种 agentic 记忆系统与滚动窗口/全量转录基线，发现成本不可由对话长度预测且成本-准确率无赢家
practical_value: '- 长期对话 agent（客服、导购、推荐助手）引入记忆系统时，不要只按对话长度或消息大小预估成本；记忆系统的内部行为（抽取、总结、检索）才是主要成本变量，必须实测
  profiling，否则成本可能偏差 18-69%。

  - 上线前做 break-even 分析：对比全量 transcript 重发、固定滚动窗口和记忆系统的单轮 serving 成本，确定在会话多少轮后记忆系统才开始省钱；本实验中最便宜系统数十轮即可回本，最贵系统
  400 轮内从未回本，选择错误会持续超支。

  - 成本与准确率联合评估：642 个 LoCoMo 问题上各系统准确率仅 21-54%，没有系统同时占优；若业务对准确率敏感，先定准确率底线，再在满足底线的系统中选成本最低者。

  - backbone 选择对成本的影响与记忆系统本身同样大，甚至可能抵消记忆系统的节省；做记忆系统选型时必须联合 backbone（如 GPT-4o vs. 轻量模型）一起压测，不能只换记忆系统而沿用原模型。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：长时间运行的对话 agent 依赖记忆系统避免每轮重发完整历史，但不同记忆系统的服务成本缺少系统基准，实际落地时不知道该选哪种策略、何时切换更省钱。

**方法关键点**：在 400 轮以内的多轮对话上，对比三种记忆系统 Mem0、Hindsight、Mastra Observational Memory 与两种参考策略（固定大小滚动窗口、全量 transcript 重发），覆盖两个 backbone；对 665 个 LoCoMo 问题同时测量回答准确率与 serving 成本。

**关键结果数字**：
- 成本回归模型对两个参考策略拟合良好，但对三个记忆系统误差达 18-69%，说明记忆系统成本由内部记忆行为驱动，不能仅用对话长度和消息大小预测。
- break-even 分析显示，记忆系统何时比全量 transcript 更省钱高度依赖具体系统和 backbone：最便宜系统几十轮内回本，最贵系统 400 轮内从未回本。
- 没有任何系统同时赢得成本和准确率：准确率跨度 21-54%，backbone 选择对成本的影响与记忆系统本身一样大。
