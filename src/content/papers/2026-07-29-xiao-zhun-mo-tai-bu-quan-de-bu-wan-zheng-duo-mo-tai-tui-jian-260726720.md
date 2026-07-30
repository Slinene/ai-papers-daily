---
title: 'CaIRec: Calibrated Modality Imputation for Incomplete Multimodal Recommendation'
title_zh: 校准模态补全的不完整多模态推荐方法
authors:
- Ruiyu Liu
- Xiaohao Liu
- Miaomiao Cai
- Yunshan Ma
- See-Kiong Ng
affiliations:
- Southern University of Science and Technology
- National University of Singapore
- Singapore Management University
arxiv_id: '2607.26720'
url: https://arxiv.org/abs/2607.26720
pdf_url: https://arxiv.org/pdf/2607.26720
published: '2026-07-29'
collected: '2026-07-30'
category: RecSys
direction: 多模态推荐 · 模态补全校准
tags:
- Multimodal Recommendation
- Modality Imputation
- Calibration
- Preference Alignment
- Graph Learning
one_liner: 通过两阶段校准框架解决模态缺失导致的跨模态结构失真与偏好适应差距，提升多模态推荐鲁棒性
practical_value: '- 模态补全时引入跨模态结构一致性约束，避免补全后多模态特征割裂，可通过对比损失或结构保持正则实现。

  - 偏好导向表征校准：构造伪缺失样本，将补全表征与经排序监督训练好的完整模态表征对齐，使补全特征直接适配推荐排序任务。

  - 构建补全感知的物品关系图，同时融合补全后的多模态内容相似性与用户行为协同信号，提升图推荐模型在模态缺失场景下的表现。

  - 两阶段设计：先做与推荐任务无关的结构校准，再做偏好微调，方便工程上逐步开发和部署，降低在线开销。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：多模态推荐中商品经常缺失图像、文本等模态，现有补全方法只追求恢复表征，忽视跨模态结构一致性和推荐任务适配，导致推荐性能下降。

**方法**：提出两阶段框架CaIRec。第一阶段结构插补校准（SIC）：从可用模态推断共享信息生成缺失模态表征，利用可观测的完整模态对进行结构正则化和对应监督，确保补全后的多模态表征保持一致的跨模态关系。第二阶段偏好导向表征校准（PRC）：构造伪缺失实例，将补全表征与在推荐排序空间中训练好的观测表征对齐，使补全信息能直接提升个性化排序。同时构建补全感知的物品图，整合补全的内容关系与协同过滤信号，用于图推荐聚合。

**结果**：在三个数据集上不同模态缺失比例下，CaIRec均优于现有方法，显著提升推荐准确性和鲁棒性。
