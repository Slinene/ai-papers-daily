---
title: 'FERN: Cross-Benchmark Table Retrieval for Text-to-SQL with Frozen Retrievers
  and Learned Ranking'
title_zh: FERN：冻结检索器与学习排序的跨基准表检索用于 Text-to-SQL
authors:
- Arjun Rao
- Nishant Gopinath
affiliations:
- SAP
arxiv_id: '2611.14477'
url: https://arxiv.org/abs/2611.14477
pdf_url: https://arxiv.org/pdf/2611.14477
published: '2026-11-10'
collected: '2026-11-14'
category: Other
direction: 检索排序 · 特征工程
tags:
- Text-to-SQL
- Table Retrieval
- Learning to Rank
- Hybrid Retrieval
- Feature Engineering
- LightGBM
one_liner: 不调用生成式 LLM，融合三个冻结检索器候选并用 LightGBM 排序，在 BIRD/Spider 上接近 Claude 3.5 方法 RASL
  的召回
practical_value: '- 多路召回融合 + LightGBM 排序可替代在线 LLM 检索：用 BM25/向量/关键词等多种冻结检索器各取 top-K
  合并成候选池，再训练轻量排序器，延迟仅 208ms，适合电商搜索/推荐里低延迟召回阶段。

  - 特征工程比模型架构更关键：论文显示非检索特征在 BIRD dev 上让 complete@5 提升 7.7 点，说明 schema 相似度、问题-候选重合度、统计特征等业务先验特征对排序增益很大，值得在商品召回或
  query 改写排序中系统设计。

  - 跨域泛化策略可借鉴：排序器只在 BIRD 上训练，却在 Spider 上把 complete@5 从 83.9% 提到 95.6%，说明多源检索信号 + 通用特征能让排序器跨场景迁移，适合广告/推荐里训练数据少的新业务快速冷启动。

  - 用候选池召回作为兜底：论文表明候选池本身在 Spider 上 recall@15 已达 98.0，排序器只是提高 precision；实际系统可先保证高召回的多路融合，再用排序层做精排，避免单一检索器召回上限过低。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

动机：Text-to-SQL 在数百张表的 pooled catalog 上必须先做 table retrieval，漏表会导致 SQL 错误，多表则消耗生成上下文。现有方法如 RASL 用 Claude 3.5 提取关键词和选表，但依赖昂贵生成式 LLM。FERN 目标是用冻结检索器和学习排序达到相近召回，同时降低延迟和成本。

方法关键点：融合三个冻结检索器得到 100 个候选表；对每个候选构建最多 120 维特征，包括检索信号和非检索特征；用 LightGBM 排序器仅在 BIRD 训练集上拟合一次，预测时对候选表重排序。整个流程不调用生成式 LLM。

关键结果：在 Spider 上，候选池本身 recall@15 达到 98.0，排序器将 complete@5 从 83.9% 提升到 95.6%；recall@5 在 Spider 上为 96.7，接近 RASL 的 97.0；在 BIRD 带 evidence 时为 96.6 vs 97.5，但不带 evidence 时落后 8.2 点。在 BEAVER 真实问题上 recall@15 为 82.1，介于两个 BEAVER 训练检索器之间；在 Fiben 上 recall@15 差距较大。BIRD dev 上中位延迟 208ms/问题，单张 A100，无托管模型调用。
