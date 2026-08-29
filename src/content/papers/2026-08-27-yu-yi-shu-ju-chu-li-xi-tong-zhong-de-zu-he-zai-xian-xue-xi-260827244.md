---
title: Compositional Online Learning for Semantic Data Processing Systems
title_zh: 语义数据处理系统中的组合在线学习
authors:
- Paweł Liskowski
- Fuheng Zhao
- Benjamin Han
- Anupam Datta
- Dimitris Tsirogiannis
affiliations:
- Snowflake Inc.
arxiv_id: '2608.27244'
url: https://arxiv.org/abs/2608.27244
pdf_url: https://arxiv.org/pdf/2608.27244
published: '2026-08-27'
collected: '2026-08-29'
category: Other
direction: LLM 语义数据系统在线优化
tags:
- online learning
- semantic data processing
- LLM cost optimization
- adaptive query processing
- Cortex AISQL
one_liner: 在 LLM 调用边界组合多个在线学习组件，将训练更新隐藏在慢速 LLM 往返中，优化语义数据查询成本
practical_value: '- 借鉴「LLM 往返延迟内做在线学习」：在电商搜索/推荐中，LLM 调用（如 query 理解、商品文案生成）占比高且慢，可以把轻量在线模型更新（如缓存命中率统计、过滤排序权重）藏在调用间隙，不增加额外延迟。

  - 分层组件化优化：对应业务中的 memoization（query-LLM 结果缓存）、per-call 过滤排序（相似商品/评论筛选时先过滤掉明显不相关项）、cascade
  routing（简单请求走小模型/规则，复杂请求走大模型）。每个组件对应一个成本因子，可独立更新、组合叠加。

  - 条件成本分解与乘法下界：优化 LLM pipeline 时，先按「每行 LLM 成本 = 调用次数 × 每次成本 × 选中行数」拆解，不同组件负责不同因子，组合后可获得乘性加速；实测从
  11.4x 理论界降为 ~8x。

  - 在线学习更新节奏分 per-call 和 per-batch：per-call 适合高频轻量参数（如排序分数），per-batch 适合阈值/路由策略，避免过拟合和样本预算浪费。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：语义数据处理系统（如 Cortex AISQL）对每行数据调用 LLM，LLM 成本占查询成本 80–90%，单次调用是关系谓词的 10^5–10^7 倍，且延迟高到可以在往返中隐藏 CPU 侧在线学习更新。

**方法关键点**：在 LLM 调用边界构建组合在线学习框架，设计空间覆盖决策粒度和更新节奏两个维度。生产案例组合三个组件：memoization 层缓存重复调用；per-call 过滤排序学习器优化过滤谓词顺序以减少 LLM 调用；per-batch 级联路由学习器选择大小模型。每个学习组件通过一个共享学习模式，将训练步骤隐藏在下一次 LLM 往返延迟中。

**关键结果**：条件成本分解将每个学习组件映射到每行 LLM 成本的不同因子。在独立性假设下，两个学习组件乘法组合，对代表性 conjunction-filter 工作负载给出 11.4× 的上界。考虑级联边界自选择、样本预算收缩和选择性估计漂移后，实际加速接近 8×。
