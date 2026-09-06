---
title: Unifying Conformal Language Tasks with In-Context Ensembles
title_zh: 利用上下文集成统一保形语言任务
authors:
- Xiao Shi Huang
- Chen-Yuan Lin
- Bruce Kuwahara
- Kin Kwan Leung
- Jesse C. Cresswell
affiliations:
- Signal 1 AI
- Layer 6 AI
arxiv_id: '2609.03005'
url: https://arxiv.org/abs/2609.03005
pdf_url: https://arxiv.org/pdf/2609.03005
published: '2026-09-02'
collected: '2026-09-06'
category: LLM
direction: Conformal Prediction 与上下文集成评分
tags:
- Conformal Prediction
- In-Context Learning
- Ensembling
- Coverage
- LLM Scoring
one_liner: 提出 Conformal Relevance 框架，用上下文样例策展与集成构建评分函数，兼顾覆盖与简洁并减少手工提示工程
practical_value: '- 在电商搜索/推荐中需要覆盖与简洁平衡的场景（如搜索摘要、推荐理由生成、广告文案过滤），可直接用 conformal prediction
  校准 LLM 评分，自动保证覆盖率，同时优化简洁性，替代手工规则。

  - 用历史标注数据策展少量高质量上下文示例，替代逐任务写 prompt 评分函数，降低多类目、多任务场景下的维护成本；示例多样性提升评分鲁棒性。

  - 集成多个 LLM 评分或同 LLM 的不同示例组合，利用文中 complementarity condition 判断是否有助于提升最差情况得分，指导工程上选择有效集成方案，用于粗排或候选过滤。

  - 在生成式推荐中，若要保证生成内容覆盖关键卖点且不冗余，可借鉴该框架对生成结果做 conformal 筛选，同时用上下文集成提高简洁性判定质量。'
score: 6
source: arxiv-stat.ML
depth: abstract
---

动机：许多 NLP 任务（摘要、抽取式问答、法律审查等）本质是在文档中检索相关内容，需同时满足覆盖（保留足够相关信息）和简洁（剔除无关信息）。现有基于 conformal prediction 的方法虽能保证覆盖，但简洁性依赖评分函数设计，而 SOTA 评分函数多靠手工编写 LLM prompt，费时且任务特定。

方法：提出 Conformal Relevance 框架。核心思想是用上下文学习示例策展和集成替代手工 prompt 工程：从标注数据中自动选取示例，输入 LLM 生成相关性评分，再通过集成多个评分（如不同示例组合或不同 LLM 输出）提升稳定性。同时从理论上分析多样性对集成 conformal 分数的影响，给出互补条件（complementarity condition）刻画何时集成能改善最差情况句子的分数，以及饱和界限（saturation bound）说明集成收益上限。

结果：在七个 NLP 任务上验证，该框架只需极少人工输入即可保持覆盖率，同时显著提升简洁性；理论结果指导如何选择有效集成的评分函数，避免无效或负向集成。
