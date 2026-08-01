---
title: 'Rethinking Inference-Time Scaling in Local Computer-Use Agents: Failure Modes
  and Compute Tradeoffs'
title_zh: 本地计算机使用智能体的推理时扩展再思考：失败模式与计算权衡
authors:
- Woongkyu Lee
- Jungwook Choi
affiliations:
- Hanyang University
arxiv_id: '2607.28573'
url: https://arxiv.org/abs/2607.28573
pdf_url: https://arxiv.org/pdf/2607.28573
published: '2026-07-30'
collected: '2026-08-01'
category: Agent
direction: 推理时扩展与失败分析
tags:
- Inference-Time Scaling
- Computer-Use Agents
- Failure Modes
- Compute Tradeoffs
- Local Deployment
- GUI Agents
one_liner: 系统实证表明，推理时扩展在本地 CUAs 中收益递减且会改变失败模式，需选择性地分配计算
practical_value: '- **在资源受限的本地推荐 Agent 中，上下文扩展的收益会饱和**：给 Agent 看更多历史轨迹（如用户会话日志）虽能提升稳定性，但
  token 成本急剧上升，且可能让 Agent 提前宣布虚假成功。实践中应设置上下文窗口截断上限，并监控 false success 类型的失败。

  - **时间维度的扩展不解决根本问题**：增加最大步数（如搜索推荐多轮对话尝试）常常只是延长错误轨迹，而非纠正错误。应结合在线失败检测（如 stall 检测）和早停机制，而非盲目扩大步数。

  - **结构化解耦（Planning + Execution）在本地模型上可能引入规划与格式解析开销**：若将推荐 agent 拆分为计划器和执行器，小模型容易产出格式有误的计划，或计划质量低下。若必须使用两阶段架构，可考虑加入格式校验和重试逻辑，或改用单阶段端到端方案。

  - **并行采样可以部分缓解单轨错误，但计算成本高**：类似 Best-of-N 采样在本地部署中可能因并行调用导致硬件压力过大。可考虑在关键决策步骤（如 item
  选择）才启用少数几次并行，并设置超时和多数投票机制。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：本地部署自主计算机使用智能体（CUA）对于隐私、成本和实用性日益重要，但在严格硬件约束下如何利用推理时扩展提升性能仍不清楚。先前研究表明推理时扩展能提升大模型 CUA 的表现，其对资源受限本地模型的效应亟需系统分析。

**方法关键点**：在 OSWorld 基准上对 Qwen3-VL-8B/30B-A3B、UI-TARS-1.5-7B、OpenCUA-7B 进行四维度扩展实验：
- **上下文扩展**：提供更长历史帧序列；
- **时间扩展**：增加最大交互步数；
- **结构扩展**：将任务分解为“规划-执行”两阶段；
- **并行扩展**：对同一状态并行采样多个动作。
分析不同扩展方式下的失败模式变迁和计算开销。

**关键结果**：
- 上下文扩展提升轨迹稳定性和任务准确率，但收益随 token 成本增加而饱和，失败模式从重复/停滞转为过早宣布成功；
- 时间扩展减少最大步数停滞，但未实质提升成功率，表明更长 horizon 往往只是延长错误轨迹；
- 结构分解在本地两阶段 agent 中引入规划开销和格式错误，并行扩展虽能部分弥补，但计算成本显著；
- 结论：高效的本地 CUA 需要选择性计算分配、失败感知控制机制，以及围绕本地模型能力设计的 agent 框架。
