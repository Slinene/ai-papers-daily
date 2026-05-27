---
title: Credit-assigned Policy Gradient for Early Stage Retrieval in Two-stage Ranking
title_zh: 两阶段排序早期检索的信贷分配策略梯度方法
authors:
- Haruka Kiyohara
- Mihaela Curmei
- Ariel Evnine
- Shankar Kalyanaraman
- Israel Nir
- Ana-Roxana Pop
- Nitzan Razin
- Sarah Dean
- Thorsten Joachims
- Udi Weinsberg
affiliations:
- Cornell University
- Meta
arxiv_id: '2605.26385'
url: https://arxiv.org/abs/2605.26385
pdf_url: https://arxiv.org/pdf/2605.26385
published: '2026-05-25'
collected: '2026-05-27'
category: RecSys
direction: 两阶段推荐 · 早期检索策略梯度
tags:
- Two-Stage Ranking
- Policy Gradient
- Credit Assignment
- Variance Reduction
- Plackett-Luce
- Recommender Systems
one_liner: 提出 CA-PG，通过对含目标项的候选集边际化概率求梯度，大幅降低方差，提升早期检索训练稳定性。
practical_value: '- **ESR 训练避坑：不要直接用 V-PG**。当候选集 K>10 时，原始策略梯度因组合动作空间（|A|^K）导致梯度溢出和不稳定，实践中推荐切换到
  CA-PG 或 TOP1-PG。

  - **TOP1-PG 是高效默认选择**：当 ESR 为单一 PL 模型（非 MoE）时，TOP1-PG 仅需 O(L) 计算，远低于 V-PG 的 O(K)，且实验收敛更快，可直接替代
  V-PG-SwR。

  - **MoE 场景用 CA-PG-SwR**：若有多个专家子检索器，CA-PG-SwR 支持多 logit 模型，计算 O(ML)，比 CA-PG 的 O(KL)
  更经济，且性能优于 V-PG-SwR，适合大规模电商多路召回。

  - **LSR 对齐要求不苛刻**：理论证明只要 LSR 排序“合理对齐”（如 ε-贪婪、随机策略），CA-PG 仍能学到最优分区（top-K 正确），因此现有业务精排模型可直接作为
  LSR 使用，不必担心偏差过大。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：大模型搜索、推荐和 RAG 系统普遍采用两阶段架构：早期检索（ESR）生成候选集，晚期排序（LSR）重排。训练 ESR 的端到端策略梯度（V-PG）面临组合动作空间带来的方差爆炸，且存在信贷分配问题——V-PG 同等对待候选集内所有物品，无法区分具体贡献，导致训练不稳定、收敛慢。

**方法关键点**：
- 提出 **CA-PG**：对 ESR 的边际概率 `π(S_K(a)|x)` 求梯度，即目标物品 `a` 被包含在任何候选集的概率，而非具体候选集的联合概率。
- 理论分析显示 CA-PG 是 V-PG 的方差缩减成分，消除了对特定候选集的依赖。
- 给出 PL 策略下的有效计算：精确 CA-PG 复杂度 O(KL)，但通过采样有放回（SwR）近似得到 CA-PG-SwR（O(ML)），特别当 M=1 时退化为 **TOP1-PG**（只考虑物品被选为 top-1 的概率），复杂度 O(L)。
- 证明只要 LSR 排序“合理对齐”（例如最优策略与均匀策略的插值），CA-PG 能学到正确的 top-K 分区。

**关键实验**：
- 合成数据（1000 用户×1000 物品，向量内积奖励）和真实 KuaiRec 数据。
- 对比 V-PG、V-PG-SwR、CA-PG、CA-PG-SwR（TOP1-PG）。
- 结果：合成数据 K=20 时，V-PG 频繁梯度溢出，CA-PG 稳定训练且 5 万步内收敛速度比 V-PG-SwR 快约 3 倍；真实数据 K=50/100/200 时，TOP1-PG 在 5 万步已显著领先 V-PG-SwR。
- MoE 场景下（M=5），CA-PGs 性能优于 V-PG，展示了多专家探索的优势。

**一句话精华**：忽略候选集具体组成的边际化梯度，可以在实际可行的样本量下实现稳定快速的 ESR 在线学习。
