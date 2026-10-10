---
title: 'EVIE: Evidence-Vector-Informed Embeddings for Visual Document Retrieval'
title_zh: EVIE：面向视觉文档检索的证据向量引导嵌入
authors:
- Zifei Wang
- Wei Wen
- Qiang Ji
- Qian-Wen Zhang
- Ruizhi Qiao
- Xing Sun
affiliations:
- Tencent IMA Product Center
- Tencent Youtu Lab
arxiv_id: '2610.11553'
url: https://arxiv.org/abs/2610.11553
pdf_url: https://arxiv.org/pdf/2610.11553
published: '2026-10-08'
collected: '2026-10-10'
category: RecSys
direction: 视觉文档检索 · 多向量召回与索引压缩
tags:
- Visual Document Retrieval
- Multi-vector Retrieval
- Matryoshka Representation Learning
- Index Compression
- Vision-Language Models
one_liner: 提出视觉文档检索方案，用证据数据治理、双向蒸馏与层级索引压缩提升精度与存储效率
practical_value: '- 数据治理方法可迁移：用多模态 judge 识别“有答案正样本”并过滤不可靠负样本，适合电商搜索、商品详情页图文匹配训练数据的自动清洗。

  - Prefix-MRL 单 checkpoint 输出多个嵌套维度，线上可按延迟/存储预算动态切换 embedding 维度，无需重新编码或训练多个模型。

  - HAC 索引压缩结合空间正则的 token 聚类，把多向量索引降到单阶段 MaxSim 可用的体积，128x 存储降低，适合大规模商品库的图文多向量召回。

  - 多向量 + MaxSim 比单向量在图文混合 query-doc 匹配上更细粒度，但需控制索引大小，HAC 提供了准确率-存储权衡的新思路。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机：** 视觉文档检索（VDR）需要在细粒度页面理解与高效索引之间取得平衡。OCR 路径增加延迟且丢失视觉结构信息；单向量视觉语言模型压缩整页损失细粒度匹配；多向量 MaxSim 索引过大，精度仍有提升空间。

**方法关键点：** EVIE 引入三方面创新：
1. **证据判定数据治理**：用多模态 judge 识别包含答案的正样本，过滤不可靠负样本。
2. **双向教师-学生学习**：对称 listwise 蒸馏 + Prefix-MRL，一个学生 checkpoint 支持六个嵌套 embedding 维度，无需重新编码。
3. **层级凝聚索引压缩（HAC）**：对页面 token 做空间正则聚类，存储语义质心，实现单阶段 MaxSim 检索。

**关键结果：** 在 ViDoRe V1/V2/V3 和 JinaVDR 共 138 个任务上验证。EVIE-8B 在 V3 上取得 66.75 nDCG@10，超出最佳外部基线 1.43 点；四个套件平均 79.51。EVIE-4.5B 搭配 HAC 在仅 3.81 GiB/百万页存储下保留 59.58 nDCG@10，相比未压缩 1024-token、256 维 BF16 索引降低向量负载 128 倍。
