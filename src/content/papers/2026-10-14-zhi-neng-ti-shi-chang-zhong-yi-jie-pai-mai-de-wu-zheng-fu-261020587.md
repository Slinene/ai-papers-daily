---
title: Price of Anarchy of First-Price Auctions in Agentic Markets
title_zh: 智能体市场中一价拍卖的无政府代价
authors:
- Shubhendu Trivedi
- Jacob Eisenstein
- Alekh Agarwal
- Ian Gemp
- Michael Kaisers
- Adam Fisch
affiliations:
- Google DeepMind
- Google Research
arxiv_id: '2610.20587'
url: https://arxiv.org/abs/2610.20587
pdf_url: https://arxiv.org/pdf/2610.20587
published: '2026-10-14'
collected: '2026-10-15'
category: MultiAgent
direction: Agentic market 拍卖机制与效率
tags:
- First-Price Auction
- Price of Anarchy
- Agentic Market
- LLM Routing
- Mechanism Design
- Multi-Agent Systems
one_liner: 证明竞争底线与近似条件独立使一价拍卖在智能体市场中福利损失远低于最坏情况，并用 EmbedLLM 仿真验证。
practical_value: '- 在 LLM 路由/多模型服务中，一价拍卖简单透明，若模型能力接近（竞争底线），福利损失极小；可替代复杂的 VCG 机制。

  - 平台可引入自有模型作为 reserve price 或预过滤弱模型，主动提升竞争底线，保护分配效率。

  - 将模型价值定义为 expected quality - inference cost，用 prompt embedding 聚类/条件化可以近似条件独立，降低
  bid shading。

  - EmbedLLM 实验显示 FPA 达到 99.2% 最优福利，远高于固定路由 best-per-cluster 的 89.4%，动态竞价在多模型路由中有实际收益。'
score: 9
source: arxiv-cs.LG
depth: full_pdf
---

**动机**：Agentic market 中多个 AI agent 对用户 prompt 出价，一价拍卖（FPA）简单透明，但非 truthful，存在 bid shading 导致福利损失。最坏情况 PoA 仅 63.2%，即使独立价值也只有 86.5%。但实际智能体市场可能具有更优结构，需要量化这些结构对效率的影响。

**方法关键点**：
- 定义 (α, m, ε)-competitive floor：至少 m 个 bidder 以概率 ≥1-ε 价值不低于 α E[V(1)]。证明确定性 floor（m=2, ε=0）下 PoA ≥ (1-1/e) + α/e；概率性 floor 下减去惩罚项 α S_m(ε)。
- 条件化公共信息 X 后，价值分布接近 independent product（TV 距离 τ(x)），PoA 接近 1-1/e^2，误差随 τ 平滑退化。
- 平台设计：预过滤弱模型可提升下界；平台自有模型以真实价值参与竞价等价于 query-specific reserve price，下界为 (1-1/e) + (1/e) E[V0]/E[V(1)]。

**关键实验**：在 EmbedLLM 数据集（30k prompts，110 模型）上用 kNN 估计准确率、线性成本，fictitious play 求解 typical 与 adversarial BNE。全市场 FPA 达到 Oracle 福利的 99.2%（typical）/ 98.8%（adversarial），显著高于 best-per-cluster 路由 89.4%。worst cluster 上 FPA 保持 96.0%/93.0%，而固定路由仅 64.0%。随机子市场经验 PoA 集中在 95% 以上；手选 cohort 显示模型能力接近时 shading 与福利损失更低。

**一句话**：当多个模型能力接近或价值在给定 prompt 后近似独立时，简单的一价拍卖已能捕获绝大部分福利，无需复杂机制。
