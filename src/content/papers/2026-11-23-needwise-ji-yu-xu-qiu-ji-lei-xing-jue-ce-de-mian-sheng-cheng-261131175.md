---
title: 'Needwise: Generation-Free Conversational Recommendation from Need-Level Typed
  Decisions'
title_zh: Needwise：基于需求级类型决策的免生成对话推荐
authors:
- Sungchul Kim
- Weixiao Huang
- Mekala Raja Sekhar Reddy
- Amrutha Srinivasan
affiliations:
- Adobe Research
- Adobe Inc.
arxiv_id: '2611.31175'
url: https://arxiv.org/abs/2611.31175
pdf_url: https://arxiv.org/pdf/2611.31175
published: '2026-11-23'
collected: '2026-11-24'
category: RecSys
direction: 对话推荐 · Typed Decision
tags:
- Conversational Recommendation
- Typed Decision Models
- Need-Level Evidence
- Preference State Tracking
- Generation-Free Ranking
one_liner: 用 typed decision 替代生成式 LLM，以 must-first 组合硬约束与需求级证据做对话推荐，质量对齐强 LLM ranker
  且成本大降
practical_value: '- 在属性驱动的对话推荐/搜索中，可以用 typed decision model 做 need-level verify：对每个候选-属性对问
  supported/contradicted/unknown，用 p_s - p_c 作为证据，unknown 计 0，避免把记录缺失当作负证据；这能替代部分
  LLM listwise re-rank，降低延迟和 API 成本。

  - 维护显式 typed feature state，而不是每轮重读对话：把消息映射到 catalog 字段值 + 用户原话需求，存下 (item, feature)
  级 verdict；撤回、反转、切回需求时复用已有判断，非 request 轮不触发重排。适合多轮 query/筛选式导购场景，但要注意撤回识别偏弱，需增加确认或软状态处理。

  - 采用 must-first 分层：category/location/price 等硬约束单独成 tier，永远不被软偏好证据覆盖；tier 内再将 holistic
  判断与 per-need 证据做等权组合。这条对电商/广告排序很实用，能同时保证业务硬规则、可解释性和文本相关性。

  - 解释层用 embedding 短列表 + typed request 做 schema-first 映射，无法落字段的需求保留用户原话并从文本中验证；但产品类型等
  hard predicate 一旦识别错，会整体降权相关 item，因此硬字段识别要更保守。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

动机：对话推荐中，真实需求常超出 catalog schema（如 cozy、not too touristy），且需求会新增、撤回、反转、切换。LLM ranker 每轮重读全部对话再排序，慢、贵，且排序不暴露 item 满足哪些 need，也不区分“未满足”与“记录缺失”。因此需要结构化的免生成方案。

方法关键点：
- 解释层：每轮对 message 做 typed request，先从 catalog 字段值构建短列表，判断每个值 want/avoid/neither；无法映射到字段的需求保留用户原话作为 inferred feature，极性统一。
- 状态跟踪：同一 typed request 判断是否 request、延续/新开/返回，并逐条判断历史 need 是保留、撤回还是反转；按 transition 路由决策，存复用 (item, feature) verdict，撤回/反转等无需重新 judge。
- 候选评分：每对 (candidate, inferred feature) 三选一 supported/contradicted/unknown，evidence = p_s - p_c；unknown 不计负分。Needwise-F 用 hard tier + soft mean；Needwise-H 用 4 级 holistic；Needwise-HF 先硬 tier，再 1/3 holistic + soft evidence，权重相等、无需调参。
- 排序只看概率分布，不用 argmax，可能 unknown 最高但 p_s-p_c 非零。

关键实验：Google Local / Yelp，属性 withheld，同 pool 重排。单请求 nDCG@10：GL Needwise-HF 0.383 vs GPT-6 Sol 0.343，显著更好；Yelp 0.428 vs 0.412，与最强 LLM ranker 无显著差异。成本 $3.00/1k vs $43/$69，延迟 2.5s vs 5.6s。对话中 typed state 显著提升 Needwise-H P2-4（+0.056/+0.047），但撤回识别仅 19%/27%。

一句话：typed decisions 加 must-first 组合能在对话推荐里以低一个量级成本对齐强 LLM ranker，瓶颈在 interpretation 与撤回识别。
