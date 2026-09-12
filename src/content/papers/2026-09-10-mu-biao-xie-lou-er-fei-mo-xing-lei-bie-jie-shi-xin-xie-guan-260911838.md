---
title: 'Target leakage, not model class, explains reported accuracy in survey-based
  cardiovascular screening: a leakage-tiered audit of glass-box and tabular foundation
  models'
title_zh: 目标泄漏而非模型类别解释心血管筛查报告准确率：玻璃盒与表格基础模型泄漏分层审计
authors:
- Raad Bin Tareaf
- Murad Al-Rajab
- Samia Loucif
- Samer Ellaham
- Cedric Schmitz
affiliations:
- Data Science and AI Cluster, XU Exponential University of Applied Sciences, Potsdam,
  Germany
- German University of Digital Science, Potsdam, Germany
- College of Engineering, Abu Dhabi University, Abu Dhabi, United Arab Emirates
- College of Technological Innovation, Zayed University, Abu Dhabi, United Arab Emirates
- Cleveland Clinic Hospital, Abu Dhabi, United Arab Emirates
arxiv_id: '2609.11838'
url: https://arxiv.org/abs/2609.11838
pdf_url: https://arxiv.org/pdf/2609.11838
published: '2026-09-10'
collected: '2026-09-12'
category: Eval
direction: 表格模型评估与目标泄漏审计
tags:
- target leakage
- tabular foundation models
- glass-box models
- conformal prediction
- fairness audit
- model evaluation
one_liner: 十个分类器在44万样本审计显示，移除两个诊断后特征使所有模型AUROC下降约0.05并收敛至0.0045带宽，性能差距来自特征泄漏而非模型架构
practical_value: '- 建立泄漏分层特征审计：把与标签有因果/后诊断关系的特征按泄漏风险分层，观察移除后所有模型 AUC 的同步下降，电商推荐里类似“用户已加购/购买后的行为特征”会带来虚假
  recall，需要消融区分特征贡献与模型能力。

  - 玻璃盒模型（EBM）在表格任务上精度可非劣于复杂模型且推理快约两个数量级，适合线上排序/召回候选生成中低延迟且可解释的模块，不必为微小 AUROC 提升引入大模型。

  - 部署前用冻结阈值跨时间/跨人群验证：推荐/广告模型在增量训练前先在下一时段数据上做 transport 检查，避免只看离线 AUC；对性别/年龄等分人群使用
  Mondrian conformal 或分组校准修复覆盖率差异。

  - 阈值公平性要在固定业务阈值下审计，而非只看全局 AUC；排序/推荐里对曝光阈值、推送文案的覆盖差异做 subgroup 召回/精确率检查，利用可解释模型的
  shape function 编辑实现可审计修复。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：基于全国健康调查的心血管筛查模型普遍报告 AUROC 约 0.89，怀疑来自目标泄漏而非模型学习能力；同时评估表格基础模型是否带来真实提升，以及部署所需属性能否联合满足。

**方法关键点**：使用 2022 BRFSS 442,067 名受访者，在五个泄漏风险递减的特征层级上，对比 10 个分类器（线性、树集成、神经、玻璃盒、表格基础），固定阈值审计区分度、校准、公平性、共形覆盖率、解释忠实度与推理成本；在 2023 年 430,755 名受访者上检验模型与阈值冻结后的迁移稳定性。

**关键结果**：移除两个诊断后特征使所有模型 AUROC 下降 0.049–0.051，模型间差异收窄至 0.0045 带宽；EBM 在预设 0.005 非劣边界内不输所有替代模型，推理速度比最强基础模型快约 100 倍。固定阈值对女性心梗检测率 75.4%，男性 89.0%；编辑 shape functions 后差距缩小至 0.010。边际共形预测对男性覆盖率 0.86、对 60 岁以上 0.82；Mondrian 校准修复所有分层。冻结模型跨年迁移 AUROC 偏差在 0.002 内。

结论：该文献中报告的模型性能空间来自特征集而非学习器；透明性不带来可测精度代价，并使公平修复与不确定性条件直接可审计。评估实践是瓶颈。
