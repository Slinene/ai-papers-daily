---
title: 'Compress What You See, Not What You Say: Anchored Context Distillation for
  Latent-Observation Software Engineering Agents'
title_zh: 压缩所见而非所说：面向隐式观测软件工程 Agent 的锚定上下文蒸馏
authors:
- Zhensheng Zou
- Guoqing Wang
- Dan Hao
affiliations:
- Peking University
arxiv_id: '2609.31430'
url: https://arxiv.org/abs/2609.31430
pdf_url: https://arxiv.org/pdf/2609.31430
published: '2026-09-25'
collected: '2026-09-28'
category: Agent
direction: Agent 上下文压缩 · 软 token 蒸馏
tags:
- Context Compression
- Soft Tokens
- Agent Distillation
- LOHA
- ACD
- SWE-bench
one_liner: LOHA 布局与 ACD 训练法将长工具观测压缩为软 token，在 SWE-bench 上降低 43-57% 上下文且性能损失较小
practical_value: '- 在电商/推荐 Agent 中，工具返回的商品列表、搜索结果、用户行为日志等长文本可压缩为软 token，保留最近 K 条原文供模型精确引用（如商品
  ID、价格），可显著降低上下文长度，提升并发吞吐。

  - 采用“锚定蒸馏”思路：在压缩上下文训练时，加入普通文本输入的对齐损失，避免模型在压缩后行为漂移，保持排序/推荐效果稳定。

  - 上下文窗口有限（如 32K）时，压缩历史比截断更好：论文中同一模型在受限窗口下，压缩版解决率 21.1% vs 全文本 11.1%，说明历史信息压缩比简单丢弃更有效。

  - 权衡压缩比与任务性能：K 越大性能越好但压缩率低，需根据业务对延迟和精度要求调节 K；对于需要精确匹配的场景（如商品 ID、用户 ID）保留最近观测很有必要。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**  
软件工程 Agent 中工具观测占上下文 69%，长交互历史导致高成本。现有压缩会丢弃动作关键信息，软 token 适配又可能改变原始行为。需要既降上下文又保行为。

**方法关键点**  
提出 LOHA 布局：将较老的工具观测压缩为软 token，保留 Agent 自身回合和最近 K 条观测原文，实现历史信息紧凑、近期内容精确。训练上采用 ACD：将基座模型全文本预测蒸馏到潜伏视图，同时在普通文本输入上锚定行为，约束漂移。

**关键结果**  
SWE-bench Verified 上，K=3 使 Qwen3-4B 上下文减少 43%，SWE-Master-4B-RL 减少 57%；解决率分别为 12.1% 和 21.8%，未压缩基座为 14.5% 和 27.5%。K=8 时单次 recency sweep 达到 14.4% 和 23.0%。在 32K token 限制下，Qwen3 K=3 在 199 实例子集解决 21.1%，全文本为 11.1%。并发单 GPU 服务吞吐是全文本的 1.9 倍。
