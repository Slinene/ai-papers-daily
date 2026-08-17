---
title: How retriever redundancy and diversity impact RAG effectiveness
title_zh: 检索冗余与多样性如何影响 RAG 生成正确性
authors:
- Jonathan J Ross
- Bevan Koopman
- Anton van der Vegt
- Guido Zuccon
affiliations:
- The University of Queensland
- CSIRO
arxiv_id: '2608.13956'
url: https://arxiv.org/abs/2608.13956
pdf_url: https://arxiv.org/pdf/2608.13956
published: '2026-08-14'
collected: '2026-08-17'
category: RAG
direction: RAG 检索多样性对生成器的影响
tags:
- RAG
- retrieval diversity
- redundancy
- LLM judge
- FictionalQA
- generation correctness
one_liner: 在虚构 QA 上证明重复/改写文档几乎无益，跨体裁多样文档可提升 RAG 正确性 17%–47%
practical_value: '- RAG 检索/重排不要只取 similarity top-k，必须引入来源/视角多样性：可复用 MMR、coverage-aware
  rerank，或在结合商品知识、用户评论、官方说明时显式跨体裁采样，让生成器获得多角度证据。

  - 对同义改写、伪文档扩展要谨慎：LLM 改写同一份 anchor 并不能稳定提升事实型 QA 正确性，不必在推理侧做同质数据扩增；省下来的上下文预算换成异质来源。

  - 在商品问答、推荐理由生成、广告文案等 RAG 场景中，文档体裁/来源可信度可能比单纯相关性更影响生成；可考虑对百科型或权威结构化内容加权，压制低质社媒文本。

  - 评估检索质量时，传统去冗余假设对生成器不一定成立：面向生成器的评估要看最终答案正确性，并控制参数知识和答案字符串匹配，否则容易误判多样性收益。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：RAG 检索器通常逐文档按相关性打分，但生成器把检索结果作为一个整体读取。检索集里的冗余和多样性如何影响生成答案正确性，已有结论混杂：有的说冗余能强化证据，有的说改写有益；多数研究没有控制 LLM 参数知识、答案字符串是否出现、来源差异等混淆。问题在短事实型 QA 上尤其重要：答案只是一个事实，重复副本是否改变模型行为仍不清楚。

**方法与关键点**：
- 使用 FictionalQA 虚构事件 QA 数据集，确保生成器无法靠参数知识作答（closed-book 正确率仅 0.01–0.04）。
- 对每个 query 构造三种证据集：`duplicate`（同一 anchor 文档复制 k 份）、`paraphrase`（LLM 对 anchor 做 k 个独立改写）、`diverse`（跨新闻/社交媒体/企业/百科/博客的 k 份不同文档），k=0–5。
- 所有文档均经 GPT-4o 验证：单独给出该文档即可推出 gold answer，因此正确信息量基线固定，变化只来自冗余/多样性形式。
- 生成器覆盖 1B–12B：Llama-3.2-1B/3B、Llama-3.1-8B、Gemma-3-12B；Qwen2.5-32B 负责 paraphrase 和 LLM-judge 正确性判断。
- 还构造 screened queryset，移除答案字符串精确或近似出现，以区分“更多明确答案”和“体裁多样性”的贡献。

**关键结果**：`duplicate` 和 `paraphrase` 相比单文档基线基本没有显著提升；`diverse` 在所有 k 和所有模型上显著提升，k=5 时较 baseline 绝对提升 0.112–0.240，相对约 17%–47%。在 screened 子集上，8B 的 diverse 正确性仍从 0.417 单调升至 0.647，说明收益来自体裁多样性而非答案字符串。此外，体裁有强主效应：百科文档 pooled 正确性 0.804，社交媒体仅 0.532。

**最值得记住的一句话**：RAG 检索应显式选择多样、独立来源的文档，而不是用近重复 passage 填满上下文窗口。
