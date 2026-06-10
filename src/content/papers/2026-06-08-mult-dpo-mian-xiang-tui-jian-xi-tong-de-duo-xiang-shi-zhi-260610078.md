---
title: 'Mult-DPO: Multinomial Direct Preference Optimization for Recommender Systems'
title_zh: Mult-DPO：面向推荐系统的多项式直接偏好优化
authors:
- Yaochen Zhu
- Harald Steck
- James McInerney
- Aditya Sinha
- Yinhan He
- Nathan Kallus
- Jundong Li
affiliations:
- University of Virginia
- Netflix
- Cornell University
arxiv_id: '2606.10078'
url: https://arxiv.org/abs/2606.10078
pdf_url: https://arxiv.org/pdf/2606.10078
published: '2026-06-08'
collected: '2026-06-10'
category: GenRec
direction: 生成式推荐 · 多正例偏好优化
tags:
- DPO
- Set-wise preferences
- LLM alignment
- Recommender Systems
- Plackett-Luce
- Multinomial surrogate
one_liner: 提出多项式替代似然，将 DPO 扩展到多正例集合式偏好对齐，并证明其为 marginalized PL 损失的上界
practical_value: '- 对于包含会话、行为序列等场景，用户通常有多个正反馈（点击/喜欢），可直接用 Mult-DPO 同时建模多个正例与负例，无需成对损失，时间复杂度从
  O(K^2) 降至 O(K)。

  - 训练时利用 KV-cache 复用 prompt 部分，使得单步计算开销与 vanilla DPO 相当，适合部署在电商/对话推荐中序列较长、候选物品较多的场景。

  - 硬负例采样能收紧损失上界，可借鉴 SPRec 风格按 epoch 动态采样高权重负例，进一步强化对齐效果。

  - 若存在多级偏好（如评分 1-5），可直接用 Mult2-DPO 保留精细偏好结构，提升排序质量，适合替换传统 BPR 损失。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
推荐系统的用户反馈往往是集合式的：一个上下文（用户、会话、对话）对应多个正例和多个负例，任何正例应优于任何负例，但正/负例内部无顺序。传统 DPO 仅支持成对偏好，直接扩展至集合式偏好需在 Plackett-Luce（PL）模型上对正例所有顺序进行边际化，复杂度为指数级。已有方法或仅用单个正例，或损失函数缺乏严谨排序解释。为此，本文提出多项式替代模型，将集合式偏好对齐转化为可处理的多项式似然，并推导出 DPO 风格的损失函数。

**方法关键点**
- 将集合式偏好事件定义为一个多项式替代似然：从正/负例总权重归一化的类别分布中独立抽取 k 次，要求每个正例恰好出现一次且无负例出现。该似然计算复杂度为 O(k)。
- 证明该多项式似然是 marginalized PL 似然的下界（即 Mult-DPO 损失是精确 PL-DPO 损失的上界），并给出紧度分析：边界紧度由正例总权重 A 与负例总权重 B 的比值 (1 + A/B)^{k-1} 控制，负例越“硬”（B 越大）边界越紧。
- 通过 RLHF 奖励-策略重参数化，将多项式替代模型转化为 DPO 风格的目标函数（Mult-DPO 损失），避免显式奖励模型训练。
- 进一步扩展至多级偏好（如 1-5 星评分），将多个等级拆分为序列化的集合式偏好事件，提出 Mult2-DPO，在每个边界上应用多项式替代，直接利用细粒度反馈。

**关键实验**
在 Goodreads、MovieLens-10M 和 Reddit-V2（对话推荐）数据集上，以 Qwen2.5 模型为骨干，对比 SFT（BigRec, D3）及多种 DPO 变体（vanilla DPO, DMPO, S-DPO, LiPO）。主要结果：
- Mult-DPO 在所有基准上全面领先最强基线，尤其在多正例密集的 Reddit-V2 上，NDCG@5 相对 LiPO 提升超 10%（0.5B 模型 0.1097 vs 0.0963，3B 模型 0.1369 vs 0.1147）。
- 动态硬负例采样（SPRec 式）进一步改善 NDCG，验证了紧度理论的实用价值。
- Mult2-DPO 在 MovieLens 四等级偏好设置下比 binary Mult-DPO 提升 NDCG@5 约 12%（0.5B: 0.0732 vs 0.0650），且大模型下收益依然存在。

**一句值得记住的话**
多项式替代让多正例对齐可处理，且是一种有理论上界 guarantee 的保守替代，硬负例能让这个上界更紧，是实践中的低成本提效手段。
