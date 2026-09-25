---
title: When Does Action Credit Need Updating?
title_zh: 何时需要更新动作信用？
authors:
- Hongye Yang
- Boxiao Huang
affiliations:
- Georgia Institute of Technology
arxiv_id: '2609.29007'
url: https://arxiv.org/abs/2609.29007
pdf_url: https://arxiv.org/pdf/2609.29007
published: '2026-09-24'
collected: '2026-09-25'
category: Agent
direction: 工具智能体动作价值更新门控
tags:
- tool-using agents
- action credit
- policy drift
- credit transport
- decision gate
one_liner: 提出基于分支敏感度的动作信用传输与决策充分门控，显著减少策略更新后的工具交互重算成本。
practical_value: '- 在线策略更新后，不必全量重新收集交互数据来更新动作价值（如工具选择、商品排序），可复用旧轨迹并做一阶修正估计新策略下的价值，减少标注和模拟成本。

  - 用 pairwise branch sensitivity 代替全局 KL/参数距离，衡量策略更新对特定两个候选动作（如两个工具、两个商品）排序的影响，精准识别哪些历史信用仍可复用。

  - DSC-Gate 的决策充分门控思路：对比估计价值差与漂移阈值，决定 reuse/transport/resample，可作为推荐系统在线学习、A/B 测试或
  Agent 工作流中节省样本和算力的工程策略。

  - 在电商客服 Agent 等工具调用场景，策略微调后可用历史交互数据做信用传输，避免每次重新模拟或真实环境交互，降低维护成本。'
score: 7
source: arxiv-stat.ML
depth: abstract
---

动机：工具使用 Agent 不断更新策略，但每次更新后历史动作信用（action credit）可能过时，重算代价高。核心问题是何时需要更新信用，而非盲目重算。

方法：作者观察到动作价值变化不一定改变最终决策，只要策略漂移不足以翻转动作排序，历史信用仍可复用。为此引入 pairwise branch sensitivity，度量策略更新对区分两个候选动作的下游分支的影响程度；基于此推导一阶 anchored credit-transport 估计器，利用旧交互轨迹修正信用；并提出 Decision-Sufficient Credit Gate (DSC-Gate)，根据分支敏感度和价值差距动态选择 reuse、transport 或 resample。

结果：实验表明 branch sensitivity 比全局策略距离更能解释信用漂移；有足够历史数据时，credit transport 降低估计误差，其决策收益集中在影响动作区分分支的更新上。在独立测试集上，DSC-Gate 相比 gap-based gate 仅增加平均 regret 0.00004，却将平均新增工具步骤从 472 降至 286，减少 39.4%；真实工具 Agent 参数更新后同样有效。结论：不必每次策略更新都重算动作信用，大部分历史证据可复用或廉价修正。
