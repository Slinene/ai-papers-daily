---
title: 'Root-Cause Attribution Is a Search Problem: Continual Search for Long-Horizon
  Agent Failures'
title_zh: 根因归因是一个搜索问题：面向长时程 Agent 失败的持续搜索
authors:
- Harsh Raj
- David Lee
- Anas Mahmoud
- Renxiong Wang
- Razvan-Gabriel Dumitru
- Chenguang Wang
- Tong Zhao
- Yunzhong He
- Darvin Yi
- Vipul Gupta
affiliations:
- Scale AI
arxiv_id: '2609.13463'
url: https://arxiv.org/abs/2609.13463
pdf_url: https://arxiv.org/pdf/2609.13463
published: '2026-09-10'
collected: '2026-09-17'
category: Agent
direction: Agent 失败根因归因与持续搜索
tags:
- Root-Cause Attribution
- LLM Judge
- Continual Search
- Long-Horizon Agents
- MegaRCA-Mix
- F1
one_liner: 提出 Continual Search 迭代框架，通过多轮唤醒 LLM 法官持续搜索未解决证据，显著提升长轨迹 Agent 失败根因归因 F1
practical_value: '- 诊断长流程 Agent/推荐链路失败时，不要依赖一次性 LLM 判断；把 RCA 改造成多轮搜索，每轮强制模型找出“尚未解释的证据”，直到证据链闭环。

  - 与其堆大模型，不如把搜索过程做扎实：论文显示同模型家族内低阶模型配合 Continual Search 可反超高阶模型，成本可控且效果更好。

  - 业务上可用于电商 Agent 执行日志、广告投放链路、搜索推荐多阶段 pipeline 的故障归因：失败信号通常稀疏且跨步骤，需要主动回溯而不是只看最后一步。

  - 建议构建类似 MegaRCA-Mix 的长时程、执行密集型测试集，用真实人工标注的失败 trial 评估诊断能力，避免只测短轨迹造成虚假达标。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：AI Agent 在长时程任务中产生海量执行日志，失败根因归因是可靠性关键。现有自动化 RCA 主要靠 LLM 一次性判断，但长轨迹里相关证据稀疏、跨距离分布且与可见失败脱节。一次性法官往往过早锁定一个看似合理的诊断，遗漏后续关键证据。

方法：提出 Continual Search，一个迭代框架。它在多轮中不断“催促”法官继续搜索未解决的诊断证据，而不是仅做一次判断。论文还发现现有基准缺乏大规模执行轨迹，于是构建 MegaRCA-Mix：50 条人工标注的长时程、执行密集型失败 trial。

结果：在四个现有 RCA 基准和 MegaRCA-Mix 上，Continual Search 持续提升归因性能。例如在 MegaRCA-Mix 上，GPT-5.5 的 F1 从 0.349 提升到 0.498，提升超过 40%。更有趣的是，同模型家族内低阶模型配合该框架可以反超高阶模型，说明有效搜索比单纯扩大模型规模更重要。
