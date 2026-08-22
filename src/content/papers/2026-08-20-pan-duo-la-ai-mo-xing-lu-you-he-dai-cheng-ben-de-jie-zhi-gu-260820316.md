---
title: 'Pandora''s AI Model Routing Box: Efficient Allocation with Costly Value Estimation'
title_zh: 潘多拉 AI 模型路由盒：带成本的价值估计与高效分配
authors:
- Adam Fisch
- Shubhendu Trivedi
- Fantine Huot
- William W. Cohen
- Michael Kaisers
- Mirella Lapata
- Kate Larson
- Jacob Eisenstein
affiliations:
- Google DeepMind
arxiv_id: '2608.20316'
url: https://arxiv.org/abs/2608.20316
pdf_url: https://arxiv.org/pdf/2608.20316
published: '2026-08-20'
collected: '2026-08-22'
category: Other
direction: 成本感知的模型路由与拍卖机制
tags:
- model routing
- Pandora's Box
- value of information
- cost-efficient inference
- auction-based allocation
one_liner: 将模型路由中昂贵价值估计的取舍建模为 Pandora's Box，以 reservation price 动态决定查询时机，在中心化与去中心化场景均接近最优。
practical_value: '- 在推荐/搜索的多模型链路（精排、重排、LLM reranker）或 RAG 中，用 cheap estimator（如 embedding
  KNN 或轻量模型）先得到期望收益和不确定性，再以 reservation price 为阈值决定是否调用昂贵路径（完整生成、检索、大模型打分）；不要固定预算或全量调用，能显著降低推理成本。

  - 当存在多个模型供应商或内部专家服务，且各自有私有评估能力时，可采用 posted-price 拍卖 + VoI 公式，让专家自行判断是否值得花钱做更准的自评估再报价；平台只需发布当前最佳价，无需了解专家内部信息，降低中心化路由的维护成本。

  - 工程实现上 Gaussian signal model 的闭式解很容易落地：用 calibration 集拟合 cheap score 到 expensive
  score 的回归得到 μ 和 σ²，再用 root-finding 求 reservation price；若候选之间分数相关，可用多元高斯后验 + mean-field
  更新阈值，进一步提升查询效率。

  - 如果预算极其有限且候选数少（如仅小模型 vs 大模型），Margin 启发式（根据 top-2 cheap score 差距决定是否查昂贵估计）已接近最优，可作为快速落地起点；但在几十上百个候选时，reservation-price
  策略能更精细地分配查询预算。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
异构 AI 系统需要将每个查询路由到最合适的专家，但价值估计本身存在成本-准确率权衡：embedding 预测便宜但有噪声，fine-tuned 模型或 partial reasoning 更准却昂贵。该权衡通常被当作免费操作，导致路由系统要么过度查询昂贵估计器，要么只依赖噪声大的便宜信号。

### 方法关键点
- 将带成本价值估计的路由形式化为 Pandora's Box 问题：每个 specialist 是一个盒子，cheap estimator f 总是可用，昂贵 estimator g 需要支付成本才能“打开盒子”获得更准估计。
- 中心化 Pandora's Router：假设 G|F 服从高斯分布，得到闭式 reservation price（满足 E[(G−u_rsv)_+] = c）和 backup price；采用 Pandora-OI 顺序检查盒子，或非强制检查 Pandora-NI 的 committing policy；对候选分数相关的情况，用多元高斯后验 + mean-field 更新逐次重算 reservation price。
- 去中心化 Pandora's Bidder：posted-price 拍卖，战略专家基于 VoI（E[(G−p)_+] − (μ−p)_+）是否大于成本来决定是否 refine 自评估，形成 [p_lo, p_hi] 决策区间。

### 关键实验
在 Math（推理缩放，16k 题）、RAG（无检索 vs Wikipedia/PubMed 检索）和 EmbedLLM（100+ 模型）三个域上验证。对比 f-only、g-always、Top-2、Coin Flip、Random-Npr、Margin-Npr。Pandora's Router 在几乎所有成本水平 c_g 取得最低 regret + inspection cost：低成本时接近 g-only 的准确度但查询量更少；高成本时自动退化为 f-only，避免无谓开销。Pandora's Bidder 也追踪下界，但在竞争价噪声大时可能牺牲全局分配效率。

### 最值得记住的一句话
只有当昂贵价值估计的信息增益超过其成本时才查询它——用 reservation price / VoI 的闭式公式即可在路由和竞价中高效实现这一决策。
