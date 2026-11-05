---
title: Alternatives to Shallow Autoencoders for Collaborative Filtering
title_zh: 协同过滤中浅层自编码器的替代方案
authors:
- Mario Mallea
- Angela Nebot
- Francisco Mugica
affiliations:
- Universitat Politècnica de Catalunya
arxiv_id: '2611.06610'
url: https://arxiv.org/abs/2611.06610
pdf_url: https://arxiv.org/pdf/2611.06610
published: '2026-11-04'
collected: '2026-11-05'
category: RecSys
direction: 协同过滤 · 浅层自编码器变体
tags:
- Collaborative Filtering
- Autoencoder
- EASE
- User-User
- Item-Item
- Hybrid Model
one_liner: 提出基于 EASE 的 user-user 变体与混合模型，融合用户和物品邻接分布，在基准上超越 EASE
practical_value: '- 工业界常以 EASE 作为 item-item 相似度强基线；可直接复现其 user-user 对偶形式，构建用户侧相似度矩阵，作为召回或排序的线性模型，尤其适合电商用户行为稀疏但商品数量巨大的场景。

  - 混合模型思路简单：将 item-item 与 user-user 的邻接分布做加权融合或集成，可在后端用低秩/稀疏求解加速，不增加推理复杂度，易于 AB 实验。

  - 若现有系统已有 item-based CF，引入 user-based 信息相当于增强用户冷启动和新用户推荐能力，可在用户行为较少时仍提供可解释推荐。

  - 注意 EASE 的正则化与求逆成本，生产环境可用共轭梯度/近似求解；若引入 user-user，需处理用户数量增长带来的计算放大，可考虑分桶或采样。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：EASE 在稀疏协同过滤中因闭式解和强排名精度受关注，但仅依赖 item-item 邻接矩阵拟合全秩线性映射，忽略用户之间的细粒度相似关系，可能限制精度。

**方法关键点**：基于 EASE 目标函数，构建 user-user 邻接分布的浅层自编码器变体；进一步提出混合模型，同时结合 item-item 与 user-user 邻接分布，仍保持闭式解特点。

**关键结果**：在多个知名推荐基准上，所提变体与混合模型均优于 EASE，验证用户侧信息对线性浅层模型的有效性。
