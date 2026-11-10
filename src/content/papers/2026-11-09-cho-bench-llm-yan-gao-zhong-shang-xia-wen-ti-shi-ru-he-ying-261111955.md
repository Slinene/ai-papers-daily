---
title: 'CHO-Bench: How Do Context Hints Affect Ad Rankings in LLM Advertising?'
title_zh: CHO-Bench：LLM 广告中上下文提示如何影响广告排序
authors:
- Shiqi Zhang
- Yang Fei
- Xiaokui Xiao
affiliations:
- National University of Singapore
- PyroWis AI
arxiv_id: '2611.11955'
url: https://arxiv.org/abs/2611.11955
pdf_url: https://arxiv.org/pdf/2611.11955
published: '2026-11-09'
collected: '2026-11-10'
category: RecSys
direction: LLM 广告排序 · 上下文提示优化
tags:
- LLM Advertising
- Context Hint Optimization
- Ad Ranking
- Benchmark
- Embedding Ranker
- LLM Ranker
one_liner: 构建 CHO 基准，评估广告侧 context hints 对 LLM 广告排序的提升与策略差异
practical_value: '- 在 LLM 广告/对话推荐场景，可在商品卡之外增加面向 ranking 的自然语言 context hints；若 ranker
  是 embedding 相似度，优先写 When/使用场景与 What/产品卖点，利用 max-sim 聚合多条 hints；若 ranker 是 LLM listwise，优先写
  Who/人群与任务，并精选一条最相关 hint 支撑排序。

  - 预算控制上，3~5 条 hints 已接近无约束生成效果，堆到 20+ 边际收益递减；embedding ranker 可适当增加 hints 数量，LLM
  ranker 更应做单条精选，避免上下文膨胀。

  - 采用 paired evaluation 做离线归因：固定 query、候选池和其他广告，只改变目标广告的 hints，比较 Δ Rank / Δ Win，低成本验证文案或上下文策略，适合迁移到电商广告文案优化。

  - 不要盲目拼接所有营销维度：Unified 不一定优于单维度，建议按 generation–ranking 模型组合做 model-specific 选择，后续可训练轻量选择器或
  budget-aware 聚合器。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：LLM 助手和生成式搜索正在成为广告投放新渠道。ChatGPT Ads 允许广告主提供自然语言 context hints，描述 offer 是什么、对谁有用、何时有用，用于在对话场景中排序广告。但 hints 是否有效、不同信息维度如何选择、不同 ranker 和预算下差异如何，此前缺少系统评估。

**方法关键点**：
- 将 Context Hint Optimization（CHO）形式化为固定广告卡、竞价设置和排序函数，只优化 hints 的广告侧排序问题。
- 依据 Value Proposition Canvas 和 Customer Journey 划分 7 个信息维度：What=Product Features/Pain Relievers/Gain Creators；Who=Customer Segments/Customer Jobs；When=Usage Scenarios/Decision Stages；另有 Unified 融合七类。
- 构建 CHO-Bench：5 个数据集（AdLib-US、AdLib-IN、LM-Market、NaiAD、E-GEO），覆盖 general ads 与 product ads；用 embedding ranker（OpenAI/Qwen）与 LLM listwise ranker（GPT/DeepSeek）做 paired evaluation。
- 指标为 Δ Rank、Δ Win，比较同 query 同候选池中有/无 hints 的目标广告排序变化。

**关键结果**：所有策略都带来正增益：Δ Rank +0.56~1.16 位，Δ Win +5.42~14.40 pp；七类单维度平均相近，Who 略优于 When/What，Unified 无一致额外优势；具体 generation–ranking 配置下差异可达 0.57 位，embedding ranker 偏 When，LLM ranker 偏 Who；预算 k 增大有递减收益，3~5 条已接近无约束，embedding ranker 更受益于更多 hints。

最值得记住的一句话：自然语言 context hints 能低成本提升 LLM 广告排序，但选择哪个维度、给多少条，要按 ranker 类型做模型特定优化，不能盲目堆叠全维度。
