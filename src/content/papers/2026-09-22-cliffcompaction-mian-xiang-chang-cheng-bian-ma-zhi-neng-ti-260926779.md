---
title: 'CliffCompaction: Cost-Efficient Compaction for Long-Horizon Coding Agents'
title_zh: CliffCompaction：面向长程编码智能体的高成本效率上下文压缩
authors:
- Trang Nguyen
- Eulrang Cho
- Bingqing Chen
- Tim Dettmers
affiliations:
- Carnegie Mellon University
- Bosch Center for AI
arxiv_id: '2609.26779'
url: https://arxiv.org/abs/2609.26779
pdf_url: https://arxiv.org/pdf/2609.26779
published: '2026-09-22'
collected: '2026-09-23'
category: Agent
direction: Agent 长程上下文压缩与成本优化
tags:
- Context Compaction
- Long-Horizon Agents
- Test-Time Scaling
- Coding Agents
- Cost Efficiency
one_liner: 一种只截断/丢弃、不重写原文的自动压缩法，在受限上下文下最多降低50%成本并保持或提升编码Agent性能
practical_value: '- 在需要长会话/多轮 Agent 的场景（如导购、客服、推荐解释）中，上下文压缩优先采用“只截断/丢弃原始内容、不重写”，避免摘要改写引入信息偏差，可显著降低
  API 成本且保持质量。

  - 强制“绝不压缩已压缩内容”，每轮压缩都基于原始会话/文档，防止跨轮次的上下文漂移累积，适合超过百万 token 的持续学习/多轮交互。

  - 将压缩逻辑做成 API proxy，不改动现有 agent scaffold 即可接入 Claude Code、Codex 等，业务侧可快速对现有推荐/广告
  Agent 工作流做成本优化和 A/B 测试。

  - 用相同预算做 test-time scaling（如并行采样多个推荐解释/策略）时，压缩带来的 per-rollout 节省让更多采样成为可能，可能以更低成本获得性能提升。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

动机：智能体处理复杂问题常需数百万 token 上下文，受限于上下文窗口，必须跨会话压缩；但现有摘要/重写式压缩容易丢失关键信息、引入漂移，限制长程任务性能与成本效率。

方法关键点：CliffCompaction 是一种自动压缩技术，核心原则是保持压缩后信息忠实——只对原始内容进行截断或丢弃，绝不改写或重组。每次压缩过程直接作用于原始内容，并丢弃上一轮压缩结果，避免“压缩的压缩”导致上下文漂移累积。该方法不依赖特定框架，通过 API proxy 实现，可配合 Claude Code、Codex 等使用。

关键结果：在受限上下文下，CliffCompaction 最多降低 50% 成本，并在 Terminal-Bench 上保持或提升性能；在 test-time scaling 中，其 per-rollout 节省使性能-成本权衡更高效，以不到两次完整上下文运行的成本在 Terminal-Bench 上提升超过 10 个百分点。并行 test-time scaling 下，Kimi K2.6 匹配 Opus 4.7，并以更低成本超过 Opus 4.6 与 GPT-5.3 Codex。在 KernelBench 上，经过 200 步达到 CUDA kernel 加速 2.23×，400 步达到 3.58×，超越专用搜索算法和训练过的智能体，尽管它只是通用压缩技术。
