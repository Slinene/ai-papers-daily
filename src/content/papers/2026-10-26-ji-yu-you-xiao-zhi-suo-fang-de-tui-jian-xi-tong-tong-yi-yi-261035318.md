---
title: Unified Heterogeneous Feature Interaction via Effective-Rank Scaling for Recommender
  Systems
title_zh: 基于有效秩缩放的推荐系统统一异构特征交互
authors:
- Ao Zhang
- Haochuan Li
- Boya Du
- Jian Yang
- Qihang Fang
- Yulin Xu
affiliations:
- Alibaba Group
- Renmin University of China
- Institute of Automation, Chinese Academy of Sciences
arxiv_id: '2610.35318'
url: https://arxiv.org/abs/2610.35318
pdf_url: https://arxiv.org/pdf/2610.35318
published: '2026-10-26'
collected: '2026-10-27'
category: RecSys
direction: 推荐系统统一异构特征交互与序列建模
tags:
- Feature Interaction
- Sequence Modeling
- Multi-Scenario
- Effective Rank
- Industrial Recommender
- CVR Prediction
one_liner: HiRank统一异构特征交互与序列建模，通过主序列引导检索和场景感知高阶注意力，在淘宝CVR线上提升2.27%订单/用户
practical_value: '- **主序列引导长期记忆检索**：不要用静态 profile 特征直接生成长期行为 memory 的 query，容易导致 query
  方向集中、有效秩低。可先让可学习 query seed attend 主行为序列，再用得到的主序列感知 query 去检索 long-term memory；同时保留
  candidate-conditioned query 从候选物品视角读取同一 memory，两条路径互补，适合电商强 candidate 相关的 CVR 建模。

  - **用有效秩(eRank)做特征交互层诊断**：在 token mixing、memory retrieval 后定期计算 eRank，若有效秩过低说明表示多样性不足，可以增加
  head-wise SwiGLU 或 per-token FFN；实验中 mixing 块和 memory retrieval 均显著提升 eRank，High-Rank
  Attention 阶段 eRank 仅小幅下降，可作为架构迭代的监控指标。

  - **场景感知压缩 + 复合投影替代全量高维投影**：在多场景/多域 CVR 中，直接用 scenario-aware cross-attention 将全部
  token 压缩为 compact state，再通过多个独立参数化的 composite projections 生成 Q/K/V 做高阶交互，比直接对拼接
  token 做大矩阵投影更省参数且能保留场景差异，适合业务线做多场景统一排序模型。

  - **用户-物品解耦实现请求级计算复用**：将 backbone token 分为 user-side 和 item-side，user-side 计算在同一个
  request 内跨候选共享；使用 masked head-wise SwiGLU 实现单向 user->item 信息流（dependency matrix
  [[1,0],[1,1]]），既降低 online serving GFLOPs，又避免 item 信息污染 user 状态，适合电商/广告推荐 RLB 架构。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
大规模工业排序模型必须联合捕捉异构特征交互、长期用户行为和场景依赖，但现有架构通常将序列编码与特征交互割裂，双向信息交换受限；直接对异构 token 做同质 self-attention 也因序列与非序列信号有效秩不同而低效，共享表示易造成场景负迁移。尤其淘宝 CVR 场景稀疏、行为信号与候选物品和场景强相关，需要一个统一框架协调行为建模与特征交互，并适配多场景学习。

**方法关键点**
- HiRank 骨干每层由 HSTU 风格 gated sequential attention 建模主行为序列，候选 token 通过共享参数做 sequence-to-candidate cross-attention，再将主序列状态、长期记忆 readout、语义特征 token 一起送入 head-wise token mixing 和 per-token SwiGLU，实现异构特征双向融合。
- 第一层用可学习 query seed attend 主序列得到 interest queries，用于检索长期记忆；同时用更新后的候选 token 初始化 candidate-conditioned queries，从同一 memory 读取互补证据。后续层由上一层的 token interaction 输出更新这些 queries，使特征上下文逐步指导后续行为证据提取。
- 非序列特征和池化行为摘要按语义分组为 token，分为 user-side 和 item-side。
- High-Rank Attention 先用 scenario token 对最后层 token bank 做 cross-attention 压缩成 compact state，再用独立参数化的 composite projections 生成多个 composite tokens 进行多头注意力，提升有效秩和表示多样性。
- 可选用户-物品解耦变体通过 user-side 计算复用和单向 user->item 信息流降低候选级计算成本。

**关键实验**
在淘宝工业 CVR 数据集（2.4B impressions / 87M items / 206M users，覆盖首页与主搜索多场景）上，HiRank 的 Homepage AUC 0.9163、GAUC 0.7801，Main Search AUC 0.8764、GAUC 0.6787，均优于 RankMixer+DIN、Hiformer+DIN、OneTrans、MixFormer、HyFormer、MDL 等强 baseline；其中 Homepage GAUC 相对最强 baseline 提升 0.0186，PCOC 更接近 1。消融显示移除 token interaction 与 High-Rank Attention 带来的 GAUC 下降最大（-0.0489），有效秩分析显示 mixing block 和 memory retrieval 使 eRank 分别提升 +16.30、+6.44、+30.36。线上 A/B 中 orders/u +2.27%（p<0.01），GMV/u +2.86%，DAC +2.13%。

**最值得记住的一句话**：显式保留主序列事件级状态，并用其引导长期记忆检索，再通过场景感知压缩与复合投影提升有效秩，是多场景 CVR 统一建模的有效路线。
