---
title: 'Decompose, Estimate, Select: Coverage-Aware Context Construction for Long-Form
  RAG'
title_zh: 分解、估计、选择：面向长文本 RAG 的覆盖感知上下文构建
authors:
- He Tu
- Aleena Bosco Kurumthottam
- Torsten Suel
affiliations:
- New York University Shanghai
- New York University
arxiv_id: '2610.40314'
url: https://arxiv.org/abs/2610.40314
pdf_url: https://arxiv.org/pdf/2610.40314
published: '2026-10-29'
collected: '2026-10-30'
category: RAG
direction: RAG 覆盖感知检索与自反馈生成
tags:
- RAG
- Coverage-aware retrieval
- Query decomposition
- Nugget evaluation
- Self-feedback
- Long-form QA
one_liner: 提出覆盖感知 RAG 流水线，通过子问题分解、覆盖矩阵估计和贪心选择提升证据覆盖，并发现检索覆盖提升未必带来答案覆盖提升
practical_value: '- **覆盖感知选择层面**：在长文本问答/报告生成场景，不要只用相关性排序，可将用户 query 拆成多个子问题，用 cross-encoder
  预测文档×子问题覆盖矩阵，再贪心选择最大化覆盖。这种思路可直接迁移到商品详情页摘要、多属性商品推荐理由生成、广告文案多卖点覆盖等任务。

  - **自反馈环节**：发现检索到的证据覆盖率提高不一定带来答案覆盖提高，瓶颈在生成器的利用。可做“生成→自我 critique→指出未充分利用的文档→在同上下文二次生成”，不增加检索成本就能提升答案完整性。在电商场景可用“第一次生成标题，让模型指出漏掉的卖点，再基于同一商品描述重写”的迭代文案优化。

  - **工程权衡**：子问题分解用 GPT-4o 比开源 7B 只高 0.027 α-nDCG，成本可控。交叉编码器估计覆盖矩阵是关键瓶颈，估计不准导致性能损失大于子问题分解，建议投入更多数据训练
  coverage estimator。

  - **评估启示**：用 α-nDCG、Vstrict 等覆盖指标区分冗余证据，比单纯 nDCG 更能反映长文本效果。若业务目标是多卖点覆盖（如商品标题需覆盖不同卖点），可引入类似
  nugget 的原子事实评估，避免模型重复强调同一卖点。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：长文本 RAG 中，传统相关性检索会返回大量冗余文档：多个文档重复覆盖同一子问题，而其他子问题缺乏证据。本文用 nugget 评估框架量化该问题：在 TREC RAG 2024 上，gold 选择器用 5 个文档就能达到与 10 个文档相同的子主题召回，而覆盖训练检索器用 10 个文档仍更低。因此，需要显式建模证据覆盖，而不是依赖嵌入相似度做多样化。

**方法关键点**：
- 流水线：LLM 将查询分解为 10 个自包含子问题 → BM25 取 top-100 → 覆盖训练的双编码器重排 → cross-encoder 预测文档×子问题覆盖矩阵 → 贪心最大边际覆盖选择 top-10 文档。
- 双编码器：在 ModernBERT 基础上，用对比学习继续训练，正样本为覆盖未覆盖子问题的文档，负样本包括冗余文档（覆盖已覆盖子问题）和不相关文档；训练数据来自 Researchy Questions 的 Llama 判断 answerability ≥4。
- 覆盖估计器：ModernBERT cross-encoder 对每个 (文档, 子问题) 打分，二值化阈值 τ=0.3。
- 自反馈循环：生成第一轮答案后，模型自我 critique 指出未充分利用的文档标识，基于同一组文档重新生成，不引入新检索结果。

**关键实验**：
- 在 TREC RAG 2024 上，从相关性双编码器 0.625 α-nDCG@10 提升到覆盖训练 0.656，再加选择和覆盖估计达到 0.702，接近 gold nuggets 上界 0.718，且 P@10 和 nDCG@10 不下降。
- Gold oracle 选择器检索覆盖 StRecall@10 达 0.888，远高于本方法的 0.799，但下游 Vstrict 反而更低（0.322 vs 0.351），说明检索覆盖提升不直接带来答案覆盖提升。
- 自反馈二次生成在相同文档上下文中将 Vstrict 从 0.338 提升到 0.424（+0.086），且两次迭代后 F1 最佳。

**最值得记住的一句话**：对于长文本 RAG，固定上下文预算下，提升生成器对已有证据的利用（自反馈）比单纯提高检索覆盖更有效；检索覆盖的进一步提高可能不会改善答案完整性。
