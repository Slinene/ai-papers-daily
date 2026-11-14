---
title: 'Auditing AI peer reviewers: a benchmark on real scientific papers'
title_zh: 审计 AI 同行评审：基于真实科学论文的基准
authors:
- Íñigo Zubeldia
- Boris Bolliet
- Francisco Villaescusa-Navarro
- Pablo Villanueva-Domingo
- Miles Cranmer
affiliations:
- University of Cambridge
- Flatiron Institute
- Universitat Autònoma de Barcelona
- Polymathic AI
arxiv_id: '2611.17052'
url: https://arxiv.org/abs/2611.17052
pdf_url: https://arxiv.org/pdf/2611.17052
published: '2026-11-12'
collected: '2026-11-14'
category: Eval
direction: AI 同行评审评估基准与多智能体审稿
tags:
- LLM
- Peer Review
- Multi-Agent
- Benchmark
- Citation Verification
- False Positive
one_liner: 提出注入可控错误的论文评审基准，评估12种LLM评审系统的检测率与误报率，并发布多智能体审稿者SKEPTHICAL
practical_value: '- 多智能体分工验证模式可迁移：将「检索证据 → 规则/代码校验 → 综合裁决」拆成独立工具，用于商品属性核验、广告文案合规、价格/库存数据校验，减少模型幻觉。

  - 评估生成内容可靠性时，可借鉴其注入可控错误（不同错误类型与严重级别）并同时测误报率的 benchmark 设计，建立内部 LLM 质检集。

  - 工具只在能补充模型知识盲区时有效：在领域知识强的场景（如 ML 论文）检索优势消失，提示业务中先评估模型自身知识覆盖，避免无效工具链增加成本和时延。

  - 数学符号/公式相关错误是主要误报源，若业务涉及计算类内容审核，要对这类错误单独调优或设置阈值，防止误杀。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

动机：LLM 评审已在生产规模使用，但缺乏系统评估。

方法：构建基准，向真实 arXiv 论文注入四类可定位错误（一般问题、数学、数值、引用），三个严重级别，测量评审系统检测率和干净副本上的误报率；提出 SKEPTHICAL 多智能体审稿者，分别通过检索原文验证引用、计算机代数验证数学、执行代码验证数值。在两个语料（天体物理、ML）各 15 篇预印本中注入 357 个错误，评估 12 个系统。

结果：模型选择影响最大，同一提示下三个前沿 LLM 总检测率相差约 50 个百分点。工具和脚手架在模型无法独立完成时有效：天体物理上 Claude Code 的数学和数值检测优于单次调用，强制引用检索使 SKEPTHICAL 引用错误检测率大幅领先。但在 ML 语料上，模型对文献更熟，SKEPTHICAL 引用检测率与最佳单 LLM 统计不可区分。多数系统误报率低于 10%，数学标志是主要误报来源。基准、注入错误和裁决日志已发布。
