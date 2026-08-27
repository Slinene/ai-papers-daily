---
title: 'RetrievalRouter: Joint Modality and Architecture Selection for Document Retrieval'
title_zh: 'RetrievalRouter: 联合模态与架构选择的文档检索路由'
authors:
- Emre Kuru
- Mehmet Onur Keskin
- Reza Farahbakhsh
- Noel Crespi
affiliations:
- SAMOV AR, Télécom SudParis, Institut Polytechnique de Paris
- Özyeğin University
arxiv_id: '2608.25625'
url: https://arxiv.org/abs/2608.25625
pdf_url: https://arxiv.org/pdf/2608.25625
published: '2026-08-25'
collected: '2026-08-27'
category: RecSys
direction: 检索召回 · 查询路由 · 效率优化
tags:
- query routing
- document retrieval
- multimodal
- dense retrieval
- late interaction
- latency-accuracy tradeoff
one_liner: 轻量 query-aware 路由仅凭查询文本选择最优检索管道，在精度和延迟上同时超越静态基线
practical_value: '- 电商搜索多路召回可借鉴其动态路由：简单 query（品牌词、短词）走轻量双塔或倒排，复杂 query 路由到多模态/交互式重排。用一个轻量分类器仅依赖
  query 文本做路由，无需动底层模型，单参数即可在线调节成本和收益。

  - 若业务中有文本嵌入、多模态嵌入、dense 与 late-interaction 等多种检索管道，不要全局固定一个。构建候选 pipeline 池，用 query-aware
  router 联合选择模态和架构，比简单级联更灵活、时延更可控。

  - 单参数 accuracy-latency 前沿的思路可直接用于 SLA 对齐：置信度阈值决定多少 query 走 expensive path，能直观给出成本—精度曲线，方便与预算、p99
  时延等业务约束权衡。

  - 论文路由只用 query 文本，开销极低，适合在线推理。电商场景可扩展轻量特征（query 长度、类目、用户历史）提升路由准确度，仍保持低延迟。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**  
文档检索在金融、医疗、法律等高风险场景中，必须同时在检索模态（纯文本 vs 多模态）和架构（dense vs late-interaction）之间选择。高精度管道太慢、成本过高，快速管道在复杂文档上容易漏召回；静态选择无法匹配不同 query 的难度差异。

**方法关键点**  
RetrievalRouter 是一个轻量 query-aware 路由器，仅从 query 文本预测该 query 最适合的检索 pipeline（模态+架构组合）。训练时离线评测所有候选 pipeline 得到最优标签，推理时只过一个小模型。单一可调参数控制选择阈值，完整暴露 accuracy–latency 前沿；无需修改底层 retriever，可无侵入部署。

**关键结果**  
在金融和科学 benchmark 上，没有静态 pipeline 能同时最优。与最佳静态 baseline 相比，RetrievalRouter 精度提高 2.5%，速度提升 12.4 倍。对比先前 adaptive strategy selection 方法，在 accuracy-oriented 设置下 nDCG@5 显著更高；在 latency-oriented 设置下同时匹配或数值上优于对比方法。
