---
title: Event-Time Confounding Under Bursty Human Dynamics
title_zh: 突发人类动态下的事件时间混杂
authors:
- Michael Iannelli
- Alan Ai
affiliations:
- Scrunch AI
arxiv_id: '2608.21294'
url: https://arxiv.org/abs/2608.21294
pdf_url: https://arxiv.org/pdf/2608.21294
published: '2026-08-21'
collected: '2026-08-24'
category: Other
direction: 因果推断 · 事件研究偏差诊断
tags:
- causal inference
- event-study
- endogenous time zero
- episode-selection bias
- negative controls
- web log analysis
one_liner: 揭示行为日志中用户自选事件时间导致的片段选择偏差，并提供诊断协议与审计工具
practical_value: '- 评估 AI 助手、推荐点击或广告曝光后的增量效果时，不要仅对比事件前后活动量，因事件常发生在用户已有任务片段中；应引入 known-null
  对照（如随机时间戳或非事件时间点）并匹配事件前的活动轨迹，避免将任务延续误判为干预效应。

  - 在 A/B 测试或因果归因分析前，可集成论文中的诊断协议或使用 burstcheck 工具审计日志：检查事件前活动是否已开始上升、事件后活动是否只是片段自然衰减；这能有效识别并过滤存在
  episode-selection bias 的数据。

  - 用户固定效应和粗粒度活动匹配（如按日活分层）无法消除这种时变混杂，建议在工程中改用 episode 级别匹配：找到具有相似爆发模式但无目标事件的用户片段作为对照，或在同一用户内匹配有事件与无事件的活动片段。

  - 该结论对搜索、推荐、广告的归因分析同样适用：例如用户点击推荐后转化提升，可能只是用户购买旅程中的自然波动；需要与未点击的类似片段比较，而不是简单依赖点击后窗口内的指标。'
score: 7
source: arxiv-cs.HC
depth: abstract
---

**动机**：数字行为研究常用事件窗口设计，将用户自选事件（如打开 AI 助手、点击推荐、访问商品页）对齐为时间零点，将之后的活跃度上升解释为事件效应。但事件往往发生在用户正在进行的任务片段中，事件后的活动增加可能只是任务片段的延续，而非对事件的响应，导致因果推断出现偏差。

**方法关键点**：
- 利用同用户跨表面网络日志，观察事件前活动模式，发现 AI、购物、新闻、编码、参考等事件前均有活动增加，峰值在时间零点之前。
- 使用 known-null 时间戳（已知不会引起任何效应的时间点）作为对照，并与 within-user placebo 比较，以量化偏差大小。
- 形式化该现象为 episode-selection bias（片段选择偏差），证明单表面事件窗口在无额外假设下无法区分真实效应与任务延续。
- 通过零效应模拟展示用户固定效应和粗粒度活动匹配为何失效：混杂是 within-user 且随时间变化的。
- 提供诊断协议、公开数据基准和轻量审计工具 burstcheck。

**关键结果数字**：
- 在满足严格前事件活动和洗脱条件的 5.8% AI 响应中，known-null 时间戳的事后搜索活动是 within-user placebo 的 3.42 倍，而真实事件为 4.32 倍。
- 已知无效时间戳复制出的超额部分在可检测活跃时刻为 0.56，在安静时刻降至 -0.04，此时设计检测不到任何效应。
