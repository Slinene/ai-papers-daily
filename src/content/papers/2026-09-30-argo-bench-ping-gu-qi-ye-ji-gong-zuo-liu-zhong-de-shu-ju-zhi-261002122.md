---
title: 'Argo-Bench: Evaluating Data Agents on Enterprise-Scale Workflows'
title_zh: Argo-Bench：评估企业级工作流中的数据智能体
authors:
- Gabriel Tomitsuka
- Arman Raayatsanati
- Emma Xing
- Duke Gand
- Joseph J Ma
affiliations:
- TextQL
arxiv_id: '2610.02122'
url: https://arxiv.org/abs/2610.02122
pdf_url: https://arxiv.org/pdf/2610.02122
published: '2026-09-30'
collected: '2026-10-03'
category: Eval
direction: 数据智能体评估 · 企业级数据工作流
tags:
- Data Agents
- Benchmark
- Enterprise Workflows
- Text-to-SQL
- Simulation
- LLM Evaluation
one_liner: 构建企业级数据智能体评估基准，模拟纽约外卖平台，要求跨235表分析并采取行动，最强模型均分仅59.5
practical_value: '- 评估 Agent 时不要只看 SQL 正确率，可以引入“动作后果评分”：在电商/推荐场景中构造仿真环境（如用户响应模型、市场模拟器）对调价、选品、发券等决策进行闭环评估

  - 复杂 schema 导航是实际瓶颈：可构建内部数据仓库查询基准，覆盖多表 join 和业务语义，并用可执行参考解保证可解性，避免错误答案误导模型评估

  - 最强模型在长链路、多表、需行动的任务上平均分仍低，说明工程上需要为 Agent 增加 schema 检索、知识图谱、规划模块或领域微调，而非仅依赖 prompt

  - 参考解设计可迁移：为每个任务提供端到端可执行方案，便于诊断 Agent 失败在导航、SQL、分析还是行动阶段，支撑针对性优化'
score: 7
source: huggingface-daily
depth: abstract
---

## 动机
现有 text-to-SQL 基准只评估查询生成，答案常错；真实企业仓库敏感不可公开，公共数据集业务事件常单表可容纳，无法覆盖跨数十表、需要统计分析并采取行动的真实工作流。

## 方法关键点
- 构建模拟纽约外卖平台：基于公共数据、行业文献和监管文件，模拟 2024 年 8100 万订单，包含经济学、欺诈模式与市场激励
- 导出为 235 张表、75 亿行的 ERP 仓库，schema 参照 Oracle E-Business Suite；模拟器 ground-truth 状态对 agent 不可见，必须通过探索仓库重建事实
- 任务不只 text-to-SQL：agent 需提交行动（封禁欺诈账户、分配骑手激励预算、补发工资），评分基于行动在模拟器中的后果
- 210 个任务，每个都有可执行参考解，证明仅凭仓库即可解决

## 关键结果
在 14 个前沿与开源模型中，最强模型仅在 34.8% 的任务上得分 ≥95，平均分 59.5，说明当前模型在企业级数据 agent 任务上仍有显著差距。
