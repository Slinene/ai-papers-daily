---
title: 'Generative Retrieval for E-commerce: Jointly Learning Embedding and Codebook
  with Same Product Cluster'
title_zh: 电商生成式检索：联合学习 Embedding 与 Codebook 的同商品簇一致性方法
authors:
- Songtao Fang
- Zihao Xu
- Shaowei Wei
- Jin Zhang
- Zhuojun Wang
affiliations:
- Alibaba Group
arxiv_id: '2608.30606'
url: https://arxiv.org/abs/2608.30606
pdf_url: https://arxiv.org/pdf/2608.30606
published: '2026-08-31'
collected: '2026-09-01'
category: GenRec
direction: 生成式检索 · 联合训练 Embedding/Codebook
tags:
- Generative Retrieval
- RQ-VAE
- Semantic ID
- E-commerce Search
- Contrastive Learning
- Product Cluster
one_liner: 用同商品簇信息联合训练 embedding 与 codebook，消除两阶段误差累积，提升生成式电商检索召回
practical_value: '- 电商场景中，可利用商品簇（同 SKU/同款不同卖家）作为强监督：对每个商品采样同簇商品并计算均值 embedding，加 MSE
  拉近商品 embedding 与簇均值，能显著提升 Semantic ID 的一致性；可直接复用现有商品关系（ASIN/货号）构造训练信号。

  - 避免两阶段训练：将 RQ-VAE 的 codebook 与 embedding model 联合优化，同时引入 query-product 对比学习，让 codebook
  不再只依赖静态商品 embedding；实现时可将 InfoNCE 分别加在原始 embedding 和量化重构表示上，端到端对齐查询与商品空间。

  - 引入新 token 的 LLM 微调可采用两阶段：先 product info -> product ID，再 query -> product ID，让模型先掌握新特殊
  token 的语义，再学习查询到 ID 的映射，对生成式检索 fine-tune 更稳定。

  - 规模配置可参考：5 层 codebook、每层 32 码、768 维、GTE 编码器、Qwen2.5-7B；20M 商品 + 40M query 训练即可获得稳定提升；ALSP
  指标适用于评估同簇商品 ID 的一致性。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
主流生成式检索通常两阶段：先训练商品 embedding，再学 codebook 将 embedding 映射到商品 ID。这带来两个问题：误差累积——第一阶段 embedding 的偏差会在 codebook 训练中被放大；交互缺失——codebook 只依赖静态 embedding，无法建模 query-product 及 product-product 交互，导致同一商品簇（同款不同卖家/尺码）被分配不一致 ID，损害检索。

**方法关键点**
- **联合训练框架**：同时优化商品 embedding 与 RQ-VAE codebook，消除两阶段误差传递。
- **同商品簇监督**：对每个商品采样同簇商品，计算簇均值 h_cluster，用 MSE 损失拉近商品 embedding 与簇均值，强制同一簇的商品具有语义一致的 ID。
- **残差量化**：L=5 层 codebook，每层 K=32，重构损失 + codebook commitment loss 训练 RQ-VAE。
- **对比学习**：对原始商品 embedding h_product 和量化重构表示 h_recon 分别与 query 计算 InfoNCE，端到端对齐查询与商品空间。
- **LLM 两阶段训练**：先 product info → product ID，再 query → product ID，帮助 LLM 掌握新增特殊 token 的语义。

**关键实验**
在阿里巴巴电商平台 20M 商品、40M query 上训练，测试集 10k query。对比 BM25、DPR、DSI、Tiger rq-vae。结果：Recall@1 4.49（vs Tiger 4.33），Recall@10 9.90（vs 8.84），Recall@100 30.71（vs 26.38），同簇 ID 公共前缀 ALSP 4.42（vs 3.92）。消融去掉 cluster 约束后，Recall@1 降至 4.39，ALSP 降至 4.01，证明联合训练和簇监督都关键。

**最值得记住**
同商品簇监督信号是让生成式 Semantic ID 具备语义一致性的关键，联合训练 embedding 与 codebook 能避免误差累积，显著提升电商生成式检索召回。
