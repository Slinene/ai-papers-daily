---
title: Explainable Transformer Models for Clinical Prediction Tasks on Structured
  Electronic Health Records
title_zh: 可解释 Transformer 模型用于结构化电子健康记录的临床预测任务
authors:
- Jun Ni Du
- Lukas Adamek
- Maxim Kryukov
- Flavio Dormont
- Ziv Bar-Joseph
- Sven Jager
- Brandon Rufino
affiliations:
- Sanofi
- Carnegie Mellon University
arxiv_id: '2608.20315'
url: https://arxiv.org/abs/2608.20315
pdf_url: https://arxiv.org/pdf/2608.20315
published: '2026-08-20'
collected: '2026-08-22'
category: Other
direction: 结构化 EHR 序列建模 · 可解释性
tags:
- EHR
- Transformer
- Explainability
- Integrated Gradients
- Percentile Binning
- Clinical Prediction
one_liner: 将化验值按百分位分箱离散为 token 并结合 Integrated Gradients，实现 EHR 序列预测与 token 级解释
practical_value: '- 数值特征离散化：将连续特征（如价格、时长、评分）通过分位数分箱映射为离散 token，既适配 Transformer 输入，又保留相对大小信息，可用于用户行为序列建模。

  - 可解释性归因：Integrated Gradients 对输入 token 序列做贡献归因，可用于诊断推荐模型中哪些历史行为或特征驱动了预测，辅助特征筛选和模型审计。

  - 预训练 + 微调：在大规模用户序列上预训练通用行为语言模型，再针对具体任务（点击率、转化率）微调，类似 BERT-LER 在 EHR 上的做法。

  - 论文是医疗领域，但序列建模和数值编码策略可迁移到电商用户行为序列、广告曝光序列等场景。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：结构化 EHR 预测模型往往忽略定量化验信息，且缺乏对输入医疗事件的解释，缺少统一框架。

**方法关键点**：提出 BERT-LER，基于 BERT 风格，在 7500 万患者去标识化 EHR 数据上预训练和微调。将化验结果按百分位分箱离散为 token，保留分级信息；结合 Integrated Gradients 实现基于输入 EHR 序列的 token 级归因。

**结果**：在 EHRShot 公共基准和哮喘严重程度进展真实数据上，预测性能与公开基准模型相当，在化验相关任务上常常超过；归因结果与临床已知风险因素一致。架构与解释方法可推广至多个治疗领域。
