---
title: 'Answer-Reconstruction Search Density: Measuring the Query and Source Work
  Compressed by Conversational Answers'
title_zh: 回答重建搜索密度：量化对话式答案的查询与来源压缩工作量
authors:
- Benjamin Tannenbaum
affiliations:
- Aiso, Tel Aviv, Israel
arxiv_id: '2607.18904'
url: https://arxiv.org/abs/2607.18904
pdf_url: https://arxiv.org/pdf/2607.18904
published: '2026-07-21'
collected: '2026-07-26'
category: QueryRec
direction: 对话搜索评估 · 查询压缩度量
tags:
- conversational search
- query decomposition
- set cover
- evaluation metric
- answer reconstruction
- search density
one_liner: 提出 ARSD 度量，用最小查询次数覆盖答案信息单元，量化对话系统对搜索工作的压缩程度
practical_value: '- 在电商对话Agent中，可用类似集合覆盖度量评估生成答案的信息密度，判断一次回答替代了多少次传统搜索，指导摘要长度与粒度优化。

  - 对RAG生成的商品对比或推荐理由，可定义可检索信息单元，计算所需最少查询数，作为回答效率KPI，嵌入A/B测试。

  - 查询分解策略设计时，可将ARSD作为奖励信号，训练模型用更少子查询覆盖关键信息，降低下游检索成本。

  - 页面密度指标可分离查询压缩与来源压缩效应，帮助定位是提问不够聚焦还是答案引用冗余，指导改写或结果聚合模块的迭代。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**  \n对话系统能将多轮搜索、结果检查、来源对比压缩为一个合成答案，但缺乏度量来量化这种压缩体现的传统搜索工作量。现有指标评估排序、努力或事实支撑，未回答“一个答案替用户省了多少次手动查询”。论文定义回答重建搜索密度（ARSD）：在固定且标注时间的重建策略下，覆盖答案中可检索原子单元指定比例所需的最小 distinct 查询次数，并辅以页面密度区分查询压缩与来源压缩。  \n\n**方法关键点**  \n- 将答案分解为可检索原子单元（如事实、观点），用一组查询原型（facets）作为集合覆盖的“集合”，求最小覆盖子集。ARSDₓ 为覆盖 x% 单元的最少 facet 数。  \n- 采用结构化facet-cover诊断：在183个信息寻求对话中用2,176个 retained 单元，人工构造 facets，计算精确覆盖。  \n- 6个合成任务、36条固定查询的实时Web校准，验证可度量性。  \n- 用Poisson模型、Bootstrap 置信区间分析多轮对话与 facet 密度的关联。  \n\n**关键结果**  \n- 对话中，ARSD₈₀ 中位数为 3 个词汇 facet（IQR 2–4），每个 facet 覆盖 3.25 个单元。  \n- 多轮对话比单轮有更高的 facet 密度，但控制答案单元数量后，差异从 +0.90 降至 +0.22（95% CI -0.35–0.78），Poisson 回归 IR 从 1.32 降至 1.06，说明答案长度主导该关联。  \n- 不同答案单元截断（8、12、16）下中位数稳定，相邻相似性策略间秩相关 0.85–0.93。  \n- 实时Web校准中，ARSD₈₀ 中位数 1.5 条查询，页面密度中位数 2 页，首条查询覆盖 70% 单元，证明度量可行性。
