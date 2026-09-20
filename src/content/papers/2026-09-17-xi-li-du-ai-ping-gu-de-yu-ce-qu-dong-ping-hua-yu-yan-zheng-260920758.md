---
title: Prediction-Powered Smoothing and Validation for Disaggregated AI Evaluation
title_zh: 细粒度 AI 评估的预测驱动平滑与验证
authors:
- Sho Kawano
- Zehang Richard Li
- Paul A. Parker
affiliations:
- Department of Statistics, University of California, Santa Cruz
arxiv_id: '2609.20758'
url: https://arxiv.org/abs/2609.20758
pdf_url: https://arxiv.org/pdf/2609.20758
published: '2026-09-17'
collected: '2026-09-20'
category: Eval
direction: AI 评估 · 小域估计与预测驱动推断
tags:
- disaggregated evaluation
- prediction-powered inference
- small area estimation
- Bayesian smoothing
- cross-validation
- LLM evaluation
one_liner: 用预测驱动推断与贝叶斯小域平滑，改善稀疏分群上的 AI 系统点估计、区间估计与估计量选择
practical_value: '- 当按类目、流量入口、用户分群评估推荐或 Agent 指标时，小分群标签极少：可先对每个分群算 prediction-powered
  estimate，再用贝叶斯模型做平滑；如果有类目树或场景层级，用 PP-TS 跨层级借力，能获得更稳的区间估计。

  - 已有 LLM judge 或自动打分器覆盖全量评估样本时，把它作为预测信号，只对少量样本做人工标注，能显著降低分群指标的方差；适合电商 Agent 多场景、多类目评估。

  - 在 direct、PPI、smoothed 等多个候选 estimator 之间做选择时，可以用文中的 design-based CV score 替代单独留出
  validation set，节省标注预算，且能更准确估计所选 estimator 的误差。

  - 应用时注意其假设评估集是有限总体且抽样设计已知；实际可适配分层抽样或 uniform sampling。若预测模型与标签存在系统性偏差，需检查 interval
  coverage，不要盲目信任 smoothed 点估计。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：AI/LLM 系统需要按任务域、用户分群或产品线做细粒度评估，但标注成本高、各域样本不均衡；直接使用各域自身标签的估计量（包括 prediction-powered inference, PPI）在标签较少时精度不足。

**方法**：把评估集视为有限总体，提出两类估计量：prediction-powered smoothing (PP-S) 先得到每个域的 prediction-powered estimate，再用贝叶斯模型平滑，利用模型预测结果降低方差；扩展 PP-TS 可跨 reporting taxonomy 借力。验证方面，提出近似无偏的 design-based cross-validation score，用于在 direct 与 smoothed estimators 之间选择，避免依赖额外验证样本。

**结果**：在一个可验证评分的 benchmark 和一个人工评分的 deployed agent traffic 数据集上，所提估计量在点估计和区间估计上均优于 direct estimators，覆盖率接近 nominal；在相同采样预算下，该 score 的选择效果与独立验证集相当，并且能更准确地估计所选估计量的误差。
