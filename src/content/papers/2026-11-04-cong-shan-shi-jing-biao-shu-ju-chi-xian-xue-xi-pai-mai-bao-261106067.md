---
title: Offline Learning of Reserve Prices from Censored Bids
title_zh: 从删失竞标数据离线学习拍卖保留价
authors:
- Lavanya Marla
- Yunzong Xu
- Boxuan Zhou
affiliations:
- University of Illinois Urbana-Champaign
arxiv_id: '2611.06067'
url: https://arxiv.org/abs/2611.06067
pdf_url: https://arxiv.org/pdf/2611.06067
published: '2026-11-04'
collected: '2026-11-05'
category: Other
direction: 离线拍卖定价 · 删失数据 minimax regret
tags:
- reserve price
- censored data
- minimax regret
- MHR
- offline learning
- auction
one_liner: 在 MHR 假设下，把删失竞拍数据中的保留价学习转化为仅依赖删失比例和边界 hazard 的 minimax regret 问题，并给出匹配的
  N^-2/5 学习率
practical_value: 以下内容可直接迁移到电商/广告平台用历史竞价日志调整底价的场景：
score: 9
source: arxiv-stat.ML
depth: full_pdf
---

**动机**：在二阶价格拍卖中，卖家从历史出价数据离线学习保留价（reserve price）。低于历史保留价的出价不可观测，导致即便无限数据，价值分布低段仍不可识别；这是电商/广告平台用历史竞价日志调整底价时的核心障碍。

**方法关键点**：
- 在单调 hazard rate（MHR）假设下，给出可识别最优保留价的充分必要条件：φ0≤0（tail-optimal）或 A=λh0（fully identified）。
- 在非识别区，minimax regret 只依赖两个可观测量：删失比例 α 和边界 hazard h0=g(λ+)/(1-α)。最坏完成分布可由至多两段常 hazard 构造，问题降为二维优化。
- 有限样本：tail-optimal 用经验尾部 O(N^-1/2)；fully identified 只用删失计数 O(N^-1)；非识别区用投影 plug-in 规则，边界 hazard 用局部线性直方图、带宽 N^-1/5，总超额 worst-case regret O(N^-2/5)，且下界匹配。
- 提出 auto-selector：先根据估计 h0 与 1/λ 比较选择分支。

**关键实验**：合成和 eBay 数据上，利用 MHR 的 robust 规则比无约束和 misspecified 参数 MLE 更稳；在 Palm Pilot 数据上，复用 opening bid 可能损失最高 54% 的 optimal revenue。

**最值得记住的一句话**：删失数据下不要直接拟合分布选最优 reserve；MHR 约束下只估计删失比例和边界 hazard 两个量，plug-in 到 minimax reserve，就能把不可识别带来的超额 regret 控制在 N^-2/5。
