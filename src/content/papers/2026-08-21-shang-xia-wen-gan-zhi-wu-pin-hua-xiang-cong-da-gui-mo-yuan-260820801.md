---
title: 'Profiling What Matters: Context-Aware Item Profiles from Large-Scale Metadata
  for LLM Recommenders'
title_zh: 上下文感知物品画像：从大规模元数据提炼 LLM 重排关键信息
authors:
- Dojun Hwang
- Seunghan Lee
- Cheonyoung Park
- Sara Yu
- SeongKu Kang
affiliations:
- Korea University
- KT Corporation
arxiv_id: '2608.20801'
url: https://arxiv.org/abs/2608.20801
pdf_url: https://arxiv.org/pdf/2608.20801
published: '2026-08-21'
collected: '2026-08-24'
category: RecSys
direction: LLM 重排 · 物品画像
tags:
- LLM Recommenders
- Item Profiling
- Reranking
- Context-Aware
- Feature Selection
- Subjective Traits
one_liner: CAIRO 将物品元数据与评论结构化为客观特征和主观特质，用轻量选择器按用户上下文生成个性化画像，显著提升 LLM 重排效果
practical_value: '- 在 LLM 重排/生成式推荐中，不要直接注入全量商品元数据或仅用标题；先离线把 metadata + reviews 结构化为「客观特征
  + 主观特质」字典，再按用户上下文挑选，可避免 +Feat 变体反而掉点。

  - 用户相关属性选择不必每次调用 LLM：用小型 controller 网络基于协同信号学习 feature importance，在线只做 softmax +
  top-k 池化，离线存储 embedding，可将单用户画像耗时压到 0.2s 级，远低于 agentic RAG 的数百秒，适合在线 serving。

  - 主观特质不要做成单一 summary；从评论中生成 3-7 个不同 facet 的 trait（如功能、品牌、使用场景），选择时用 user profile
  embedding 做 cosine 相似度，能覆盖同一商品对不同用户的不同卖点。

  - 若要对生成画像做优化，可构造 proxy task（next-item 预测错误案例）让 LLM 诊断 trait 缺陷，并强制用客观属性 grounding
  后修订，提升 profile 质量且更不易幻觉。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：尽管 LLM 已广泛用于推荐重排，item 侧信息往往只给标题或固定属性；真实商品元数据规模大、格式混乱、关键信号埋在长文本中，且同一属性对不同商品和不同用户的重要性不同。直接把原始元数据塞进 prompt 会撑爆上下文并引入噪声，已有 +Feat 变体甚至不如仅用标题的 LLMRank。因此需要结构化和上下文相关的 item profile。

**方法关键点**：
- 结构化为两类记录：客观特征（objective features）从领域 key 中提取商品属性，要求 LLM 先验证元数据中是否有证据再赋值，防止幻觉；主观特质（subjective traits）从评论中提取 multi-faceted 的 3-7 个 traits，每条关联支持它的客观特征。
- 轻量 profiler：客观特征选择由一个小型 controller 网络配合轻量推荐模型，学习 feature importance，在线 softmax + top-k 池化选 4 个特征；主观特质选择用用户画像 embedding 与 trait embedding 的 cosine 相似度。
- 在线仅矩阵运算，离线预存所有 item embedding，单用户画像耗时约 0.21-0.22s，远低于 agentic RAG 的数百秒。
- 可选 trait refinement：通过 proxy next-item 预测收集 LLM 错误案例，诊断 trait 缺陷，并基于客观特征修订，提升对齐度和防幻觉。

**关键结果**：在 Amazon Video Games / Sports / Electronics 三个域的重排设置中，CAIRO 在所有数据集和指标上超过 BPR、SASRec、BERT4Rec、xDeepFM、AdaFS、REACTION 以及 LLM 基线 LLMRank、EXP3RT、M-LLM3Rec；Video Games 上 nDCG@5 从最强 LLM baseline 0.1674 提升到 0.1839，加 refine 到 0.1895；Electronics 从 0.1581 提升到 0.1741。对比 REAP，CAIRO 用不到 0.3s 的画像耗时达到与数百秒 RAG 近似的效果。直接注入 raw metadata 的 +Feat 方法低于仅用标题，证明选择比堆料更重要。

**最值得记住的一句话**：LLM 重排中 item 信息不是越多越好，关键是「为每个 user-item 对挑选什么才重要」。
