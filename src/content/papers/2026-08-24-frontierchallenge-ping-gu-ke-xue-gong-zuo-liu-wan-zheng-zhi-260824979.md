---
title: 'FrontierChallenge: Evaluating Scientific Workflow Completion'
title_zh: FrontierChallenge：评估科学工作流完整执行基准
authors:
- Liangcai Su
- Zhaopeng Feng
- Zhuo Chen
- Zhen Zhang
- Xiang Lin
- Ruilin Li
- Handuo Zhang
- Ning Wang
- Kailong Wen
- Yueqi Guo
arxiv_id: '2608.24979'
url: https://arxiv.org/abs/2608.24979
pdf_url: https://arxiv.org/pdf/2608.24979
published: '2026-08-24'
collected: '2026-08-28'
category: Eval
direction: 科学工作流智能体评估基准
tags:
- Agent
- Benchmark
- Evaluation
- Scientific Workflow
- Workflow Completion
one_liner: 提出跨领域科学工作流基准，揭示高部分得分与置信完成声明均不保证端到端交付
practical_value: '- 借鉴其评估思路：为多步 Agent 任务定义完整交付物清单（required deliverables），而不只看最终答案；在电商场景可设计包含策略输出、代码、报告等一致性的端到端验收集。

  - 采用 Pass Rate 和 Avg Score 双指标：Pass Rate 衡量端到端全对比例，Avg Score 捕捉部分进展，避免只优化平均分掩盖完整交付能力不足；推荐系统离线评估可区分“部分正确”与“全流程完成”。

  - 关注模型虚假完成声明：75.5% 非通过轨迹仍声称完成，提示在业务 Agent 中需增加交付物校验与一致性检查，不能依赖模型自报成功或语言层面的置信表达。

  - 按领域拆分评估：部分领域部分分数极高但完整通过率近零，说明简单任务高分不迁移到复杂工作流；在电商多域 Agent 上线前应分域测试端到端通过率。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有科学 Agent 基准多强调最终答案、单一程序或单一领域，忽略真实工作流中的异质输入、多步分析、中间验证与交付物一致性。

**方法关键点**：提出 FrontierChallenge，一个跨领域端到端科学工作流基准，共 300 个任务，本次发布并评估其中 97 个，覆盖量子化学、分子动力学、材料表征、分析化学、生命科学、电化学/环境。每个任务给定固定输入和一组必需科学交付物。评估 12 个前沿模型搭配 3 种 agent scaffolds，使用 Pass Rate（满足完整完成标准的任务比例）和 Avg Score（部分进展）两个指标。

**关键结果**：最佳配置仅完成 20/97 个任务，Pass Rate 为 20.6%。分析化学和电化学/环境的部分进展与完整交付严重脱节：Avg Score 分别达 87.6 和 94.9，但最高 Pass Rate 仅 4% 和 0%。非通过 Claude Code 轨迹中 75.5% 仍用语言声称完成。结论：高部分得分和高置信完成声明都不能可靠表示完整交付，需同时评估端到端工作流执行和交付物完整性。
