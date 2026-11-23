---
title: 'ERA: Embed, Route, Adapt for Cold-Start Cross-Model Latent Retrieval'
title_zh: ERA：冷启动跨模型潜在检索的嵌入、路由与适配
authors:
- Venkata Chivukula
- Zifeng Wang
- Jinsung Yoon
affiliations:
- Google
arxiv_id: '2611.26919'
url: https://arxiv.org/abs/2611.26919
pdf_url: https://arxiv.org/pdf/2611.26919
published: '2026-11-20'
collected: '2026-11-23'
category: RAG
direction: 冷启动跨模型向量检索与路由
tags:
- cross-model retrieval
- embedding alignment
- anchor selection
- cold-start
- latent routing
- RAG
one_liner: FPS选anchor+流形对齐损失+硬查询路由，实现无重建索引的冷启动跨模型检索
practical_value: '- 已有线上向量库（商品/内容/广告 embedding 由某个大模型或 API 构建）要换新的 query encoder 时，不必全量重建索引：用目标空间里的
  Cosine FPS 从库存向量中挑几百到几千个 anchor 训 MLP adapter，能覆盖 corpus 流形并省大量 API/GPU 成本，适合电商搜索/推荐召回快速试新模型或多模型融合。

  - 冷启动无监督投影时，单独用 MSE/ℓ2 容易把投影 collapse 到窄 cone；加上 Global Orthogonal Regularization
  保持 hypersphere 均匀，能稳定提升长尾类目和稀疏商品的召回保真，可复用到 embedding 迁移任务。

  - Router 解耦设计值得抄：用一个与升级目标解耦的轻量本地 encoder/MLP 预测 query 投影质量，按预算对低 agreement 的复杂 query
  升级到大模型/API，避免 escalated query 付两次昂贵 API 费；在电商搜索里可以把 20% 预算集中到高价值长尾 query，获得大部分质量并降低
  p99 延迟。

  - 冷启动没有 query log 时，可先用文档或 candidate 语料做 anchor 训练投影，再逐步加入无标签 in-domain query 和跨域
  query；这个渐进课程对推荐/广告排序模型的 embedding 迁移同样适用。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：生产检索系统通常绑定用于构建向量索引的 embedding model，更换 query encoder 需要重嵌整个语料；冷启动阶段没有 query log 和标签，且每个 anchor 都要消耗 API 或算力。现实中索引可能由第三方托管、原始文档不可访问，因此必须在极小 anchor 预算下学习跨模型投影，并处理最影响体验的尾部难 query。

**方法关键点**：
- Embed：在目标 embedding 空间使用 Cosine Farthest Point Sampling 选 anchor。与随机采样相比，FPS 先覆盖流形上不同区域，避免把预算浪费在近似重复的 dense cluster 上。
- Adapt：训练轻量 MLP adapter，损失为 Manifold Alignment Loss = 方向 cosine loss + Global Orthogonal Regularization。正交项促使投影在 target hypersphere 上保持均匀，防止小样本下 representation collapse。
- Route：独立于 source encoder 的轻量 router 预测 top-K retrieval agreement，按预算分位数把低 agreement 的 query 升级给 target model。升级 query 不额外调用 source API，避免双重昂贵编码。
- 三阶段课程：Cold 仅用 anchor；Independent 用无标签 in-domain queries；Foundation 池化跨域 queries，逐步闭合 query-document 偏移。

**关键结果**：在五个 BEIR 数据集上，将 Qwen-Embedding-3-0.6B 与 text-embedding-004 投影到 gemini-embedding-001 索引。与 LEAF（point-wise ℓ2）相比，nDCG@10 相对提升 Arguana +35.0%、FiQA +11.8%、NFCorpus +5.4%；FPS 在固定 anchor 预算下也改善 LEAF 与 Embedding-Converter。20% escalation 预算下，router 捕捉 SciFact 37.5% 的 Huge-Gap queries，而随机策略有 15.9% 概率完全错过；总延迟从约 160ms 降至 38–86ms，adapter+router 仅 1.2ms。

**最值得记住**：小预算冷启动下，选对 anchor 分布 + 方向对齐 + 正交正则 + 难 query 路由，可在不重建索引时同时拿到低延迟与可接受质量。
