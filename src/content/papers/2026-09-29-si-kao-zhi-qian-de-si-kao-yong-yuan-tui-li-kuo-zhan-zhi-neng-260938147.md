---
title: 'Thinking Before Thinking: Scaling Agentic Inference Through Meta-Reasoning'
title_zh: 思考之前的思考：用元推理扩展智能体推理规模
authors:
- Paras Dahal
- Anton Bakhtin
- Taco Cohen
- Zhengxing Chen
- Carole-Jean Wu
- Rob Fergus
- Scott Yih
- Gabriel Synnaeve
- Ruslan Salakhutdinov
- Sanjeev Arora
affiliations:
- Meta Superintelligence Labs
arxiv_id: '2609.38147'
url: https://arxiv.org/abs/2609.38147
pdf_url: https://arxiv.org/pdf/2609.38147
published: '2026-09-29'
collected: '2026-09-30'
category: Agent
direction: Agent 元推理控制与 artifact graph
tags:
- Agentic Meta-Reasoning
- Test-time Compute
- Artifact Graph
- Metacognition
- Long-horizon Agents
one_liner: 将 Agent 的控制决策与目标级计算分离，用显式元推理管理 artifact 图、预算和 worker 调度，提升长程任务性能并随预算持续扩展
practical_value: '- 把“控制”与“执行”拆开：在电商推荐/搜索的 Agent 流程中，不要让每个动作都携带完整历史；用轻量 controller
  state + 可检索 artifact memory，worker 只接收必要 context，能显著降低长上下文信息丢失，提高多步决策稳定性。

  - 用 artifact graph 做系统诊断：记录每个中间候选/策略的依赖关系，将失败分解为 coverage（是否产生过正确结果）和 selection（是否选中），类似论文中的覆盖率和
  frontier 选择增益，快速定位是召回/生成不足还是最终排序/选择错误。

  - 做预算感知的元推理：在线上低延迟场景可以设置 model-call 预算，由 Evaluate 阶段判断剩余预算下每个候选动作的计算价值，小预算时自动关闭深层次控制；论文中低预算
  crossover 现象说明元推理 overhead 对简单任务可能有害。

  - 引入独立 controller verdict，而非只依赖 worker 自我置信：在推荐 Agent 中对生成结果做独立评估和打分，其排序信号往往比生成模型自报置信度更可靠，可用于最终候选选择。'
score: 9
source: arxiv-cs.AI
depth: full_pdf
---

**动机**
Agent 处理更长更复杂任务时，控制执行本身成为独立问题：每一步都可能选择继续、放弃、重做或停止。现有 Agent 往往把控制决策与目标级计算交织在同一个上下文里，导致有用工作难以组合、预算利用率低、且随着历史膨胀噪声越来越大。

**方法关键点**
- 把系统分成 controller 与 workers：controller 维护一个紧凑的当前状态，全量 worker 输出存入 persistent memory，可按需检索；worker 只接收 controller 选定的指令和必要 artifact，不接触 controller 私有状态。
- 每个控制周期包含四个显式阶段：Assess（更新状态）、Propose（枚举候选下一步计算）、Evaluate（在剩余预算下评估每个候选的价值）、Dispatch（生成 worker 指令并选择其上下文）。
- worker 可以是单次模型调用或完整的 coding agent；所有 controller 和 worker 调用从同一模型调用预算中扣除。
- 自动记录 artifact graph：每个 worker 产出作为节点，输入 artifact 作为依赖边，形成有向无环图，用于诊断计算结构、复用和分支行为。
- 设置 Direct Control Agent 作为匹配消融：使用相同 workers 和接口，但每次只从累积历史单步选择动作，以隔离控制设计的影响。

**关键实验**
在 IMO ProofBench-Advanced、ARC-AGI-2、LongCoT-mini 和 ProgramBench 四个基准上，用 Gemini 3.1 Pro、GPT-5.5、Opus 4.8 三种前沿模型测试。主预算为推理基准 100 次模型调用、ProgramBench 1200 次。结果：12 个匹配比较全部提升，平均提升 3.6–4.2 分；ProgramBench 上 GPT-5.5 达到 71.5%，超过 Codex 的 58.0% 和 Direct Control 的 63.7%；Opus 4.8 达到 67.2%，超过 Claude Code 的 65.5%。预算扫描显示元推理随预算继续提升，而直接控制常出现平台期；但低预算下（如 Opus 4.8 400 calls）元推理 56.6% 低于直接控制 62.7%，说明控制开销需要足够预算才能回收。artifact graph 分析显示元推理产生更多 worker 输出且更复用早期工作；controller 独立 verdict 的 Type-2 AUC 可达 0.88，明显高于 worker 自我置信的 0.55；运行状态从直接控制的上百万字符降到几千到几万字符。

**最值得记住的一句话**
Agent 的性能不仅取决于它做工作的能力，还取决于它决定哪些计算值得做的能力——后者本身也是一项需要显式设计的工作。
