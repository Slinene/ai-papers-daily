---
title: 'RouteRec: Behavior-Guided Sparse Routing for Sequential Recommendation'
title_zh: 行为引导稀疏路由的序列推荐
authors:
- Junyeong Song
- Jaemin Yoo
affiliations:
- Korea Advanced Institute of Science and Technology
- Seoul National University
arxiv_id: '2609.39007'
url: https://arxiv.org/abs/2609.39007
pdf_url: https://arxiv.org/pdf/2609.39007
published: '2026-09-30'
collected: '2026-10-01'
category: RecSys
direction: 行为引导的MoE序列推荐
tags:
- Sequential Recommendation
- Mixture of Experts
- Sparse Routing
- Behavioral Cues
- Session-aware
one_liner: 用会话行为线索（节奏/主题/记忆/流行度）引导MoE稀疏路由，让不同行为模式的会话走不同计算路径
practical_value: '- 电商/广告序列推荐中，可以用日志侧特征构造行为线索作为MoE路由信号：从timestamp算interaction tempo，从类目标签算focus/switch
  rate，从item id算repeat/carryover，从训练集频次算popularity tendency；这些信号在预测前可算，且比纯hidden state更能反映会话行为差异。

  - 分层稀疏路由值得借鉴：先由行为线索选 top-k 专家组（如tempo/focus/memory/popularity各组），再在组内结合当前hidden
  state选专家；组选择保持行为语义，组内选择保留位置级适应。

  - 训练时不要用load balancing，改用route consistency + z-loss：前者让相似行为session的路由分布接近，后者压制路由logit过大；论文显示load
  balancing会伤害行为依赖分配。

  - 多尺度路由（macro/mid/micro）对电商session有效：跨历史、当前会话、最近局部窗口分别聚合线索，macro/mid共享、micro随位置重算；若缺少类目或时间特征，可退化为sequence-only线索，仍能保持竞争力。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
序列推荐中不同会话的行为模式差异很大：快速切换的会话依赖近期变化，重复消费的会话依赖跨会话记忆，但现有模型让所有会话共享同一套参数。MoE 提供条件计算，但路由信号如何选择是核心问题。RouteRec 用观察到的会话行为作为路由准则，从 sessionized 历史中提取线索，让不同行为模式的会话走不同专家路径。

**方法关键点**  
- 四类行为线索：Tempo（时间戳间隔）、Focus（类目/主题切换）、Memory（会话内及跨会话重复）、Popularity（训练集频次）。每类线索在 macro（跨会话历史）、mid（当前会话前缀）、micro（最近 5 个交互）三个 scope 分别聚合。  
- 骨干为 SASRec，保留 self-attention，将三个 scope 的 FFN 替换为 routed expert blocks。  
- 分层稀疏 MoE：先由家族线索投影选 top-3 专家组（共 4 组，每组对应一个行为家族），再在组内结合当前 hidden state 选 top-2 专家；组选择 macro/mid 会话级共享，micro 位置级重算；专家权重稀疏归一化。  
- 训练损失：next-item cross-entropy + route consistency（相似会话路由分布 JS 散度）+ z-loss；不使用 load balancing。

**关键实验**  
在 6 个公开数据集（KuaiRec、LastFM、Retail Rocket、ML-1M、Foursquare、Beauty）上与 9 个 baseline 对比，18 个 dataset–metric 组合中 RouteRec 12 个第一、3 个第二，平均 rank 1.61，次优 FDSA 为 4.11。LastFM NDCG@10 相对提升 6.0%；KuaiRec 上 role swap 扰动使 MRR@10 下降约 35%，高于 zero cues 的 28%，说明路由依赖行为语义。消融显示三 scope 均有效，层次化稀疏优于 flat/dense，去掉 load balancing 反提升性能。

**最值得记住的一句话**：用可观测的行为线索（节奏、主题、记忆、流行度）作为 MoE 路由信号，能比仅用 hidden state 更精准地为不同行为模式的会话分配专家计算路径。
