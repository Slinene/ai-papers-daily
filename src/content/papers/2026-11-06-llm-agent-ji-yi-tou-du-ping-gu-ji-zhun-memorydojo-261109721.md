---
title: 'MemoryDojo: Benchmarking Poisoning Through LLM Agent Memory'
title_zh: LLM Agent 记忆投毒评估基准 MemoryDojo
authors:
- David H. Yang
- Blake Bullwinkel
- Amanda Minnich
- Mohammad Mohammadi Amiri
- Giorgio Severi
affiliations:
- Rensselaer Polytechnic Institute
- Microsoft
arxiv_id: '2611.09721'
url: https://arxiv.org/abs/2611.09721
pdf_url: https://arxiv.org/pdf/2611.09721
published: '2026-11-06'
collected: '2026-11-09'
category: Agent
direction: LLM Agent 记忆安全基准与投毒评估
tags:
- LLM agents
- memory poisoning
- prompt injection
- benchmark
- agentic memory
- security
one_liner: 提出 MemoryDojo 基准，量化投毒信息在五种 LLM 记忆系统中的传播与下游影响，并给出记忆感知投毒优化
practical_value: '- 在电商/搜索推荐 Agent 的记忆模块中，外部商品描述、用户评论、广告文案都可能成为投毒载体；写入记忆前需做来源可信度评分与内容净化，阻断恶意指令跨会话持久化。

  - 为记忆管道增加元数据（来源、时间戳、是否来自外部）并支持检索时降权/隔离高风险来源，可降低被投毒信息复用的概率。

  - 借鉴 MemoryDojo 的评测思路，搭建多会话长程轨迹测试集，对不同记忆架构（向量库、摘要、图存储等）做投毒敏感性评估，把安全性纳入记忆系统选型指标。

  - 对已上线 Agent 系统，可周期性注入模拟投毒样本，监测后续行为偏差，作为安全回归测试的一部分。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM Agent 依靠记忆系统压缩上下文、跨会话保留信息，显著提升长程任务能力。但记忆成为新的攻击面：外部环境中的恶意指令可在一次会话中被存储，之后被检索并驱动危险动作。不同记忆系统在存储、检索、压缩方式上的差异会导致投毒影响差异很大，但缺少统一量化基准。

**方法**：推出 MemoryDojo，一个可扩展的评测基准，包含 155 条多会话长程轨迹，覆盖四个领域，支持五种记忆系统。基准追踪被投毒信息在记忆中的完整生命周期（写入→存储→检索→执行），并测量其对后续 Agent 行为的影响。同时提出 memory-aware 投毒优化过程，针对不同记忆架构调整投毒策略以提升攻击效果。

**关键结果**：所有被测记忆系统均易受记忆投毒影响，但下游行为偏离程度差异显著；经 memory-aware 优化后投毒效能进一步提升，不同架构之间的脆弱性差异被放大。基准和攻击方法为后续研究防御与缓解提供了可复现的测试平台。
