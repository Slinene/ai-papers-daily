---
title: 'Explaining When PRF Fails: Participatory Auditing for Selective Query Expansion'
title_zh: 解释伪相关反馈何时失效：面向选择性查询扩展的参与式审计
authors:
- Zeyan Liang
- Graham McDonald
- Iadh Ounis
arxiv_id: '2607.12098'
url: https://arxiv.org/abs/2607.12098
pdf_url: https://arxiv.org/pdf/2607.12098
published: '2026-07-13'
collected: '2026-07-15'
category: QueryRec
direction: 查询扩展·选择性PRF·LLM审计
tags:
- Pseudo-Relevance Feedback
- Selective Query Expansion
- Query Drift
- LLM Reranker
- Explainability
- Participatory Audit
one_liner: 通过用户审计量化PRF的损害并优先避免，用LLM重排序器自动预测选择性决策并给出可解释证据
practical_value: '- 在搜索/广告/推荐场景的查询扩展模块中，可引入参与式审计（小规模用户测评）来标定真实体验风险，发现哪些查询因扩展导致漂移，量化避免损害的价值

  - 用LLM重排序器作为选择性查询扩展的决策器：输入原始查询和候选扩展词，让LLM基于文档证据预测用户偏好（受益或受损），并提供可检查的文本解释，实现审计自动化

  - 架构上采用「先审计后自动化」两阶段：先用用户标签构建偏好数据集，再训练或微调LLM预测器，让系统决策与用户感知对齐，而非仅依赖QPP统计量

  - 业务中面对高风险查询（如品牌词、长尾精确词），优先遵循「避免伤害」原则，在扩展收益不确定时保守处理，将拦截损害的价值置于放大成功之上'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机** 伪相关反馈(PRF)在平均指标上改善检索，但隐藏在均值背后的查询漂移会显著恶化部分查询。现有选择性PRF(sPRF)依赖查询性能预测(QPP)，这些预测与造成漂移的排序统计同源，未能真正解决不透明性。核心痛点是缺乏用户感知的标定与可解释的决策。

**方法** 提出审计-自动化两阶段框架。阶段1：对43个TREC DL 2019查询进行108名用户参与式审计，让用户直接对比PRF扩展前后搜索结果，标注“受益”“受损”或“无差异”。结果显示仅20.9%查询受益，25.6%查询体验下降，且避免损害的价值几乎是利用成功扩展的两倍。阶段2：将LLM重排序器改造为系统偏好预测器，输入原始查询及其扩展词，结合检索到的文档，要求LLM同时给出二元决策（是否应用PRF）和基于文档证据的自然语言解释，从而自动复现用户标签，并让决策可被审计。

**关键结果** 用户审计揭示了PRF失败的高发与严重性；LLM预测器在复制用户偏好上达到较高一致性，且通过文档证据使每个sPRF决策可追溯。整套方案将不透明的查询扩展组件转变为可审计、与用户感知对齐的组件。
