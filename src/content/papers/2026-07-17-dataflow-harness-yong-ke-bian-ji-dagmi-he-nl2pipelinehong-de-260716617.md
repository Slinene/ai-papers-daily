---
title: 'DataFlow-Harness: A Grounded Code-Agent Platform for Constructing Editable
  LLM Data Pipelines'
title_zh: DataFlow-Harness：用可编辑DAG弥合NL2Pipeline鸿沟的代码智能体平台
authors:
- Runming He
- Zhen Hao Wong
- Hao Liang
- Zimo Meng
- Chengyu Shen
- Xiaochen Ma
- Wentao Zhang
affiliations:
- Peking University
- Institute for Advanced Algorithms Research Shanghai
- Zhongguancun Academy
arxiv_id: '2607.16617'
url: https://arxiv.org/abs/2607.16617
pdf_url: https://arxiv.org/pdf/2607.16617
published: '2026-07-17'
collected: '2026-07-23'
category: Agent
direction: Agent辅助的代码生成与流水线构建
tags:
- LLM Agent
- Data Pipeline
- DAG
- MCP
- Workflow Synthesis
- Grounded Platform
one_liner: 通过类型化增量突变和MCP落地，引导LLM代理构建可持久编辑的数据流水线DAG，成本与延迟大幅降低。
practical_value: '- **流水线即DAG而非脚本**：推荐系统中的特征工程、模型训练、数据回流等流水线常以一次性脚本实现，维护成本高。借鉴DataFlow-Harness，可将LLM生成的流水线固化为可编辑、可复用的DAG，便于版本控制和协作。

  - **MCP结构化工具暴露**：Agent与平台交互时，通过MCP（Model Context Protocol）暴露算子注册、状态等，确保工具调用类型安全。电商Agent场景中，可类似将召回、排序、特征库等组件注册为MCP工具，让LLM可靠编排。

  - **增量突变降低生成风险**：直接生成完整脚本易出错，改为指导Agent进行类型化增量操作（添加/删除节点、连线），可提升流水线构建成功率。在复杂推荐流水线（多路召回、重排、实验配置）中，这种可控构建思路能减少调试成本。

  - **Skills编码隐性过程知识**：对于依赖领域经验的流水线步骤（如数据分桶、采样策略），可沉淀为Skills指导Agent，减少Prompt工程负担。电商搜索推荐中如索引构建、特征拼接等流程可借鉴。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：LLM编码代理虽能自动生成数据处理脚本，但脚本不能自动转化为持久、可编辑的平台组件，形成「NL2Pipeline」鸿沟。

**方法**：提出DataFlow-Harness平台，包含三部分：① **DataFlow-Skills** 将流程知识编码为过程指导，辅助LLM进行流水线构建；② **MCP层** 将算子注册表、当前流水线状态等以结构化协议暴露给Agent，实现落地约束下的安全操作；③ **DataFlow-WebUI** 同步对话式编写与可视化DAG编辑器。Agent通过**类型化增量突变**（增加节点、连接等）逐步构建平台原生DAG，而非生成整体脚本。

**结果**：在12任务数据工程基准上，端到端通过率达93.3%。相比Vanilla Claude Code，成本降低72.5%，生成延迟降低49.9%；与Context-Aware Claude Code相比，通过率仅低0.9个百分点，但成本再降42.8%。分析显示，Skills在依赖隐性过程知识的任务中价值最大。
