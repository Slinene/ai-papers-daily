---
title: Teaching Language Models to Narrow Boolean Patent Searches from Search Feedback
title_zh: 用搜索反馈教会语言模型收窄布尔专利检索式
authors:
- Seiya Kawano
- Koji Marusaki
- Hirofumi Nonaka
- Koichiro Yoshino
affiliations:
- Kyoto Institute of Technology
- Guardian Robot Project, RIKEN
- Nagaoka University of Technology
- Aichi Institute of Technology
- The University of Osaka
arxiv_id: '2611.22270'
url: https://arxiv.org/abs/2611.22270
pdf_url: https://arxiv.org/pdf/2611.22270
published: '2026-11-17'
collected: '2026-11-18'
category: QueryRec
direction: LLM 生成布尔查询 · 反馈驱动适配
tags:
- Boolean query
- LLM
- offline adaptation
- patent retrieval
- search feedback
one_liner: 从日本专利局检索报告蒸馏专家策略，用行级引用保持的收窄信用离线适配LLM，将引文所在集合中位数从768降至50以内
practical_value: '- 可复用「执行-评分-再学习」的闭环：对 LLM 生成的召回表达式/query 用线上反馈（点击、转化、引用）构建偏好数据，做
  offline RL 或 DPO，不需任何标注。

  - 把 query 拆成「行级」信用分配，定位哪些词/条件让目标商品或文档保留在更小的候选集里，适合优化「召回集合过大」的生成式 query。

  - 将筛选成本写进 reward，而非只奖励命中：电商搜索里可以同时奖励「目标商品排名靠前且结果集可控」，避免 L2R/生成式模型偏向高召回但大海捞针。

  - 策略级与行级奖励互补的结论值得借鉴：先用策略级偏好学习保召回，再用行级收窄信用压候选集，类似两阶段精排/召回优化。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**
专利审查员写布尔查询时逐行扩展和收窄，既要覆盖相关文献，又要控制需人工筛选的文档量。现有 LLM 直接生成查询能高召回，但命中集合过大，不符合专业搜索实践。

**方法关键点**
作者从 38,397 份日本专利局检索报告提炼出可执行的专家策略并重新执行，用引用召回率和包含每篇引用的最小集合评估。针对 generator，提出两种离线适配：
1. **策略级学习**：用 screening-aware 的策略分做偏好学习，兼顾召回与集合大小。
2. **行级学习**：用 citation-preserving narrowing credit 给查询行赋权，让保留命中引文且集合更小的行获得更高权重，再做生成式微调。

**关键结果数字**
- 相同 rollout 下，行级 credit 在 screening 指标上优于策略级打分。
- 迭代行级学习后，包含引文的文档集合中位数从 768 降至 **50 以下**。
- 更多引文被放进 <100 文档的集合，比专家策略更集中，但召回有所下降。
- 策略级偏好学习可达到接近完备的召回（near-complete recall）。
- 两种方式互补：策略级保召回，行级压候选集。
