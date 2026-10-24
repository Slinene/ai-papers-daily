---
title: 'Real PMIDs, Wrong Papers: Harness Design for Biomedical Claim-Verification
  Agents'
title_zh: 真实 PMID，错误论文：生物医学声明验证代理的 Harness 设计
authors:
- Mohammed Saqlain
affiliations:
- Independent Researcher
arxiv_id: '2610.29812'
url: https://arxiv.org/abs/2610.29812
pdf_url: https://arxiv.org/pdf/2610.29812
published: '2026-10-21'
collected: '2026-10-24'
category: Agent
direction: Agent 检索 harness 设计与瓶颈分析
tags:
- Agent
- Retrieval
- PubMed
- Claim Verification
- Hallucination
- RAG
one_liner: 对照实验表明检索而非推理是医疗文献验证代理的瓶颈，自写查询代理提升召回但预算利用不足
practical_value: '- 在需要检索工具的 LLM 应用（如电商导购、客服问答、商品知识库问答）中，直接用用户原始 query 做单次检索往往不可靠，应让模型自己改写/生成多个查询，或采用
  ReAct 式迭代检索，能显著提升召回和最终答案质量。

  - 检索质量通常是整体效果的瓶颈，而不是推理能力：即便给予黄金文档，模型准确率仍有较大提升空间，因此应优先投入优化检索/召回环节，而非只调大模型推理。

  - 对返回结果进行“存在性检查”不够，必须做相关性校验：模型可能吐出真实存在的商品 ID 或文档 ID，但与问题无关，应增加一个独立的 LLM judge 或相关性过滤步骤。

  - 让 agent 具备搜索预算意识：实验发现 agent 只使用了不到一半的搜索预算，可设计显式的预算消耗策略（如强制步数、每次搜索的查询数量限制）以充分探索检索空间。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：生命科学文献搜索代理逐渐成为科研助手的标配，但 harness 设计缺乏对照实验证据。作者在 SciFact 生物医学声明验证任务上，以 PubMed API 为唯一工具，固定 backbone 和输出格式，系统对比四种 harness。

方法关键点：四种设置包括 closed-book 直接回答、用声明作为 query 的单次检索、ReAct 式代理自行编写 PubMed 查询、以及提供黄金摘要的 oracle，均使用两个 efficient frontier 模型。

关键结果：单次检索仅能找到 6% 声明的黄金论文，且将过度自信错误转为弃权但未提升准确率；代理自写查询使黄金召回提升三倍，最高 verdict 准确率 62%，对比其他 realistic harness 的 49-59%，但样本量下差异不显著，且代理使用搜索预算不到一半；oracle 准确率 79-86%，与 realistic 设置存在 17-24 个点的显著差距，说明检索而非推理是主要瓶颈。引用审计显示 closed-book 模型给出的 PMID 几乎都存在（327/335），但几乎不相关：跨家族 LLM judge 仅认定 3/327 个引用相关，而搜索代理的引用相关性达 67%。因此仅做存在性检查不足以保障科学代理的安全。
