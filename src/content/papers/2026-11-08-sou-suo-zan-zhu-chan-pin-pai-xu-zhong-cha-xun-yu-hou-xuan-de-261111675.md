---
title: Query- and Candidate-Aware Long User Sequence Modeling for Sponsored Product
  Ranking in Search
title_zh: 搜索赞助产品排序中查询与候选感知的长用户序列建模
authors:
- Dongyue Xie
- Sergey Kolbin
- Manavender Malgireddy
- Iurii Shcherbak
- Weixing Tang
- Arushi Jain
- Wanchen Shao
- Kurt Zimmer
- Raja Hafiz Affandi
- Matt Lindsay
affiliations:
- Wayfair LLC
arxiv_id: '2611.11675'
url: https://arxiv.org/abs/2611.11675
pdf_url: https://arxiv.org/pdf/2611.11675
published: '2026-11-08'
collected: '2026-11-10'
category: RecSys
direction: 搜索广告长序列建模 · 双路检索
tags:
- Long User Sequence Modeling
- Sponsored Search
- CTR Prediction
- Candidate-aware Early Fusion
- Dual Retrieval
- Transformer
one_liner: 在搜索广告排序中，将候选商品与查询双路检索的长历史行为和候选早期融合结合，显著提升 CTR 与转化
practical_value: '- 在搜索/广告等同时有 query 和 candidate 上下文的场景，长历史建模可模仿“双路检索”：分别用 query 和
  candidate embedding 从长历史 ANN 检索 top-K，再与最近行为拼接去重；生产预算可参考 100 recent + 50 candidate
  + 50 query，长历史池约 O(10^3) 即可。

  - candidate early fusion 不能省：把 candidate embedding 拼进每个 history token 的输入，而不是只放一个全局
  candidate token；否则模型很难间接学到 candidate-history 匹配。这在多路召回后的精排 Transformer 中可复用。

  - 若要加 next-action 辅助 loss 并防止泄漏，可采用 hybrid attention：前几层 causal + 允许 history 看 query/candidate，context
  token 只互看；后几层 bidirectional 做最终表示。这样 NAL 和 ranking loss 可以共享编码。

  - 工程上检索用低维语义 embedding（如 32 维）控制 ANN lookup 延迟，序列长度控制在 200 内，端到端延迟仅 +12%，线上 CTR/订单提升明显；可作为广告精排或生成式推荐的架构参考。'
score: 10
source: arxiv-stat.ML
depth: full_pdf
---

在搜索广告排序中，当前 query 表达即时意图，候选商品决定长历史中哪些行为相关。近期行为窗口窄，长历史有语义相关产品和持久偏好，但原始历史有数万动作且绝大多数无关，在线 latency 限制不能全量过 Transformer。因此需要按请求目标从长历史中检索/压缩相关子序列。现有 candidate-only 检索可能召回与候选相似的历史商品，却漏掉与 query 高度相关但和候选仅间接相关的行为；反之亦然。该工作把 query 和 candidate 两个视角同时作为检索条件，并在序列 token 构造中显式注入两个上下文。

方法关键点：
- 历史序列由三部分拼接：最近 100 条近期行为；从剩余长历史（一年窗口，约 O(10^3)）中用 candidate-SKU 语义相似度检索 50 条；用 query-SKU 语义相似度检索 50 条；去重后最多 200 条。检索用 32 维 SKU embedding，降低 ANN 成本。
- 输入序列为 [query token; candidate token; history tokens]。query/candidate token 由投影向量加 role embedding 后 LN；每个 history token 除 action/SKU/metadata/surface/time 外，还拼接 candidate embedding，实现 token 级 candidate-aware early fusion。
- 2 层 Transformer，首层 hybrid attention：history 之间 causal，history 可看两个 context token，但 context token 只互相看；次层全双向。首层输出用于 NAL（next-action loss，in-batch negatives），避免未来行为泄漏到前层。
- 最终表示汇总 h_q、h_c、sequence projection、candidate-aware attention pooling、masked max pooling；多任务 BCE/MSE 训练。

关键实验：离线 M0-M6 ablation 相对 recent-only baseline，单 candidate-NN +1.16% click AUC / +1.35% order-7d AUC；单 query-NN +1.00%/+1.16%；双检索 +1.37%/+2.19%。去掉 query/candidate token 掉到 +0.45%/+0.28%；去掉 NAL 降到 +1.11%/+1.46%；去掉 early fusion 最严重，-4.71%/-6.06%。在线 5 周 A/B：CTR +6.0%，orders/impression +11.5%，attributed CVR +5.2%，CPC -1.3%，ad spend +0.8%，均显著；端到端模型推理延迟增加约 12%。

最值得记住的一句话：早期融合（candidate 注入每个 history token）比全局 candidate token 重要得多；双路检索互补，适合 query + candidate 双重上下文的搜索广告排序。
