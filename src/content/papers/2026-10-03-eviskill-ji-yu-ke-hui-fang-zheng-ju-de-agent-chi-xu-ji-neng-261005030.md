---
title: 'EVISKILL: Grounding Skill Evolution in Replayable Evidence'
title_zh: EVISKILL：基于可回放证据的 Agent 持续技能演化
authors:
- Yan Zhou
- Yili Wang
- Yiwei Dai
- Qinggang Zhang
- Xin Wang
affiliations:
- School of Artificial Intelligence, Jilin University, Changchun, China
arxiv_id: '2610.05030'
url: https://arxiv.org/abs/2610.05030
pdf_url: https://arxiv.org/pdf/2610.05030
published: '2026-10-03'
collected: '2026-10-07'
category: Agent
direction: Agent 持续技能进化与证据回放
tags:
- LLM Agents
- Skill Evolution
- Evidence Replay
- Continual Learning
- Tool Use
one_liner: 用可回放证据卡与定向重放验证技能编辑，缓解经验驱动技能演化中证据丢失和全局验证粒度过粗问题
practical_value: '- 把 agent 执行轨迹中的 state/action/observation/context 打包成结构化证据卡，技能修改时显式绑定支撑证据；后续可用同一批轨迹做定向重放验证，让技能更新可审计、可回滚。

  - 将验证拆成编辑级回放与全局验证两层：先用局部证据筛选出可信候选修订并暂存，再按整体任务集决定是否并入正式技能，避免一次性拒绝丢失有效局部修正；适合电商客服
  SOP、选品策略等需要长期迭代 agent 流程的场景。

  - 跨 epoch 保留证据和候选修订，允许证据不足的编辑等待更多交互经验再确认，提供一种更稳的 agent 策略在线进化机制；对推荐策略、工具选择规则等可复现程序知识的维护有价值。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM agent 在交互任务中需要积累可复用程序性知识，但现有经验驱动技能演化方法会丢失支持修改的行为证据与任务上下文，且全局验证对局部修改判断粒度过粗：局部有效的修正可能随整体被拒而丢弃，而某些证据需要更多经验才能形成可靠更新。

**方法关键点**：EVISKILL 是证据驱动框架，将执行观察组织成可回放证据卡，合成技能编辑时显式关联支撑上下文；通过定向重放重新执行相关轨迹来验证编辑，并生成纠正反馈；跨 epoch 保留证据、暂存受支持的编辑供进一步细化，最终由全局验证决定是否并入正式技能。

**结果**：在三个交互式 benchmark、六个 LLM 骨干上验证了方法有效性。
