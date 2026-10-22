---
title: 'Generative Recommenders Forget the Long Tail: Restoring Memorization in Retrieval
  and Ranking'
title_zh: 生成式推荐遗忘长尾：检索与排序中的记忆恢复
authors:
- Xu Huang
- Jiancan Wu
- Hongzheng Qin
- Jiawei Feng
- Can Ye
- Wencong Zeng
- Fengze Li
- Xiang Wang
affiliations:
- University of Science and Technology of China
- Ant Group
arxiv_id: '2610.29298'
url: https://arxiv.org/abs/2610.29298
pdf_url: https://arxiv.org/pdf/2610.29298
published: '2026-10-21'
collected: '2026-10-22'
category: GenRec
direction: 生成式推荐 · 长尾纠偏
tags:
- Generative Recommendation
- Long-tail
- Beam Search
- Memorization
- Co-occurrence
- Semantic ID
one_liner: 提出无训练插件 CAPE，用 item-level 共现记忆同时修复生成式推荐的检索剪枝和排序偏差，显著提升长尾命中
practical_value: '- 线上生成式推荐不要只扩 beam 或只做重排：先用 beam 的 tail recall 和 tail conversion
  定位瓶颈。若 beam 尾召回不足，需要额外候选；若 recall 足够但命中差，重排更关键。论文 Proposition 2.1 可作为上线前检查。

  - 用原始 item-item 共现矩阵构建轻量长尾候选通道，比训练 LightGCN 更适合精确记忆。用户级 support 进候选、事件级 mean 做排序，min-max
  归一化后与生成 likelihood 融合，只需一个超参 λ。电商可直接统计用户历史商品与候选商品在多少用户中共同出现，补足 beam 外的长尾。

  - top-1 anchoring 是无痛上线关键：保持 backbone 首项不变，只重排第 2-K 位；若更看重整体 GMV，可去掉 tail mask 把共现证据用于全部候选。

  - 工程成本低：CSR 稀疏矩阵存共现，每请求只增加约 100 token teacher forcing，延迟增 11-16%，可批处理；而扩 beam 50%
  延迟翻倍还不一定提升尾命中。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

动机：生成式推荐用 semantic ID 一个模型同时做检索和排序，但共享 likelihood 导致长尾物品被遗忘两次。beam search 按 prefix subtree mass 保留，长尾物品前缀少，50 宽 beam 只覆盖 5-12% 长尾目标；即使给生成器额外 25 个共现支持的尾物品，likelihood 在 Amazon 工业域几乎一个也排不进 top-10。现有 popularity correction、diversity rerank 只作用于候选重排，受 beam recall 上限约束。

方法关键点：
- 诊断：检索与排序共享同一 likelihood，Proposition 2.1 排序受 beam recall 封顶；Proposition 2.2 beam 按子树总质量保留前缀，尾部前缀被头物品 mass 淹没。
- CAPE 训练-free 插件：
  1) 记忆通道：用用户级共现矩阵 U[j,c]，对历史物品求 support S_u(c)=Σ U[i_p,c]，从 beam 外尾部物品中取 top-B'=25 项加入候选池；冻结生成器 teacher forcing 给这些候选算 likelihood。
  2) 记忆校准排序：事件级共现证据 e_u(c)=I[c∈T]·(1/n)Σ W[i_p,c]，对 likelihood 和 evidence 分别 min-max 归一化后融合：s_u(c)=N(ℓ_u(c))+λ N(e_u(c))；只有单一超参 λ。
  3) top-1 anchoring：保持 backbone 第一项不变，降低部署风险。

关键实验：在 MiniOneRec 和 TIGER 两个 backbone，Amazon I&S/Office/Beauty 和 LastFM-1K 上评估。CAPE 在所有四个主要设置中取得最高 tail HR@10，相对 backbone 提升 2.5-13.3 点，相对最强 reranker 提升 1.6-7.3 点；overall HR@10 在 I&S 不变，其他三个设置提高。LastFM 上两个 backbone 尾 HR@10 差异近 2 倍（7.89 vs 3.94），CAPE 都拉到 17.19，说明主要补的是记忆缺口。消融显示去掉检索通道或去掉校准排序都显著下降；随机/流行尾部填充无效；LightGCN 通道不如 item-level 共现；移除 tail mask 可换来整体指标。延迟只增加 11-16%，而加宽 beam 增加 109-143%。

最值得记住的一句话：生成式推荐的长尾损失不是单阶段问题：检索被 prefix mass 剪掉，排序又用同一个 likelihood 把已召回尾巴压下去；必须在候选生成和排序两侧同时注入 item-level 共现记忆，而不是只扩 beam 或只重排。
