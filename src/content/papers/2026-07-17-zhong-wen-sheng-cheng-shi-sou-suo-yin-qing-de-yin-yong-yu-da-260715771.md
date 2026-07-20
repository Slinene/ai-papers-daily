---
title: What Do Chinese-Language Generative Search Engines Cite and Surface? A Large-Scale
  Empirical Study
title_zh: 中文生成式搜索引擎的引用与展示：大规模实证研究
authors:
- Tao Zhen
- Yue Liu
- Gege Zhang
- Yixuan Niu
affiliations:
- Aidso Wendao Research Institute, Beijing Aichacha Technology Co., Ltd., Beijing,
  China
arxiv_id: '2607.15771'
url: https://arxiv.org/abs/2607.15771
pdf_url: https://arxiv.org/pdf/2607.15771
published: '2026-07-17'
collected: '2026-07-20'
category: Eval
direction: 生成式搜索评估 · 引用行为分析
tags:
- citation analysis
- generative search
- source attribution
- brand exposure
- GEO
- empirical study
one_liner: 大规模实证分析中文生成式搜索的引用选择、品牌曝光及跨接口差异，揭示品牌选择率仅8.3%
practical_value: '- **内容优化方向转移**：预测品牌是否被生成式搜索引用时，跨源内容一致性（cross-source occurrence count）和内容匹配度比传统百度综合质量分更重要，SEO从业者应调整优化重心至多源内容协同。

  - **监控“无源”品牌曝光**：约13%的品牌曝光无法匹配到抓取的引用池，可能源自模型内部知识。电商品牌需专门追踪AI问答中的直接提及，而非仅依赖抓取结果。

  - **时效性内容半衰期**：高时效性查询被引页面的半衰期约39天，低时效性约68天。营销内容应据此频率更新，以维持生成式搜索中的可见度。

  - **分端优化策略**：同一平台的App与Web接口引用源集存在系统性差异，品牌若追求全端覆盖，需分别监控和优化两端表现，不可混为一谈。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：AI问答系统正重塑信息可见性，从传统搜索排名转向生成答案中的检索、引用和呈现。现有对中文生成式搜索引用行为的系统性理解不足。  
**方法**：在四个主流中文平台的Web与App共八个接口上，使用614个查询，每查询-平台-接口组合重复三次，收集214,119条原始记录，清洗后得到160,860条引用级数据集。构建统一分析框架，研究引用选择、来源归因、实体暴露及跨接口一致性。  
**关键结果**：品牌被选择性展示，整体品牌选择率仅8.3%；12.4%包含联系方式的被引来源将联系信息带入答案。预测模型中，内容拟合度、跨源出现次数和语义角色较为重要，传统百度综合质量分并非主导因子。被引页面半衰期：高时效查询约39天，低时效约68天。约13%的品牌曝光和71%的联系信息曝光无法追溯至抓取的引用池或正文。同一平台App与Web的引用源集合差异显著。结论：中文生成式搜索系统在信息选择、归因和展示上呈现复杂模式，接口类型是关键分析维度。
