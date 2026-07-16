---
title: 'MyAG: A Graph-Based Framework for Designing and Analyzing Composable LLM Agent
  Systems'
title_zh: MyAG：基于图的组合式LLM Agent系统设计与分析框架
authors:
- Zhisong Zhang
affiliations:
- City University of Hong Kong
arxiv_id: '2607.13474'
url: https://arxiv.org/abs/2607.13474
pdf_url: https://arxiv.org/pdf/2607.13474
published: '2026-07-15'
collected: '2026-07-16'
category: Agent
direction: LLM Agent 框架设计与优化
tags:
- LLM Agent
- Graph-Based Framework
- Composable Systems
- Workflow
- Monitoring
one_liner: 将Agent系统解耦为组件图、工作流图和搜索图三层图抽象，支持灵活复用与层级组合，并提供监控分析工具。
practical_value: '- **模块化解耦设计**：将Agent系统拆分为组件、工作流、搜索三个图，可单独替换策略（如LLM调用、规划器、搜索算法），适合电商多场景Agent快速实验。

  - **层级组合与递归**：通过递归系统节点支持子Agent嵌套，可直接用于构建多级推荐/对话系统（如店铺级、商品级、用户级Agent分层协作）。

  - **运行时执行成本分析**：内建LLM调用次数、环境动作次数等统计，方便评估搜索推荐场景下Agent的延迟与成本，指导工程优化。

  - **可视化与监控工具**：提供Agent执行过程的图形化追踪，便于调试复杂推荐链路中LLM调用异常或工作流死锁问题。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM Agent系统设计涉及模块构成、工作流逻辑和搜索策略，这些部分紧密耦合但需求各异，修改任一维度常需整体重构，缺乏同时支持灵活组合、运行时策略替换与性能分析的框架。

**方法**：提出三层图抽象：
- **组件图（Component Graph）**：定义Agent、环境和可调用模块的静态结构；
- **工作流图（Workflow Graph）**：描述执行控制流，通过节点和边定义步骤序列、条件和循环；
- **搜索图（Search Graph）**：在运行时动态决定下一步动作，如树搜索、回溯等。

三层解耦允许同一组件搭配不同工作流或搜索策略。支持**层级组合**：可将一个完整系统封装为递归节点，作为上层系统的子系统。内建**监控与可视化**，自动记录LLM调用、环境交互，并生成执行图。

**关键结果**：在数学推理、Web搜索等典型Agent任务上验证，显示框架可灵活切换搜索策略（如广度优先vs深度优先），并直观分析不同策略下LLM调用次数与任务成功率的权衡。
