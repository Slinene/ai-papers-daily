---
title: 'OneModel: A Unified Foundation for Platform-Scale Multi-Scenario Ranking'
title_zh: OneModel：平台级多场景排序的统一基础模型
authors:
- Yinqi Zhang
- Peiyu Hu
- Yuntian Tang
- Siying Gu
- Jiahao Liang
- Longxin Kou
- Haiqing Hu
- Shuman Zhuang
- Yubin Xu
- Chenggen Sun
affiliations:
- Xiaohongshu
arxiv_id: '2608.18606'
url: https://arxiv.org/abs/2608.18606
pdf_url: https://arxiv.org/pdf/2608.18606
published: '2026-08-19'
collected: '2026-08-20'
category: RecSys
direction: 多场景统一排序 · 长序列用户建模
tags:
- Multi-Scenario Ranking
- Long-context User Modeling
- Generative Ranking
- Industrial Recommender
- SAIM
- Cross-Domain
one_liner: 用共享事件序列与场景感知门控统一推荐、广告、商家排序，平衡跨场景迁移与专用化并大幅降低在线延迟
practical_value: '- 跨场景统一事件序列：把不同业务（推荐/广告/商家）的行为映射成统一的 event token，用 scenario-specific
  projector + 结构上下文（scenario/action/Δt/pos），可直接复用于多业务共享排序模型，减少重复建模和用户表征碎片化。

  - SAIM 门控：在 FFN 中用 scenario id 生成 gate 对通道做调制，保持共享计算图却给各业务留下自适应空间；比完全分塔省资源，比硬共享抗负迁移。

  - 工程部署：用户塔增量缓存 + 请求期 candidate 打分分离、用户特征预取、图级推理优化，将 latency 从 270ms 降至 90ms；在电商/广告多场景排序里做统一模型时可参考这套
  serving 拆分。

  - 训练稳定 trick：跨流采样避免高频业务主导、warm-up 梯度隔离、按各流验证 AUC 反比加权 loss、选择性 backprop；多目标多业务联合训练时能有效抑制负迁移。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
平台同时存在推荐、广告、商家服务等多条业务流，用户行为形成跨流轨迹，但独立排序系统割裂用户表征、重复建设昂贵的长序列/内容理解能力。统一建模可复用跨流信息并降低成本，但面临特征异构、目标冲突、在线长序列推理成本高等挑战。

**方法关键点**
- 统一跨场景表征：用 scenario-specific projector 将异构 item 特征映射到共享 embedding 空间，并注入 scenario、action、时间间隔、位置等结构上下文，形成可比的 event token。
- 动作导向 backbone：采用 GenRank 风格，将 action 作为预测目标、item 作为上下文，结合显式 item-context 交互、causal decoder 与 candidate masking，压缩有效序列长度。
- SAIM：在 FFN 中根据 scenario id 生成 channel gate，对特征做元素级调制，共享计算图下实现业务专用化。
- 分层用户表征：global attention pooling 与最后 local state 拼接，捕捉长期偏好与短期意图。
- 多目标优化：自监督 next-item 预测 + 各业务监督 loss，α 衰减、β 增大，λ 按验证 AUC 反比加权；配合跨流采样、warm-up 梯度隔离、选择性 backprop。
- 服务优化：用户状态增量缓存、特征分解、用户特征预取、共享用户塔、图级推理优化。

**关键实验**
在 Xiaohongshu 生产 10% 流量上对比 HSTU、GenRank。单流 Ads Click AUC 从 GenRank 0.7648 提升到 0.7682；统一训练后 OneModel 达 0.7712，较 GenRank 提升 6.4‰，且 Rec 无负迁移、Merchant +3.0‰。在线 A/B：Explore Feed Time Spent +0.33%、Engagement +1.25%；Feed Ads ADVV +3.43%、CTR +8.18%；Merchant DGMV +1.1867%、GPM +2.1585%。Dense 参数从 173M 增至 230M，但延迟从 270ms 降至 90ms。消融显示 unified representation、SAIM、stratified representation 分别贡献 1.4‰、1.1‰、0.8‰。

> 最值得记住的一句话：跨业务统一排序时，用场景感知门控调制一个共享 backbone，配合用户状态缓存与梯度隔离，可以在不牺牲各业务指标的情况下复用昂贵的用户/内容理解能力。
