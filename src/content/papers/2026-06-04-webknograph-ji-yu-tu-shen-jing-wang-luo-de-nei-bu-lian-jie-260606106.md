---
title: 'WebKnoGraph: GNN-Powered Internal Linking'
title_zh: WebKnoGraph：基于图神经网络的内部链接评估框架
authors:
- Emilija Gjorgjevska
- Georgina Mirceva
- Miroslav Mirchev
affiliations:
- Technical University of Munich
- Ss. Cyril and Methodius University in Skopje
arxiv_id: '2606.06106'
url: https://arxiv.org/abs/2606.06106
pdf_url: https://arxiv.org/pdf/2606.06106
published: '2026-06-04'
collected: '2026-06-07'
category: Other
direction: SEO·内部链接评估·图学习
tags:
- SEO
- Internal Linking
- GraphSAGE
- PageRank
- Semantic Coherence
- Link Evaluation
one_liner: 用GraphSAGE评分候选内部链接并嵌入主机环境图，评估权威度与语义连贯性影响
practical_value: '- 电商网站商品页、分类页间的内部链接优化可借鉴GraphSAGE预测语义连贯性作为链接评分，替代人工规则。

  - 多指标联合评估（权威收益、语义成本、波动性、损失-收益比）的思路可直接用于推荐系统中物品关联关系的离线评估，避免单一指标误导。

  - 构建host-level环境图模拟外部影响的方法，可迁移到电商推荐中评估跨域或跨店铺链接的效果。

  - 自动化生成候选集+专家审核的流水线，适用于电商运营对自动推荐关联商品进行人工把关，平衡流量效率和用户体验。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：SEO内部链接优化依赖人工判断或固定模板，缺乏部署前对权威分布和语义连贯性的量化评估工具。

**方法**：提出WebKnoGraph，将网站建模为有向图，用页面嵌入表示，GraphSAGE评分候选内部链接；通过嵌入更大的主机环境图（FineWeb实证图或BA合成图）评估干预效果，使用基于PageRank的权威度指标（Authority Yield、Volatility、损失-收益比）和语义连贯性进行多维评估。

**结果**：在Kalicube.com爬虫数据上，自动选择通常获得更高Authority Yield但语义损失更大；专家辅助选择更好保持语义连贯性，且在针对低PageRank页面时Authority Yield最高，但损失-收益平衡最差。权威波动性受干预集数量影响需谨慎解读。验证了“大规模生成候选集→多指标联合评估→人工审核”工作流的可行性。
