---
title: 'Heterogeneous Ranking in Industrial-Scale Recommender Systems: A Case Study'
title_zh: 工业级推荐系统的异构排序：Google Discover 案例研究
authors:
- Di Bai
- Jintao Liu
- Zhenwei Tang
- Peifan Wu
- Nada Al-Thawr
- Luoshu Wang
affiliations:
- Google
arxiv_id: '2607.27577'
url: https://arxiv.org/abs/2607.27577
pdf_url: https://arxiv.org/pdf/2607.27577
published: '2026-07-30'
collected: '2026-07-31'
category: RecSys
direction: 多任务 MoE 异构排序 · 跨类型公平性
tags:
- Multi-Task Learning
- Mixture-of-Experts
- Heterogeneous Ranking
- Industrial Recommender Systems
- Model Observability
- Cross-Segment AUC
one_liner: 提出 HA-MoE 架构将内容类型异构信号显式注入门控与专家调制，通过 LENS 可观测框架与 DL-AUC 指标打破负迁移并保障跨类型排序公平性。
practical_value: '- **用显式类型信号调节 MoE 门控与专家**：在电商/信息流中若需混排广告、直播、图文等多种内容，可在 MMoE 基础上将
  item_type 等离散特征直接拼接入门控输入，并对专家输出做 FiLM 式的 scale & shift 调制，低成本实现内容自适应，避免少数类被淹没。

  - **轻量级跨类型排序公平性指标**：业务中常用全局 AUC，但可能掩盖广告压制短视频等问题。可参考 DL-AUC = λ·Micro-AUC + (1-λ)·Macro-xAUC，计算各内容类型间正负样本的交叉
  AUC 均值，作为模型选优的硬约束，尤其适合有流量倾斜风险的场景。

  - **MoE 专家分工的可视化与监控**：LENS 的激活切片能直观展示不同内容类型/任务所用专家的分布；PIEM 通过匈牙利匹配计算跨 run 的专家功能相似度，可做成自动巡检指标，在
  warm-start 训练中快速发现专家坍缩或功能漂移，比等跑完完整评估更快更省。

  - **多任务冲突的缓解技巧**：共享底层 MLP 容易造成正负目标 seesaw，MMoE 直接替换有时仍会恶化某项。HA-MoE 通过异构信号解耦专家泛化能力，可复制到广告/搜索的「点击率+转化率+负反馈」联合优化中，尝试将场景/媒体特征注入类似
  gate 和 expert 内部。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
Google Discover 在一个统一排序模型中评估来自开放网页的极多元内容（文章、长短视频、UGC、AI 摘要卡片等），面临两大异构挑战：特征密度与元数据结构不一致导致的数据异构，以及不同内容类型在点击、长停留、点赞/踩等交互模式上差异巨大的交互异构。单一共享 MLP 容易产生严重的负迁移和多数类崩塌（低质文章压制高价值视频），亟需在严格的生产资源约束下提升模型对异构内容的适应能力。

**方法关键点**  
- **HA-MoE 架构**：在 MMoE 基础上做两处轻量改动。**HA-Gating** 将显式异构信号（如 content_type、创作者关系等）与稠密特征直接拼接输入任务级门控，引导专家为不同内容段分配权重。**HDLM**（异构驱动的线性调制）对每个专家最终层的输出做 FiLM 式的 scale & shift：𝛾(ℎ)⊙E(x)+𝛽(ℎ)，参数仅依赖异构信号，使同一专家能按内容类型切换行为模式，无需成倍增加参数。  
- **多任务优化**：联合 11 个正负反馈预测头（点、赞、踩、停留等），损失由 pointwise BCE 与 intra-session 的 pairwise RankNet 组合而成，配合 GradNorm 动态调权。  
- **LENS 可观测框架**：激活切片按内容类型行归一化 gating 概率，可视化专家分工；PIEM 用 JSD 衡量专家行为剖面，通过匈牙利算法进行跨模型版本的无标签对齐，用于持续训练中自动检测功能异构性的崩塌。  
- **DL-AUC 评估指标**：DL-AUC = λ·Micro-AUC + (1-λ)·Macro-xAUC，后者计算所有内容类型对间的双向交叉 AUC 均值，能有效惩罚多数类分数抬高带来的生态损害，相比纯全局 AUC 更能反映模型在保障少数类内容公平排序上的表现。

**关键结果**  
在全量生产数据的 7 天留出集上（~1 千万样本），HA-MoE 较共享 MLP 和标准 MMoE 在正负反馈两组任务的聚合 DL-AUC 上均有提升（例如 pDisinterest 从 0.939 到 0.949），且克服了标准 MMoE 在负反馈上的负迁移。跨类型公平性方面，视频 vs. 文章的负样本对交叉 AUC 差距从 0.141 缩小至 0.060。在线 A/B 测试中，DAU +0.22%，多样内容曝光率 +0.36%，多样内容互动率 +0.54%，均统计显著。模型参数增量低于 5%，服务延迟增幅小于 0.5%，完全适配生产环境。

**最值得记住的一句话**  
将内容类型等显式异构信号同时注入 MMoE 的门控与专家内部做轻量级调制，是在不突破生产资源预算下打破多任务负迁移并提升跨类型排序公平性的有效模式。
