---
title: 'GLASS: Graph-Language Alignment with Spherical Scoring for Transferable Graph-Level
  Anomaly Detection'
title_zh: GLASS：图-语言对齐与球面评分实现可迁移图级异常检测
authors:
- Xudong Wang
- Chris Ding
- Tongxin Li
- Jicong Fan
affiliations:
- School of Data Science, The Chinese University of Hong Kong, Shenzhen (CUHK-Shenzhen)
arxiv_id: '2609.05253'
url: https://arxiv.org/abs/2609.05253
pdf_url: https://arxiv.org/pdf/2609.05253
published: '2026-09-04'
collected: '2026-09-08'
category: Other
direction: 图异常检测 · 图-语言对齐
tags:
- graph anomaly detection
- graph-language alignment
- von Mises-Fisher
- zero-shot transfer
- Matryoshka representation
one_liner: GLASS 将图编码器与文本嵌入对齐到超球面，用球面密度评分实现跨域图异常检测，支持零样本/少样本迁移
practical_value: '- 风控/反作弊：电商平台可将商家、交易、用户关系建模成图，用 GraphDP 模板描述图的局部/全局/语义属性，并与文本嵌入对齐，快速构建跨品类/场景的异常检测模型，解决冷启动问题。

  - 零样本跨域迁移：新业务线或新市场缺少标注异常样本时，可直接复用对齐好的图-文本空间，用目标域图描述文本做零样本检测，或用极少量正常样本校准参考集，避免重新训练。

  - 多尺度表示训练：Matryoshka 表示切片可一次训练得到多个维度的嵌入，线上推理时按需截取低维部分，降低存储和计算成本，适合大规模图数据的实时风控。

  - 球面密度评分：SMS 的 vMF 核密度估计比原始 kNN 更平滑，且能融合图结构和文本语义两个模态的异常信号；在商品风险、异常评论等场景，可将文本描述与图结构融合，提升异常检测鲁棒性；对推荐排序核心链路直接收益有限，但平台治理/风控可借鉴。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：现有图级异常检测（GLAD）方法通常针对单一数据集训练，缺乏跨域迁移能力；不同领域图的结构和属性差异大，难以复用。

**方法关键点**：
- 将结构感知图编码器与指令感知文本嵌入对齐到单位超球面；
- 使用 Graph Descriptor Prompt（GraphDP）将图的局部、全局和语义属性序列化为文本，作为跨领域桥梁；
- 通过 Matryoshka 表示切片施加多尺度一致性，捕获不同粒度的异常；
- 引入 Spherical Multi-Modal Scoring（SMS），在图和文本两个嵌入空间分别构建 von Mises-Fisher 核密度估计，融合结构/语义异常信号，角度 kNN 评分是高浓度极限情形；
- 共享文本空间支持零样本跨域检测，用少量正常样本即可 reference-set calibration 做少样本适配。

**关键结果**：在 12 个基准、3 个元领域上取得最佳平均 AUROC 和排名，优于近期先进 GLAD 基线，并验证了零样本/少样本跨域迁移的有效性。
