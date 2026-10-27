---
title: 'Octen-WebGR: Scaling Generative Retrieval to 200 Million Web Pages'
title_zh: Octen-WebGR：将生成式检索扩展到2亿网页
authors:
- Guangwei Xu
- Wenkai Zhang
- Yawen Liu
- Dongxu Zhang
- Xijie Xu
- Kuan Zou
affiliations:
- Octen AI
arxiv_id: '2610.35256'
url: https://arxiv.org/abs/2610.35256
pdf_url: https://arxiv.org/pdf/2610.35256
published: '2026-10-26'
collected: '2026-10-27'
category: GenRec
direction: 生成式检索 · Semantic ID
tags:
- Generative Retrieval
- Semantic ID
- Navigational Search
- Constrained Decoding
- Web-scale Retrieval
- LLM
one_liner: 首个覆盖2亿网页的生成式检索模型，用两token语义ID直接生成URL，导航点击命中率59.6%
practical_value: '- 商品/落地页生成式索引：可把商品或页面编码为两 token Semantic ID；用标题/类目+高频搜索词构造类似 URL
  text 的文本，经残差量化+碰撞消解生成唯一 ID。两套 token（s0/s1）比共享 token 更能区分语义前缀与组内排序。

  - 训练采样与曝光：点击对按 n(q,u)/Nq × Nq^β (β=0.5) 加权，平衡头部 query 与长尾；对导航/转化集中 query 加保底样本；document-indexing
  把商品文本当 query，一次曝光覆盖多条关联 query。

  - 推理与资源：constrained beam search 只输出存在 item，避免下架商品/假 URL；点击表可用 lookup→GR 兜底。GR 4B
  模型单 GPU 10GB，比 exact dense 索引省约40倍内存。

  - 混合路由：GR 擅长热门 item 的新 query 表达，dense 擅长冷 item；用 GR 首位 item 的训练对数 + beam 概率做 serving
  路由，可同时拿到两者优势，电商搜索/推荐可直接复用。

  - 扩展训练：遗忘主要由曝光后的累积学习率 Λ 决定，而非模型容量；把高价值 pair 放在低 Λ 的晚期窗口曝光，或加大 batch 并等比升 lr，能提升保留率与样本效率。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
导航搜索要在数亿网页中命中唯一目标页。Click table 对未见 query 无能为力，dense retriever 常把同站其他页排到第一，且索引2亿页需 412GB 内存；闭卷 LLM 答得不准且贵。生成式检索适合该任务，但此前未超过 MS MARCO 的8.8M passages，扩展到2亿独立网页仍是未解难题。

**方法关键点**
- 每 URL 编码为两 token Semantic ID (s0,s1) 两个16-bit code；用 URL text（URL+最多5条高频 query）过 Octen-Embedding-4B 截断到1024维，两级残差 k-means，第二级 collision-free 唯一分配。
- Qwen3 增加两套各 65,536 个新 token；s0 token 初始化用相关 query 的 final hidden state 均值，加速早期收敛。
- 训练样本为 query-URL pair，权重 n(q,u)/Nq × Nq^0.5；navigational floor 保底；document-indexing 把 URL text 当 query；损失只在两个 SID token 上，softmax 限制在合法 code。
- 推理 beam width 20 在 identifier trie 上 constrained decoding，只输出存在 URL；模型即索引，4B 模型单 GPU 10GB。

**关键结果数字**
- U201M = 201,231,792 URL，训练 1.13B query-URL pairs；2026年9月导航流量上 GR hit@1 59.6%，dense+click prior 46.5%，dense 24.8%，最强闭卷 LLM 37.5%。
- 新 query 熟页：GR 30.9% vs dense 17.2%（+prior 21.4%）；冷目标反转，dense 24.3% vs GR 14.3%。lookup→GR→路由组合到 63.1%。
- 候选 URL 从 2M 增至 201M，GR hit@1 仅降 4.7 点，dense 降 22.2 点。
- 遗忘由曝光后的累积学习率 Λ 主导，而非模型容量；曝光时间和 batch 调度可替代部分参数。

**最值得记住的一句话**
生成式检索擅长新表达方式下的“熟页”命中，embedding 擅长冷页面；两者按目标页点击数/beam 概率路由可互补，且 GR 的规模上限受曝光调度而非参数容量限制。
