---
title: 'BALMS: Benchmarking Agentic LLMs for Longitudinal Mental Health Sensing'
title_zh: BALMS：长期心理健康感知的智能体 LLM 基准测试
authors:
- Yu Yvonne Wu
- Arvind Pillai
- Yuliang Chen
- Yuwei Zhang
- Sudarshan Regmi
- Tess Z. Griffin
- Michael V. Heinz
- Lisa A. Marsch
- Nicholas C. Jacobson
- Andrew Campbell
affiliations:
- Dartmouth College
- University of Cambridge
arxiv_id: '2608.27219'
url: https://arxiv.org/abs/2608.27219
pdf_url: https://arxiv.org/pdf/2608.27219
published: '2026-08-27'
collected: '2026-08-30'
category: Agent
direction: LLM Agent 在纵向时序健康感知的评测
tags:
- Agentic Benchmark
- Longitudinal Sensing
- LLM-as-Judge
- CoT
- Time-series Reasoning
- Mental Health
one_liner: 首个系统性基准，评估 LLM Agent 从长期可穿戴信号预测心理健康得分并生成有理据解释的能力
practical_value: '- 在电商/推荐场景，用户行为序列同样长且稀疏，零样本 LLM 直接预测数值型指标（如 CTR、GMV、复购率）可能不如简单均值或周期基线；上线前必须用域内基线严格对比，避免高估
  LLM 能力。

  - 将原始时间序列压缩为紧凑的语义化特征（如“活跃度”“睡眠质量”）能显著提升 LLM Agent 的推理效果，同时降低上下文长度；可借鉴到用户行为序列的语义摘要，再交给
  LLM 做归因或策略生成。

  - CoT 对推理型骨干有增益，但不保证时间定位和数值正确性；在 Agent 设计中应加入强制检索步骤、外部工具校验或硬约束，而非仅依赖模型自我解释。

  - LLM-as-Judge 可用于自动评估生成式解释的质量，但需将其与数值预测准确率解耦，因为 LLM 可能对流畅但事实错误的 rationale 给出高分；建立多维评估体系可迁移到推荐解释、诊断报告等场景。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

动机：传统心理健康评估依赖稀疏的自陈量表，可穿戴设备提供了连续行为/生理信号，但现有 LLM Agent 只做短期检索查询（如“上周最高步数”），缺乏对长期信号进行健康评分预测和证据支撑推理的系统评估。

方法关键点：BALMS 覆盖 3 个真实纵向数据集，设计 2 类任务——封闭式健康评分预测和由 LLM-as-Judge 自动评分的 rationale 生成；评估 3 种 Agent 范式（零样本、CoT、带检索/记忆的变体）在 5 个开源/闭源 LLM 骨干上的表现。

关键结果：零样本 Agent 很少超过简单均值基线，仅在使用更强骨干或紧凑语义特征时才勉强超越；CoT 对推理型骨干有提升，但不保证时间 grounding 和数值正确性。效率和时序缩放分析进一步表明，现有 Agent 缺少选择性历史检索、时间证据锚定和对可解释行为特征的推理能力。
