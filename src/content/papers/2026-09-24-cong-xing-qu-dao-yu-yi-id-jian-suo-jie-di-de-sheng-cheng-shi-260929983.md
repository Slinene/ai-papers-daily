---
title: 'From Interests to Semantic IDs: Retrieval-Grounded Credit Assignment for Generative
  Recommendation'
title_zh: 从兴趣到语义ID：检索接地的生成式推荐信用分配
authors:
- Mengdan Zhu
- Yufan Zhao
- Yao Zhao
- Sophie Di
- Tao Di
- Yulan Yan
- Sridhar Iyer
- Liang Zhao
affiliations:
- Emory University
- Microsoft
- Cornell University
arxiv_id: '2609.29983'
url: https://arxiv.org/abs/2609.29983
pdf_url: https://arxiv.org/pdf/2609.29983
published: '2026-09-24'
collected: '2026-09-27'
category: GenRec
direction: 生成式推荐 · Semantic ID · RL 信用分配
tags:
- Generative Recommendation
- Semantic IDs
- Credit Assignment
- Reinforcement Learning
- Retrieval
one_liner: 用冻结检索器执行生成兴趣查询，按查询命中证据把检索奖励局部化到 interest span，缓解 SID 精确匹配奖励稀疏
practical_value: '- 在电商/生成式推荐中，如果使用 LLM 直接生成 item ID（Semantic ID），可以要求模型同时输出结构化的“用户兴趣
  query”，用已有的商品检索服务执行每个 query，把“目标商品是否被召回”作为辅助 reward；这比单纯 exact-match item reward
  提供更密的训练信号。

  - 信用分配不要 broadcast 到整段 trace：记录每个 query 的命中 indicator，positive rollout 只把 retrieval
  advantage 路由到命中 query 所在 token span；negative rollout 平分到所有 query，final SID span
  不给 retrieval reward。这种 span-level 路由在消融里明显优于整段 broadcast。

  - 推理时把生成的兴趣 query 直接当成召回接口：合并 top-K 结果做去重，作为候选池；如果后端是受限 beam search，可用候选 SID 构建
  trie 约束解码，而不是只在全目录上 beam search。论文 oracle 显示选对 query 时 Recall@10 可以 11.95→14.93，说明兴趣条件解码有空间。

  - reward retriever 用 4B embedding 已接近 8B，训练 cutoff 选 50 是中间甜点，不必盲目增大 encoder/扩大
  K；这个结论在预算有限时可以直接复用。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：SID 生成式推荐通常先产生推理 trace，再自回归解码下一 item SID，强化学习用 exact-match SID reward。这个 reward 在大目录下非常稀疏：一个 rollout group 内所有采样 SID 可能全不中，组内标准化后 advantage 为零；即使多个 rollout 拿到相同 SID reward，它们的 trace 被等同对待，无法区分哪个兴趣假设有贡献。因此 item-level reward 只反馈 final SID，对 trace 存在 credit assignment gap。

**方法关键点**：
- 响应结构化为 history_summary + future_interests + final SID；每个 future_interest 行是一条可执行 query。
- 训练时用冻结 dense retriever 对每条 interest query 检索目录，若 target SID 进入 top-K 则产生 query-level hit；rollout 级 retrieval reward 为 any hit。
- 信用分三个通道：SID exact match → full response，trace validity → reasoning trace，retrieval advantage 按 query hit indicator 路由，只给命中 interest lines；negative rollout 平分给所有 interest lines；final SID span 永远不接收 retrieval advantage。
- Stage1 SID alignment，Stage2 用 GPT-4o 构造结构化 trace，Stage3 group-relative RL + dual-clip PPO，并用 trie 保证 SID 采样合法。
- 推理时可复用生成 interests 做候选召回，或将候选 SID 集合构建成 trie 约束 beam search。

**关键实验**：三个 Amazon Reviews 类别（Video Games / Office / Industrial）。相对 matched SID+trace 控制，Video Games Recall@10 0.0856→0.1195 (+39.6%)、NDCG@10 0.0493→0.0796 (+61.5%)；Office Recall@10 0.1512→0.1765 (+16.7%)；Industrial Recall@10 0.1387→0.1602 (+15.5%)，12 个指标全部最优。检索信号在 SID-inactive group 中恢复优势：Games reactivation rate 37.8%、Office 37.7%、Industrial 19.6%。消融显示 hit-query routing > interest-block routing > full broadcast。Oracle interest-conditioned SID decoding 将 Video Games Recall@10 从 11.95 提到 14.93。

最值得记住的一句话：把中间生成文本改造成可执行、可验证的查询，用检索命中证据在 span 级分配信用，就能让稀疏的 final-item reward 在生成式推荐中提供有效过程监督。
