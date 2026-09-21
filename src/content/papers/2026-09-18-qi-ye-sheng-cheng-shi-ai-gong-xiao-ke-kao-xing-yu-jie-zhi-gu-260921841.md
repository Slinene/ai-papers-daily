---
title: 'EnterpriseVal: Quantifying the Efficacy, Reliability and Value of Generative
  AI in the Enterprise'
title_zh: 企业生成式 AI 功效、可靠性与价值量化评估系统
authors:
- Abbas Raza Ali
- Muhammad Ajmal Siddiqui
- Moona Zahid
arxiv_id: '2609.21841'
url: https://arxiv.org/abs/2609.21841
pdf_url: https://arxiv.org/pdf/2609.21841
published: '2026-09-18'
collected: '2026-09-21'
category: Eval
direction: 企业 GenAI 用例级评估与门控
tags:
- LLM Evaluation
- Enterprise AI
- Prediction-Powered Inference
- Value Model
- Reliability
- Agentic Workflows
one_liner: 提出企业级 GenAI 用例评估系统，融合度量目录、校准 LLM-as-judge、阈值门与价值风险模型，并在银行试点验证
practical_value: '- 可借鉴其用例级评估门控：把度量向量（保真度、效用、效率、可靠性、保证、监督）和置信区间映射到 REJECT/CONDITIONAL/SCALE，适合电商推荐中
  LLM 生成文案、推荐理由或 Agent 流程的灰盒评估。

  - 用 prediction-powered inference 校准 LLM-as-judge 评分，降低人工盲评成本，同时保证统计可靠性；可直接用于商品文案改写、搜索摘要等生成模块的持续质量监控。

  - 按 autonomy level（自动化程度）与 consequence tier（后果等级）设定评估强度，为不同风险场景（如支付、金融推荐）分级投入评估资源，避免过度或不足测试。

  - 价值风险模型中把 reviewer catch rate 作为可测参数，量化人审在环路中的检出率与成本，有助于计算生成式推荐/Agent 项目的实际 ROI
  和扩量决策。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

## 动机
企业 GenAI 项目大多失败，主要原因是测量问题：公共基准只回答“模型能做什么”，而部署决策需要回答“该工作流在特定数据、控制条件下是否适配、可靠、安全且值得扩量”。

## 方法关键点
提出 EnterpriseVal 评估系统，包含五个组件：
1. **用例规范**：形式化描述用例及冻结的社会技术配置（模型、prompt、检索、工具、护栏、人审），通过 autonomy level 与 consequence tier 决定评估强度。
2. **度量目录**：覆盖 fidelity、utility、efficiency、reliability、assurance、oversight 六个维度。
3. **分级协议**：用 prediction-powered inference 校准 LLM-as-judge，低成本扩展盲评专家判断。
4. **两层阈值门**：可执行算法，将度量向量与置信区间映射为 REJECT / CONDITIONAL / SCALE 决策。
5. **价值风险模型**：将 reviewer catch rate 作为实测参数，量化人审在环路中的风险与成本。

## 关键结果
全球银行三项工作流试点：
- 信用备忘录起草：最佳模型人工评估 citation precision 达到 88%，幻觉率 1.6%，优于 70% / 5% 的门限。
- 程序转换：分析师精炼时间从约 27.4 小时/文档降至 2.9 小时/文档。
论文明确区分已确立结果、试点证据、提议系统与开放假设，并列出完全验证所需实验。
