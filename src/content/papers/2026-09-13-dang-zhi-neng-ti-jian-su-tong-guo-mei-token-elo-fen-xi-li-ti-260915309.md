---
title: 'When Agents Slow Down: Understanding LLM Agents'' Test-Time Strategies via
  Elo-per-token Analysis'
title_zh: 当智能体减速：通过每 token Elo 分析理解 LLM 智能体的测试时策略
authors:
- Kaiyuan Liu
- Qiuyang Mang
- Bo Peng
- Wenhao Chai
- Hanchen Li
- Shreyas Pimpalgaonkar
- Luke Zettlemoyer
- Alex Dimakis
- Alvin Cheung
affiliations:
- UC Berkeley
- University of Washington
- Princeton University
- Bespoke Labs
arxiv_id: '2609.15309'
url: https://arxiv.org/abs/2609.15309
pdf_url: https://arxiv.org/pdf/2609.15309
published: '2026-09-13'
collected: '2026-09-15'
category: Agent
direction: Agent 测试时计算缩放分析
tags:
- LLM Agents
- Test-time Compute
- Elo Rating
- Scaling Laws
- Bradley-Terry
- Token Efficiency
one_liner: 提出 Elo-per-token 分析量化 LLM Agent 测试时计算缩放，发现边际收益递减且拆分并行预算更优
practical_value: '- 对搜索/推荐 Agent 的多步推理或工具调用，可以用 Elo-per-token 曲线监控 token 投入的边际收益，而不是只看最终指标；在边际收益低于独立采样参考线时及时停止或调整策略。

  - 独立采样参考线是简单有效的 baseline：如果 Agent 的规划、反思、工具调用不能稳定跑赢重复采样，说明额外复杂度没有带来 token 效率，可考虑简化
  Agent 流程或增加采样并行度。

  - 利用 scaling inflection point 分配长任务预算：将总 token 预算拆成多个并行 sessions 可能比一个超长 session
  获得更高 Elo，对线上高并发 Agent 服务的请求拆分和成本控制有直接指导意义。

  - Bradley-Terry 聚合跨任务分数排序的方法可以迁移到电商多指标评估，处理不同 reward 尺度下的成对比较，适合离线评测 Agent 生成物品文案、搜索
  query 等开放任务。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM Agent 在测试时动态分配计算（修改方案、调用工具、探索替代方案、决定停止），使性能随计算量的缩放难以度量。开放任务提供连续中间反馈，适合观察长期轨迹中的进展。

**方法**：提出 Elo-per-token 分析，在每个 token budget 下追踪找到的最优解，并用 Bradley-Terry 模型将同一任务内的排序聚合为跨任务可比 Elo 评分。在 4 个通用 Agent、4 个开放基准（会话最长 100M tokens）和 3 个反馈驱动优化 harness 上应用。用独立采样作为理论参考，其 Elo 随 log compute 线性增长。

**关键结果**：Agent 初始将 token 转换为 Elo 的效率高于独立采样，但边际收益递减，最终低于参考线；最强历史人类选手在 AtCoder Heuristic Contest 上随时间超线性提升，表明 agent 减速后仍有大量提升空间。定义 scaling inflection point 为边际 Elo 增益与独立采样参考相等的 per-session budget。在 FrontierCS Polyomino Packing 上，将 100M tokens 拆成并行 sessions，比一个长 session 高 +264 Elo，比十个短 session 高 +355 Elo。
