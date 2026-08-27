---
title: 'Query Expansion Is More Than Generation: Improving Dense Retrieval through
  Better Integration'
title_zh: 查询扩展不只是生成：通过更好的集成改进稠密检索
authors:
- Siyuan Sun
- Mihai Surdeanu
affiliations:
- University of Arizona
arxiv_id: '2608.25521'
url: https://arxiv.org/abs/2608.25521
pdf_url: https://arxiv.org/pdf/2608.25521
published: '2026-08-26'
collected: '2026-08-27'
category: QueryRec
direction: LLM 查询扩展与稠密检索向量集成
tags:
- Query Expansion
- Dense Retrieval
- LLM
- Vector Interpolation
- Unsupervised Calibration
- Dual Encoder
one_liner: 将原查询与 LLM 扩展分别编码后做向量插值，并用无监督前缀估计扩展信任度，单向量提升稠密检索
practical_value: '- 在搜索/推荐中如果使用 LLM 生成 query 改写、语义扩展或类目词，不要直接拼接进 embedding 或仅用扩展文本检索；把原始
  query 和扩展分别过 query encoder，再做归一化向量插值，权重 α 显式控制扩展贡献，可避免 token 截断、attention 纠缠带来的退化。

  - 无监督在线校准 α：用流量前 8-16 个无标注 query 估计 stream-level α，按 r_top1 × r_sup 计算，即扩展自身检索强度
  × 与原始 query top10 证据一致度；电商搜索流或推荐 query 流可零标注启动，之后冻结为单向量服务。

  - 工程架构上，如果只需同一 dense space 的线性融合，用单向量 AnchorQE 等价加权 CombSUM，一次 ANN 检索即可，不要做 N+1
  路融合；但混合 sparse/dense 或非线性融合不适用。

  - 扩展质量仍是上限：集成只能控制影响，不能修复 LLM 生成的无关内容；生成质量差时应优先优化 prompt 或过滤，而不是只调 α。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：LLM 生成的 query expansion 在零样本下并不稳定，传统集成方式如 expansion-only 或 query-expansion 文本拼接常让 frozen dense retriever 性能低于无扩展基线。论文固定扩展文本、只改变集成方式，发现退化主要来自集成方法本身，而不是生成质量。

**方法关键点**：
- AnchorQE：对原 query q 和扩展 z_i 分别用同一 query encoder 编码并归一化；将扩展混合后与 q 做向量插值 bq_α = normalize((1−α)q + αm)，α∈[0,1] 显式控制扩展信任，保留原 query 作为锚点；不改文档索引和编码器，只产生一个 query 向量。
- SC-AnchorQE：从未标注流量前缀 B=8 个 query 估计 α_stream = r_top1 × r_sup。r_top1 衡量扩展自身 top1 检索强度，r_sup 衡量扩展与原 query top10 检索证据的一致性；两者都高才给扩展较高权重。校准阶段每 query 两次探测，之后冻结为单向量请求。
- 理论性质：与同 dense 空间加权 CombSUM 排序等价，但请求数从 N+1 降为 1；α<1/2 时扩展最多改变检索方向 arcsin(α/(1−α))，如 α=.10 不超过 6.38°。

**关键实验**：
- 设置：Qwen3-8B 生成 HyDE/Query2Doc/Q2E/CoT terms 四类扩展；主 retriever BGE-large-en-v1.5；测试 TREC-DL 19/20、LoTTE Search/Forum、BEIR-14；跨 3 生成器 × 3 检索器共 9 配置。
- 结果：固定 α=.15 的 AnchorQE 在所有 20 个 strategy-benchmark 上超过 DR baseline 和 published integration，相对提升 .46%–12.89%。SC-AnchorQE 在所有 20 组超过 published integration，最大 BEIR-14 CoT terms +13.03%；相对 DR baseline 19/20 组为正，相对 dev-tuned 固定 α 17/20 组为正。跨模型 45 组中 44 组优于 DR baseline，与 QuDAR 复现对比全胜。
- 消融：Conjunctive product 比 cosine/top10 overlap/entropy 等规则更稳定，17/20 优于固定 α，且无需后续每 query 探测；per-query product 18/20 但需持续两次检索。

**最值得记住的一句话**：生成的扩展只是原料，集成方式决定它是增益还是噪声；把原始 query 当作锚点、显式控制扩展信任比单纯选择更好的生成文本更关键。
