---
title: Repeated Queries Exhaust an LLM's Brand Recommendations but Not Its Sources
title_zh: 生成式搜索的采样完整性：重复查询下品牌与引用域累积
authors:
- Dmitrij Żatuchin
affiliations:
- Estonian Entrepreneurship University of Applied Sciences (EUAS)
- Rankfor.AI
arxiv_id: '2609.05059'
url: https://arxiv.org/abs/2609.05059
pdf_url: https://arxiv.org/pdf/2609.05059
published: '2026-09-04'
collected: '2026-09-08'
category: Eval
direction: LLM品牌推荐的采样完整性评估
tags:
- LLM
- sampling completeness
- rarefaction
- brand recommendation
- retrieval-augmented
- generative search
one_liner: 通过稀疏化与Chao2评估，发现无检索LLM品牌推荐持续新增，检索收敛品牌但引用域名不饱和
practical_value: '- 在电商品牌监控、竞品分析或LLM选品/品类拓展中，不要依赖单次或少量运行；应做多次采样（5-10次以上），用开放抽取而非固定候选表，否则会误判覆盖度并漏掉长尾品牌。

  - 为LLM增加检索（RAG）可显著收敛品牌推荐列表，适合需要稳定主流品牌的场景（如搜索结果页优先展示、品牌白名单），但须知道引用来源/域名仍会持续增长，合规审查仍需多次采样。

  - 跨引擎聚合很关键：中位每个query涌现38个组织，约15个仅出现在单一引擎；构建品牌库、竞品库或黑名单时应跨平台/跨模型收集，单引擎覆盖不足。

  - 用稀疏化曲线（rarefaction）和Chao2估计器可以量化“还有多少未观测到”，可作为生成式推荐系统评估指标，监控输出多样性是否被吃干。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：LLM回答商业购买问题（如品牌推荐）存在随机性，传统审计/品牌追踪通常单次或少量运行，隐式假设已覆盖模型可输出的全部品牌/来源。该论文检验重复相同query下的累积结构，区分有无检索增强。

方法：将运行视为抽样单元，品牌或引用域名视为“物种”，使用经典生态学累积方法：精确稀疏化曲线A(k)（任意k次运行期望去重项数）、Q1比例（仅出现一次的项）、Chao2丰富度下界。研究包含300个question-engine cells（50问题×6引擎×15次运行），开放抽取1470个经裁定组织；另加四个深度cell和固定名单抽取对照。

结果：五种无检索引擎在15次运行后仍有86-92%的cells在新增品牌，中位品牌库15-31个；唯一检索增强引擎中位仅8个，64%的cells仍新增，符合深度实验里10次饱和。但引用域名在所有水平持续增长，深度实验24次仍有增长，仅观测到Chao2下界的59-84%。单次运行仅见62-77%的五次运行品牌集；跨引擎中位38个组织，15个仅在该引擎出现。固定名单抽取制造平台假象，开放抽取揭示真实累积。
