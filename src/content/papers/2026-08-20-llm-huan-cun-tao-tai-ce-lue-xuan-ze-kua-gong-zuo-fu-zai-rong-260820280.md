---
title: Which Eviction Policy Should an LLM Cache Use? A Systematic Study Across Workloads,
  Capacities, and Encoders
title_zh: LLM 缓存淘汰策略选择：跨工作负载、容量与编码器的系统研究
authors:
- Yash Kulkarni
- Shubham Harkare
- Arvind Suresh Yogesh Babu
affiliations:
- University of Michigan
arxiv_id: '2608.20280'
url: https://arxiv.org/abs/2608.20280
pdf_url: https://arxiv.org/pdf/2608.20280
published: '2026-08-20'
collected: '2026-08-22'
category: LLM
direction: LLM 语义缓存淘汰策略评估
tags:
- semantic caching
- cache eviction
- LLM serving
- LFU
- quality-adjusted hit rate
one_liner: 系统比较多种语义缓存淘汰策略，发现 LFU 为最强简单默认，且需先验证答案有效性
practical_value: '- 在业务中部署 LLM 语义缓存时，淘汰策略无需复杂化：LFU 在 18 种设置下几乎总是最优或接近最优，实现简单且省资源；避免引入几何感知复杂策略，因为精确查找下新插入条目在命中半径内无邻居，难以获得额外信号。

  - 缓存命中质量是更大的风险：在典型阈值下，原始命中率 51–60% 中只有 2.1–3.9% 的命中答案可替代，质量调整后命中率仅 1.1–2.2%。上线前必须用
  LLM-as-judge 或人工审计验证缓存命中的可替代性，不能只看 embedding 距离。

  - 阈值需按编码器单独标定：跨编码器研究显示阈值不可迁移；更换 embedding 模型后必须重新设定距离阈值，否则可能缓存大量无效响应。

  - 对于小容量缓存，使用精确搜索（如暴力扫描）而非 ANN，以保留准确的邻居结构用于淘汰决策；同时关注 LFU 与 FIFO 在紧容量下的差异可达 8 个百分点，容量越紧越应该选简单有效的
  LFU。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

动机：LLM 语义缓存通过重用嵌入邻近的响应降低推理成本，但各种淘汰策略缺乏统一协议比较，选择困难。

方法：在 CLEVER 框架下，对比 FIFO、LRU、LFU、ARC、GDSF、流式 SISO 和语义冗余策略，覆盖 3 个有序去重 query 语料、3 种缓存容量、2 种编码器共 18 个设置；同时用 LLM-as-judge 审计命中质量，并进行跨编码器阈值迁移实验。

结果：没有任何策略能比 LFU 提升超过 0.041 个百分点；FIFO 和流式 SISO 在紧容量下落后 LFU 最高 8.67 和 8.55 个百分点。条件填充分析显示，精确查找且 miss 时插入的新条目在命中半径内无邻居，几何感知淘汰规则缺乏冗余信号。质量审计更严重：MiniLM 中位阈值下，LMSYS 和 QQP 命中仅 2.1–3.9% 被判定为答案可替代，质量调整命中率从 51–60% 降至 1.1–2.2%，且阈值在不同编码器间不可迁移。

结论：LFU 是当前协议下最强的简单默认；部署时应先通过答案有效性审计确定阈值，再用精确搜索测试微小策略差异。
