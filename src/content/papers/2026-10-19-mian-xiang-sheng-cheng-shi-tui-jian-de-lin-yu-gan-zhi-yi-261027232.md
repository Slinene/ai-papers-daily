---
title: Neighborhood-Aware Unlearning for Generative Recommendation
title_zh: 面向生成式推荐的邻域感知遗忘
authors:
- Pierre Lubitzsch
- Yubao Tang
- Maarten de Rijke
- Sebastian Schelter
affiliations:
- BIFOLD & TU Berlin, Germany
- University of Amsterdam, The Netherlands
arxiv_id: '2610.27232'
url: https://arxiv.org/abs/2610.27232
pdf_url: https://arxiv.org/pdf/2610.27232
published: '2026-10-19'
collected: '2026-10-21'
category: GenRec
direction: 生成式推荐 · SID 邻域感知遗忘
tags:
- Machine Unlearning
- Generative Recommendation
- Semantic ID
- Neighborhood-Aware
- Spam Removal
- Sequential Recommendation
one_liner: NAU 结合 SID 级遗忘目标与邻域概率质量控制，消除生成式推荐遗忘对共享 token 邻近物品的泄漏，保持超 95% 重训效用
practical_value: '- 在 SID / Semantic ID 生成式推荐中做遗忘时，不要只对目标 item 做 gradient ascent，要在
  loss 中显式加入邻居概率质量项；λ_n 取正保留合法邻近替代品（spam 删除），取负抑制相似语义邻居（不想推的类目），一个参数控制两种删除场景。

  - 评估遗忘效果不能只看全局 NDCG，必须增加“被删 item 的 SID 邻域”上的 utility/exposure 指标；本文显示全局 NDCG 几乎不变时邻域
  NDCG 可能掉 13 个百分点以上。

  - 工程上可复用 retain+forget+separation+neighborhood 四类 loss 组合，无需二阶信息，模型架构和 SID 保持固定，推理时也不做候选过滤；遗忘耗时
  3.7s vs retrain 17,399s，适合频繁删除请求。

  - 邻居构建可以直接用 pre-quantization embedding 的 top-k（k=8），评估用 SID 第一 token 邻域；这种结构对商品语义编码相似的电商场景可快速迁移。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

动机：生成式推荐通过自回归生成 Semantic ID（SID）预测 next item，语义相近的 item 共享 token。当需要删除训练交互（刷单注入、用户要求不推某类目）时，直接 unlearning 会通过共享 token 把影响扩散到“邻域” item，全局 NDCG 可能几乎不变，但邻域效用大幅下降，这种局部失效被全局指标掩盖。

方法关键点：
- 将 token-level 训练损失改为 item-level 的完整 SID 负对数似然。
- 遗忘目标由 4 项组成：L_ret 保留 retained 交互；L_for 在 forget set 上做 gradient ascent；L_sep 对 forget targets 做对比分离，防止其在新推荐中仍排在前列；L_nbr 显式控制目标邻居的总生成概率 mass。
- λ_n 符号切换：>0 保留合法邻近替代品（spam removal）；<0 抑制相似语义邻居（unwanted item removal）。
- 无需二阶信息，模型架构与 SID 保持固定。

关键结果：在 Amazon Beauty/Sports/Toys 三个数据集，TIGER backbone 加 RQ-KMeans、RQ-VAE、LETTER 等 tokenizer 上，spam removal 场景 NAU 在 Beauty/Toys 的 ΔretrSH 分别为 0.081% 和 0.074%，优于 Forget+Repair 的 0.106%/0.195%，同时保持 96.2–101.8% 重训 NDCG@10。Beauty 邻域维度，NAU 把 Forget+Repair 丢失的邻域效用从 87.0% 恢复到 108.1%。unwanted item removal 场景，Sports 的 UHF@10 从 27.6% 降到 11.1%，且对无关用户的影响更小；遗忘耗时 3.7s，对比 retrain 17,399s。

最值得记住：在 SID 生成式推荐中，遗忘不是只移除目标 item 的分数，而是要显式控制邻居概率质量，否则全局指标会掩盖局部崩塌。
