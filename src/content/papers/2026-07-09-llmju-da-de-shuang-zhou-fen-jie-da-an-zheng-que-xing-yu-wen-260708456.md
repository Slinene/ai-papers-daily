---
title: 'Two Axes of LLM Abstention: Answer Correctness and Question Answerability'
title_zh: LLM拒答的双轴分解：答案正确性与问题可回答性
authors:
- Benedikt J. Wagner
affiliations:
- City St George’s, University of London
arxiv_id: '2607.08456'
url: https://arxiv.org/abs/2607.08456
pdf_url: https://arxiv.org/pdf/2607.08456
published: '2026-07-09'
collected: '2026-07-10'
category: LLM
direction: LLM选择性回答的双轴风险控制
tags:
- abstention
- answerability
- hidden state probes
- confidence calibration
- risk control
one_liner: 揭示LLM拒答中答案正确性和问题可回答性是两个独立维度，提出用隐藏探针和双阈值策略分别控制风险
practical_value: '- 在拒答模块中分离“答案正确性”与“问题可回答性”两个信号，而非共享单一置信度；可对隐藏状态训练线性探针检测不可回答问题（AUROC>0.69），作为路由组件前置过滤不应答查询。

  - 避免直接使用LLM自我前提检查，其错误挑战率高达57%；改用探针先筛选可疑问题再执行检查，可三倍提升挑战精度，适合电商Agent中拒答虚假前提提问（如“这款已下架商品为何涨价？”）。

  - 采用双阈值校准框架：为错误回答率和不可回答回答率设定独立预算，在独立验证集上计算二项式界获得统计保障，满足业务风险可控要求（如信贷推荐咨询的准确性和合规拒答）。

  - 模型内部可回答性表示随规模稳定，但输出置信度不反映，因此不必依赖模型自评；可将探针部署为轻量级可插拔组件，适配多模型。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM通常用单一置信度阈值决定是否拒答，但混淆了两种失败模式：回答错误和回答不该答的问题（如无法回答、含错误前提）。需要区分并分别控制。

**方法**：在5个模型上，分析正确可回答(C)、错误可回答(W)、不可回答(U)问题在决策空间中的几何。训练线性探针从隐藏状态读取可回答性，与输出置信度对比。在自然错误前提集CREPE上测试。提出探针路由的修复方案，并设计双阈值认证策略：用可回答性分数和正确性分数分别控制两类风险，在独立验证集上用二项式界保证。

**结果**：输出置信度对可回答性AUROC仅0.54-0.67（无规模趋势），隐藏探针达0.97-0.99；在CREPE上探针达0.69-0.77，而P(IK)等接近随机。提示检查前提导致57%错误挑战，探针路由后精度提升3倍。双阈值策略在8B模型上以0.75覆盖率同时认证两个预算（单阈值仅0.31），14B上为唯一认证策略。
