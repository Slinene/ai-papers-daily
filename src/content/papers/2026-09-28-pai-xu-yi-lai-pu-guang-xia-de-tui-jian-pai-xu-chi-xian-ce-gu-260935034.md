---
title: Recommendation Ranking Off-Policy Evaluation under Ranking-Dependent Examination
  via Examination-Relevance Decomposition
title_zh: 排序依赖曝光下的推荐排序离线策略评估：曝光-相关性分解
authors:
- Riki Okamura
- Toshiharu Sugawara
affiliations:
- Waseda University
arxiv_id: '2609.35034'
url: https://arxiv.org/abs/2609.35034
pdf_url: https://arxiv.org/pdf/2609.35034
published: '2026-09-28'
collected: '2026-09-30'
category: RecSys
direction: 离线评估 · 曝光-相关性分解
tags:
- Off-Policy Evaluation
- Ranking
- Click Model
- Examination-Relevance Decomposition
- Doubly Robust
- Recommender Systems
one_liner: 将点击分解为曝光与相关性，提出 LE-IIPS 与 ED-DR，修正排序依赖曝光下的 OPE 偏差
practical_value: '- 在电商/广告排序评估新策略时，点击日志无法区分“未曝光”和“曝光未点击”，直接使用 IIPS 会在曝光概率依赖整个排序（如邻近商品吸引注意力）时产生偏差；可显式建模
  e_k(x,a) 和 r(x,a(k))，在权重中乘上 \bar{e}_k^π / e_k 修正。

  - ED-DR 的双重稳健性适合工程落地：只要曝光概率估计正确，即使相关性模型不准确，评估仍无偏；可在相关性模型不确定时优先保证曝光模型的准确性，降低风险。

  - 样本量小时 IIPS 方差更低，大样本时 ED-DR MSE 更低，存在临界 n*；线上评估前可按历史样本量选择估计器，不必一味用 DR。

  - 用 regression EM + intervention harvesting 初始化估计曝光概率，relevance 模型只依赖 item 不依赖位置，可跨位置池化数据，缓解稀疏
  item-position 对。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
推荐排序策略上线前通常依赖离线策略评估（OPE）降低 A/B 测试风险。然而点击日志中 Y_k=0 同时包含“未曝光”和“曝光未点击”两种情况，无法区分。现有 IIPS、RIPS、cascade DR、AIPS 等估计器未显式建模曝光，当曝光概率依赖整个排序（例如邻近商品吸引注意力）时，IIPS 的核心假设（位置点击只依赖该位置 item）失效，产生偏差。

**方法关键点**
- 点击模型分解：Y_k = O_k R_k，其中 O_k ~ Bern(e_k(x,a)) 表示曝光，R_k ~ Bern(r(x,a(k))) 表示相关性，并假设 O_k 与 R_k 条件独立，q_k = e_k·r。
- 曝光模型分类：(E1) PBM 仅依赖位置、(E2) contextual PBM 依赖位置与 context、(E3) 排序依赖曝光，本文聚焦 (E3)。
- LE-IIPS：在 IIPS 权重上乘以 \bar{e}_k^π(x,a(k)) / e_k(x,a)，修正排序依赖曝光下的偏差。
- ED-DR：LE-IIPS 扩展到 doubly robust 框架，加入 DM 项，利用全部观测；权重同 LE-IIPS。
- 理论性质：ED-DR 在曝光概率估计正确时无偏，且与相关性模型无关；在 (E1)/(E2) 下即使曝光和相关性都估计不准也无偏；排序依赖曝光下样本量超过 n* 后 MSE 低于 IIPS。
- 估计实现：regression EM + intervention harvesting 初始化，relevance 模型位置无关从而跨位置池化，使用 cross-fitting。

**关键实验**
- 合成数据：n=4000，K=5，m=10，logging 为 Plackett-Luce，evaluation 为 ε-greedy。
- 对比 IIPS、RIPS、cascade DR、AIPS、DM、DR-IIPS。
- 在 (E3) 下，非 oracle 估计器中 ED-DR 相对 MSE 最低；小样本时 IIPS 方差更低，大样本 ED-DR 占优，符合 n* 理论。
- 曝光结构误设：true (E3) assumed (E3) 相对 MSE 3.24e-3，误设为 (E2)/(E1) 增至 5.25/5.24e-3。
- DBN 行为下随离开概率 ρ 增大，ED-DR 偏差增加但方差不变；ρ=1 时 RIPS 与 cascade DR 方差显著下降，相对 MSE 反超 ED-DR。
- 低 logging 温度 τ0 下权重类估计器方差爆炸，DM 稳定但偏差持续。

**最值得记住的一句话**：ED-DR 的无偏性在曝光概率正确时对相关性模型不敏感，排序依赖曝光下样本量超过临界值 n* 后 MSE 优于 IIPS。
