---
title: 'Switch-SWE: Do Coding Agents Hold Focus When Switching Between Unfinished
  Tasks?'
title_zh: Switch-SWE：编码代理在未完成任务间切换时能否保持专注？
authors:
- Shuochen Chang
- Qianli Ma
- Yibo Miao
- Qingyang Liu
- Bingjie Gao
- Haonan Zhao
- Siyu Sun
- Yulin Sun
- Han Zhao
- Jiangtong Li
affiliations:
- Shanghai Jiao Tong University
- Tongji University
arxiv_id: '2611.02017'
url: https://arxiv.org/abs/2611.02017
pdf_url: https://arxiv.org/pdf/2611.02017
published: '2026-10-31'
collected: '2026-11-05'
category: Agent
direction: Coding Agent 任务切换评测与状态管理
tags:
- Coding Agents
- Task Switching
- Context Management
- Benchmark
- State Summarization
one_liner: 构建交错未完成任务的编码 Agent 评测，发现切换使解决率平均下降 11.5 个百分点，并提出上下文管理模块提升恢复能力
practical_value: '- 多意图会话管理：电商客服/导购 Agent 常在同一会话切换商品咨询、订单、推荐等未完成任务，可借鉴 task-state
  summary + relevant history selection，在切回旧意图时先恢复状态，避免重复提问和需求混淆。

  - 上下文工程：用“任务相关历史选择 + 简洁状态摘要”代替全量记忆，能降低多轮 Agent 的 prompt/KV cache 压力，同时提升旧任务恢复准确率；类似
  RAG 的 memory 模块可直接复用。

  - 评测指标：引入 matched uninterrupted vs. switched sessions，只打最终任务，把“切换损耗”独立量化；推荐/Agent
  评测可增加交错意图场景，而不是只测单任务成功率。

  - 调度与 checkout：为每个未完成任务维护持久状态/checkout，执行其它任务后通过摘要恢复；适合推荐 Agent 的多任务调度（如商品补货提醒+用户退换货+猜你喜欢）。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：真实软件开发中一个会话经常交错多个未完成任务，而现有仓库级评测只测单 issue→patch，不能反映 Agent 在切换到其它任务后的恢复能力。

**方法**：构造 Switch-SWE，从 19 个 Python 仓库的 issue、PR、review 历史重建 200 个焦点任务，形成 400 个配对会话： uninterrupted 与 switched。Switched 会插入同仓库其它未完成任务的有序阶段；每个任务有持久 checkout，且只对最终焦点 patch 打分。

**结果**：7 个 coding agents 在交错任务下，焦点任务解决率平均下降 11.5 个百分点（6.0–15.0）。轨迹分析显示跨任务需求混淆和任务状态丢失是主要恢复行为。提出的 plug-in 上下文管理模块通过选择任务相关历史并维护简洁状态摘要，在 OpenCode 上带来 5.5–15.5 个百分点提升。
