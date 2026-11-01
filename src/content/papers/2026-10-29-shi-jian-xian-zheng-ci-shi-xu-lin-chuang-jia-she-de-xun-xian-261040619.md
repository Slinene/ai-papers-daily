---
title: 'Testimony from Timelines: Evidence-Grounded Significance Testing of Temporal
  Clinical Hypotheses'
title_zh: 时间线证词：时序临床假设的循证显著性检验
authors:
- Chengyang He
- Wenlong Zhang
- Koduvayur Subbalakshmi
- Ping Wang
affiliations:
- Stevens Institute of Technology
arxiv_id: '2610.40619'
url: https://arxiv.org/abs/2610.40619
pdf_url: https://arxiv.org/pdf/2610.40619
published: '2026-10-29'
collected: '2026-11-01'
category: Eval
direction: LLM 评估 · 时序假设检验
tags:
- LLM evaluation
- temporal reasoning
- statistical hypothesis testing
- benchmark
- retrieval-augmented
- clinical timelines
one_liner: 提出STRATA基准与ART分阶段范式，暴露并显著缩小LLM在时序临床假设检验中的证据-结论差距
practical_value: '- 在电商/广告Agent做实验分析、归因或用户行为假设验证时，强制模型显式输出“分析计划 / 证据集 / 统计检验”三段，而不是只给结论；这样能定位“证据选错但结论碰巧对”的隐性失败。

  - 把业务中的指标定义、统计口径、实验设计规则写成结构化的codebook注入prompt或知识库；论文显示frontier models在拿到codebook后成功率明显提升，说明确定性规则能大幅增强LLM做数据分析的可信度。

  - 分层评估Agent：除最终指标外，还要评估中间检索/筛选的证据集和检验选择；否则准确率会掩盖证据-结论差距，类似只评估推荐点击率而忽视归因与排序过程错误。

  - 优先优化记录筛选与过滤逻辑，而非盲目加大模型规模；实验表明主要瓶颈是“哪些记录算数”而不是统计方法选择，对应RAG或Agent中检索质量比生成模型规模更影响最终可靠性。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

动机：LLM常对“召回后销量是否下滑”“疫苗后一个副作用是否先于另一个出现”等时序假设给出流畅但无检验的答案。网上的断言大多需要显著性检验才能成立，而验证过程必须明确零假设、选择检验方法并决定哪些记录相关；任一环节出错都可能导致结论看似正确但证据错误。现有LM数据分析基准只评最终结论，且直接给出相关数据，无法暴露中间决策问题。

方法关键点：STRATA基准包含8,735个时序临床假设，基于疫苗不良事件报告的时间线，提供gold plans、证据集、p值和verdicts，全部由发布codebook和确定性oracle生成。ART范式将推理拆为三步：articulate（明确假设与检验计划）、retrieve（检索相关记录）、test（执行统计检验），每一步作为可检查的中间输出。

关键结果：五个模型配置的实验显示，系统主要失败在“选择哪些记录算数”，即证据-结论差距；只看结论准确率会掩盖这一失败。ART大幅缩小该差距，使31B开放模型与frontier models在同一范式下仅差0.01；frontier models在获得codebook后表现成功。
