---
title: Why Pay for Long Reasoning When Rewrite Do Trick? Causal Effects of Reasoning
  History Compaction on Future Generation and Agent Cost
title_zh: 为何为长推理付费？重写历史压缩对后续生成与Agent成本的因果效应
authors:
- Anton Hristov
affiliations:
- Technological School Electronic Systems
arxiv_id: '2611.03852'
url: https://arxiv.org/abs/2611.03852
pdf_url: https://arxiv.org/pdf/2611.03852
published: '2026-11-01'
collected: '2026-11-08'
category: Reasoning
direction: 推理历史压缩 · Agent成本优化
tags:
- reasoning compaction
- LLM inference cost
- agent efficiency
- history rewriting
- causal effect
- token reduction
one_liner: 将先前推理改写为紧凑状态记录可缩短后续推理并降低Agent成本，但效果依赖模型与压缩器
practical_value: '- 在 Agent 工作流中，工具调用返回结果前将冗长推理历史重写为紧凑状态记录（保留关键事实、约束、候选方案），可降低后续推理
  token 消耗，适合多步工具调用场景（如商品信息检索、库存查询）。

  - 压缩策略需针对目标模型和压缩器做离线评估：对比原始历史与压缩历史的任务完成率和 token 成本，选择模型特定的压缩格式/阈值，避免无脑压缩导致任务质量下降。

  - 编码类 Agent 中，共享候选方案后压缩历史可减少重复验证；迁移到电商多轮对话，可将已确认的商品属性、用户约束压缩为状态记录，减少模型反复询问或重复列举。

  - 工程实现上可加一个轻量历史重写模块，在 pending tool results 之前触发，用规则或小模型进行压缩，而不是等历史无限积累。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：长推理显著提升模型解决复杂问题的能力，但成本高昂。数据显示 GLM 5.2 推理 token 占生成总量的 84.9%，Claude Fable 5 占 75.1%，DeepSeek V4 Pro 推理输出占 API 成本的 53.4%。Agent 反复处理早期 scratchpad 也加重开销。高效推理应在保留有用分析的同时减少重复和低价值 token。

**方法关键点**：针对开源模型，在不 retraining 的前提下，干预时机选择在 pending tool results 揭示之前——将先前的完整推理重写为紧凑状态记录，然后对比原始历史与压缩历史下的 continuation。该方法直接改变模型自身早期思考的形式，观察后续生成是否更简洁。

**关键结果**：多数测试模型接受压缩历史后，后续推理显著缩短；编码案例中，共享候选解决方案后压缩历史减少了重复验证；软件 Agent 部署中，压缩能降低总花费，但任务质量和包含重写的时间取决于目标模型与压缩器。结论指出推理历史是减少未来推理 token 的一个可操作杠杆，应针对具体模型设计压缩策略，并同时评估效率与能力保留。
