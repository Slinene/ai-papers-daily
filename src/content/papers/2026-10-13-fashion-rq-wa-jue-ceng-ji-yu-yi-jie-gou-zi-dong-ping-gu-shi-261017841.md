---
title: 'FASHION-RQ: Mining Hierarchical Semantic Structure for Automated Evaluation
  of Fashion Retrieval'
title_zh: FASHION-RQ：挖掘层级语义结构自动评估时尚检索
authors:
- Tripti Shukla
- Shwetha Somasundaram
- Akshat Gupta
- Rohit Garg
- Paul Duff
- Ian Anderson
affiliations:
- Glance
arxiv_id: '2610.17841'
url: https://arxiv.org/abs/2610.17841
pdf_url: https://arxiv.org/pdf/2610.17841
published: '2026-10-13'
collected: '2026-10-14'
category: Eval
direction: 检索评测基准 · Semantic ID 层级
tags:
- Fashion Retrieval
- Benchmark
- RQ-VAE
- Semantic ID
- Attribute-Level
- LLM Query Generation
one_liner: 利用 RQ-VAE 语义层级自动生成查询与分级相关性，构建可诊断属性的时尚检索基准
practical_value: '- 可直接借鉴「Semantic ID 前缀作为相关性标签」的思路：在电商商品检索中，用 RQ-VAE 生成的层级 ID 前缀定义
  Exact/Sibling/Related/Irrelevant 四级相关性，无需人工标注，适合大规模、可再生的评测集构建。

  - 引入「attribute exclusivity loss」让量化层对应单一属性（如品类、款式、颜色等），能显著提升 Semantic ID 簇的语义纯度，对生成式推荐中的
  SID 质量改进有直接迁移价值；注意 codebook size 不宜过大，64 在纯度与簇密度之间取得平衡。

  - LLM 只负责把簇的属性分布与 parent/sibling 差异「verbalize」成购物 query，相关性仍由 SID 层级确定，避免 LLM 逐对打分带来的幻觉与不可复现问题；这个分离设计值得在自动化评测
  pipeline 中复用。

  - 属性级诊断指标值得落到推荐/搜索系统的离线评估：aggregate nDCG 会掩盖模型在 material、style 等长尾属性上的短板，建议在例行评测中增加
  per-attribute match score，定位具体失败模式。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
时尚检索本质是 set-valued 且 graded：一个 query 如「lightweight cotton kurtas for summer」约束多个属性，多个商品可能部分匹配。但现有基准要么人工标注单目标 item，要么用 LLM 逐对打分，无法分解属性，掩盖「颜色对但款式错」的差异。需要一种可扩展、属性可分解的自动评测方法。

**方法关键点**
- 用 RQ-VAE 对商品生成 3 层 Semantic ID，prefix 定义相关集，共享 prefix 长度定义分级相关性。
- 引入 attribute exclusivity loss：在量化向量上施加 SupCon，让 level 1/2/3 分别对应 masterCategory、articleType、joint attributes，提升簇纯度。
- 从 Myntra 44,446 商品构建 FASHION-RQBENCH：588 个簇（17/135/436），5,380 条 query；LLM 根据簇属性分布和 parent/sibling 差异生成 shopper-style queries，但相关性由 SID 层级确定性继承，LLM 只 verbalize 不判相关。
- 四项任务：T1 ranking（E>S>R>I）、T2 四分类、T3 sibling discrimination、T4 paraphrase robustness；并提供加权 query relevance 与 per-attribute 指标。

**关键结果**
在 10 个 off-the-shelf 检索模型上评估：Qwen3-Embedding-4B 在 T1 nDCG@10=0.8719、T2 accuracy=0.5145、T4 consistency 最高；SPLADE++ 在 T3 nDCG@3=0.6662 最好。BM25 nDCG@10=0.7736、accuracy=0.4023。属性级显示 product type/gender>0.93，但 material≈0.52、style≈0.43。人评表明 RQBENCH query 自然度与真实用户 query 接近（3.62 vs 3.52），意图清晰度显著更高（3.91 vs 2.83）。

**最值得记住的一句话**：Semantic ID 层级可以直接充当相关性的自动标注器，LLM 只负责把结构化证据说成人话，属性级指标才能暴露模型在材质、风格等长尾上的短板。
