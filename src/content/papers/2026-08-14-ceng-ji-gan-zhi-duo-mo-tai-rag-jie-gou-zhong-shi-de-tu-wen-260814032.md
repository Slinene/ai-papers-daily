---
title: 'HAM-RAG: Hierarchy-Aware Multimodal RAG for Structure-Faithful Interleaved
  Generation'
title_zh: 层级感知多模态RAG：结构忠实的图文交错生成
authors:
- Yin Li
- Ziyang Hu
- Zhiyu Guo
- Xiangyu Liu
- Wenbin Li
- Boo-Ho Yang
- Rav Lawana
- Ziyue Li
- Wei Zeng
- Fugee Tsung
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
- ASCETEX INTERNATIONAL LIMITED
- MOVENSYS Inc.
- Schneider Electric
- Technical University of Munich
arxiv_id: '2608.14032'
url: https://arxiv.org/abs/2608.14032
pdf_url: https://arxiv.org/pdf/2608.14032
published: '2026-08-14'
collected: '2026-08-17'
category: RAG
direction: 层级感知多模态RAG
tags:
- Multimodal RAG
- Hierarchy-Aware
- Interleaved Generation
- Image-Text Alignment
- Document Grounding
one_liner: 利用文档层级引导检索与生成，实现多模态RAG中的结构忠实与图文对齐，在多个基准上平均提升17.3%
practical_value: '- 在电商详情页、说明书、SOP等多模态文档RAG中，优先保留文档层级（标题/章节/步骤）作为检索单元，而不是切割成扁平chunk；可将章节路径和父子关系编码进索引和prompt，提升证据选择的忠实度。

  - 对于需要图文交错生成（如商品使用教程、维修指南）的场景，在prompt中保留局部文本-图像对及其在源文档中的位置，可显著减少图片放错和图文不匹配；考虑将图片与相邻文本绑定作为最小检索单元。

  - 构建内部评测基准时，可借鉴HAM-Bench的分类覆盖（攻略/网页/论文/食谱），针对结构化多模态文档设计图文一致性、步骤顺序等指标，而非仅用文本相似度。

  - 工程上，层次化RAG可以结合文档解析工具（如PDF结构抽取、DOM树）自动提取层级，再对同一层内的text和image做关联索引，生成时用层级路径作为约束。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：现有multimodal RAG常将结构化文档扁平化为孤立的文本和图像单元，丢失源组织结构和局部图文逻辑，导致证据选择与放置不忠实。

**方法关键点**：HAM-RAG以文档层级（章节、步骤等）作为grounding信号贯穿检索与生成，在prompt中保留源位置和局部文本-图像关系；引入HAM-Bench，覆盖Wukong游戏攻略、Wiki网页、arXiv论文和Recipe食谱四类结构化文档。

**关键结果**：在多个backbone上，HAM-RAG的主要多模态平均分比最强非层级基线高17.3%；在Wukong上Img-CBS提升24.2%，表明局部图文对齐显著改善；消融证实文档层级是关键信号。
