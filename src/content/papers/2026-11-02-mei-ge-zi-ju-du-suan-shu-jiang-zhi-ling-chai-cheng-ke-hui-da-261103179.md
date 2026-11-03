---
title: 'Every Clause Counts: Instruction-Following Reranking by Multiplying Small,
  Answerable Questions'
title_zh: 每个子句都算数：将指令拆成可回答小问题做零样本重排
authors:
- S. M. Mahbub Uddin Ahmed
- Abdullah Al Musaddiq
affiliations:
- United International University
- Islamic University of Technology
arxiv_id: '2611.03179'
url: https://arxiv.org/abs/2611.03179
pdf_url: https://arxiv.org/pdf/2611.03179
published: '2026-11-02'
collected: '2026-11-03'
category: RecSys
direction: 搜索重排 · 指令拆分逐项打分
tags:
- instruction-following
- reranking
- zero-shot
- LLM judge
- search
- probabilistic scoring
one_liner: 把带指令查询拆为主题与多个类型化子句，逐项用小型 judge 输出概率并相乘，零样本提升指令遵循重排效果
practical_value: '- 电商搜索/广告精排可复用：将带约束 query（如“官方旗舰店”“适合新手”“西班牙语”）拆成主商品意图 + 多个类型化 clause，每个
  clause 用轻量 judge 问“候选是否满足 X？”，用 P(yes) 乘到相关性分上；不需要重训线上模型，直接用于 top-K 精排或 RAG rerank。

  - 不要把复杂指令塞进单个 LLM prompt。论文显示同 judge 下拆句重排把 WISE 从 32.9 提升到 47.6。多条件筛选场景（价格段+品牌+适用人群）越细，越应独立判分再融合，降低指令遗漏。

  - 原始概率乘积在跨查询比较时不稳定，导致 SICR 失真。若要做坏 case 阈值或准出判断，建议用 rank-based 融合或对分项概率做对数加和/校准，而不是直接拿原始分跨
  query 设阈值；候选内排序可以用 product/rank，但跨流量控制要谨慎。

  - 成本可控：小模型可做零样本 judge，全维打分约 $10。线上可对高频指令用规则/属性过滤替代，只对长尾复杂指令调用 LLM clause 判断，并做并行与缓存。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：搜索查询常附带指令（官方来源、初学者、特定语言），但多数重排器只关注主题相关性，把指令当额外词。InfoSearch 上 GPT-4o 作为 list-wise reranker 的 WISE 仅 33.5。

**方法**：DMReranker 将带指令查询解析为 topic + 若干 typed clauses。每个 clause 由一个冻结的小型 judge 模型回答一个窄的 yes/no 问题，答案为“是”的概率作为该子项分；最终将各子项概率与主题相关性相乘得到单一排序分。全程无训练，配置冻结。

**结果**：在相同 top-100 候选上，DMReranker 在 InfoSearch 六维度 macro WISE 达 50.9，同时 original-mode nDCG@10 维持 82.9；原始分 SICR 19.2 仍低于 GPT-4o 32.1，但基于排名的 SICR 为 67.0。同 judge 下，拆分指令比单个合并问题把 WISE 从 32.9 提升到 47.6。六维打分成本约 $10。
