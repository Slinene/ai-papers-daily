---
title: 'Agentic Transaction: Towards ACID-Compliant Agent Systems'
title_zh: ACID 合规智能体系统：语义化事务执行框架
authors:
- Zhaoyan Sun
- Xiaoxiao Wang
- Guoliang Li
affiliations:
- Tsinghua University
arxiv_id: '2608.13900'
url: https://arxiv.org/abs/2608.13900
pdf_url: https://arxiv.org/pdf/2608.13900
published: '2026-08-13'
collected: '2026-08-18'
category: Agent
direction: LLM Agent 事务化执行与可靠性增强
tags:
- Agentic Transactions
- ACID
- LLM Agents
- Data Agent
- Reliability
- Semantic Consistency
one_liner: 以语义化 ACID 事务约束 Agent 执行，在 KramaBench 上超 Claude Code 10.6 个百分点
practical_value: '- 把一次「探索→执行→验证」看作一个事务单元，commit 前用小模型做置信度分歧校验，失败即丢弃该步 workspace 与上下文；可直接用于电商/广告数据分析
  Agent 或推荐策略多步工具调用，防止中间错误污染后续决策。

  - 置信度分歧信号很便宜：用 token 平均 log-prob 估计，API 模型没有概率时挂一个本地 0.6B 模型即可；可对关键决策（过滤条件、人群圈选、代码生成）做有无证据支持下的置信度差，低于阈值触发重试。

  - 语义隔离按依赖类型分 independent/collaborative/competitive：独立子任务给 Docker 独立权限，协作任务用 branch+定时同步，竞标任务
  copy-on-write 并早停低分分支；适合多 Agent 并行做召回/排序/评估时的资源与上下文隔离。

  - 只把 validated 步骤写入 append-only workspace，再用知识图谱组织长期记忆，既减少上下文（文中 7.7k→0.7k tokens），又支持审计回滚；推荐/搜索会话
  Agent 可借鉴来做持久化状态管理。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
LLM Agent 从单轮对话走向长程自主执行，需在持续环境上完成多步推理、工具调用、代码生成和工作区修改。与数据库事务类似，它面临可靠执行、一致结果、安全并发、持久状态四类问题，但传统 ACID 假设确定性的读写和结构化状态，无法直接套用到非确定性的 LLM 推理和动态工具副作用上。因此论文提出 agentic transaction 概念，并把 ACID 重新解释为四种语义保证，构建 ACID 合规 Agent 系统。

**方法关键点**
- 语义原子性：将「探索-执行-验证」周期视为一个事务单元，只有验证通过的更新才 commit，失败则丢弃/补偿；离线构建带事务护栏的技能 hub，在线用 staged execution 保证 commit-or-retry。
- 语义一致性：提出 confidence divergence 验证，综合执行错误、决策/代码置信度分歧和 LLM 反思信号；置信度用 token 平均 log-prob 估计，API 模型缺失概率时用本地 Qwen3-0.6B 近似。
- 语义隔离：按子任务依赖关系分独立、协作、竞争三类，分别采用独立 Docker 权限、分支+定时同步、copy-on-write+早停等策略；操作级通过版本化 workspace 和乐观验证避免污染。
- 语义持久性：用事务感知记忆和 append-only workspace，只记录 validated 状态；记忆以知识图谱形式演进，并保留 provenance 和版本化 trace 支持审计与恢复。

**关键实验**
在 KramaBench（104 个任务、1,700 个真实数据文件、24 个数据源、6 个领域）上评估。ACID-Agent 使用 Qwen3.5-397B-A17B 获得 74.6 分，比 Claude Code 的 64.0 分提高 10.6 个百分点；且超过 Claude Code + GLM-5.2（74.2）。一致性方面，Environment 域三次运行得 88.9±18.6，波动明显低于 Claude Code 的 63.9±30.9。消融显示去掉失败步骤隔离后从 90.0 降至 78.3，说明隔离失败状态能带来 11.7 分增益；同域下 ACID-Agent 以 444K tokens 超过 Claude Code 三跑投票的 75.2 分/1121K tokens。

**最值得记住的一句话**
把 Agent 的一次探索-执行-验证当作事务，只提交 validated effects、用置信度分歧做验证，能显著提升长程任务的可靠性、一致性和 token 效率。
