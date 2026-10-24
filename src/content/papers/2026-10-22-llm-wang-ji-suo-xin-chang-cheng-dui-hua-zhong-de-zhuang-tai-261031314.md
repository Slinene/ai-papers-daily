---
title: 'When LLMs Forget What They Believe: Characterizing State Integrity Collapse
  in Long-Horizon Dialogues'
title_zh: LLM 忘记所信：长程对话中的状态完整性崩塌表征
authors:
- Yancheng Zhu
- Yifan Yuan
affiliations:
- School of Artificial Intelligence, Shenzhen University
arxiv_id: '2610.31314'
url: https://arxiv.org/abs/2610.31314
pdf_url: https://arxiv.org/pdf/2610.31314
published: '2026-10-22'
collected: '2026-10-24'
category: Eval
direction: 长对话状态完整性评估与缓解
tags:
- state integrity collapse
- long-horizon dialogue
- instruction following
- behavioral drift
- structured state anchoring
- evaluation
one_liner: 定义状态完整性崩塌，用 StateTrack-Bench 揭示长对话中模型“记得但不执行”约束的失败模式，并验证结构化锚定可部分恢复
practical_value: '- 在对话式推荐/客服 Agent 中，用户偏好、预算、格式或业务规则常在多轮对话中设定；不能只测单轮遵循，要构建类似 StateTrack
  的“约束保持”回归集，监控长 session 下 recall 与 compliance 是否解耦。

  - 将关键状态用结构化锚点注入每轮上下文（如 system state block / 结构化 memory），实验显示可恢复最多 24.4 点；可在电商 Agent
  中用类似“状态锚定”方式（固定摘要或 key-value constraints）防止行为漂移。

  - 区分“忘记”和“记得但不做”很重要：排查线上 case 时，如果模型能复述约束却违反，补 RAG/摘要可能无效，需要改进推理或加显式约束检查。

  - 对多轮推荐/搜索场景，格式约束（如输出 JSON、候选 ID 格式）容易发生 symbolic degradation，考虑后处理校验或每轮显式重申约束。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

动机：单轮指令遵循评估太弱，部署中的助手需在数十轮对话里持续保持目标、偏好、安全边界与格式要求。存在一种危险失败：模型能复述约束却不再执行，本文将其定义为 State Integrity Collapse (SIC)，区别于普通遗忘。

方法关键点：构建 StateTrack-Bench，覆盖数值、格式、角色/人设、事实记忆、逻辑规则五类约束；在七个 provider-pinned 模型快照与五个对话深度探针上测试；用 forked recall audit 区分行为漂移与普通遗忘；扩展至 50 轮长对话；提出 Structured State Anchoring 作为缓解。

关键结果：严格联合保留率从 62.4% 到 100.0%，退化集中在 symbolic constraints 和一个脆弱模型；88.6% 的失败是行为漂移而非遗忘（排除异常值后为 84.4%）；深度扩展确认现象持续存在；结构化状态锚定在不可变约束上最多恢复 24.4 点。结论：可靠性不能只看单轮指令遵循，评估必须跟踪记忆约束在对话状态增长时是否仍然可操作。
