---
title: How Much Conversation History Does an AI Agent Need?
title_zh: AI Agent 需要多少对话历史？
authors:
- Danny Kim
- Fernando Koch
affiliations:
- Pembroke Pines Charter High School
- Florida Atlantic University
arxiv_id: '2611.09662'
url: https://arxiv.org/abs/2611.09662
pdf_url: https://arxiv.org/pdf/2611.09662
published: '2026-11-06'
collected: '2026-11-09'
category: Agent
direction: Agent 对话记忆与上下文预算优化
tags:
- conversational memory
- context budgeting
- message retention
- BEAM
- token-cost tradeoff
- long-context LLM
one_liner: 在 BEAM 任务上量化对话历史预算对 reader token 与得分的影响，发现边际收益递减，记忆保留策略需按证据类型选择
practical_value: '- 对话记忆预算可做显式分层：对直接属性/需求类问题保留用户原话，对依赖历史 offer/多跳引用的问题必须保留早期关键消息，而不是简单按
  recency 截断；这与电商导购 Agent 中“用户先说预算、后说偏好”的场景直接对应。

  - Token-分数曲线呈边际递减：业务可在线做类似离线回放或 A/B，找本领域“3 vs 10 passages”的拐点；未必默认最长上下文，尤其在排序/召回后给
  LLM 拼 context 时，省 67.8% tokens 可能只损失几分。

  - 评估分数不可全信：该文 scoring audit 发现 BEAM 答案正确性 unresolved；迁移到业务时，离线 judge/answer quality
  要与线上转化、点击等真实指标校准，否则容易选错 memory budget。

  - 模型选择要验证 memory retention 能力：Mistral 在所有 retention 条件下接近地板，说明不同 LLM 对长对话状态保持能力差异大；接入电商导购
  Agent 前应对“保留用户消息 vs recency”做专项评测。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：AI Agent 处理长对话时，reader token 随历史增长，成本与效果需要平衡。论文研究到底需要多少对话历史，以及不同保留策略如何影响 token 使用和 benchmark 得分。

**方法关键点**：在 1,100 道 BEAM 问题上固定 retrieval ranking 和 reader（Qwen2.5-14B），比较 1、3、5、10、20 五种 passage budget 下的 token 与 assigned score；另在受控任务中显式设定 conversational-state targets，对比“保留用户消息”与 token-matched recency，测试 Qwen 和 Mistral；并做 scoring audit 检验 BEAM 答案正确性。

**关键结果数字**：随 passage budget 增长，mean assigned scores 上升，但边际收益递减；3 passages 比 10 passages 少 67.8% reader tokens，分数低 5.45 分；10 passages 到 20 passages 仅 +2.39 分。Answerable questions 通常需要更多 context；abstention 分在 budget 缩小时有时上升。Qwen 在直接需求上保留用户消息更能匹配完整状态，但依赖 earlier offers 引用时下降；Mistral 接近地板。审计表明 BEAM 答案正确性 unresolved。结论是 reliable budget selection 取决于保留问题所需证据，并验证评估质量。
