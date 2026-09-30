---
title: 'MERGE: Multi-LLM Ensemble for Retrieval via Generative Enrichment'
title_zh: MERGE：生成式增强的多LLM检索集成
authors:
- Tzu-I Ho
- Yung-Yu Shih
- Shang-Yu Su
- Dongzhe Wang
- Yun-Nung Chen
affiliations:
- University of Waterloo
- National Taiwan University
- Rakuten Group, Inc.
- Rakuten Asia Pte. Ltd.
- Taiwan Rakuten Ichiba, Inc.
arxiv_id: '2609.37574'
url: https://arxiv.org/abs/2609.37574
pdf_url: https://arxiv.org/pdf/2609.37574
published: '2026-09-29'
collected: '2026-09-30'
category: QueryRec
direction: 生成式查询扩展 · 多LLM集成
tags:
- Query Expansion
- LLM Ensemble
- BM25
- Automatic Prompt Optimization
- Generative Enrichment
- Retrieval
one_liner: 两阶段多LLM查询扩展框架，用任务驱动自动提示优化在BM25上实现最高+14.9 nDCG@10提升
practical_value: '- 电商搜索中，买家口语化 query 与商品标题/属性词之间常有词汇 gap，可借鉴 MERGE 两阶段设计：多个异构小模型各自扩展候选，再用稍大模型融合成一条查询，无需改语料或重建索引，可直接接入现有
  BM25/Elasticsearch 流程。

  - 用下游检索指标（如 nDCG@10、点击率或相关性人工评估）代替 LLM judge 做 prompt 优化，在 20% dev 子集上跑小 tournament，能自动把「seed
  prompt 可能削弱检索」转为稳定收益；适合快速迭代新模型或新增 generator 时免去手工 prompt 调优。

  - APO 收敛后的 prompt 可能不是自然语言、读起来像 token 包，但它生成的 query 可读性没问题，不影响线上使用；可接受这种 prompt
  形态，重点看最终 query 质量。

  - 输出是 plain text query，只做一次 BM25/ES 检索，没有 rank fusion 和重索引开销；既能 query-time 在线扩召回，也能离线作为训练数据增强供
  dense retriever 使用。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
LLM 查询扩展通常依赖单一模型，受训练数据和架构偏差影响，生成风格窄、易幻觉或过度倾向某一解释；同时提示词需要按模型手工调，跨模型迁移差，多模型集成难以规模化。MERGE 针对查询与语料的词汇/风格 gap 以及 prompt 工程瓶颈，提出两阶段多 LLM 集成，并将下游检索指标引入提示优化，替代手工调参。

## 方法关键点
- **Stage 1 多模型生成**：三个异构 7–8B 指令模型（Llama-3.1-8B、Qwen2.5-7B、Mistral-7B）并行生成候选查询扩展，每个模型使用 APO 针对自身优化的专属 prompt。
- **Stage 2 生成式融合**：Qwen2.5-14B 将候选扩展合成为一个统一查询，输出在 `<result>` 标签内；融合模型与 Stage-1 模型不同，避免自偏好。
- **任务驱动 APO**：用 BM25 nDCG@10 在 20% dev 子集上给 prompt 打分，取代 LLM judge；采用小 tournament：每轮优化器把当前冠军 prompt 改写为两个 draft，和冠军共三个候选比较，胜者成为新冠军，冠军连续两轮未被打败即收敛。history 变体把最近 5 轮轨迹反馈给优化器。
- **工程特性**：输出为纯文本查询，只需一次 BM25 检索，无 rank fusion、无监督文档扩展、不重建索引；APO 通常不到 10 轮收敛，单 H100 不到 1 小时。

## 关键实验
在五个 BEIR 基准（NQ、SciFact、FiQA、Touché-2020、DBPedia）上，MERGE (APO) 相比原始 BM25 提升 nDCG@10 从 +2.1（FiQA）到 +14.9（NQ）；在 5/5 基准上超过 BM25+Exp4Fuse，并在 3/5 上持平或超过 docT5query+Exp4Fuse。APO 把种子 prompt 在 FiQA（−4.4）和 Touché-2020（−5.5）的负增益转为全数据集正增益；消融显示 Stage-2 集成严格优于最佳 Stage-1 单模型。

## 最值得记住的一句话
用下游检索分数作为 prompt 优化信号，让多模型查询扩展从手工 prompt 工程变成自动、可扩展的流程；两阶段“多生成 + 融合”比单模型更稳。
