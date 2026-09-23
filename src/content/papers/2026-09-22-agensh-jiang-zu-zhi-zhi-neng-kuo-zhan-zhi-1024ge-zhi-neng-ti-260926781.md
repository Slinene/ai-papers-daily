---
title: 'Agensh: Scaling Organizational Intelligence to 1,024 Agents'
title_zh: Agensh：将组织智能扩展至1024个智能体
authors:
- Zhihao Zhan
- Ting Song
- Li Dong
- Shaohan Huang
- Jianxun Lian
- Yan Xia
- Furu Wei
affiliations:
- Microsoft Research
arxiv_id: '2609.26781'
url: https://arxiv.org/abs/2609.26781
pdf_url: https://arxiv.org/pdf/2609.26781
published: '2026-09-22'
collected: '2026-09-23'
category: MultiAgent
direction: 多智能体自组织协作扩展
tags:
- Multi-Agent
- Self-Organization
- Scaling
- ProgramBench
- Shared Context
- Agent Infrastructure
one_liner: 去中心化自组织多智能体框架，无中心协调者扩展到1024 agents，长程重建任务成功率随agent数量提升且更快达标
practical_value: '- 去中心化任务自组织：在选品、搜索 query 挖掘、商品知识库构建等需要大量并行探索的场景中，用 shared context
  中的 CLAIM + 类型化记录替代中心 planner，能避免单点瓶颈；尤其 FAIL 记录可以防止多个 worker 重复尝试无效方案。

  - 用成熟组件搭 multi-agent 基础设施：Git / Gitea 做 workspace，Mattermost 做消息，append-only board
  做共享记忆，工程成本低且原生支持并发合并与冲突检测；电商 Agent 并发修改商品文案、活动页时可直接借用。

  - 消息分级与 mid-turn 注入：对冲突或依赖用 direct message 在当前 turn 送达，普通公告在下一回合开始处理，能显著降低协调延迟；适合实时广告调价、大促实时选品等对延迟敏感的业务。

  - 规模化带来“更快达到同一效果”：如果业务任务有硬时间预算，增加并发 worker 数不仅提升最终质量，还能缩短达到给定质量的时间；可尝试从少量 Agent
  扩展到 100+ 做长程生成式任务。'
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

**动机**
单 Agent 系统受限于单个上下文窗口、单条动作流和记忆流，长程复杂任务延迟高且能力边界明显。现有多智能体框架普遍采用 orchestrator-worker 结构，中心协调者负责规划、分配和集成，其管理容量成为系统扩展瓶颈。Agensh 的目标是去掉中心协调者，让 Agent 数量本身成为新的扩展维度。

**方法关键点**
- **多智能体合作循环**：每个 worker 异步执行五步：gather context → claim sub-task → take action → verify results → merge progress，循环直至目标达成。
- **三类组织基础设施**：shared workspace 由 Git/Gitea 实现，保存进行中和已完成工作，支持并发写、异步读、版本历史和冲突检测；message interface 由 Mattermost 实现，包含共享任务频道和 direct message，直发消息可在当前 turn 内注入，用于紧急冲突协调；shared context 为 append-only 类型化记录，包含 OBSERVED / FACT / FAIL / CLAIM / PATCH_SUMMARY，并提供 board_read / board_grep 进行全历史检索。
- **完全去中心化**：所有 worker 使用相同的 prompt（仅 worker ID 不同），任务发现、分配、协调和集成全部由 worker 自组织完成。
- **事件驱动 runtime**：Gitea/Mattermost 事件触发 worker，direct message 和新的 shared context 条目可在工具返回时 mid-turn 追加，降低协调延迟。

**关键实验**
在 ProgramBench 五个最难任务（FFmpeg、gromacs、pandoc、PHP-src、ctags）上，6 小时预算、无互联网，使用 GPT-5.6-sol (high) 与 Copilot 底层 harness。1→128 agents 平均最终 test-pass rate 从 19.31% 升至 28.78%，相对提升约 49%。pandoc 上继续扩展到 1024 agents，test-pass rate 从单 Agent 的 33.89% 升至 128 agents 的 50.94%，1024 agents 达 55.06%。更大组织更快达到相同水平：pandoc 上 128 agents 在 30 分钟就超过 30% pass rate，32 和 8 agents 分别需要 60 和 90 分钟，单 Agent 前 2 小时低于该阈值。轨迹还显示协作形式随规模涌现：8 agents 出现接口协调，32 agents 出现多工集成，128 agents 出现专业化与标准化工作流，1024 agents 出现组织级角色专业化。

**最值得记住的一句话**：Agent 数量可以成为扩展组织智能的新维度，去中心化基础设施能让自组织协作从几十扩展到上千 Agent，同时提升长程任务质量与速度。
