---
title: 'UniRec: Cross-stage Multi-Task Fusion with Preference Alignment for Cascaded
  Recommender Systems'
title_zh: UniRec：级联推荐中跨阶段多任务融合与偏好对齐
authors:
- Lingyuan Kong
- Jiaqi Cui
- Fanjiao Zeng
- Congqi Wang
- Yu Li
- Yuan Cheng
- Jingxin Liu
- Xiaoshuang Chen
- Kaiqiao Zhan
affiliations:
- Kuaishou Technology
arxiv_id: '2609.11052'
url: https://arxiv.org/abs/2609.11052
pdf_url: https://arxiv.org/pdf/2609.11052
published: '2026-09-10'
collected: '2026-09-11'
category: RecSys
direction: 级联推荐 · 跨阶段偏好对齐与多任务融合
tags:
- Cascaded Recommender Systems
- Cross-Stage Optimization
- Multi-Task Fusion
- Preference Alignment
- Attribute Bias Regularization
one_liner: 提出 UniRec 联合优化粗排与精排融合模块，通过共享嵌入、跨阶段偏好对齐和属性组正则提升一致性与线上指标
practical_value: '- **跨阶段融合模块联合优化**：粗排和精排的融合公式常被独立设计或学习，可将两个融合 agent 共享输入嵌入并在同一计算图训练，用下游
  pairwise 偏好序对齐上游分数，避免复杂蒸馏；共享嵌入让梯度双向流动，实现对称耦合。

  - **紧凑多目标 pairwise 聚合（CPPA）**：当目标数 M 很大时，将每个 pair 的多个目标按符号聚合成正/负偏好证据，再计算 Softplus
  损失，数学等价但可微项从 O(MN^2) 降到 O(N^2)，训练吞吐提升 30%+；电商多目标精排融合可直接采用。

  - **属性组相对正则（AGRR）**：借鉴 GRPO，按属性分桶（如价格带、时长分位）内计算 advantage 并做 KL，防止融合模型整体抬高高分属性组导致分布漂移；保留跨属性排序能力，适合短视频时长、商品价格等偏差场景。

  - **adapter 注入上游决策时使用 stop-gradient**：下游融合模型需要感知上游决策时，将上游表示 detach 后拼接，避免下游目标反向重塑上游表示；跨阶段梯度耦合留给共享嵌入，保持各阶段局部目标稳定。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**

工业级推荐系统采用级联架构（召回→粗排→精排→重排），各阶段目标、特征和延迟约束不同，通常独立优化。独立优化导致跨阶段偏好不一致：粗排可能过滤掉精排偏好的物品，且精排融合也无法纠正候选池偏差；现有跨阶段协调方法只对齐粗排打分模型，不优化融合模块，而融合模块是各阶段最终排序决策的核心。

**方法关键点**

- **耦合双 agent 架构**：粗排和精排各有一个融合 agent，共享输入嵌入（用户、物品、上下文及粗排 pXTR），精排额外有私有 pXTR 嵌入；共享嵌入使两个 agent 在同一计算图训练，梯度可双向传播。粗排用 MLP-Mixer，精排用轻量 AutoInt-Lite，适配不同延迟预算。
- **adapter + stop-gradient**：精排 agent 通过 adapter 将粗排表示拼接进来，但 detach 梯度，只传递信息不回传，避免下游目标破坏上游表示。
- **双轴偏好对齐**：垂直轴用下游 pairwise 偏好（排序一致性）约束上游分数，只对齐序不回归数值；水平轴 CPPA 将每个 pair 的 M 个目标按符号聚合成正/负偏好证据，再用两个 Softplus 项聚合，数学等价但将可微项从 O(MN^2) 降到 O(N^2)。
- **属性组相对正则（AGRR）**：从偏好证据构造 item-level reward，按属性分桶（如视频时长），在桶内计算 advantage 并做 KL 正则，防止模型整体褒奖高 reward 属性组，保留跨属性排序能力。

**关键结果**

在 RecFlow 公共级联数据集上，UniRec 在 NDCG@10/30/50 及跨阶段一致性指标全面优于 Weighted-Sum、EMER、UMRE、COPR；ASH 达 0.9978，Kendall's τ 0.6318。工业数据集消融显示后验反馈损失影响最大，对齐损失只提升粗排一致性不影响精排，CPPA 提高训练吞吐 30.1%。在线 A/B 实验：AppUsageTime +0.616%，TotalWatchTime +0.675%，VideoWatchTime +0.755%，ActiveUsers +0.189%，无指标下降，已在快手全量部署。

最值得记住的一句话：**融合模块而非仅打分模型，是跨阶段偏好不一致的关键，应作为整体联合优化而非独立调参。**
