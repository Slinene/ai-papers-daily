---
title: 'BrickBench: Evaluating Agentic Brick Design'
title_zh: BrickBench：评估智能体乐高设计能力的基准
authors:
- Peter Kulits
- Yiqing Xu
- R. Kenny Jones
- Cordelia Schmid
- Jiajun Wu
affiliations:
- Stanford University
- Max Planck Institute for Intelligent Systems
- Inria
arxiv_id: '2610.12452'
url: https://arxiv.org/abs/2610.12452
pdf_url: https://arxiv.org/pdf/2610.12452
published: '2026-10-07'
collected: '2026-10-11'
category: Eval
direction: Agent 设计评估基准
tags:
- Agentic Design
- Benchmark
- LEGO
- Coding Agents
- Evaluation
one_liner: 提出 BrickBench 基准与环境，评估编码 Agent 在文本条件 LEGO 设计中的物理与语义满足度
practical_value: '- 评估复杂约束生成任务时，可拆分 validity/alignment/design 三指标，对应推荐系统中的可执行性/相关性/体验质量，便于定位
  Agent 短板。

  - BrickAgent 的“编码-执行-检查-修订”循环是评估推荐 Agent 的可借鉴范式：给 Agent 提供可调用的库存查询、规则校验、模拟器接口，而非仅做文本输出。

  - 三种约束设置（不同零件库规模与可用性）提示在推荐场景中应测试 Agent 在不同库存、预算或商品池约束下的泛化能力。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**  
LEGO 设计需要从离散零件库中选件并同时满足局部与全局物理约束，传统生成方法依赖专门模型，编码 Agent 提供新途径但缺乏系统评估。  
**方法关键点**  
BrickBench 包含三个设置：Model（≤400 件）、Set（400–4000 件）、Alt-Build（使用 set 10698 库存），从 validity（可物理搭建）、alignment（语义一致）、design（设计质量）三维度评分。提供 BrickAgent 环境，允许 coding agent 编写程序、执行、检查、迭代设计。  
**关键结果**  
主流 Agent 基本满足可验证的物理与语义要求，但与人类设计质量仍有差距。
