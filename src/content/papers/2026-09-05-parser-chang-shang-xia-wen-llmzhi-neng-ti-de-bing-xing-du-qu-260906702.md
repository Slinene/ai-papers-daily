---
title: 'PARSER: Read in Parallel, Reason in Depth for Long-Context LLM Agents'
title_zh: PARSER：长上下文LLM智能体的并行读取与深度推理解耦
authors:
- Kun Li
- Zexuan Qiu
- Tianhua Zhang
- Irwin King
- Helen Meng
affiliations:
- The Chinese University of Hong Kong
arxiv_id: '2609.06702'
url: https://arxiv.org/abs/2609.06702
pdf_url: https://arxiv.org/pdf/2609.06702
published: '2026-09-05'
collected: '2026-09-11'
category: MultiAgent
direction: 长上下文多智能体并行阅读与推理
tags:
- long-context
- multi-agent
- reinforcement learning
- parallel reading
- multi-hop QA
- LLM agents
one_liner: 解耦阅读与推理，并行子代理读全文，主导代理迭代scatter-gather深度推理，长上下文QA大幅提升且延迟降低11倍
practical_value: '- 解耦阅读与推理：用多个轻量 subagent 并行读取长文档 chunk 并返回证据，lead agent 只做深度推理，可迁移到电商场景处理海量商品详情、用户评论、政策文档等长文本，避免顺序阅读延迟，适合在线服务。

  - RL 只优化 lead agent，subagents 冻结，显著降低训练成本；业务中可复用：固定检索/抽取模块，用强化学习训练策略/推理模块，如商品对比、复杂推荐解释生成。

  - 对证据位置、顺序、距离鲁棒，适用于证据分散的场景（如多个用户评价中找关键信息、跨文档商品属性对比），减少因文档顺序引起的性能波动。

  - 迭代 scatter-gather 的查询生成机制可借鉴：每一轮基于已有证据生成更深查询，逐步聚焦关键信息，可用于多轮对话式推荐或搜索 query 细化。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**
顺序记忆智能体（sequential memory agents）逐块读取长文档并维护紧凑记忆状态，将文档遍历与推理深度耦合，导致对证据位置敏感且推理延迟随文档长度线性增长。在百万级上下文的多跳QA中，直接全上下文回答准确率大幅下降（context rot），证据位置偏差严重。

**方法关键点**
PARSER 将阅读与推理解耦：一组轻量 subagents 各自绑定一个 chunk，并行读取整个文档；lead agent 负责深度推理，通过迭代 scatter-gather 轮次工作——每轮向所有 subagents 广播查询，聚合返回的证据，再基于已有发现生成更深的后续查询。所有可学习行为集中在 lead agent，用强化学习优化；subagents 保持冻结的现成模型。

**关键结果**
在 7K 到 896K tokens 的多跳 QA 上，基于 4B 骨干的 PARSER 平均超过最强顺序记忆基线 5.7 点，在 896K 时领先 12.0 点；扩展到 9B 骨干，超过 DeepSeek-V4-Pro 6.3 点。控制实验表明，PARSER 对证据位置、顺序、距离的扰动具有鲁棒性，而这些条件会引起顺序方法的大幅准确率波动；推理延迟最多降低 11 倍。
