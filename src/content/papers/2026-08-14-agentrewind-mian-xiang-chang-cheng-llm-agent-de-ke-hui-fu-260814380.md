---
title: 'AgentRewind: Recoverable Execution for Long-Horizon LLM Agents'
title_zh: AgentRewind：面向长程 LLM Agent 的可恢复执行框架
authors:
- Yu Zhuang
- Kefei Chen
- Yitong Duan
- Shuxin Zheng
- Jian Li
- Xu-Yao Zhang
affiliations:
- University of Chinese Academy of Sciences
- IIIS, Tsinghua University
- Zhongguancun Academy
- Institute of Automation, Chinese Academy of Sciences
arxiv_id: '2608.14380'
url: https://arxiv.org/abs/2608.14380
pdf_url: https://arxiv.org/pdf/2608.14380
published: '2026-08-14'
collected: '2026-08-17'
category: Agent
direction: Agent 执行恢复与 checkpoint
tags:
- LLM agents
- runtime recovery
- checkpointing
- long-horizon
- benchmark
- tool use
one_liner: 通过对齐的上下文与环境 checkpoint 回滚，并注入失败摘要，提升长程 Agent 任务成功率
practical_value: '- 做电商/搜索/广告领域的 Agent 时，把失败恢复做成 runtime 层，不只回滚 message history，必须同时回滚工作区或数据库状态；否则被污染的中间状态会拖垮后续步骤。

  - 把 rewind 作为工具暴露给 LLM，而不是外部固定策略：让 agent 根据 checkpoint metadata 选择回退点并写 memory_summary，适合长任务和多步修改场景。

  - 借鉴 MettleBench 的「有序 checklist + 只返回第一个未满足项 + prefix progress」作为 Agent 任务验收与诊断指标，比只看最终成功率更能测量部分完成度。

  - 工程上要明确恢复边界：只回滚可控文件系统，外部副作用需要隔离或记录；回滚时用执行日志恢复前缀，避免重新执行产生新的副作用。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**
长程 LLM Agent 执行中，早期错误会同时污染 agent context 和环境状态，且很难通过后续动作完全逆转。现有方法主要靠事前规划或安全检查降低错误率，但对错误发生后的恢复支持很少。因此需要一个运行时恢复机制，让 Agent 在发现当前轨迹无法推进时能回到更早状态。

**方法关键点**
- AgentRewind 作为 runtime layer，位于 agent 与受控环境之间，透明记录每个 LLM 决策边界的 checkpoint：`d_t = (c_t, s_t)`，其中 `c_t` 是 agent context，`s_t` 是 workspace 文件系统状态。
- 将 rewind 暴露为两个工具：`backtrack_candidates` 列出候选回退点及 metadata；`backtrack_commit` 执行回退，要求 agent 写一段 memory_summary，记录失败假设和替代策略。
- 回滚时，环境恢复到选定 checkpoint 的文件状态，context 恢复到对应历史消息；保留的前缀从执行日志恢复，不重新执行。累积的 rewind memory 注入恢复后的 context。
- 恢复边界明确为 workspace 文件树；网络请求、外部服务等不可逆副作用无法撤销，但也不会在回滚时重放。
- 同时提出 MettleBench：82 个长程工程任务，来自 Terminal-Bench 2.0、SWE-bench 等 5 个 benchmark，每个任务包含有序 acceptance criteria，提交后只返回第一个未满足项；用 checklist prefix progress 衡量部分完成度。

**关键实验与结果**
- MettleBench 上，GPT-5.4 的 Continue baseline 成功率 62.2%，checklist progress 81.4%；AgentRewind 将成功率提升到 87.8%（+25.6），progress 到 94.3%（+12.9）。
- GPT-5.4 mini 上同样提升，且跨 mini-SWE-agent、FnCallAgent、CodeAgent 三种 harness 均有效。
- Terminal-Bench 2.0 上，AgentRewind 成功率 83.1%，高于 Continue 78.7% 和 Restart with Experiences 70.8%。
- 50 个失败 Continue 终点的配对恢复实验中，AgentRewind 恢复率 30%，Continue 仅 8%；checklist progress 变化 +12.2 pp vs +5.1 pp。
- 消融显示，去掉环境回滚导致最大退化（成功率从 87.8% 降到 43.9%），说明对齐的 context–environment 恢复是核心。

**最值得记住的一句话**
长程 Agent 的可恢复性来自「上下文 + 环境」的对齐 checkpoint 和失败摘要注入，只回滚上下文或只保留记忆都不够。
