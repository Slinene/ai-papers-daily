---
title: 'TimeRoute: Time-Aware Modality Routing and Diffusion for Multi-Modal Recommendation'
title_zh: TimeRoute：时间感知模态路由与扩散的多模态推荐
authors:
- Pengyu Zhang
- Yangqin Jiang
- Klim Zaporojets
- Congfeng Cao
- Paul Groth
affiliations:
- University of Amsterdam
- University of Hong Kong
- Aarhus University
arxiv_id: '2608.10983'
url: https://arxiv.org/abs/2608.10983
pdf_url: https://arxiv.org/pdf/2608.10983
published: '2026-08-11'
collected: '2026-08-12'
category: RecSys
direction: 时间感知多模态融合推荐
tags:
- Multi-modal Recommendation
- Time-aware Recommendation
- Diffusion Models
- Modality Routing
- Graph Reconstruction
one_liner: 利用时间感知模态路由和基于扩散的图重构，动态调整多模态融合权重并抑制过时模态信号
practical_value: '- **动态模态融合权重**：电商推荐中，商品文本、图片、视频在不同时间节点的重要性不同（如大促期间视觉主导，日常文本更重要），可借鉴
  TimeRoute 的时态感知路由器，用用户行为序列和交互时间戳生成个性化的模态权重，代替人工设定或全局共享权重。

  - **扩散模型用于模态去噪**：在做物品图或特征传播前，可以用扩散过程对模态交互边去噪，剔除因时间漂移而过时的边，减少噪声引入。FiLM 条件注入长短期时序信号的设计可复用到召回/排序的特征清洗环节。

  - **双流长短时去噪头**：区分长期偏好和短期兴趣对模态敏感性的差异，可以在现有推荐模型中加入类似的结构，例如在用户表征层用两个独立的编码路径分别建模长短期行为，再通过门控融合，提升对时间敏感的模态利用率。

  - **工程落地方案**：论文在 TikTok 和 Amazon 数据集上验证，且代码开源，适配多模态推荐场景可直接尝试迁移，尤其适合内容形态丰富、用户兴趣随时间明显漂移的业务（如电商、短视频）。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：多模态推荐中，文本、图像、音频等模态的时效性不同且随时间漂移。例如巧克力购买平时靠文本成分描述，情人节期间转向视觉包装和环境音频。这种模态-时间尺度错配导致两个问题：用户在不同时间上下文需要不同的模态比例，且过时或无关模态容易引入误导信号。现有方法使用全局共享的融合权重，无法捕捉个性化和时间动态。

**方法**：提出 TimeRoute，一个基于扩散的多模态推荐框架。核心包括：
1. **时态感知模态路由器**：将用户聚合行为特征映射为个性化模态分布，取代静态融合权重，根据时间上下文动态调整各模态的重要性。
2. **扩散图重构器**：用同一时间剖面通过 FiLM 条件控制扩散过程，配备双流长期和短期去噪头，在传播前抑制过时的模态交互边，生成更干净的图用于 GCN 推荐。

**结果**：在 TikTok、Amazon-Baby 和 Amazon-Sports 三个数据集上进行 10 次随机种子配对测试，Recall@K、Precision@K 和 NDCG@K 相比强基线最高提升 9.8%，一致性的显著改进验证了动态模态路由和扩散去噪的有效性。
