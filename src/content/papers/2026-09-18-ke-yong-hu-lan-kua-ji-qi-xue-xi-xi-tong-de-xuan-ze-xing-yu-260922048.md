---
title: 'Available Guardrails: Certifying Selective Prediction across ML Systems'
title_zh: 可用护栏：跨机器学习系统的选择性预测认证
authors:
- Parivesh Priye
- Yufeng Wang
- Haibin Ling
- Michael Chaykowsky
affiliations:
- Rivian and Volkswagen Group Technologies
- Stony Brook University
- Westlake University
arxiv_id: '2609.22048'
url: https://arxiv.org/abs/2609.22048
pdf_url: https://arxiv.org/pdf/2609.22048
published: '2026-09-18'
collected: '2026-09-21'
category: Eval
direction: 安全门认证可用性计算与分区规划
tags:
- Selective Prediction
- Certification
- Exact Binomial
- Dynamic Programming
- Calibration
- Deployment
one_liner: 将选择性预测认证可用性转化为可计算量，用动态规划优化分区，在安全、粒度和覆盖间达到权衡
practical_value: '- 在电商/Agent 安全门（工具调用、自动拦截、推荐展示）中，按业务单元认证目标精度时，用精确二项反演快速判断每个单元是否有足够样本；对长尾单元提前规划数据采集或流量分配，避免无法认证。

  - 借鉴动态规划分区：当需要按类目/用户层/策略标签认证时，合并相邻小流量单元形成分区，可在保持整体安全认证的同时最大化服务流量；用两个数据划分（规划/选择）减少过拟合。

  - 错误预算重分配：不同业务单元风险容忍不同，非均匀分配家族错误预算可放松部分单元精度要求，提升整体覆盖率；在线上可对高频低风险单元采用较松门限。

  - 注意人口机会与有限样本差距巨大（0.157 vs 0.005），认证流程设计不能只依赖朴素估计，需显式考虑样本量或采用稳健选择策略。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：选择性预测器作为安全门，只在高置信度时输出，部署要求按报告单元（工具、策略标签、患者子群）认证目标精度。难点不在证书有效性，而在于有限校准数据是否足以产生证书。

**方法关键点**：基于精确二项反演计算认证可用性；将报告分区选择（固定组序）形式化为动态规划，揭示安全性、粒度和服务流量间的权衡前沿；提出规划/选择两阶段策略构造并选择候选分区；提出重分配家族错误预算的杠杆。

**关键结果数字**：人口真实规划相比支持平衡提升平均覆盖率 0.157，但朴素估计仅恢复 0.005，表明有限样本是核心挑战；规划/选择策略恢复 0.060，方向在 3 个意图路由数据集、两种架构共 60 个模型效应中 59 个复现；错误预算重分配进一步恢复覆盖率。前沿在 LLM 工具调用、内容审核、病变分类和推荐中重现。
