---
title: 'Certified Domain Consistency for Multi-Domain Retrieval: Label-Free Per-Domain
  Contamination Control with Conformal Risk Guarantees'
title_zh: 多域检索中无标签逐域污染控制及共形风险保证
authors:
- Jayakumar Manoharan
affiliations:
- Electric Power Research Institute (EPRI)
arxiv_id: '2607.14157'
url: https://arxiv.org/abs/2607.14157
pdf_url: https://arxiv.org/pdf/2607.14157
published: '2026-07-14'
collected: '2026-07-19'
category: RAG
direction: 共形风险控制 · 多域检索污染保证
tags:
- Conformal Prediction
- Multi-Domain Retrieval
- Contamination Control
- Risk Control
- RAG
one_liner: 提出 C3R，一种即插即用的共形控制层，无标签情况下逐域认证污染预算，在最难域上保证污染降低。
practical_value: '- **无标签域污染控制**：无需查询时域标注，仅用推断的域后验即可逐域设定污染预算，适合电商多源检索（商品、评价、攻略）中低成本抑制错误域文档。

  - **可认证的风险保证**：提供有限样本下逐域污染上界的严格证书，且在最差域上保证污染降低而非仅边际平均，适合对权威性/安全性要求高的金融、法规等场景。

  - **软降级优于硬级联**：软降级策略在相同认证污染水平下比传统校准级联保留更多召回，可直接作为检索后安全层，不破坏原有排序。

  - **堆栈冻结与重排器无关**：C3R 作为外挂控制层，不改动现有检索和重排模型，迁移成本极低，适合现有搜索推荐系统快速落地。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：多域检索系统常返回语义相关但域错误的文档（如金融查询返回生物医学文献），传统边际共形风险控制只保证平均污染，忽略最差域，导致高风险场景下隐蔽错误。

**方法**：提出 C3R，一种冻结堆栈、与重排器无关的控制层。核心是通过两分裂方案（two-split scheme）构建风险控制预测集，利用推断的域后验（无需查询时真值标签）为每个域认证污染预算，并通过有限样本传递界（transfer bound）将推断域保证转换为真域保证，松弛量完全可估计。支持异质预算，并可直接部署。

**结果**：在 1,000 次重采样校准中，C3R 的证书从未违反，而边际控制每次都违反最污染域；软降级策略在同等认证污染下召回率高于最强校准级联。方法在两个开放测试集（含独立联邦法规集）上成功复现，LLM 评估也显示错误权威基础随污染上升，受控后下降。
