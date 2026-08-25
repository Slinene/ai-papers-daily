---
title: The Emergence of Relevance Through Axiomatic Attention Patterns During LoRA
  Fine-Tuning
title_zh: LoRA 微调中通过公理化注意力模式涌现相关性
authors:
- Matthew Perlman
- Atharva Nijasure
- James Allan
affiliations:
- University of Massachusetts Amherst
arxiv_id: '2608.23338'
url: https://arxiv.org/abs/2608.23338
pdf_url: https://arxiv.org/pdf/2608.23338
published: '2026-08-24'
collected: '2026-08-25'
category: RecSys
direction: LoRA 微调可解释性 · 重排序
tags:
- LoRA
- Reranking
- Attention Interpretability
- Axiomatic IR
- RankLLaMA
- Mechanistic Interpretability
one_liner: 用 keep/omit 消融定位 RankLLaMA 中 LoRA 注意力更新关键层，并发现其与罕见词敏感、query-doc 交互等公理化注意力模式强相关
practical_value: '- 对搜索/广告 reranker 做 LoRA 时，不必全量微调所有注意力层：在 MLP 全量 LoRA 的前提下，只对中间紧凑窗口（如
  RankLLaMA 的 layers 10–18）应用注意力 LoRA，即可恢复全量注意力微调一半以上增益，文档 reranker 变体甚至恢复 70%+，可显著降低训练和推理适配成本。

  - 借鉴 keep/omit 消融设计：先用小候选集+Mean Score Margin 快速筛选关键 head/layer/window，再用 NDCG 在更接近线上候选规模上验证，成本低且能定位冗余层，适合业务侧快速做模型裁剪。

  - 可用 Normalized Feature Attention 监控 LoRA 微调效果：排除 attention sink（首 token）后，观察模型是否学到
  document-query interaction、rare token sensitivity 等业务相关注意力模式，作为微调质量的辅助指标。

  - 若线上 reranker 可解释性要求高，可优先关注不同层对 query-doc 交互和稀有词敏感的组合特征，这些组合特征与性能提升相关性最高（keep ρ=0.92,
  omit ρ=-0.94），能帮助判断模型是否学到类 BM25 的联合相关性信号。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
LoRA 已成为 LLM reranker 适配的默认方式，但一直不清楚任务相关行为到底在网络的哪些位置被学到，attention 层又发生了什么变化。该工作面向 RankLLaMA 这一类 decoder-only 重排序模型，研究 LoRA 注意力更新在哪些层/头最关键，以及这些关键区域是否对应可解释的经典 IR 公理化注意力模式。

**方法关键点**
- 模型：RankLLaMA-7B（passage 和 document 两个变体），基于 Llama-2-7B 做 pointwise relevance scoring，LoRA rank r=32, α=64，注入 attention 和 MLP，base 冻结。
- 消融策略：只消融 attention 矩阵，MLP 始终保留 LoRA；采用 keep（仅该组件保留 LoRA）和 omit（仅该组件回退 base）两种互补方式。
- 粒度：单 head、单 layer、6 层窗口（另验证 3/4 层窗口）。
- 评估：MS MARCO Dev 随机 50 queries；head 级用 10 candidates/query，layer/window 级用 100 candidates/query；指标为 NDCG 和 Mean Score Margin。
- 可解释特征：定义 lexical matching、rarity sensitivity（基于 500k 文档 IDF 阈值）、document-query interaction 三类公理化 token-pair 特征，并提出 Normalized Feature Attention，排除 attention sink（首 token）后计算有效 attention mass 占比。

**关键结果**
- Base NDCG 0.199，全量 LoRA 后 0.911，增益 0.712；Mean Score Margin 从 -0.204 提升至 8.768。
- 无论 keep 还是 omit，中间层 10–18 都是最关键的注意力更新区域，层 14 和 29 是突出单点；仅 keep 10–18 窗口可恢复超过一半全注意力增益。
- 文档 reranker 变体上，关键区域约在 7–16 层，仅 keep 该窗口可恢复超过 70% 的 NDCG 增益。
- 注意力变化与性能强相关：rarity sensitivity keep ρ=0.92, omit ρ=-0.89；document-query interaction keep ρ=0.71, omit ρ=-0.68；组合特征“rare document token 关注 rare lexical match query token” keep ρ=0.88, omit ρ=-0.94。

**最值得记住的一句话**
给定 MLP 全量 LoRA，重排序性能的关键注意力更新集中在中间紧凑层区间，并且这些区间正是微调后显著增强罕见词敏感和 query-document 交互注意力的地方。
