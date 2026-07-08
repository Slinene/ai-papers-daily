---
title: Faithful or Findable? Evaluating LLM-Generated Metadata for RDF Dataset Search
title_zh: 评估LLM生成元数据在RDF数据集搜索中的忠实性与可检索性
authors:
- Riccardo Terrenzi
- Serkan Ayvaz
affiliations:
- University of Southern Denmark
arxiv_id: '2607.05970'
url: https://arxiv.org/abs/2607.05970
pdf_url: https://arxiv.org/pdf/2607.05970
published: '2026-07-07'
collected: '2026-07-08'
category: Eval
direction: 生成式元数据评估 · 检索效果与忠实性权衡
tags:
- Dataset Search
- Metadata Generation
- Faithfulness
- Retrieval Evaluation
- LLM
- RDF
one_liner: 无约束LLM改写元数据检索效果最好但忠实性最差，基于概貌的改写提供最佳平衡
practical_value: '- 在商品搜索中，用LLM改写标题/描述可提升召回，但需评估忠实性，避免描述与商品实际属性不符，建议仿照本文设计联合评估指标。

  - 可采用基于概貌（profile-grounded）的生成策略，例如利用商品类目、属性或用户画像作为约束，在不牺牲太多检索提升的前提下保证内容可信度。

  - 对合成元数据设置溯源与可解释性机制，例如关联原始字段或提供依据摘要，防止幻觉内容误导搜索排序。

  - 本文的评估框架（同时考量检索效果与生成忠实性）可迁移至推荐系统的特征工程或内容补全场景，用于控制LLM生成特征的风险。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：数据集搜索高度依赖元数据，LLM自动生成或改写元数据正成为检索基础设施的一部分，但既可能提升检索效果，也可能引入不忠实内容，损害信任。研究如何在检索效能与忠实性之间权衡是实际落地的关键。  
**方法**：在RDF数据集上，定义了6种元数据生成设置：原始元数据、简单改写、基于数据集概貌（profile）的改写、图结构引导的改写、以及智能体驱动的图生成。检索效果用NDCG@10评测，忠实性通过人工判定生成内容是否有据可查。综合比较不同设置下的检索提升与忠实性表现。  
**关键结果**：
- 无约束的元数据改写带来最大的检索增益（NDCG提升显著），但忠实性最低，说明语义扩展常脱离原始依据。
- 基于概貌的改写大幅提高忠实性（约80%以上生成有依据），且检索效果仅略低于无约束改写，成为最佳折中方案。
- 智能体图生成忠实性高但检索提升有限，因其依赖结构化数据，灵活性不足。
- 将合成元数据视为系统级IR问题，必须联合评估有效性、来源与可信度，单一指标会误导决策。
