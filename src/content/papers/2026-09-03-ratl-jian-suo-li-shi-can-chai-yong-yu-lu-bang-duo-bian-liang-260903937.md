---
title: 'RATL: Learning from Retrieved Residuals for Robust Multivariate Time-Series
  Forecasting'
title_zh: RATL：检索历史残差用于鲁棒多变量时间序列预测
authors:
- Yuchen He
- Yueyang Cang
- Zhiyuan Ning
- Ningyu Wang
- Li Shi
affiliations:
- Department of Automation, Tsinghua University
- State Key Laboratory of Hydroscience and Engineering, Tsinghua University
arxiv_id: '2609.03937'
url: https://arxiv.org/abs/2609.03937
pdf_url: https://arxiv.org/pdf/2609.03937
published: '2026-09-03'
collected: '2026-09-06'
category: RAG
direction: 检索增强 · 残差反馈修正
tags:
- Retrieval-Augmented
- Residual Correction
- Time-Series Forecasting
- Multivariate
- iTransformer
one_liner: 将 RAG 思想用于连续预测：冻结基座模型，检索相似历史残差并路由融合以纠偏
practical_value: '- 电商销量/流量/广告消耗等多变量预测场景，可维护基座模型的历史残差记忆库，上线后检索相似上下文残差做轻量级后处理纠偏，无需重训基座。

  - 冻结已部署的预测模型，只额外训练残差检索与融合模块，降低迭代成本与上线风险，适合工程化快速验证。

  - 利用验证集自动选择 correction strength 控制残差注入幅度，防止过度修正导致线上指标波动，该机制可迁移到任何 additive correction
  的预估模型。

  - set-aware router 按 forecast block 和 variable 维度选择残差，可借鉴到多指标联合预测（如 GMV、订单量、转化率），让不同指标学习不同的融合权重。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：RAG 在生成任务中有效，但直接检索目标值用于连续回归不鲁棒——样本间输出水平、数值尺度、局部动态差异大；传统预测流程只用残差做模型优化和误差诊断，没有保留历史残差作为推理时可访问的记忆。

**方法关键点**：RATL 冻结基座预测器，利用基座模型构造检索键，将其历史预测残差转化为 train-only memory；推理时按因果可用性约束检索相似上下文的残差轨迹，再用 set-aware router 在 forecast block 和 variable 维度上选择并组合这些残差；通过验证集选择 correction strength 限制残差过度注入。

**关键结果**：在真实基准上以 iTransformer 为主冻结基座，RATL 在大多数设置下提升性能；消融表明 learned routing 强化原始残差反馈，validation-based strength selection 有效防止过度修正；跨 backbone 迁移实验显示方法具备通用性。
