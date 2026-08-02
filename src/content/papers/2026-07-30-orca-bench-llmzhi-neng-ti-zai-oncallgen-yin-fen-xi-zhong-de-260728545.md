---
title: 'ORCA-bench: How Ready Are Language Model Agents for Oncall?'
title_zh: ORCA-bench：LLM智能体在oncall根因分析中的准备度评估
authors:
- Albert Gong
- Kyuseong Choi
- Abhineet Agarwal
- Jason Schechner
- Ryan Huang
- Raj Agrawal
- Anish Agarwal
- Raaz Dwivedi
affiliations:
- Cornell Tech
- Traversal
- Columbia University
arxiv_id: '2607.28545'
url: https://arxiv.org/abs/2607.28545
pdf_url: https://arxiv.org/pdf/2607.28545
published: '2026-07-30'
collected: '2026-08-02'
category: Agent
direction: Agent 根因分析基准评估
tags:
- Agent
- RCA
- Benchmark
- Hallucination
- Telemetry
- Root Cause Analysis
one_liner: 在真实微服务系统中评估LLM Agent的根因分析能力，最佳准确率仅25.3%，暴露严重幻觉与代码依赖
practical_value: '- 构建推荐系统智能运维Agent时，需警惕幻觉风险：即使最强模型在部分任务中也给出完全无关根因，可借鉴其幻觉率指标与人工评审机制

  - 源端可观测性（指标、日志、追踪）完整性与代码访问权至关重要：移除源码访问会全面降低Agent表现，建议在推荐系统线上故障排查Agent中强制集成代码检索工具

  - 任务难度分级方法可复用：根据报告特异性、检测延迟、并发故障等维度系统构造评测集，用于评估电商搜索推荐场景下的异常检测Agent

  - LLM-as-judge与专家对齐（Cohen’s κ_w=0.90）的验证流程，可直接用于生产环境中Agent输出的自动化评估，减少人工审核成本'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM能写代码、修Bug，但oncall根因分析（RCA）要求从模糊用户报告出发，在数小时延迟后结合噪声指标、日志、追踪与源码进行推理，现有Agent能力未知。

**方法**：构建ORCA-bench，一个生产级微服务系统（OpenTelemetry仪表化，暴露6天Prometheus/Jaeger/OpenSearch数据），设计1079个RCA任务，系统变化报告特异性、故障发现延迟和并发故障场景。由SRE标注真实症状，LLM-as-judge评分经人工独立重评（Cohen’s κ_w=0.90）。评估5个前沿Agent（Claude Opus 4.7、Sonnet 4.6、GPT-5.5、GLM-5、DeepSeek-V4-Pro）。

**关键结果**：中等难度任务（真实输入设定）最佳RCA准确率仅25.3%，困难任务10.0%；最弱模型在40%的事故报告中生成完全无关的根因；移除源码访问权限后所有指标下降。表明即使在精心策划的50GB/6天测试床中，Agent表现也严重不足，真实系统规模更大、更动态，差距为下限。
