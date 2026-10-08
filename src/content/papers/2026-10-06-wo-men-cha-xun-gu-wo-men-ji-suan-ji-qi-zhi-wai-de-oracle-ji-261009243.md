---
title: 'We Query, Therefore We Compute: On Oracle Computation beyond the Machine,
  with an Application to Agents'
title_zh: 我们查询，故我们计算：机器之外的 Oracle 计算及其在 Agent 中的应用
authors:
- Kefan Liu
- Fengning Ou
- Yelin Luo
- Jingdi Lei
affiliations:
- Institute of Computing Technology, CAS
- University of Chinese Academy of Sciences
- Nanjing University
- Institute of Automation, CAS
- Nanyang Technological University
arxiv_id: '2610.09243'
url: https://arxiv.org/abs/2610.09243
pdf_url: https://arxiv.org/pdf/2610.09243
published: '2026-10-06'
collected: '2026-10-08'
category: Agent
direction: Agent 系统抽象计算模型
tags:
- Agent
- LLM
- Oracle
- Workflow
- Operating System
- Abstract Machine
one_liner: 将 LLM 作为 Oracle 构建抽象机，统一 Workflow 和 Agent，并提出 ArchNights 操作系统实现
practical_value: '- 将 Agent 控制流与 LLM 推理分离：把业务状态机、调度和审计放在确定性代码（Priestess）中，让 LLM 只作为
  Oracle 做内容生成或决策，可显著降低系统不确定性，便于测试、回滚与灰度发布。

  - 借鉴“栈即上下文”和查询指令设计：每次查询将整个上下文栈交给 LLM 并追加结果，明确上下文边界；缓存可以基于栈内容哈希实现，重复上下文直接跳过 LLM 调用，适合推荐话术生成、商品摘要、广告文案等高频相似场景。

  - 对称破缺区分 Workflow 与 Agent：任务程序放在控制流侧是可控的工作流，放在 LLM 侧生成则是自主 Agent；业务中可混合部署，关键链路用
  Workflow 保证 SLA，探索性任务用 Agent 提升灵活性。

  - 借鉴 OS 抽象：在 Agent 平台中显式实现调度、隔离、持久化和缓存等机制，而不是每个 Agent 自建一套；ArchNights 表明可在扩展 ISA/OS
  层面承载 LLM 查询，为统一资源管理和性能边界提供参考。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：现有 Agent 系统从操作系统中零散借用调度、缓存、隔离等抽象，机制间缺乏共同基础，Workflow 与 Agent 两种形态也缺少统一视图。

方法关键点：将 LLM 视为 Oracle，扩展双栈下推自动机，增加一条指令：把一个完整栈作为查询交给 Oracle，并将回答追加到同一栈上。机器同时运行两个计算——Oracle 的计算和一个图灵完备的 Priestess 控制流。程序只追加的栈随自回归生成增长，模拟 Agent 上下文。通过两个对称破缺 S（存储）与 T（转换），Priestess 程序成为 Oracle 运行程序的操作系统，并由此产生 Agent 与 Workflow 两种任务程序放置方式。对内部自回归 Oracle，在一定条件下两个计算在每次回答结束时同步，该同步用于建模缓存与分析调度。无法保证对任意 Oracle 固定哪些内容跨计算边界，但可固定边界本身。

结果：构造 V 将该抽象机适配到冯·诺依曼计算机。提出 ArchNights——一种扩展 RISC-V ISA 与 Linux 风格操作系统，原生实现该机器。ArchNights-SE 在 gem5 上作为计算机系统运行，当接入 LLM 作为 Oracle 时成为 Agent 系统，并将开源。未来 Agent 系统可像计算机系统一样被设计，共享不变量与边界条件。
