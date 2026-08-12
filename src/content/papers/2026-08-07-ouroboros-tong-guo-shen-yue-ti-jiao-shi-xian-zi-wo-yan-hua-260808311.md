---
title: 'Ouroboros: A Self-Developing Frontier Coding Agent with Reviewed Core Evolution'
title_zh: Ouroboros：通过审阅提交实现自我演化的前沿编码 Agent
authors:
- Anton Razzhigaev
- Andrei Gritsaev
- Andrei Kaznacheev
- Nikita Dragunov
- Roman Yampolskiy
- Andrei Kuznetsov
affiliations:
- Lomonosov Moscow State University
- Skolkovo Institute of Science and Technology
- Joi Lab
- FusionBrain Lab at AIRI
- HSE University
arxiv_id: '2608.08311'
url: https://arxiv.org/abs/2608.08311
pdf_url: https://arxiv.org/pdf/2608.08311
published: '2026-08-07'
collected: '2026-08-12'
category: Agent
direction: 自我演化 Agent · 核心演化与安全控制
tags:
- self-evolving agent
- coding agent
- benchmark
- guardrails
- reviewed commits
- continual learning
one_liner: 一个自我修改运行时（harness）的编码 Agent，通过审阅提交通道持续演化，在 Terminal-Bench、OSWorld 等基准上取得最优结果。
practical_value: '- 在电商推荐 Agent 中采用**经验驱动演化**：把线上故障、用户反馈、任务执行痛点自动转换为改进待办，经审查后修改 Agent
  的工具链或提示词，形成自我优化的闭环。

  - 实施**多模型审查门控**对抗自我修改风险：对 Agent 主动提交的代码/配置变更进行强制 diff 审查、指纹校验和 quorum 投票，防止模型自行绕过安全约束（如越权调用
  API 或改变路由）。

  - 将**模型路由、宪法文件、紧急停止路径**设为受保护的“治理表面”，通过外部预算、操作员通道和 /panic 信号保持人类权威，避免 Agent 演化过程中削弱控制。

  - 借鉴长期运行 Agent 的**持久化记忆层设计**：维护故障模式注册表（error class → root cause → structural fix），让推荐系统
  Agent 能将一次性错误提升为结构性改进，持续提升服务质量。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机

当前长周期 Agent 的性能不仅取决于基座模型，更依赖其运行时框架（harness）对上下文组装、工具调用、验证与恢复的策略。然而主流系统在部署后便固化这些策略。Ouroboros 将 harness 视为可演化的对象，通过审阅提交机制，让 Agent 在持续工作中自我改进——既能提升任务表现，也为安全控制提出了新挑战。

## 方法关键点

- **双模核心演化**：
  - *递归自由演化*：把“改进系统”本身作为任务，Agent 选择并实施变更，完成后可调度下一轮演化，形成连续的自我更新。
  - *经验驱动演化*：从日常任务执行、反思、审查卡点和社交反馈中捕获缺陷与粗糙点，记录为持久错误类，然后决定是否发起维护修改。
- **审查提交门控**：所有对自身仓库的修改必须通过确定性预检、分阶段 diff 指纹、多模型评审（quorum 机制）和二次指纹校验；所有者可配置上下文模式以控制全仓库范围审查。
- **Hope 部署线**：持续 161 天的公开部署，通过 7 个通信表面与 ~3600 人交互，累计自我修改 1085 次 commit，其中 94.2% 由 Agent 自主完成，展示了人类反馈驱动的持续演化。
- **安全边界**：始终加载的宪法文件、治理文件保护、外部花费上限、隔离的操作员通道和 /panic 紧急停止，确保能力提升不削弱控制权威。

## 关键实验

- **Terminal-Bench 2.1**（89 任务 × 5 试次）：Opus 5 原始分数 86.97%，轨迹审计后 86.74%，超越 Claude Code+Fable 5 的 83.8% 和 Codex CLI 的 83.1%。
- **OSWorld-Verified**（361 任务）：Opus 5 得分 90.69%，超过此前最佳 90.19%。
- **CL-Bench**：Sonnet 4.6 归一化奖励 0.2301（5 次有序 rollout），显著高于 ICL 基线 0.1960。
- **SWE-bench Pro 与 GAIA**：与 Codex 和 Claude Code 达到统计不可区分的平局，表明自我演化 harness 可匹配前沿固定 harness。
