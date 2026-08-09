---
title: 'Tracing the Heart: An Evidence-Linked Pipeline for Heart-Failure Feature Engineering'
title_zh: 心衰特征工程自动化：证据链接的多智体流水线
authors:
- Soorya Ram Shimgekar
- Michelle Hu
- Dorisa Shehi
- Daniel Kang
- Roy Ka-Wei Lee
- Koustuv Saha
- Christian Poellabauer
- Christopher Lee
- Sajeev Singh
- Piyum Zonooz
affiliations:
- Nimblemind
- Singapore University of Technology and Design
- University of Illinois Urbana-Champaign
- Florida International University
- University of California Los Angeles
arxiv_id: '2608.06366'
url: https://arxiv.org/abs/2608.06366
pdf_url: https://arxiv.org/pdf/2608.06366
published: '2026-08-06'
collected: '2026-08-09'
category: MultiAgent
direction: Agent协作自动化特征工程与审计
tags:
- Multi-Agent System
- Feature Engineering
- Evidence-Linked
- Rubric Scoring
- EHR
- Healthcare AI
one_liner: 多Agent协同生成可审计聚合特征，将心衰表型预测AUROC从0.895提升至0.963
practical_value: '- **自动化特征工程流水线**：多Agent分工协作（理解临床指南、检索证据、生成SQL/聚合特征）可迁移到电商推荐，用LLM
  Agent自动从用户行为日志、商品属性中生成高阶聚合特征，替代大量手工特征工程，提升CTR/CVR模型AUC。

  - **证据链接与审计机制**：每个特征关联生成依据（如原始表、映射规则），可解释且可审计，适合对模型效果变动进行归因追踪，在推荐系统中排查特征漂移或线上效果波动时有工程价值。

  - **Rubric打分过滤低质特征**：为特征生成设计量化评分标准（有效性、证据支持度），可在Agent pipeline中置入质检步骤，避免无效特征进入模型，减少特征膨胀和过拟合风险。

  - **受限LLM审计确保合规**：推荐系统中的风控、生态规则等场景可借鉴，用独立Agent审核生成特征是否符合业务规范，提升系统安全性。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：EHR特征工程占数据科学家39-45%工作量，心衰需要整合碎片化数据与临床指南推理。现有规则和LLM方法自动化有限，缺乏证据追溯和可维护性。  
**方法**：提出Nimblemind Multi-Agent System (nMAS)，一个证据链接、基于评分标准（rubric）的多Agent流水线。Agent分别负责理解临床指南、检索证据、生成SQL查询和聚合特征，并由受限LLM审计质量。在9张源表、500份虚拟患者记录上评估，生成132个结构化特征和70个经评分标准打分的聚合特征，验证结构完整性和来源可溯性。  
**结果**：加入聚合特征后，HFrEF表型预测AUROC从0.895升至0.963，HFpEF从0.870升至0.910；独立LLM评估证据支持与方法学合理性得分为满分81.5%。实验表明自动、可审计的特征工程在复杂心血管EHR数据上可行，但局限于单机构队列，需外部验证。
