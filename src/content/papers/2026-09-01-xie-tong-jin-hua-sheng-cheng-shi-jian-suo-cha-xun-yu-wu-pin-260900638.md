---
title: 'It Takes Two to Match: Co-Evolving Generative Retriever with Reinforcement
  Learning'
title_zh: 协同进化生成式检索：查询与物品双侧关键词空间的强化学习联合优化
authors:
- Runpeng Dai
- Kaili Huang
- Changsung Kang
- Ciya Liao
affiliations:
- University of North Carolina at Chapel Hill
- Apple
arxiv_id: '2609.00638'
url: https://arxiv.org/abs/2609.00638
pdf_url: https://arxiv.org/pdf/2609.00638
published: '2026-09-01'
collected: '2026-09-02'
category: GenRec
direction: 生成式检索 · 双侧关键词协同进化 RL
tags:
- Generative Retrieval
- LLM
- GRPO
- Keyword Matching
- Inverted Index
- Co-Evolving RL
one_liner: 用双侧 LLM 生成关键词并直接做倒排索引匹配，通过 SFT 对齐与交替 GRPO 协同进化，F1 最高提升 36.1%
practical_value: '- **可直接落在电商/广告关键词召回系统**：用两个 LLM 分别生成 item 侧搜索词和 query 侧扩展词，再通过倒排索引匹配，天然兼容广告主
  keyword bidding 和现有 keyword-based 基础设施，比只优化 query 侧更贴近业务可控性。

  - **SFT 对齐初始化便宜且有效**：先用 base LLM 离线为每个 item 生成关键词，再按相关 item 的关键词池聚合出 query 目标关键词；这样能避免
  RL 冷启动，也适合用行为/成交 labels 构造对齐数据。

  - **item 侧用 counterfactual marginal reward 优化全局 F1 很实用**：工程上通过缓存参考索引和只计算受影响 query
  集合，避免每次 rollout 重建全量索引；在业务中可以把 F1 换成加权 F-measure，按 precision/recall 优先级调节，例如更严地惩罚无关广告。

  - **给 query 生成器加搜索结果或在线提示，能明显提升效果**：Internal 数据集上 +Search Results 将 F1 从 0.3963
  提升到 0.4379，适合解决拼写错误、非英文、实体型 query；在 Agent 搜索/推荐场景中，可把已有检索结果作为 context 注入生成器。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

## 动机

检索是搜索/广告系统的第一阶段，漏召回基本不可逆。现有 LLM 检索大多只做 query 侧扩写或改写，最终匹配仍交给下游 retriever，query 与 item 的表示空间没有被联合构建。CoGR 试图让两个 LLM 分别生成关键词集合，直接在倒排索引上匹配，既保留 keyword-based 基础设施，又能端到端优化匹配质量。

## 方法关键点

- **两个独立生成器**：G_q 生成 query keywords，G_i 生成 item keywords；匹配方式为 `(S_q ∪ {q}) ∩ (S_i ∪ {i}) ≠ ∅`，排序用 BM25。
- **SFT 初始化**：先用 base LLM 为 item 生成 M 个关键词；再把每个 query 相关 item 的关键词合并，取 top-N 高频词作为 query 目标。这样让相关 pair 天然拥有重叠关键词。
- **协同进化 RL**：用 GRPO 交替更新两侧。Query 侧 reward 为直接检索 F1；item 侧 reward 为替换该 item 关键词后对全局 query F1 的边际贡献。每次只训练一侧，另一侧的 index 冻结。
- **高效实现**：item 侧 reward 只需查找 query index，定位受影响的 query，用缓存计数做增量 F1 更新，不需要重建全量 item index。
- **预算约束**：两侧关键词数超过 K_max 时 reward 置 0。

## 关键结果

在 Internal APP Marketplace（13.5k train / 1.5k eval queries，39.6k apps）和 WANDS（430/50 queries，42,994 products）上，CoGR-4B 的 F1 分别为 0.3963 与 0.6819，较最强基线 ANCE-Qwen4B 相对提升 10.9% 和 36.1%。冻结 item 侧仅做 query RL 的 CoGR❄ 大幅落后，说明双侧协同进化必要。消融显示：删除 SFT、共享 generator、替换 item reward 为转置 F1 均会掉点。加入搜索结果的 query 提示把 Internal F1 从 0.3963 提升到 0.4379。

最值得记住：**query 与 item 的关键词空间应放在同一个检索目标下交替优化，而不是只优化一侧。**
