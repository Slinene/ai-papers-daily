---
title: 'From Tokens to Behaviors: Rethinking Generative Recommendation for User Trajectory
  Prediction'
title_zh: 从 Tokens 到 Behaviors：生成式推荐用于用户轨迹预测的再思考
authors:
- Jiaqi Wang
- Hanchen Yang
- Hengyu Zhang
- Hongxu Ma
- Wenqi Rao
- Hongyang Wang
- Zhongbo Sun
- Renliang Qian
- Weixin Chen
- Wengen Li
affiliations:
- Tongji University
- The Chinese University of Hong Kong
- Kuaishou Technology
- Fudan University
arxiv_id: '2611.16159'
url: https://arxiv.org/abs/2611.16159
pdf_url: https://arxiv.org/pdf/2611.16159
published: '2026-11-12'
collected: '2026-11-13'
category: GenRec
direction: 生成式推荐 · 行为级轨迹预测
tags:
- Generative Recommendation
- Semantic ID
- User Trajectory Prediction
- Probability Feedback
- Reinforcement Learning
one_liner: 提出 TraGR，以行为级并行 SID 生成、概率反馈和关系感知轨迹学习，在四个公开数据集上全面超越现有方法
practical_value: '- 行为级生成架构：将 item 内 SID 并行预测与 item 间循环状态更新解耦，避免 token 级自回归导致的多次依赖解码。在生成式推荐中做多步预测/轨迹生成时，可直接复用此设计，减少推理延迟并显式建模行为状态转移。

  - 概率反馈机制：除 top-1 item 外，将当前预测分布中概率加权且与选中 item 相似的候选 summary 作为状态输入。在 autoregressive
  多步 rollout 中传递预测不确定性，缓解后续步误差累积；电商场景可对候选集/采样近似计算，不必 full catalog。

  - 关系感知轨迹学习：采用“监督初始化 + 采样生成轨迹 RL 微调”，设计位置准确 reward 与全局协同转移 reward，并用后续 credit assignment
  优化早期选择。业务上可借鉴其使用离线协同转移矩阵作为先验 reward、冻结参考模型做 KL 约束，低成本桥接训练-推理 gap。

  - 工程注意：full catalog 归一化和概率反馈的 O(Nd) 成本在小目录/候选集可行，大规模目录需配合 ANN/采样；Stage I 的 joint
  SID + item 监督和 Stage II 的 on-policy 采样重放值得复现。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：现有生成式推荐多聚焦 next-item，无法刻画用户连续行为序列的演化；基于 Semantic ID (SID) 的自回归生成在预测未来轨迹时存在三个核心问题：token 级解码与行为状态耦合、离散 item 反馈忽略预测不确定性、teacher forcing 训练与推理不匹配。

**方法关键点**：
- TraGR 以行为为基本单位：OPQ 构造 SID，每步用独立残差头并行预测 L 个 SID token，组合成 catalog 分布；循环行为状态 ht 每预测一个 item 更新一次，将 item 内 token 并行与 item 间状态转移分离。
- 概率反馈：状态更新输入不仅包含选中 item 表示，还加入由当前预测概率和与选中 item 相似度双重加权的候选 summary，使后续预测能感知当前分布中的备选信息。
- 两阶段训练：Stage I 用 next item 损失和 teacher-forced 轨迹损失联合监督 SID 头和状态转移；Stage II 在模型自生成轨迹上做关系感知学习，结合当前位置准确 reward 和离线协同转移 reward，并通过后续 credit assignment 和 KL 正则化优化整个轨迹生成。

**实验**：在 Beauty、Cell Phones & Accessories、ML-1M、Last-FM 四个数据集上，K=3/5，对比 FPMC、SASRec、DiffuRec、TIGER、RPG、LPDO、GCB 等 13 个 baseline，在 36 个 dataset-metric 组合（含 SeqMatch@50）全部最优。SeqMatch@50 相对提升 6.63%-75.65%；消融显示状态更新、概率反馈、协同转移 reward 和 continuation credit 均有贡献；在 K=3/5/7/10 不同 horizon 下优势也基本保持。

**最值得记住的一句话**：生成式轨迹预测的关键不是更长的 token 自回归，而是行为级状态更新 + 预测分布作为反馈 + 在自生成轨迹上做关系感知优化。
