---
title: 'RAFT: A Stateful Retrieval-Augmented Framework for Troubleshooting Agents'
title_zh: RAFT：面向故障排查 Agent 的有状态检索增强框架
authors:
- Mingxuan Zhang
- Xiaowen Wang
- Anupma Sharan
- Zhengyi Chen
- Chenyu Diana Zhang
- Shanshan Yang
- Chittibabu Pacharu
affiliations:
- Microsoft
arxiv_id: '2609.20754'
url: https://arxiv.org/abs/2609.20754
pdf_url: https://arxiv.org/pdf/2609.20754
published: '2026-09-17'
collected: '2026-09-18'
category: RAG
direction: 有状态 RAG 检索层用于故障排查 Agent
tags:
- RAG
- Stateful Retrieval
- Troubleshooting Agent
- Timeline
- Case Retrieval
- Synthetic Benchmark
one_liner: 将历史案例建模为有向时间线条目链，在条目级检索匹配中间状态，显著提升案例命中率
practical_value: '- 将长流程业务数据（如售后工单、客服会话、广告异常处理）建模为有向时间链条目，用条目级 embedding 检索，能匹配中间状态而非仅整篇相似度，提升问题定位精度。

  - 检索时返回锚定在匹配状态的父案例轨迹，而不是完整长文档，可减少无关上下文噪声，降低后续 LLM 推理成本与干扰。

  - 利用可配置相似性表示构建案例级图，可连接相似案例用于图检索或辅助导航，适合构建案例库的推荐和聚类功能。

  - 只评估检索层（Case Hit）而非整个 Agent 系统，无需生产部署即可快速迭代检索策略；在业务中可先离线验证检索质量，再集成到在线 Agent。

  - 合成数据结合真实标签数据（如 Jira duplicate labels）验证迁移性，对有标签的真实业务数据可低成本验证方法有效性。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：企业客户支持中的故障排查 Agent 需要从历史案例中检索可操作指导，但现有 RAG 将案例视为静态文档，忽略了故障排查的多阶段、有状态特性，导致检索不到中间状态匹配的案例。

**方法关键点**：RAFT 将每个已关闭历史案例抽象为有向时间线条目链，在条目级别进行检索，匹配活跃案例的中间状态；返回锚定在匹配状态的父案例轨迹，而非整篇文档。此外，可选的案例级图通过可配置相似性表示连接相关案例。评估只针对检索层，无需部署完整 Agent 系统。

**关键结果**：在基于 Microsoft Learn Windows Server 文档构建的合成基准上，RAFT 在案例进展的每个阶段均提升 Case Hit，相对最强基线（vanilla RAG 与 GraphRAG）有统计显著增益；在 Apache Jira 真实数据上提供方向性证据，表明优势可迁移到真实案例历史。论文发布基准、实现与 Jira 评估集。
