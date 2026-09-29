---
title: 'PEAR: Progressive Evidence-Based AutoResearch for Industrial Search Systems'
title_zh: PEAR：面向工业搜索系统的渐进式证据驱动自动研究框架
authors:
- Yifan Wang
- Shipeng Zhu
- Fei Xiong
- Yuqin Yang
- Yonghui Huang
- Kunyao Wu
- Yue Wang
- Weichao Meng
- Yu Gong
affiliations:
- Global E-Commerce Agentic Search Team
arxiv_id: '2609.35031'
url: https://arxiv.org/abs/2609.35031
pdf_url: https://arxiv.org/pdf/2609.35031
published: '2026-09-28'
collected: '2026-09-29'
category: Agent
direction: Agent 驱动的搜索策略自动优化
tags:
- AutoResearch
- LLM Agent
- Search Optimization
- Confidence Gating
- A-B Testing
- Industrial Search
one_liner: 提出 PEAR 框架，以证据驱动研究状态和置信门控多级验证阶梯，在电商搜索中显著提升订单指标
practical_value: '- **多级验证阶梯 + 统一置信区间晋升规则**：把候选评估拆成 Offline Replay / Shadow-Traffic
  / Rapid Online / Decision-Grade 四级，每级都输出效应量和置信区间，只有 CI 下界>0 才 PROMOTE，CI 包含 0 保留，CI
  上界<0 停止。这个规则能避免在非平稳电商流量下用单点分数“keep-if-better”导致的瞬时增益误判，可直接复用到排序策略参数、召回权重、重排规则的自动化搜索。

  - **独立研究状态 + 上下文证据积累**：每个策略任务维护独立的假设、候选空间、证据记录，通过 Plan–Execute–Evaluate–Update 循环持续修订假设。在电商场景中，同一策略在不同时间、不同流量组成下效果可能完全不同，记录实验上下文并让
  Agent 基于 CI 和假设得分（Support - Refute）做候选生成，比单纯保留历史最优更可靠。

  - **代理指标选择要优先对齐订单等业务目标**：论文发现代理模型对订单的聚合相对误差最小（-3.49%），点击（-16.02%）和 GMV（-18.23%）误差较大。在构建
  Agent 自动化优化链路时，若要用代理模型做低层筛选，应优先选择预测误差小、与最终业务指标对齐的代理信号，而不是盲目用 CTR。

  - **低层广筛 + 高层精评，严格控制在线实验成本**：L2 阶段的 promotion rate 只有 1.5%~7.14%，意味着大部分候选在影子流量阶段就被过滤掉，只有少数进入真实在线实验。工程上可以借鉴这种漏斗式评估，把昂贵且有风险的在线
  A/B 留给统计上显著的正效应候选，同时保留大规模探索能力。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机

工业搜索系统优化通常依赖人工迭代实验，但存在两个痛点：非平稳流量下，常见的 keep-if-better 规则会把短期波动误判为真实提升，破坏知识积累；不同评估方式（离线代理、影子流量、在线实验）成本、对齐度、统计可靠性差异巨大，缺乏统一的晋升标准。AutoResearch 虽然能用 LLM Agent 自动做实验，但如何在上下文变化和异构证据下可靠地筛选候选、更新假设，仍是一个开放问题。

## 方法关键点

PEAR 由两部分组成：

- **Evidence-driven AutoResearch**：每个策略任务维护独立研究状态，包含系统上下文、当前假设、候选干预空间和累积证据。状态通过 Plan–Execute–Evaluate–Update 循环演进。Agent 在生成候选时结合 Bayesian-optimization-inspired 推理，平衡对已支持区域的精炼与对未知区域的探索；评估后，证据按实验上下文解释，支持、反驳或中立地区分假设，并据此修订假设和候选空间。
- **Confidence-Gated Verifier Ladder**：将评估组织为四级递增保真度：Offline Replay（L1）、Shadow-Traffic Evaluation（L2）、Rapid Online Evaluation（L3）、Decision-Grade Online Evaluation（L4）。L1/L2 使用列表级代理模型打分，L3/L4 使用真实用户在线结果。统一的晋升规则基于效应量置信区间：CI 下界 > 0 则 PROMOTE，CI 包含 0 则 RETAIN，CI 上界 < 0 则 STOP。低层低成本筛选大量候选，只有被提升的候选才进入高层在线实验，从而控制流量风险和成本。

## 关键实验

在真实电商搜索系统上部署，3 个匿名策略任务，由于数据访问限制未使用 L1，从 L2 开始。典型任务 A 优化结果密度约束，19 轮实验，L2 promotion rate 仅 1.50%，说明筛选严格。两个候选从 L2 到 L4 方向一致：候选 A 的订单代理效应 +45.88%，L3 观察订单 +15.48%，最终 Main Order/DAU +2.73%；候选 B 相应为 +61.64%、+29.76%、+2.16%。最终两个策略任务在 Decision-Grade A/B 中，Main Order/DAU 分别显著提升 2.7336% 和 3.2957%，同时 ASN、SKU Order/DAU、OPMS 等指标也显著正向。

## 最值得记住的一句话

不要用单点分数做 keep-if-better，而是用置信区间门控多级评估 + 上下文证据积累，把非平稳流量下的瞬时增益与真实改进区分开。
