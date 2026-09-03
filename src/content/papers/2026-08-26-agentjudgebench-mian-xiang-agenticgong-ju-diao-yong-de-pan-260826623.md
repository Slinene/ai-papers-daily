---
title: 'AgentJudgeBench: A Multi-Difficulty Benchmark for Evaluating LLM Judges on
  Agentic Tool-Calling'
title_zh: AgentJudgeBench：面向Agentic工具调用的LLM评判器多难度基准
authors:
- Abhigya Verma
- Amit Kumar Saha
- Seganrasan Subramanian
- Sai Harshitha Aluru
affiliations:
- ServiceNow AI
arxiv_id: '2608.26623'
url: https://arxiv.org/abs/2608.26623
pdf_url: https://arxiv.org/pdf/2608.26623
published: '2026-08-26'
collected: '2026-09-03'
category: Eval
direction: Agentic Tool-Calling 评测 · LLM-as-a-Judge
tags:
- LLM-as-a-Judge
- Agentic Tool-Calling
- Benchmark
- DAG Workflows
- Evaluation Reliability
one_liner: 首个系统性评估LLM评判器在依赖型Agentic工具调用工作流上的可靠性基准，揭示无真值时所有评判器收敛于77-82%的结构性天花板
practical_value: '- 在电商/广告的 Agentic 工作流评测中，若缺乏 ground truth，多个 LLM judges 对困难任务的打分可能收敛到同一窄带（77-82%），区分度不足；建议对关键路径使用
  programmatic reference 或人工标注作为主评测，LLM judge 仅作为辅助。

  - 结构化 evaluation rubric 可提升对齐最高 6.5 pp，但效果随 judge-generator 组合波动；落地前需用小规模标注集对 rubric
  做 pair-wise 校准，不要直接套用通用模板。

  - CoT 和温度对 judge 对齐几乎无影响，生产环境可省去这两项调参，把算力投入到更细粒度的 rubric 或真实依赖建模。

  - 提供 ground truth 并不总是好事：GPT-5.4 和 Gemini-2.5-Pro 在有真值时对齐下降，存在 over-anchoring；建议评估时对强模型采用“先独立评分，再给参考”的流程，或显式要求忽略
  anchor。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM judges 广泛用于评估 agentic tool-calling 系统，但其在结构化、依赖驱动工作流上的可靠性未被系统检验。

**方法关键点**：构建 AgentJudgeBench，包含 3,808 实例、6 种 DAG 拓扑、3 个难度层级；5 个生成器（3B-70B 开源与 GPT-5.4）和 6 个 judges（20B 到 frontier）在有/无 ground truth 两种条件下，对比 judge 与 programmatic reference 及人类标注的对齐。

**关键结果**：对齐随难度单调下降，无 ground truth 时下降快 1.5 倍；hard queries 无 ground truth 时所有 judges 收敛到 77-82% 窄带，表现为结构性天花板，模型规模无法突破。Ground truth 暴露非均匀有益：GPT-5.4 下降 1.5 pp，Gemini-2.5-Pro 下降 3.9 pp，存在 over-anchoring。CoT 和温度几乎无效；结构化 rubric 提升最高 6.5 pp但泛化不一致。有 ground truth 时 QwQ-32B 最匹配 programmatic reference，人类验证发现 GPT-OSS-120B 最符合人类；无 ground truth 时 frontier 只在共享天花板内略微领先。
