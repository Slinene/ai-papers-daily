---
title: 'Beyond Static Leaderboards: Predictive Validity for the Evaluation of LLM
  Agents'
title_zh: 超越静态排行榜：面向 LLM Agent 的预测效度评估
authors:
- Dhaval C. Patel
- Kaoutar El Maghraoui
- Shuxin Lin
- Yusheng Li
- Tianjun Feng
- Chun-Yi Tsai
- Yihan Sun
- Wei Alexander Xin
- Akshat Bhandari
- Tanisha Rathod
affiliations:
- IBM
arxiv_id: '2606.19704'
url: https://arxiv.org/abs/2606.19704
pdf_url: https://arxiv.org/pdf/2606.19704
published: '2026-06-17'
collected: '2026-06-19'
category: Agent
direction: Agent 评估基准与方法论
tags:
- Agent Evaluation
- Benchmark
- Predictive Validity
- OOD
- Leaderboard
- MCP
one_liner: 揭示聚合排行榜在分布外环境下排名不稳定，提出以预测效度替代平均分评估 Agent 配置
practical_value: '- **评估构建警惕排行榜过拟合**：在构建内部 Agent 评估集时，不要过分追求固定基准上的平均分提升；需检验在业务分布变化（如季节、新物品）下的排名稳定性，可借鉴论文的预测效度指标。

  - **多维度测量取代单一分数**：可参照提出十二层测量装置，覆盖推理、检索、编排等维度，设计针对电商搜索推荐 Agent 的细粒度诊断，避免重要维度被聚合分数掩盖。

  - **分布外实验纳入评估流水线**：将 OOD 测试作为 Agent 上线前的必要检查，设定可证伪阈值，防止仅在历史数据拟合上优异、线上失效。

  - **预注册实验设计提升评估可信度**：在关键 Agent 选型中，预先固定评估方案和成功标准，避免事后解释偏差，增强决策说服力。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有 LLM Agent 基准各自仅覆盖少数维度，聚合分数排行榜在分布外环境下排名极不稳定，无法指导真实部署。

**方法**：本文通过一次大规模工业 Agent 基准的 14 项并行实现研究（覆盖多模态、编排、检索、推理、基础设施等变体），结合 7 个已有基准，实证展示排名随分布变化而翻转。提出用**预测效度**（样本内排名与样本外排名的相关性）替代平均分作为评估准则，并设计了一套十二层测量装置，解耦 HELM 等评测框架所折叠的部署相关维度。此外，设定了三个可证伪的 OOD 标准及显式阈值，以操作化该评估立场。

**结果**：现有证据部分支持该评估框架，但尚不充分；本文最终提出一个预注册的试点设计，并展望下一代 Agent 基准应报告的内容。
