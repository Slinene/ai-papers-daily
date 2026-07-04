---
title: 'What Survives Into Context: A Diagnostic for Budget-Constrained Multi-Hop
  RAG and When Submodular Evidence Packing Improves It'
title_zh: 预算受限多跳RAG的诊断指标与子模证据打包增益条件
authors:
- Ananto Nayan Bala
affiliations:
- Ahsanullah University of Science and Technology
arxiv_id: '2607.00725'
url: https://arxiv.org/abs/2607.00725
pdf_url: https://arxiv.org/pdf/2607.00725
published: '2026-07-01'
collected: '2026-07-04'
category: RAG
direction: 预算受限多跳RAG证据选择
tags:
- RAG
- Multi-hop
- Submodular Optimization
- Evidence Packing
- Answer-in-Context
- Reader Budget
one_liner: 提出 answer-in-context 诊断，并揭示子模证据打包仅在弱 reader、多跳互补结构下有效
practical_value: '- **离线评估指标**：在上下文窗口局限时，用 answer-in-context（答案是否作为连续片段出现在最终上下文）替代传统文档召回率评估打包质量，与下游
  F1 相关性更高。

  - **证据打包策略**：当使用弱 reader（<7B）且面临多跳互补证据时，将上下文构建建模为预算约束的子模最大化，同时优化相关性、查询覆盖、代表性和多样性，可获得明显提升（最高
  +5.1 F1）。

  - **适用条件判断**：该打包收益仅在四种条件同时满足时成立：多跳互补结构、检索已召回证据、严格但非极端预算、reader 能力不足。若使用 7B+ 模型，优势消失甚至反转为负，应切换为简单截断或启发式。

  - **RAG Agent 工具**：在为搜索推荐系统构建 RAG Agent 时，可部署轻量级子模打包模块，针对弱基座模型在预算敏感场景（如商品知识问答、个性化推荐解释生成）中提升证据密度，但需持续监测
  reader 规模边界。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：固定上下文预算的 RAG 系统中，检索后只允许部分证据送入 reader，传统文档召回率无法准确衡量“哪些证据真正进入最终上下文”，导致选择策略与下游任务脱节。

**方法关键点**：
- 提出 **answer-in-context** 诊断指标：衡量黄金答案是否以连续片段形式出现在打包后的 reader 上下文中，比召回率能更好预测答案 F1（r=0.39–0.55 vs. ~0.31），且携带超出检索的增量信息。
- 将上下文构建形式化为预算约束的单调子模最大化问题，设计了一个打包器联合优化 **相关性、查询覆盖、代表性与多样性**。

**关键结果**：
- 在 HotpotQA 上，160 token 预算、3B reader 下，子模打包比强聚焦启发式、MMR 等提升最高 +5.1 F1，且 token 成本持平或更低。
- 收益严格依赖于四个条件的共同出现：多跳互补结构、检索已召回证据、预算严格但不过分、reader 较弱（3B）。通过量化控制 reader 规模（3B→7B→14B），发现 7B 时优势消失，14B 时显著反转，诊断指标用一个变量解释了所有边界。
- 介入实验证实：在 2WikiMultiHopQA 上，只提升覆盖率但不提升 answer-in-context 的打包改变不会带来准确率增益。
