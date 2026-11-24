---
title: 'VistaTree: Question Answering over Long Multimodal Documents with Image-Derived
  Summary Trees'
title_zh: VistaTree：基于图像摘要树的长多模态文档问答
authors:
- Yexiang Cheng
- Xiaochen Zheng
- David Tokar
- Tatyana Y. Doktorova
affiliations:
- Translational Safety Assessment and Computational Toxicology, Roche, Basel, Switzerland
arxiv_id: '2611.29419'
url: https://arxiv.org/abs/2611.29419
pdf_url: https://arxiv.org/pdf/2611.29419
published: '2026-11-22'
collected: '2026-11-24'
category: RAG
direction: 长文档多模态RAG · 图像摘要树
tags:
- Multimodal RAG
- Document QA
- Summary Tree
- Vision-Language Model
- Hierarchical Retrieval
one_liner: 提出从渲染页面图像构建层级摘要树，用区分性节点摘要做长多模态文档选择性检索问答
practical_value: '- 电商商品详情长图、广告素材审核、平台规则等长文档问答场景，可借鉴“渲染页面图像直接建摘要树”的方式，绕过文本解析，保留表格/图表证据，减少OCR错误。

  - “递归分组 + 兄弟摘要精炼”能区分相似章节或相邻卖点，适合迁移到商品类目层级摘要、活动规则差异标注等结构化管理。

  - 查询时当全局outline超出context预算，采用层级导航逐层选择节点，在检索成本与答案质量之间做折中；本地部署VLM适合敏感数据合规场景。

  - 评估时量化全局索引 vs 层级索引的访问性能差距，业务落地上可先测差距再决定是否牺牲少量精度换取更低成本。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：长多模态文档如临床研究报告常达千页，包含文本、表格、图，外部托管模型受隐私限制，本地视觉语言模型又受context window限制；且长上下文不一定有效利用证据。传统稠密检索基于相似度，面对重复主题和术语时难以区分不同实体、时间段或测量指标，需要更具结构性的证据访问方式。

方法关键点：VistaTree是一个文档问答agent，直接从渲染后的页面图像构建摘要树。先对文档做连续页面span切分，递归分组形成主题层级，并通过“兄弟摘要精炼”让相邻章节摘要更具区分度。查询阶段，先用节点摘要选择相关节点，再读取对应页面；当完整outline超出context预算时，采用层级导航逐层访问索引。

关键结果：在MMLongBench-Doc和LongDocURL两个基准上，使用本地托管的视觉语言模型评估答案质量与检索成本，并量化全局索引访问与层级索引访问之间的性能差距。摘要未给出具体数值，但实验表明层级摘要树可作为长多模态文档选择性检索的有效替代路径。
