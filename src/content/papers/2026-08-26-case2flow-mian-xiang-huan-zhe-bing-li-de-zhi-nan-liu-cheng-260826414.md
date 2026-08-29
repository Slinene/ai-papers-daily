---
title: 'Case2Flow: Bridging Patient Cases and Guideline Flowcharts through Multimodal
  Retrieval'
title_zh: Case2Flow：面向患者病例的指南流程图多模态检索
authors:
- Jiale Wei
- Yufan Chen
- Alexander Jaus
- Zdravko Marinov
- Julian Friedrich
- Simon Reiß
- Jens Kleesiek
- Rainer Stiefelhagen
affiliations:
- Karlsruhe Institute of Technology
- Helmholtz Information and Data Science School for Health (HIDSS4Health)
- University Hospital Essen
arxiv_id: '2608.26414'
url: https://arxiv.org/abs/2608.26414
pdf_url: https://arxiv.org/pdf/2608.26414
published: '2026-08-26'
collected: '2026-08-29'
category: Multimodal
direction: 多模态检索 · 医疗流程图
tags:
- Multimodal Retrieval
- Late Interaction
- Training-Free
- Vision-Language
- Medical Flowcharts
- CRISP
one_liner: 提出训练-free 的 CRISP 评分，抑制无用 patch 并加入双向对齐，显著提升病例到流程图检索
practical_value: '- CRISP 的 patch 抑制与歧义 token 折扣可直接迁移到商品主图/广告创意的多模态检索：背景杂乱、促销文案 token
  常引入伪匹配，在 late-interaction 阶段做后处理即可提升 Recall，无需重训模型。

  - 双向 query-image 对齐思路适用于“用户 query ↔ 创意/商品图”互搜场景，能降低单向相似度误报，可作为排序重打分模块加入现有召回链路。

  - FlowAtlas 的合成对齐数据管线（从结构化文档/决策树生成 case-flowchart 对）可借鉴用于生成电商 SOP/政策文档与商品或广告场景的匹配对，低成本构造多模态检索训练/评测数据。

  - 失败模式分析（关键词过度依赖、背景 patch 匹配）值得在电商图文检索评估中复现，帮助定位精排模型偏置。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

动机：临床指南流程图编码可执行决策路径，但医生很难在大量指南中定位相关流程图；现有工作主要利用文本段落，流程图未得到充分利用。

方法：构建 FlowAtlas 语料，从 2080 份指南中提取 202 张流程图，并合成 1911 对病例-流程图对齐样本。评估现有多模态检索方法后发现系统性失败：过度依赖关键词，以及流程图背景区域引发伪 token-patch 匹配。为此提出 CRISP，一种训练-free 的 late-interaction 评分方法，通过抑制无信息 patch、折扣歧义 token 匹配、加入双向 query-image 对齐来锐化检索。

结果：CRISP 将 Recall@1 最多提升 18.71 个百分点；在已发表病例叙事上的盲法医生评估显示其具备超出合成查询的初步可行性。
