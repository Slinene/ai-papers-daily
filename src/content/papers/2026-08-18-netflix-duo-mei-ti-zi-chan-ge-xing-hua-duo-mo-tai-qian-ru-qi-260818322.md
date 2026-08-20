---
title: Multimedia Asset Personalization via Multimodal Embeddings at Netflix
title_zh: Netflix 多媒体资产个性化：多模态嵌入解决冷启动并统一画布
authors:
- Emma Yanyang Kong
- Aditya Deshpande
- Bowei Yan
- Asad Abbasi
- Santiago Castro
- Avneesh Saluja
- David Fagnan
- Ashish Rastogi
affiliations:
- Netflix
- Cohere
arxiv_id: '2608.18322'
url: https://arxiv.org/abs/2608.18322
pdf_url: https://arxiv.org/pdf/2608.18322
published: '2026-08-18'
collected: '2026-08-20'
category: RecSys
direction: 多模态嵌入 · 冷启动资产个性化
tags:
- multimodal embeddings
- cold-start
- two-tower
- CLIP
- MediaFM
- IPS
one_liner: 将 CLIP 与三模态 MediaFM 嵌入拼入双塔 item tower，统一画布模型并显著提升冷启动与搜索效果
practical_value: '- 冷启动创意/素材优选：电商/广告中的商品主图、广告创意、短视频封面等，可以把 CLIP 类预训练 embedding 作为冻结特征拼进
  item tower，不改双塔架构，即可获得跨类目、跨场景的知识迁移，特别适合新商品新创意。

  - 多场景模型统一与数据平衡：多个展示位/画布若分开训练，可考虑合并为单一模型，并用 reward-based weighting 按长期价值给样本加权，而非手调
  per-scene 权重；但必须同时注入内容特征，单独统一模型或单独内容嵌入在线可能都不显著。

  - 评估与筛选：用 explore data 记录精确 propensity，IPS 离线指标更能预测线上；构建 popularity winner 线性 probe
  作为廉价 gate，先筛选 embedding 版本再上端到端 A/B，可大幅降低实验成本。

  - 工程部署：precompute-first 三层预计算：素材 embedding、item tower 输出、个性化选择都离线/日更算好，在线只做 KV lookup，多模态模型不进请求路径；只对
  top N 候选物料化，平衡成本与覆盖。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

动机：Netflix 的个性化推荐素材（artwork 图片与 video preview 视频预览）传统上只用 asset ID 与交互历史，内容盲，新标题和新素材冷启动严重，只能回退流行度。本文报告把多模态 foundation model embedding 接入生产双塔推荐的系统实践。

方法关键点：
- 共享 Embedding Store：解耦基础模型更新与下游模型部署，基础模型嵌入注册/回填即可被多个推荐系统消费。
- 美术图个性化：在 item tower 拼接 CLIP image embedding（768 维），MLP 投影回原维度；用单一模型取代五个画布各自模型，并用 long-term reward-based weighting 平衡不同画布、不同正反馈类型；CLIP 文本-图像共享空间支持 query-aware artwork，将个性化分数与 query-image cos 线性混合。
- 视频预览个性化：采用内部三模态 MediaFM，shot 级融合 SeqCLIP 视觉、wav2vec 2.0 音频、text-embedding-3-large timed-text，3 层 BERT 式 Transformer 做 Masked Shot Modeling，取 contextualized shot mean-pool 进 item tower。
- 评估与工程：在 explore data 上做 IPS 评估，使用已知 randomization propensity；precompute-first 三层预计算，在线只做 KV lookup。

关键结果：
- 美术图消融：单独 CLIP 嵌入(V1)或单独统一模型(V2)在线均不显著；合并 V3 在 core discovery metric +0.127%（p<0.005），离线短面板 ΔIPS +5.691%。在 Eclipse UI 画布切换期间 holdback，V3 +0.233% discovery、+0.184% streaming hours，约 3.5 亿小时/年。
- Query-aware artwork 搜索页 playthrough rate +0.36%（p<0.05）。
- 视频预览在线 streaming：SeqCLIP +0.187%，MediaFM +0.193%（p<0.02）；离线 IPS 0.332% / 0.380%。
- popularity winner 线性 probe：MediaFM top-1 比随机高 25.90 个百分点，SeqCLIP 高 18.75，排序与离线/在线一致，用作 A/B 前 gate。
- MediaFM intrinsic 消融：contextualization 比单纯多模态拼接更重要，concat-inputs 在 popularity ranking 低于视觉 SeqCLIP。

最值得记住：内容信号和模型容量互补，单独用预训练嵌入或单独统一多场景模型都可能不显著，两者结合才放大冷启动收益；廉价的 popularity probe 可以低成本筛选嵌入候选。
