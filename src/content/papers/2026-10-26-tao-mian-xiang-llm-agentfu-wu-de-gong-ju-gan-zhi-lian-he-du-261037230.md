---
title: 'TAO: Tool-Aware Joint Scheduling for LLM-Based Agentic Serving'
title_zh: TAO：面向LLM Agent服务的工具感知联合调度框架
authors:
- Shuhuai Li
- Shengdong Ye
- Dongdong Ge
- Yinyu Ye
- Jianghao Lin
affiliations:
- Shanghai Jiao Tong University
- Stanford University
arxiv_id: '2610.37230'
url: https://arxiv.org/abs/2610.37230
pdf_url: https://arxiv.org/pdf/2610.37230
published: '2026-10-26'
collected: '2026-10-29'
category: Agent
direction: Agent 服务调度优化
tags:
- Agentic Serving
- Scheduling
- KV Cache
- TTFT
- Dynamic Programming
- Tool-Aware
one_liner: 提出工具感知联合调度框架TAO，融合工具就绪度、缓存信用与token占用进行动态规划调度，显著降低延迟和TTFT
practical_value: '- 在 LLM Agent 服务中，工具调用（如商品检索、数据库查询、API 调用）会使 GPU 推理可中断，调度时需将「工具返回就绪时间」纳入准入/放置决策，避免
  GPU 空转和资源浪费。

  - 借鉴 TAO 的 value interface：组合「近期工具就绪度 + 节点级缓存信用（时间衰减）+ token footprint」来评估一个 session
  的调度价值，而不是只看队列长度或显存。

  - 动态规划联合选择等待中的 sessions 并放置到 GPU 节点，在容量约束下最大化整体收益，比启发式 admission/placement 更优；可实现在线调度器，在
  GPU 空闲或工具返回事件时触发。

  - 如果推荐/搜索 Agent 涉及多步工具调用（如商品召回、属性查询、库存检查），可以对工具返回时间做预测或标记，并结合 prefix cache 命中（例如共享
  system prompt 或工具 schema）优先调度相似 session 以提高 decode throughput。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有 LLM Agent 服务系统在 Clustered-GPUs with Distributed-CPUs（CGDC）场景下，GPU 推理与外部 CPU 工具交替执行，但调度普遍忽视「工具返回就绪时间」，且采用启发式准入/放置策略，导致资源浪费和次优调度。

**方法关键点**：TAO 定义 value interface，将三个信号纳入调度评估：1) near-term tool readiness——预测 session 下一次工具调用返回的临近程度；2) node-specific cache credit——考虑节点缓存命中收益，并引入时间衰减；3) token footprint——session 的 token 占用规模。基于该 value interface，TAO 用动态规划在 GPU 容量约束下联合完成等待 session 的准入选择和节点放置，替代传统 evaluate-then-decide 的分离启发式。

**关键结果**：在 12 个 model–workload–concurrency 设置下，相对各指标最优的 SOTA baseline，TAO 最高将 latency 降低 26.8%，mean TTFT 降低 36.3%，decode throughput 提升 29.5%。
