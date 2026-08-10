---
title: An End-to-End Agent Auditing Engine
title_zh: A2E：端到端智能体审计引擎
authors:
- Haoning Wang
- Mingxun Zhang
- Chenyue Yu
- Yingjun Shang
- Xia Hu
- Guanchu Wang
- Na Zou
affiliations:
- Shanghai Artificial Intelligence Laboratory
arxiv_id: '2608.07346'
url: https://arxiv.org/abs/2608.07346
pdf_url: https://arxiv.org/pdf/2608.07346
published: '2026-08-07'
collected: '2026-08-10'
category: Eval
direction: Agent 评估引擎与多维指标体系
tags:
- Agent Evaluation
- Harness
- Agent Task Protocol
- Multidimensional Metrics
- Execution Trace
one_liner: 提出A2E端到端评估引擎，通过ATP协议和多维指标系统揭示Agent框架能力差异
practical_value: '- 在电商搜索推荐Agent落地中，可借鉴ATP协议思想，定义统一的Agent任务接口，降低不同框架之间的切换与评估成本。

  - 多维指标（工具调用、规划完整性、错误恢复等）比单一准确率更能定位Agent短板，可直接用于Agent迭代优化与A/B测试。

  - 自动注入的Monitor机制，能无侵入采集执行轨迹，适合构建线上Agent的全链路观测与质量监控。

  - 实验揭示“模型+框架”组合效果强依赖任务类型，提示业务选型时需按场景分别评测，避免单一组合大一统。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：LLM驱动的智能体框架（harness）日益多样，但其系统化、端到端的评估流程缺失，导致难以公平对比不同框架的真实能力，也无法指导模型与框架的协同优化。

**方法**：提出A2E（Agent Auditing Engine），核心包括三部分：
- **Agent Task Protocol（ATP）**：统一的Agent任务描述协议，实现不同harness与评测任务的快速对接，屏蔽框架差异；
- **自动注入Monitor**：在实验执行时无侵入捕获标准化执行轨迹，记录完整交互过程；
- **多维评估体系**：除正确性外，引入运行效率、工具使用、任务规划、错误恢复、幻觉程度等多维度指标，提供细粒度能力画像。

**关键结果**：在9个主流harness与多个任务矩阵上的实验显示，各指标跨度极大（如工具调用合规性tool_inv 0.12–0.91，执行成功率0.989–1.000），且没有单一模型-框架组合能在所有任务上领先。该结果量化了框架间的能力差异，验证了多维评估的必要性，并为模型与框架协同演进提供了方向。
