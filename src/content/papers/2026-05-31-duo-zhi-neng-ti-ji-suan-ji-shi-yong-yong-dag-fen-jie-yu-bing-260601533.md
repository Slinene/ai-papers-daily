---
title: Multi-Agent Computer Use
title_zh: 多智能体计算机使用：用 DAG 分解与并行执行提升长程 GUI 任务
authors:
- Jing Yu Koh
- Ruslan Salakhutdinov
- Daniel Fried
affiliations:
- Carnegie Mellon University
arxiv_id: '2606.01533'
url: https://arxiv.org/abs/2606.01533
pdf_url: https://arxiv.org/pdf/2606.01533
published: '2026-05-31'
collected: '2026-06-02'
category: MultiAgent
direction: Multi-Agent 计算机使用 · DAG 任务分解
tags:
- multi-agent
- computer-use
- task-decomposition
- DAG
- parallel-execution
- test-time-scaling
one_liner: 提出多智能体计算机使用框架 MACU，通过 DAG 子任务分解、并行子代理和持续重规划，在桌面和网页导航基准上大幅超越串行单一代理
practical_value: '- **借鉴 DAG 分解与重规划范式**：对电商自动化任务（如多源比价、竞品监控、跨店铺信息收集）可构建 manager-worker
  架构，用 LLM 将复杂任务拆成有向无环图，根据中间结果动态增减/重写节点，避免单一串行 Agent 陷入死胡同。

  - **利用并行子 Agent 加速长周期任务**：对需要同时查询多个商品页、不同平台价格的任务，可派发同类 GUI 子 Agent 并行执行，收集结果后由 manager
  汇总，显著降低端到端耗时（论文中 Odysseys 任务墙钟时间减少约 1.5 倍）。

  - **部分可观测状态管理技巧**：通过虚拟机快照、文件系统 diff 和截图传递保留关键中间状态，解决 web/GUI 环境中下游子任务无法重新观测状态的难题，可直接用于需要跨页面保持登录态、购物车状态的电商场景。

  - **推理预算灵活分配**：发现多智能体系统的成功率和行动数呈更好的 scaling 趋势，在复杂任务上允许更多并行/重试能解锁串行 Agent 无法解决的任务，可指导电商自动化系统的资源调度策略。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：当前计算机使用 Agent 大多以单一串行方式运行，难以处理需要分解、并行探索和基于新信息动态调整的长程复杂任务。MACU 旨在用多智能体协作弥补这一缺陷，直接应对计算机使用特有的部分可观测性挑战。

**方法关键点**：
- **Manager–Worker 架构**：一个 manager LLM 负责将用户任务分解为有向无环图（DAG）的子任务，并统一调度同构的 CUA 子 Agent 在隔离虚拟机中并行执行。
- **持续重规划**：每当子 Agent 完成或发现新信息，manager 可修改 DAG（增删节点、改变依赖、取消运行中任务），使计划随观测动态演进，而非固定初始规划。
- **状态传递**：通过文件系统 diff、截图存档、VM 快照等机制，将上游子 Agent 获得的信息传递给下游，克服部分可观测性。
- **黑盒子 Agent 复用**：子 Agent 只需是标准 ReAct 循环的 GUI 操作模型，manager 不依赖模型内部细节，因此可无缝升级为更强的 CUA 模型。

**关键实验**：在 OSWorld（桌面）、Online-Mind2Web、WebTailBench-v2、Odysseys（长程网页）四个基准上，以 Qwen3.6-27B 为子 Agent、Claude Opus 4.6 为 manager，MACU 成功率的绝对提升分别为 +4.7%、+3.4%、+8.7%、+25.5%；Odysseys 中位墙钟时间减少约 1.5 倍。随子 Agent 总步数增加，MACU 与单 Agent 的成功率差距拉大，展现出更优的推理预算 scaling 特性。消融表明连续重规划是关键，并行度从 1 增至 4 可带来 3.2 倍理论加速。

**值得记住的一句话**：多智能体计算机使用在“可分解、需并行信息搜集”的任务上优势巨大，核心在于用 DAG 重规划而非一次性计划，让系统随新信息不断修正执行路径。
