---
title: Tracing and Taming Hallucinated Terms via Subsequence-Association Filtering
  and Breadth-Aware Selection for LLM Query Expansion
title_zh: 基于子序列关联过滤与广度感知选择的LLM查询扩展幻觉词抑制
authors:
- Amit Kumar Jaiswal
- Sagar Uprety
- Prayag Tiwari
affiliations:
- Indian Institute of Technology (BHU), Varanasi, India
- University College London, London, UK
- Halmstad University, Halmstad, Sweden
arxiv_id: '2610.13810'
url: https://arxiv.org/abs/2610.13810
pdf_url: https://arxiv.org/pdf/2610.13810
published: '2026-10-09'
collected: '2026-10-12'
category: QueryRec
direction: LLM查询扩展幻觉过滤
tags:
- Query Expansion
- Hallucination
- LLM
- Subsequence Association
- Faithfulness
- Retrieval
one_liner: 用跨上下文可再现性与语料支撑度识别幻觉term，在nDCG@10无损下将注入query的无支撑词减少85%-93%
practical_value: '- 可直接复用 SAFE-QE 的过滤评分：对 LLM 生成的候选扩展词/phrase，用「随机扰动 prompt 后的重现率
  ρ(t)」+「与 top-k 相关文档的最大支持度 γ(t)」做加权，公式 s(t)=γ(t)-λρ(t)(1-γ(t))+μfreq(t)。在电商搜索 query
  改写、广告关键词扩展中，能有效识别并降权「无论上下文都被生成但无商品/文档支撑」的幻觉词。

  - 词选择不要固定 top-k，改为带 grounding 约束的 budget 最大覆盖问题：用贪心近似（1-1/e）从候选词里选最多覆盖伪相关文档/商品 faceting
  的子集，避免多个高分词重复覆盖同一意图。电商多意图 query（如“苹果”）尤其需要这种 breadth-aware selection。

  - 稳定性过滤很便宜：对 LLM 采样 N 次，只保留 freq(t)≥θ 的稳定 term，能额外过滤掉少量采样中出现的幻觉词。工程上可简单并行多次采样，几乎不增加线上复杂度。

  - 建立 HETR 监控指标：在业务评估里同时看「幻觉率」和「幻觉负载＝HETR×注入词数」，不要只看率；强 retriever / dense retrieval
  下生成式扩展收益小，但幻觉过滤的收益最大，这时候尤其值得上线。

  - 结论可迁移：一个 0.5B 小生成器 + 过滤器，faithfulness 可以超过 9B HyDE，说明过滤机制比生成器规模更重要；训练无关、检索器无关，适合低成本接入已有
  generate-then-expand 流程。但注意 grounding 阈值 τg 需要按 retriever 分别标定（SPLADE 下的伪相关集合会让更多候选通过阈值）。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
LLM 用于 query expansion 已成为标准做法，但 LLM 会幻觉，注入不存在的实体和离题词，增加 ranking noise，伤害强 retriever。已有缓解方法（corpus grounding、mutual verification、preference alignment）只是按共现或一致性启发式过滤，没有从生成机制解释为什么某个 term 会出现，也缺少「保留多少个词、如何平衡覆盖与忠实度」的原则性选择标准。论文引入两个理论工具：decoder-only transformer 的子序列关联（subsequence-association）幻觉解释，以及语言生成的 consistency–breadth–stability 权衡，把 query expansion 形式化为「在近似 broad 且 consistent 的目标词汇上做受限选择」。

## 方法关键点
- **候选生成**：LLM 对 query 做 N 次采样，得到候选扩展 term 及采样频率 freq(t)。
- **语料条件可再现性评分**：对每个 term 计算跨上下文可再现性 ρ(t)（在 P 个随机扰动 prompt 下 term 是否重现），以及语料 grounding γ(t)（term 与 top-k 伪相关文档的最大支持度）。综合评分为 s(t)=γ(t)−λρ(t)(1−γ(t))+μfreq(t)，专门惩罚「高重现但无相关文档支撑」的幻觉 term。
- **广度感知选择**：在 grounding 约束 τg 下，用 budget-B 最大覆盖目标（submodular greedy）从 grounded 候选里选子集，覆盖伪相关文档的不同 facet；再做 freq(t)≥θ 的稳定性过滤。
- **新指标 HETR**：Hallucinated Expansion Term Rate，度量注入扩展词中无相关文档支持的比例；同时提出 hallucinated term load = HETR × |E(q)|，反映检索器实际收到的坏词数。

## 关键实验与结果
在 6 个集合（TREC DL 19/20 + 4 个 BEIR）和 3 个检索器（BM25、SPLADE、Contriever）上，用 Gemma-2-9B 生成。
- **效果**：nDCG@10 与 Query2doc、HyDE、CSQE、MILL 统计无显著差异（|Δ|≤0.008）；过滤无支撑词不会伤害排名质量。
- **幻觉负载**：HETR 0.465 vs Query2doc 0.656、HyDE 0.663；每 query 无支撑词 load 4.30 vs 27.83、57.47，降低 85%–93%；相对 CSQE、MILL 也降低 43%–45%。
- **检索器影响**：在 SPLADE 上所有扩展都退化，SAFE-QE 将退化减半；在 Contriever 上 faithfulness 优势最大。
- **生成器规模**：0.5B 小生成器 + SAFE-QE 的 faithfulness 优于 9B HyDE，说明过滤机制而非生成器规模贡献主要收益。

最值得记住的一句话：**在强 retriever 上，faithfulness 与 ranking quality 并非零和；用机制驱动的 grounding + 覆盖率选择可以在不损失 nDCG@10 的前提下，把 LLM 注入 query 的无支撑词减少 85% 以上。**
