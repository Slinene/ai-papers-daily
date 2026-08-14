---
title: Generative Universal Multimodal Retrieval with Dual-role Identifiers
title_zh: 双角色标识符的生成式通用多模态检索
authors:
- Kaipeng Li
- Haitao Yu
- Xuanchen Zhou
affiliations:
- Independent Researcher, Japan
- Institute of Library, Information and Media Science, University of Tsukuba, Japan
- College of Knowledge and Library Sciences, University of Tsukuba, Japan
arxiv_id: '2608.12987'
url: https://arxiv.org/abs/2608.12987
pdf_url: https://arxiv.org/pdf/2608.12987
published: '2026-08-13'
collected: '2026-08-14'
category: GenRec
direction: 生成式多模态检索 · 双角色 Semantic ID
tags:
- Generative Retrieval
- Multimodal Retrieval
- Semantic ID
- Residual Quantization
- Beam Search
- Hybrid Reranking
one_liner: DrIG 将同一残差量化 ID 同时作为顺序解码序列和无序集合先验，缓解前缀剪枝错误，并以 dense 重排补偿量化损失
practical_value: '- **双角色 Semantic ID 可直接用于生成式召回**：将商品 ID 设计为分层量化 token，第一层编码类目/模态，其余层编码语义；推理时
  beam search 不仅用 decoder 序列分数，还加入由 ID 无序集合计算的全局相关性分数，缓解 beam search 前缀剪枝误杀。

  - **生成召回 + dense 精排是现实的混合架构**：先用轻量生成式模型通过 Trie 约束 beam search 召回 top-k，再用 query/item
  embedding 余弦相似度重排，避免全库 ANN 打分，额外成本仅为 O(kd)，适合大规模电商商品库。

  - **Query augmentation 与判别排序目标可迁移**：用 query-target embedding 的 Beta 插值生成增强 query
  稳定生成器训练；用 teacher 相似度计算 adaptive margin 的 pairwise ranking loss，使 decoder 序列分数更贴近排序目标，适合用于生成式商品召回的训练。

  - **LMM 作为多模态 item embedding 编码器**：用 “summarize in one word” 提示提取 <emb> 前 hidden
  state 作为通用多模态表示，再做多任务对比微调，可复用到图文商品/内容理解与跨模态召回。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
生成式检索 GIR 通过直接生成离散标识符来定位相关项，但左到右受限解码极易因前缀剪枝丢失相关候选；同时大多数 GIR 研究仍停留在单模态，通用多模态检索（query 与 candidate 可为文本、图像或图文混合，且指令感知）探索不足。离散标识符虽然推理高效，但精度仍落后于稠密向量检索。

**方法关键点**
- 用 LMM（Qwen2-VL）对 query 和 candidate 做 instruction-aware 共享嵌入，二阶段微调：先文本 NLI 对比学习，再 M-BEIR 多任务 InfoNCE。
- 每个候选通过残差量化生成一个 ID：第一 token 由大小为 3 的模态 codebook 编码 text/image/image-text，后续 token 编码渐进细粒度语义。
- 同一 ID 具有双角色：顺序角色用于 autoregressive 解码；集合角色将 token 视为无序集合，通过聚合 token-level 分数得到 prefix-independent relevance prior。
- 推理时 Trie 约束 beam search 的扩展得分融合前缀有效性约束、顺序解码分数和集合全局先验 λφ(t≤i)。
- 训练 decoder 时加入 query-target embedding 插值扩充，以及基于 teacher cosine margin 的判别排序损失，缩小 token 级生成与排序目标差距。
- 混合检索：生成 top-k 后用 dense embedding cosine 重排，top-k 很小，额外成本 O(kd)。

**关键结果**
在 M-BEIR local-pool 与 global-pool 上，DrIG 平均召回显著优于生成式基线 GENIUS：local 38.0 vs 29.5（+28.8%），global 36.4 vs 28.6（+27.3%）。加上 dense rerank 后 DrIG-LT 在 local 达到 50.4，但仍低于 LamRA 等强 dense baseline；尤其在 WebQA 知识密集文本任务差距明显（65.9 vs 96.7），说明离散压缩有信息损失，但混合方案提供效率-效果权衡。

**最值得记住**
同一个离散 ID 可以被同时用作有序解码序列和无序集合先验，能有效缓解生成式检索的前缀剪枝局部最优；生成召回 + dense 重排是现实可落地的混合检索架构。
