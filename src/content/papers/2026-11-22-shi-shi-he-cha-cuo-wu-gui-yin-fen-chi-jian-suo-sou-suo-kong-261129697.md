---
title: Where Do Fact-Checking Errors Arise? Separating Retrieval, Search Control and
  Judgement in Evidence-Grounded Verification
title_zh: 事实核查错误归因：分离检索、搜索控制与判断
authors:
- Martin Pavlíček
- Martin Kotyrba
- Eva Volná
- Tomáš Filip
- Petr Sosík
affiliations:
- Institute for Research and Applications of Fuzzy Modeling, University of Ostrava
- Department of Informatics and Computers, Faculty of Science, University of Ostrava
arxiv_id: '2611.29697'
url: https://arxiv.org/abs/2611.29697
pdf_url: https://arxiv.org/pdf/2611.29697
published: '2026-11-22'
collected: '2026-11-24'
category: Eval
direction: RAG 错误归因与分层评估
tags:
- fact-checking
- RAG evaluation
- retrieval
- search control
- verdict validation
- agent
one_liner: 提出分离检索、搜索控制、判断与验证的评估协议，揭示端到端准确率掩盖的错误来源
practical_value: '- 在 RAG/Agent 链路中把「证据找回率」「判断准确率」「最终决策一致性」分层打点，错误归因时先确认 evidence
  packet 是否完整，再决定改检索还是改 judge。

  - 单次 hybrid retrieval 往往已经够用；iterative/agentic controller 可能多花 2-9 倍模型调用却没有一致增益，线上成本敏感场景先用廉价
  hybrid retrieval。

  - 增加规则化的 verdict validation 可以拦截过度自信判决，即使牺牲单次通过率也值得；类似电商审核的规则兜底。

  - 从小型标注证据库换到全量源库后，性能下降主要来自 evidence recovery，需单独评估检索质量，避免把错误误判给 LLM 判断环节。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：端到端事实核查准确率无法区分错误来自找不到证据还是不会用证据，需要分层归因。

方法关键点：设计协议沿证据从存储到判决的链路，拆成 retrieval、search control、judgement、verdict validation 四个环节；在 FEVER、FEVER 2.0、AVeriTeC 的 293 条 claim 上，使用 open-weights 9B 模型；控制条件用标注证据小库，完整源库作对照，比较单次 hybrid retrieval 与 adaptive controllers / tool agent。

关键结果：小库中 228 条有证据 claim 里 226 条单次 hybrid retrieval 能拿到完整参考证据；adaptive controllers 和 tool agent 多花 2-9 倍模型调用但没有一致增益；34 条被标为缺乏证据的 decisive claims 中 33 条证据实际完整：15 条法官弃权，18 条验证规则推翻判决；AVeriTeC 上验证规则使单次准确率降到 65.0%（balanced 57.6%）；完整源库下单次 hybrid 准确率下降 17-29 点，没有 controller 能恢复；714 条 Wikipedia claims 上 agent 也无明显增益。
