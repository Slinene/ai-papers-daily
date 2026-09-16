---
title: Evaluating Brand Retrieval and Ranking in Large Language Model Recommendations
title_zh: LLM 品牌推荐的检索与排序评估框架
authors:
- Edward Malthouse
- Kun-Yu Lee
- Jing Yang
- Sanchary Pal
- Xueyan Feng
affiliations:
- Northwestern University
- Boston University
arxiv_id: '2609.16304'
url: https://arxiv.org/abs/2609.16304
pdf_url: https://arxiv.org/pdf/2609.16304
published: '2026-09-14'
collected: '2026-09-16'
category: Eval
direction: LLM 推荐评估 · 随机检索排序
tags:
- LLM evaluation
- brand recommendation
- BRP@k
- MRR@k
- stochastic retrieval
- popularity bias
one_liner: 提出基于重复采样的 BRP@k / MRR@k 框架，将 LLM 品牌推荐视为随机检索与排序过程
practical_value: '- 在电商/广告场景用 LLM 直接推荐品牌或商品时，不要把单次输出当稳定排序；应做多次重复采样，用 BRP@k 和 MRR@k
  估计品牌/商品出现概率与排名分布，避免误判模型偏好。

  - 品类词泛 query 会系统性遗漏大量成熟品牌，且 LLM prominence 与传统销量/品牌热度关联有限，更贴近搜索热度、线上讨论声量等全域可见度信号；做
  LLM 品牌曝光优化时，应重点运营搜索与内容生态，而不是只堆 GMV。

  - 需求化 prompt 会显著改变品牌检索集合；如果想让某些品牌在 LLM 推荐中被召回，不要只依赖品类词，可以在 prompt 中植入用户目标、约束或差异化卖点，类似于
  GEO 的 prompt 策略。

  - 诊断 probe 可识别“条件可检索品牌”：品牌在泛 prompt 下不出现，但提供独特线索后能被召回。这可用于评估品牌语义关联是否被 LLM 学到，并指导品牌描述、属性标签和内容投放。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：LLM 越来越多被用于产品推荐，但其开放生成特性带来新挑战：没有固定候选集，同一 query 多次回答会产出不同品牌和排序，传统 IR/推荐评估方法不适用。

**方法关键点**：提出独立于模型输出定义竞争集的评估框架，通过重复采样估计品牌被推荐的 prevalence 与 prominence。具体用 Brand Recommendation Probability (BRP@k) 度量品牌被推荐概率，用 Mean Reciprocal Rank (MRR@k) 度量排名位置；在六个 LLM、五个产品品类上测试品类-only query、需求-based query 和诊断性定位 probe。

**关键结果**：品类-only query 下 LLM 大量遗漏既有知名品牌；推荐 prominence 与传统品牌热度关联有限，更多与搜索兴趣、线上品牌讨论等 marketplace-visibility 信号相关；需求化 query 会改变被检索品牌集合；提供差异化线索后，普通推荐中被遗漏的品牌可被条件检索。结论是应把 LLM 推荐作为随机检索-排序过程评估，而不是只看单条生成列表。
