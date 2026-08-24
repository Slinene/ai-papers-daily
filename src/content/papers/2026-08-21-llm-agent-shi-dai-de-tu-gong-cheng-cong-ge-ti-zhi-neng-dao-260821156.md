---
title: 'Graph Engineering in the Era of LLM Agents: From Individual Intelligence to
  System Intelligence'
title_zh: LLM Agent 时代的图工程：从个体智能到系统智能
authors:
- Yuyuan Feng
- Zhishang Xiang
- Chaobin Yang
- Qichao Ma
- Zerui Chen
- Yujing Zhang
- Ke Huang
- Chuanjie Wu
- Zhaoxu Liu
- Yili Wang
affiliations:
- Jilin University
arxiv_id: '2608.21156'
url: https://arxiv.org/abs/2608.21156
pdf_url: https://arxiv.org/pdf/2608.21156
published: '2026-08-21'
collected: '2026-08-24'
category: MultiAgent
direction: 多智能体图工程系统智能
tags:
- Graph Engineering
- LLM Agents
- Multi-Agent Systems
- System Intelligence
- Task Organization
- Runtime State
one_liner: 系统梳理用图结构组织任务、代理与运行时状态的多智能体图工程范式，为复杂 Agent 系统提供统一抽象
practical_value: '- **用图结构显式刻画多 Agent 工作流**：在电商搜索推荐/Agent 系统中，把一次完整服务链路（意图理解、召回、粗排、精排、生成、校验）抽象为
  DAG，节点是可执行子任务，边表示依赖/并行/验证约束。这样可以直接调度并行分支（如多路召回、多策略生成），避免单 Agent 串行执行造成的上下文挤占和故障定位困难。

  - **把 Agent 能力建模为可路由的资源**：对异构专家 Agent（如商品知识 Agent、用户意图 Agent、价格策略 Agent）建立能力标签和技能图谱，由协调器按任务需求动态组队与通信。可借鉴
  `Agent Capability Modeling + Team Organization` 思路，替代固定的顺序 pipeline，适合促销活动、类目导购等需要多角色协作的场景。

  - **引入 Runtime State Management 做状态持久化与恢复**：在长流程推荐/Agent 任务中，显式记录每个子任务的执行状态、中间结果和
  provenance，实现故障隔离与局部重试。这能显著改善“推荐链路某一步失败导致整个请求重算”的问题，尤其适合大促高并发下的降级和恢复。

  - **关注 System Evolution 提升系统自优化能力**：基于历史执行轨迹和运行时证据动态调整任务分解或 Agent 拓扑，类似从日志中提取可复用
  skills/workflows。可用于电商 Agent 的持续优化，例如自动沉淀用户高频问题的解决路径，或根据转化反馈调整推荐 Agent 的协作结构。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
LLM 已从单模型推理进化到能自主规划、调用工具、与环境交互的 Agent。然而真实任务往往需要异构专长、相互依赖的子任务、并行执行、独立验证和持久状态，单 Agent 的上下文和串行控制结构难以承载这些需求。仅靠增强单个 Agent 的能力或上下文，无法解决架构上的错配，智能需要被分布到多个专业 Agent 上并在系统层面组织，即系统智能。

**方法关键点**
- 提出 **Graph Engineering** 作为下一代 Agent 系统的工程范式，用显式、动态、演化的图结构统一表示任务、代理和运行时状态。
- 抽象三层核心问题：
  1. **Task Organization**：将全局目标分解为可执行子任务，显式表示依赖、顺序、并发与验证约束；支持目标分解与工作流优化。
  2. **Agent Coordination**：将子任务映射到异构 Agent，建模 Agent 能力、组织团队拓扑、路由通信；包含能力建模、团队组织和多代理通信。
  3. **Runtime State Management**：记录执行状态、定位故障、恢复失败、支持系统演化；跟踪进度、协调并发更新、保留 provenance。
- 梳理从 Model Intelligence → Individual Intelligence → System Intelligence 的演进谱系，将 Prompt/Context Engineering、Harness/Loop Engineering 与 Graph Engineering 系统化，并给出形式化定义：`Agent = Loop(LLM + Harness)`，`Agent System = (Agent Team, Shared Resources, Environment, Coordination, System State)`。
- 覆盖大量相关方法，如 HuggingGPT、MetaGPT、GPTSwarm、AFlow、DyFlow、StateFlow、LangGraph、AutoGen 等，并整理 benchmarks、开源库与应用领域。

**关键结果**
该工作是综述，没有单一基准实验。其主要贡献在于：提出统一的 Graph Engineering 分类体系，将任务组织、代理协调和运行时状态管理作为系统智能的三大支柱；梳理软件工程、科学发现、医疗、企业工作流、通用数字 Agent 等领域的应用；归纳评估原则与开源生态，并指出开放挑战（图原生能力、自演化图系统、图原生 Agent OS、隐私伦理）。

**最值得记住的一句话**
系统智能的核心不是增加 Agent 数量，而是用图结构显式组织任务、代理与状态，使异构组件成为一个连贯、自适应整体。
