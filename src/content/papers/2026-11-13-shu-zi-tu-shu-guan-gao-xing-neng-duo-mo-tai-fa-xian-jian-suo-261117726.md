---
title: 'Towards High-Performance Multimodal Discovery: Evaluating Retrieval Efficacy
  and Operational Scalability in Digital Libraries'
title_zh: 数字图书馆高性能多模态发现：检索效能与可扩展性评估
authors:
- Krishna Priya
- Sai Navya Jyesta
- Sachith Withana
- Neelesh Karthikeyan
- Beth Plale
affiliations:
- Indiana University Bloomington
- University of Oregon
arxiv_id: '2611.17726'
url: https://arxiv.org/abs/2611.17726
pdf_url: https://arxiv.org/pdf/2611.17726
published: '2026-11-13'
collected: '2026-11-16'
category: Multimodal
direction: 多模态向量检索与向量库可扩展性评估
tags:
- Multimodal Retrieval
- Vector Database
- VLM Embeddings
- Digital Libraries
- Scalability
- Semantic Search
one_liner: 把页面整体转为图文统一向量，在向量库中实现多模态检索，并验证精度提升与亚线性扩展性
practical_value: '- 电商商品详情页、海报、图文混排内容可借鉴整页向量化：用 VLM 对图片+文本区域统一编码，替代仅 OCR 文本建倒排，提升对视觉风格、结构图、复杂布局的语义召回。

  - 向量数据库配置是生产化关键：即便 embedding 质量高，也需实测 HNSW/IVF 索引、分片、量化参数，观察 recall@k 与 QPS/延迟权衡，确保数据规模增长时延迟与资源增长保持亚线性。

  - 用数值向量代替明文文本检索可降低版权/合规风险：电商场景涉及商品描述、用户评论等敏感内容时，向量索引既能匹配语义又减少原文泄露或逆向还原。

  - 评估框架可直接迁移：构建包含图表/多模态查询的基准集，同时报告精度指标（如 nDCG）与扩展性指标（QPS、延迟随库规模变化），避免只优化离线精度而忽视线上吞吐。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

动机：百万级数字图书馆（如 HathiTrust 1700 万+卷）中查找特定研究或教育材料日益困难，传统倒排索引（Lucene/Solr）只做字符串匹配，对页面中的图表、注释和复杂布局“视而不见”。

方法关键点：将页面图像整体转为数值向量，不再依赖 OCR 提取文字建索引；用 VLM 分别对页面上的文本区域和视觉区域生成 embedding，融合图文语义后存入向量数据库进行检索。评估分为语义精度和架构可扩展性两部分，重点考察向量数据库配置对生产化的影响。

关键结果：融合视觉与文本特征显著提升检索相关性，尤其在图表内容对概念理解至关重要的领域；系统扩展性呈亚线性，即馆藏规模增长时检索延迟/资源增长低于线性，可水平扩容支撑生产环境；优化的向量数据库配置（如索引类型、分片、量化）是把 VLM embedding 转化为 library-scale 发现方案的决定性因素。
