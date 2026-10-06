---
title: 'SPRIG: Semantic-ID-enhanced Paths for Knowledge Graph-based Generative Recommendation'
title_zh: SPRIG：语义ID增强路径的知识图谱生成式推荐
authors:
- Justin Hangoebl
- Marta Moscati
- Alessandro B. Melchiorre
- Shah Nawaz
- Markus Schedl
affiliations:
- Johannes Kepler University Linz
- Albatross AI
- Criteo AI Lab
- Linz Institute of Technology
arxiv_id: '2610.06590'
url: https://arxiv.org/abs/2610.06590
pdf_url: https://arxiv.org/pdf/2610.06590
published: '2026-10-05'
collected: '2026-10-06'
category: GenRec
direction: 生成式推荐 · Semantic ID + KG path
tags:
- Semantic ID
- Knowledge Graph
- Generative Recommendation
- Path Reasoning
- Residual Quantization
- Transformer Decoder
one_liner: 首次在KG路径推理生成式推荐中将物品表示为层级语义ID，统一共享词表，以更少参数实现更强推荐
practical_value: '- 商品/广告ID语义化：用内容embedding + residual K-means生成层级Semantic ID（如3层×256码），替代原子item
  token，词表从|I|降至固定768，大catalog下可省~24x参数，相似商品共享前缀利于长尾与冷启动。

  - 两阶段路径语言建模：先在无协同信号的通用KG路径上预训练，再在用户-物品路径上微调；推理用diverse beam search（60 beams/5组/diversity
  penalty 0.4）生成路径并按路径log-likelihood排序候选商品。

  - 量化器选择：residual K-means优于RVQ/RQ-VAE但差距仅~1%，可优先选简单方案；模型对底层item特征质量敏感，需先保证内容表征质量。

  - 若业务有商品知识图谱（类目/品牌/属性关系），值得将KG路径生成与SID结合，而非单独用SID或单独用KG；两者互补，在稀疏数据集上提升明显。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
生成式推荐的两条路线各有短板：基于Semantic ID（SID）的方法缺乏关系接地；基于知识图谱（KG）路径推理的方法仍用原子item token，词表随catalog线性增长，参数共享与泛化差。SPRIG将内容量化的层级SID写进KG路径，在一个因果Transformer里同时获得关系推理与跨物品泛化。

**方法关键点**  
- 用residual K-means对item内容embedding量化得到SID：3层、每层256码，语义相似item共享更长前缀；总item token数为Ls×K=768，与catalog规模无关。
- 构建SID增强路径：将KG路径中每个item实体替换为其SID序列，得到统一词表（SID token + 非item实体 + 关系 + 特殊token）。
- 两阶段训练：先在通用KG路径（排除用户-物品边）上预训练，再在从用户出发、经全图、终止于目标item的路径上微调；目标均为next-token NLL。
- 推理：条件为用户和watched关系，diverse beam search生成3-hop路径，按路径log-likelihood排序终端item。

**关键结果**  
在ML-1M与Onion两个数据集上，SPRIG（gen+spec）相比直接基线KGGLM（gen+spec）：ML-1M nDCG@10从0.0864升至0.1241（+44%），Onion从0.0421升至0.0669（+58%），所有指标显著。SASRec的nDCG略高，但其全catalog排序与生成式beam search候选不可直接对比。SPRIG在Onion上比KGGLM少19%参数、近一半FLOPs；词表从18,415压缩到768，约24x。量化器选择上residual K-means最优但与RVQ/RQ-VAE差距<1%，模型对底层内容特征质量敏感。

**最值得记住的一句话**  
把物品表示为内容量化得到的层级Semantic ID并写进KG路径，能在更小词表与更低计算下同时获得关系接地和跨物品泛化。
