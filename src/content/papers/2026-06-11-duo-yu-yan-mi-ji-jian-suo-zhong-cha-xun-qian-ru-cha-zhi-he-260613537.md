---
title: When Does Mixing Help? Analyzing Query Embedding Interpolation in Multilingual
  Dense Retrieval
title_zh: 多语言密集检索中查询嵌入插值何时有效？
authors:
- Tongyao Zhu
- Chao-Ming Huang
- Min-Yen Kan
affiliations:
- National University of Singapore
arxiv_id: '2606.13537'
url: https://arxiv.org/abs/2606.13537
pdf_url: https://arxiv.org/pdf/2606.13537
published: '2026-06-11'
collected: '2026-06-14'
category: Other
direction: 多语言密集检索 · 查询嵌入混合策略
tags:
- multilingual dense retrieval
- query embedding interpolation
- code-mixing
- BGE-M3
- typological distance
one_liner: 英语主导非对称性：非英语文档混合查询有益，英语文档索引纯英语最优，英语是最强混合伙伴
practical_value: '- **跨境电商多语言搜索优化**：当商品文档主要为非英语语言时，可以尝试将用户查询的英语翻译与原查询嵌入插值，利用英语作为“锚点”提升跨语言理解，实验中非英语文档索引上混合查询均优于单语查询。

  - **索引语言决定混合策略**：若索引中包含大量英语文档（如全球站），建议保持纯英语查询以获得最佳效果，混合反而有害；该非对称性可指导工程上按索引语言动态选择是否启用查询混合。

  - **选择最佳混合伙伴**：英语与任何非英语语言混合均有增益，且是通用最强伙伴；在多语言Agent或推荐系统中，可优先使用英语变体作为辅助表示，无需为每个语言对单独寻优。

  - **根据语言类型距离调参**：当排除英语干扰后，混合收益与语言间类型距离负相关；对于语法结构相近的语言对（如西班牙语-意大利语），可预期更高混合收益，可用于启发式设计混合比例超参数。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：多语言社区中用户常混合语言表达单一信息需求，但密集检索对这种混合查询的敏感性缺乏系统分析。本文旨在揭示查询嵌入混合对检索性能的影响规律。

**方法**：在mMARCO数据集上，使用BGE-M3编码器获取平行查询的单语嵌入，通过插值（线性加权）构造混合查询嵌入，系统改变混合比例进行检索实验。分析不同文档语言索引下，混合比例与nDCG@10的关系，并考察语言类型距离等因素。

**关键结果**：
- 最优混合比例在88/105个实验设置中超越最佳单语端点，证明混合整体有益。
- 非对称性：对非英语文档索引，混合一致提升性能；对包含英语的文档索引，纯英语查询始终最优。
- 英语作为混合伙伴：对任何非英语文档语言，英语混合均带来最大增益，是最强“锚点”。
- 控制英语效应后，混合收益与语言类型距离显著负相关（如德语-荷兰语收益高于汉语-芬兰语），表明语言结构越近，混合越有效。
- 上述规律在模型规模和系列间保持稳健。

结论：混合语言查询的敏感性是结构化和可预测的，可指导实际多语言检索系统的查询表示设计。
