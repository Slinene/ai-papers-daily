---
title: 'EXCISE: Query-Side Exclusion for Late-Interaction Retrieval'
title_zh: EXCISE：查询端排除模块修正后期交互检索的排除反转问题
authors:
- Mohammed Ali
- Abdelrahman Abdallah
- Adam Jatowt
affiliations:
- University of Innsbruck
arxiv_id: '2608.05497'
url: https://arxiv.org/abs/2608.05497
pdf_url: https://arxiv.org/pdf/2608.05497
published: '2026-08-06'
collected: '2026-08-07'
category: Other
direction: 查询端排除修正 · 后期交互检索
tags:
- late-interaction retrieval
- exclusion query
- query-side module
- ColBERT
- exclusion inversion
one_liner: 用查询端轻量模块识别排除主题并重排，无需修改索引，大幅提升排除查询准确率。
practical_value: '- 对现有多向量检索系统（如 ColBERT），可加接 1.5M 参数的查询端模块，识别排除主题并对候选降权，无需重建索引，工程成本低。

  - 电商搜索中常有排除条件（如“连衣裙 不是红色”），可直接复用该方法，冻结基础检索器，仅部署查询端校正，提升排除查询满意度。

  - 方法中的无参数降权规则简单有效，可快速集成到线上服务，对短列表重排延迟影响小。

  - 配套发布的 X-BENCH 基准可用于评估自身系统对显式、隐式及复合排除查询的处理能力，定位召回缺陷。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：晚期交互检索器（如 ColBERT）的 MaxSim 评分在面对排除查询（“X 但不含 Z”）时会产生**排除反转**：包含排除主题 Z 的文档反而得分更高，导致不相关内容排在前面。现有方法无法通过冻结向量直接读出排除约束，因为识别“应该排除什么”依赖查询本身。

**方法**：EXCISE 在查询端操作，保持索引不变。两个查询端模块（共 1.5M 参数）分别识别排除主题，并对前 100 候选重嵌入；再用一个无参数规则对匹配排除主题的文档进行降权。整个过程不修改或微调索引。

**结果**：在 6 个数据集和 3 个骨干模型上，EXCISE 在全部 18 个骨干-集合组合中均超越冻结与微调基线。ExcluIR 上的排除成功@10 从 0.058 提升至 0.691，布尔 NOT 准确率从 0.25-0.29 提升至 0.90-0.92。汇总 1,860 个查询，EXCISE 超过所有微调交叉编码器，且在其最强骨干上与冻结基线的无损害 nDCG@10 持平。同时发布了包含显式、隐式及复合排除的基准 X-BENCH。
