---
title: 'LongHorizon-Harness: Advancing Long-Horizon Agents for Real-World Tasks'
title_zh: LongHorizon-Harness：将长期执行重构为任务状态管理问题，大幅提升长程代理性能
authors:
- Ziyu Ma
- Hailang Huang
- Shun Zou
- Yong Wang
- Shidong Yang
- Yiming Hu
- Fei Wei
- XiangXiang Chu
affiliations:
- DreamX Team, Alibaba Group
arxiv_id: '2608.01964'
url: https://arxiv.org/abs/2608.01964
pdf_url: https://arxiv.org/pdf/2608.01964
published: '2026-08-02'
collected: '2026-08-05'
category: Agent
direction: 长期任务代理 · 任务状态管理
tags:
- Long-Horizon Agent
- Task-State Management
- MEA Loop
- Multi-Role
- Computer Use
- Agent Framework
one_liner: 通过管理-执行-审计（MEA）循环显式维护任务状态并独立审计，在 WeaveBench 上将完成率从 51.8% 提升至 80.7%
practical_value: '- 在电商搜索/推荐的多步代理任务（如复杂购物助手、多轮商品对比）中，可引入 MEA 架构：经理根据用户意图分解子任务，执行器在干净上下文中完成（如检索、对比），审计员独立验证执行结果，防止错误累积导致后续决策偏离。

  - 显式任务状态与执行上下文分离的技巧，能有效避免长对话/操作历史带来的上下文遗忘问题，适合需要维护用户画像、购物车等中间状态的对话式推荐代理。

  - 独立审计机制可应用于广告投放优化、商品批量上架等需多步验证的业务流程，确保每一步操作结果符合预期后才更新全局状态，提升流程可靠性。

  - AgentAdapter 的设计表明可以通过轻量适配层统一接入不同的 LLM 或工具后端，便于在生产中灵活切换模型和底层执行引擎。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：长程代理在执行跨越多步的复杂任务时，面临错误累积、上下文膨胀导致信息检索困难（“上下文腐烂”）、以及任务状态难以跟踪和更新三大难题。现有代理框架将任务执行与状态管理耦合在同一个不断增长的上下文中，错误的自评结果容易污染后续决策。

**方法关键点**：
- 将长程执行重新定义为任务状态管理问题，在外部显式维护任务状态，仅用独立审计验证的环境事实更新状态。
- 设计“管理-执行-审计”（MEA）循环：**经理**读取当前任务状态，构造一个带依赖、约束和验收标准的子任务合同；**执行器**在全新上下文中执行该合同，不携帯历史轨迹；**审计员**以只读方式独立检查环境，生成审计报告，明确完成状态、完整性状态及支持证据。
- 经理根据审计报告更新任务状态，决定下一子任务或终止；执行器的原始交互历史在每轮后丢弃，仅紧凑的审计事实跨轮持久化。
- 通过 AgentAdapter 统一接口，兼容 Claude Code、Codex CLI 等多种后端，三个角色均可更换底层模型。

**关键结果**：
- 在 WeaveBench（114 个跨 GUI/CLI 任务）上，Qwen 3.7-Plus 的完成率从 51.8% 提升至 **80.7%**（均值分从 0.702 到 0.835）。
- 在 Terminal-Bench 2.1 上，完成率从 69.7% 提升至 **77.2%**。
- 在 OSWorld 2.0（108 个桌面任务）上，二进制完成率从 2.8% 提升至 **8.3%**，部分完成分数从 21.5% 升至 35.2%；用 Claude Opus 4.7 在 34 任务子集上也将二进制完成率从 20.6% 提升至 35.3%。
- 经理角色的 token 消耗仅占 2-8%，框架主要额外成本来自审计，但总体成本因任务与模型强弱而异。

**值得记住的一句话**：长期任务的可靠执行不仅取决于模型能力，更取决于如何组织、验证和将局部成功累积为端到端完成——把状态从混乱的执行轨迹中剥离，并让每一步的完成只是经过审计的事实。
