---
title: 'Same Question, Different Source, Different Answer: Auditing Source-Dependence
  in Medical Multi-Source RAG'
title_zh: 同一问题，不同来源，不同答案：审计医疗多源RAG中的源依赖性
authors:
- Yubo Li
- Rema Padman
- Ramayya Krishnan
affiliations:
- Carnegie Mellon University
arxiv_id: '2605.29084'
url: https://arxiv.org/abs/2605.29084
pdf_url: https://arxiv.org/pdf/2605.29084
published: '2026-05-27'
collected: '2026-05-31'
category: Eval
direction: 多源RAG评估 · 源依赖性审计
tags:
- RAG
- Source-Dependence
- Evaluation
- Medical QA
- Benchmark
one_liner: 将RAG评估从单答案正确性转向源间关系审计，揭示多源异质性被严重低估
practical_value: '- 多源RAG审计框架可直接迁移至电商问答：当知识库包含不同商家政策、商品描述时，检测答案源依赖性，避免单一来源给出误导性高置信回复。

  - HERO-QA层次化检索和结构化输出judge的设计可复用于多源知识库冲突检测，在电商产品推荐解释、政策问答中自动标注答案一致/矛盾关系。

  - 5标签源间关系分类法（一致/互补/部分重叠/矛盾等）适合作为Agent或推荐系统多路召回融合的后处理标准，用于冲突消解或多角度信息呈现。

  - 启示：更好的检索会暴露更多分歧，业务中盲目提升召回而不审计源依赖性可能放大风险，需建立持续监控体系。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

动机：现有RAG评估仅关注答案是否符合单一金标准，无法诊断多源系统因检索文档不同而产生矛盾答案的失效模式。作者提出“源依赖性”是NLP评估缺失的维度，审计它意味着将评估单元从答案正确性转向源间关系，尤其适用于多作者机构知识库。

方法：以移植患者教育为场景，发布TransplantQA基准——收集真实患者问题，利用多家机构手册作为候选源生成答案；提出HERO-QA层次化检索策略，确保每个答案可溯源并进行审计；设计结构化输出judge，基于经过验证的5标签分类法（如完全一致、互补、矛盾等）自动评分源间关系。

结果：大规模实验表明，性能更好的检索器反而揭示出远超以往估计的源间分歧，此前研究低估了分歧的普遍性而非严重性。该审计框架具备领域无关性，可迁移至法律、教育等多源RAG系统。
