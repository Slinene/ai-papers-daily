---
title: 'Conservative Meta-Agent Search: Architecture Adaptation under Non-Stationarity'
title_zh: 保守元代理搜索：非平稳环境下的架构自适应
authors:
- Ali Atiah Alzahrani
arxiv_id: '2610.31436'
url: https://arxiv.org/abs/2610.31436
pdf_url: https://arxiv.org/pdf/2610.31436
published: '2026-10-22'
collected: '2026-10-25'
category: Agent
direction: 元代理架构搜索与在线自适应
tags:
- Meta-Agent
- Architecture Search
- Non-Stationary
- Risk Control
- Agentic Systems
- Shadow Replay
one_liner: CMAS通过保守提升、切换成本与风险约束降低在线架构搜索的回归与成本，在96个流上优于最强自适应基线
practical_value: '- 在线架构变更采用“影子回放”评估：用共同随机数重放历史流量，对新旧架构计算配对分数，能显著减少评估噪声，适合在电商推荐、广告投放等延迟反馈场景中做
  A/B 测试前的离线消融。

  - 提升门槛加入方差惩罚和切换成本：只有显著优于现任方案才允许上线，避免频繁替换导致系统不稳定。可直接借鉴到电商 Agent 工作流的组件升级策略。

  - 模拟金丝雀阶段与自动回滚：小流量试运行并预设指标阈值，失败自动回滚，降低线上风险。适合部署生成式推荐或广告文案生成等高风险模块。

  - 当新增组件不贡献价值时收缩到最小有效团队，定期剪枝，可减少推理成本与维护复杂度。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：部署的 Agent 系统面临持续漂移、延迟反馈、组件故障和架构切换成本，静态任务套件评估不足以验证元代理设计的在线性能。

**方法关键点**：CMAS 将架构搜索形式化为顺序更替问题，引入切换成本和硬风险约束。它检索存档架构，提出类型化图编辑；采用共同随机数下的配对影子回放进行评分，组件信用为干预式。提升要求经过校准的方差惩罚同时分数高于预设阈值，并通过模拟金丝雀阶段和预定义回滚进行保护。

**关键结果数字**：在 96 个流上，CMAS 将归一化平均替代动态预言遗憾从 0.116 降至 0.104，保留效用从 0.44 提升至 0.48（对比最强自适应基线）；部署推理成本降低约 6%，但搜索总 token 成本最高；每次更新假提升率为 3.4%（名义目标 5%）。
