---
title: 'ForestHG-Trace: Traceable Long-Horizon Ecological Reasoning over Large-Scale
  Forest Scenes'
title_zh: ForestHG-Trace：大规模森林场景中可追踪的长期生态推理框架
authors:
- Zihang Cheng
- Duanchu Wang
- Cheng Li
- Jing Huang
- Huanzhao Fu
- Di Wang
affiliations:
- Xi'an Jiaotong University
- Xidian University
- Zhejiang University
arxiv_id: '2605.27590'
url: https://arxiv.org/abs/2605.27590
pdf_url: https://arxiv.org/pdf/2605.27590
published: '2026-05-26'
collected: '2026-05-31'
category: Agent
direction: Agent 长期推理 · 工具增强 · 可审计执行
tags:
- Remote Sensing QA
- Agent
- Tool-Augmented
- Hypergraph
- Traceable Reasoning
- Benchmark
one_liner: 用生态超图和工具增强的 LLM Agent 实现可审计的长期推理，将问答转化为可执行分析流程
practical_value: '- **工具化推理链可移植至电商分析 Agent**：将复杂查询拆解为过滤、聚合、比较等确定性原子工具，每条操作可追踪和审计，适用于竞品分析、用户行为归因等场景。

  - **超图表示捕获高阶关系**：使用超图建模实体间的多边交互（如用户会话超图、商品共现超图），比场景图更能表达复杂的生态或业务结构，可提升 Agent 对上下文的推理精度。

  - **执行深度是长链推理的核心瓶颈**：论文指出多步工具调用的深度显著影响成功率，提示在 Agent 工程中需重点优化长链规划、中间状态管理和错误恢复。

  - **构建可执行的评估基准**：为 Agent 推理任务设计带有中间步骤验证的 Benchmark（如 ForestTraceQA），可借鉴到电商领域构造复杂查询的审计型评测集，推动模型从端到端预测转向可验证执行。'
score: 7
source: arxiv-cs.MM
depth: abstract
---

**动机**：遥感问答常被简化为视觉语义预测，但生态分析需要多步过滤、数值聚合、邻域推理和可验证证据，现有方法缺乏结构化、可追踪的执行机制。  
**方法**：提出 ForestHG-Trace，用生态超图表示森林场景，将树木实例、空间单元、语义群组和邻域关系编码为高阶结构化实体，支持超越成对场景图的交互。在此之上，LLM 引导的 Agent 调用六类确定性工具（读取、过滤、扩展、聚合、比较、审计），生成可重放的执行轨迹和紧凑的证据记录，实现从直接答案预测向可审计分析流程的转变。同时构建 ForestTraceQA 基准，涵盖结构分析、种群统计和空间关系等任务，要求模型执行长期分析程序。  
**结果**：ForestHG-Trace 在答案准确率和执行忠实度上显著优于单步基线和场景图 Agent，并揭示执行深度是长期生态问答的主要瓶颈，为多模态 Agent 的可执行环境分析提供了标准化平台。
