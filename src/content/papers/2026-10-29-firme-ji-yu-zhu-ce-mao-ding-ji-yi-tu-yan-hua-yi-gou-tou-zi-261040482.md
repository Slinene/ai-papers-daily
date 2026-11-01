---
title: 'FIRME: Registry-Anchored Memory Graphs for Evolving, Heterogeneous Investor
  Knowledge'
title_zh: FIRME：基于注册锚定记忆图演化异构投资者知识
authors:
- Yunbai Zhang
- Yunyi Gao
- Han-Tai Shiao
affiliations:
- The Vanguard
arxiv_id: '2610.40482'
url: https://arxiv.org/abs/2610.40482
pdf_url: https://arxiv.org/pdf/2610.40482
published: '2026-10-29'
collected: '2026-11-01'
category: Agent
direction: Agent 持久记忆 · 实体对齐知识图谱
tags:
- Knowledge Graph
- Memory
- Entity Resolution
- Alias
- Provenance
- Financial AI
one_liner: 用注册锚定记忆图解决知识图谱中同一关系表面形式不同导致的历史碎片化问题，提升跨期实体对齐与证据积累
practical_value: '- 可借鉴 registry-anchored 的实体管理思路：在电商/推荐场景中，同一商品、用户、话题常以不同表面形式出现在搜索、评论、会话、交易等来源，建立
  canonical identity + persistent alias 的注册表能避免关系历史碎片化，让跨渠道、跨会话证据持续积累。

  - deterministic updates 对强化、休眠、再激活的总结方法可以迁移到用户兴趣或商品热度的时间衰减模型：不依赖重训 embedding，而是在图谱层维护带时间戳的聚合状态，降低工程复杂度。

  - rule-based fusion 结合固定 ontology 的做法可作为轻量级替代：在没有大量标注的情况下，把非结构化文本（如客服对话、商品评论）与结构化信号（如购买、现金流）对齐，适合快速搭建可解释的领域知识层。

  - 关注 provenance 与 round-trip 诊断：在 Agent 或 RAG 系统中输出必须可溯源，FIRME 保留 source/time/context
  并提供提取忠实度检验，这对线上推荐解释、风控审计有直接参考价值。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

动机：金融 AI 工作流复用投资者知识时，需要跨来源、跨时期整合观察，同时保留身份和溯源。知识图谱中同一关系常出现不同表面形式，导致关系历史碎片化，证据无法累积。

方法关键点：FIRME 采用 registry-anchored memory graph。期间内，基于规则的融合将投资者电话会讨论与组合现金流信号关联，可直接连接或经固定产品-主题本体连接；跨期间，规范身份和持久别名将反复出现的观察指向同一关系历史；确定性更新总结强化、休眠与再激活，并保留来源、时间和上下文。

关键结果：在专有投资者电话会/现金流记录及 S&P 500 财报电话会文本上，与缺少别名记忆的历史 registry 相比，在固定裁判和回退审查协议下，四个数据集-后端设置的最终期正确匹配率提升 7.8–12.1 个百分点；盲审显示正确匹配率提升 9.0–16.5 点，重新挂接召回提升 22.5–29.0 点，四个样本合并精度均更高。另 293/300 输出来自完整的期间内融合具有有效证据路径。
