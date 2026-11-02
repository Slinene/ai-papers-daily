---
title: Subquadratic Attention with a Hierarchical Tree-Structured Indexer
title_zh: 基于层级树索引器的次二次方注意力机制
authors:
- Leon Lufkin
- Cutter Dawes
- Alexander Speicher
- Kamesh Krishnamurthy
- Tomás Figliolia
- Beren Millidge
affiliations:
- Zyphra Research
arxiv_id: '2610.42112'
url: https://arxiv.org/abs/2610.42112
pdf_url: https://arxiv.org/pdf/2610.42112
published: '2026-10-30'
collected: '2026-11-02'
category: LLM
direction: 层级树索引稀疏注意力加速长上下文
tags:
- Sparse Attention
- KV Cache
- Hierarchical Indexer
- Long Context
- Subquadratic
- LLM
one_liner: 提出层级树结构索引器对KV cache递归压缩，使注意力总成本随序列长度亚线性增长，实现次二次方缩放
practical_value: '- 电商长序列建模：用户历史行为、商品序列、会话记录可视为 KV cache，借鉴层级树压缩摘要，在推理时自上而下检索相关 token，实现长上下文稀疏注意力，降低
  inference cost。

  - 轻量适配存量基座模型：仅需数亿 token 的 KL 蒸馏，业务侧可为已有 LLM 加装该索引器，无需重新预训练。

  - 树深度稳健：即使 6 层深树也不显著掉点，工程上可自由调整索引层级，在精度与延迟间取平衡。

  - Agent 场景收益：长上下文 agentic coding 性能不降，适合需要超长工具调用历史 / 文档上下文的电商导购 Agent 或智能客服，可直接扩展
  context window 而不更换模型。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

动机：注意力二次复杂度限制 LLM 长上下文；现有线性注意力有表达力损失，稀疏注意力索引器自身仍可能二次。
方法关键点：ZHA 构建层级树索引器，对 KV cache 递归压缩 key summaries；查询从树顶向下路由，只检索稀疏 key 子集。随树深增加，路由与最终注意力总成本按序列长度亚线性增长，整体注意力呈次二次方（超线性）缩放。可对预训练模型做几亿 token 的 KL 蒸馏轻量适配。
结果：在长上下文检索、推理、数学和 agentic coding 任务上保持性能；对树几何（最深 6 层）鲁棒；性能模型显示在超过 1M context 时显著优于竞争方法，有潜力扩展至数亿到十亿 token。
