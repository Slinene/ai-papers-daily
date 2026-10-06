---
title: Query Generation with Direct Preference Optimization for Document Expansion
  in E-commerce Search
title_zh: 电商搜索文档扩展中基于 DPO 的查询生成 QGDPO
authors:
- Kaihao Li
- Feng Liu
- Juexin Lin
- Xunfan Cai
- Zhen Yang
- Tony Lee
- Ciya Liao
affiliations:
- Walmart Global Technology
arxiv_id: '2610.04352'
url: https://arxiv.org/abs/2610.04352
pdf_url: https://arxiv.org/pdf/2610.04352
published: '2026-10-03'
collected: '2026-10-06'
category: QueryRec
direction: 生成式查询扩展 · DPO 偏好对齐
tags:
- Doc2Query
- DPO
- E-commerce Search
- Document Expansion
- Relevance Filter
- Query Generation
one_liner: 用相关模型构造偏好对做 DPO，再将生成 query 过相关过滤，显著减少 Doc2Query 幻觉并提升线上搜索相关性与加购率
practical_value: '- 可直接复用「相关模型自动构造 DPO 偏好对」：用已有的三分类相关模型 exact/substitute/irrelevant
  对 SFT 生成的 query 打分，按 exact 和 irrelevant 自动配对，省去人工偏好标注；DPO 学习率用 1e-6（远低于 SFT 的 1e-4），β
  取 0.1，能明显压住幻觉。

  - SFT + DPO 之后再接 relevance filter，两个增益相互独立、可叠加；过滤阈值选 95% recall，既能保持较高 precision（0.866），又不过度牺牲生成的新
  token 数量，适合商品文档扩展场景。

  - Query 生成式检索里，beam search（beam=10，no repeat ngram=2）比 top-k / top-k+top-p 更稳定，exact
  率更高、irrelevant 率更低；如果业务追求线上检索结果稳定可复现，优先用 beam search。

  - 用 Mistral-7B + LoRA（rank=256, alpha=64）替代 T5-base 做 Doc2Query，在媒体、玩具等依赖世界知识的商品上能生成更多有用新
  token，但需离线批量推理并权衡成本；可以只对长尾或特殊品类启用 LLM 版本。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：电商搜索存在词汇不匹配问题，用户查询词和商品标题/属性措辞不一致，导致相关商品漏召回。Doc2Query 通过 seq2seq 模型为商品生成潜在 query 并加入索引，能缓解该问题，但 T5 等模型容易生成与商品无关的幻觉 query 或重复已有词，单纯后置过滤无法从源头提升生成质量。

**方法关键点**：
- 先对 T5-base 做 SFT，输入商品标题与属性，生成 top-5 query。
- 用现有三分类相关模型 exact/substitute/irrelevant 对生成 query 打分，自动构造 (doc, winning query, losing query) 三元组作为偏好对。
- 在 SFT 模型上做 DPO 微调，β=0.1，学习率 1e-6，10M 三元组，训练 10 epoch。
- 推理后接相关模型过滤，只保留 exact 概率超过 95% recall 阈值的 query；只把商品信息中未出现的 novel tokens 写入 Solr 索引。

**关键结果**：
- 小评估集上，相比 Doc2Query baseline，QGDPO 使 exact 预测 +8.07%，irrelevant 预测 -49.87%；加上 relevance filter 后 exact +9.63%，irrelevant -64.48%。
- 线上 A/B 测试：NDCG@5 +0.93%，NDCG@10 +0.86%，Search Session ATC Rate +0.36%（统计显著），GMV 正向趋势 +0.17%。
- Mistral-7B + LoRA 替代 T5-base，exact +2.00%，irrelevant -22.84%，在媒体/玩具类受益于世界知识。

最值得记住的一句话：用现成相关模型自动构造偏好对做 DPO，能直接从生成器端砍掉约一半无关 query，且与后置 relevance filter 增益正交，可以叠加使用。
