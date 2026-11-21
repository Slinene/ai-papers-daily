---
title: 'SheetAlign: Grounded Interaction and Stage-Isolated Learning for Spreadsheet
  Agents'
title_zh: SheetAlign：电子表格代理的接地交互与分阶段策略学习
authors:
- Yuxiang Wang
- Junhao Gan
- Jianzhong Qi
affiliations:
- The University of Melbourne
arxiv_id: '2611.26069'
url: https://arxiv.org/abs/2611.26069
pdf_url: https://arxiv.org/pdf/2611.26069
published: '2026-11-19'
collected: '2026-11-21'
category: Agent
direction: Agent 电子表格操作策略学习
tags:
- Agent
- LLM
- Spreadsheet
- Grounded Interaction
- Stage-Isolated Learning
- Execution Consistency
one_liner: 通过任务引导检查、API 接地和阶段隔离学习，将开源小模型电子表格操作准确率提升至 32.8%
practical_value: '- 将复杂数据操作任务拆成“定位目标 → 定义变更 → 实现转换”三阶段，让 LLM 在每个阶段专注单一子问题，降低长链路推理压力；电商数据运营/BI
  取数 Agent 可直接套用。

  - 用 API grounding 把模型生成锚定在可用工具签名和参数上，减少无效工具调用；对推荐系统中 LLM 调用商品 API、数据库查询等同样有效，能显著提升小模型工具使用准确率。

  - 采用 execution consistency：推理时对同一指令生成多个程序，执行后比较工作簿/数据库状态选出一致结果，类似 self-consistency
  但针对结构化状态，可迁移到生成 SQL、特征计算等场景。

  - 阶段隔离学习使用 edit-progress rewards 做细粒度奖励，缓解整体成功/失败信号稀疏问题；Agent 训练中可按子步骤生成过程奖励，优化中间策略。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：电子表格自动化要兼顾数据敏感性与部署成本，倾向本地开源小模型；但复杂任务同时需要任务推理、工作簿理解，预定义操作接口又增加工具选择与调用负担。

**方法关键点**：SheetAlign 把操作过程解耦为“在哪操作、改什么、如何实现转换”三阶段。任务引导检查与 API grounding 将代码生成锚定在工作簿观察和可用操作上，减少错误目标与无效 API 调用。阶段隔离策略学习用 edit-progress rewards 对程序生成和审查做细粒度优化，缓解整体失败信号稀疏问题。推理阶段用 execution consistency，根据多次生成程序执行后工作簿状态的一致性选择结果。

**关键结果**：在 SpreadsheetBench 上，仅用 grounding 接口，Qwen3-4B 准确率从 13.5% 升至 29.2%（无训练）；加入阶段隔离学习与执行一致性后，平均准确率达 32.8%，Domain-Spreadsheet 达 30.1%，超过可比基线。
