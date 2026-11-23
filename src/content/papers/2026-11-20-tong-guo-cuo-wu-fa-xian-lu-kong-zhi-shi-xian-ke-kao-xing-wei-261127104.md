---
title: Reliable Behavior Discovery via False Discovery Rate Control
title_zh: 通过错误发现率控制实现可靠行为发现
authors:
- David Madras
- Zi Wang
- Marco Andreetto
- Ken Burke
- Caroline Pantofaru
- Utsav Prabhu
affiliations:
- Google DeepMind
arxiv_id: '2611.27104'
url: https://arxiv.org/abs/2611.27104
pdf_url: https://arxiv.org/pdf/2611.27104
published: '2026-11-20'
collected: '2026-11-23'
category: Eval
direction: 行为发现 · FDR 控制
tags:
- False Discovery Rate
- Behavior Discovery
- Large Generative Models
- Multiple Hypothesis Testing
- Reliability
- e-BH
one_liner: 提出 DISCO，用 coarsened e-processes 在行为发现中控制 FDR 并提高检验 power
practical_value: '- 在用户分群、意图挖掘、失效模式发现中，当使用 LLM 生成大量候选标签/模式时，可借鉴 DISCO 的 FDR 控制避免把噪声当成真实用户行为或商品属性，尤其适用于离线批量生成假设后的验证。

  - e-process 支持顺序/迭代检验，可与实时实验或数据流结合，例如不断积累用户反馈后逐步确认或放弃某个投放策略、推荐理由模板，无需预设固定假设数量。

  - 在 Agent 生成推荐解释、商品卖点时，可先自动发现高频共现模式，再用 DISCO 筛选统计显著的模式，减少文案中的虚假归因。

  - 工程实现上可集成到评估 pipeline，对 LLM 输出的行为聚类/规则进行多重检验校正，提升自动化洞察的可信度。'
score: 6
source: arxiv-stat.ML
depth: abstract
---

动机：大型生成模型的行为模式发现（如失效模式）需要统计可靠性，单凭少数案例容易过度推断，LLM 系统本身也存在幻觉问题，因此需要控制错误发现率（FDR）。

方法：论文将行为发现形式化为多假设检验问题，提出 DISCO（Discovery through Iterative Search with COarsened e-processes）。DISCO 基于 e-BH 框架，通过 coarsened e-processes 支持数据依赖的假设数量自适应，逐步迭代搜索候选行为模式，并在温和条件下证明 FDR 控制。

结果：在合成数据和将大型生成模型同时作为发现引擎与目标的实证中，DISCO 都能控制 FDR，且与 eBH 方法相比具有更高统计 power，能发现更多真实模式。
