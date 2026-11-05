---
title: 'FrontierPhysics: Evaluating Agents for End-to-End Physics Research'
title_zh: FrontierPhysics：端到端物理研究智能体评测基准
authors:
- Bingran You
- Wenjun Ke
- Ria Rosenauer
- Bo Liu
- Wenbo Chen
- Min Chen
- Shuqi Xu
- Yue Ma
- Jiechao Feng
- Bo Chen
arxiv_id: '2611.06910'
url: https://arxiv.org/abs/2611.06910
pdf_url: https://arxiv.org/pdf/2611.06910
published: '2026-11-03'
collected: '2026-11-05'
category: Eval
direction: Agent 端到端科研评测基准
tags:
- Agent
- Benchmark
- Evaluation
- Scientific Research
- LLM
- Trajectory Analysis
one_liner: 56 个物理学家真实研究任务构成的端到端评测，揭示前沿 Agent 推理严谨性与专家直觉不足
practical_value: '- 评测设计可借鉴：用「确定性验证器 + 专家 rubrics」混合打分，而不是仅自动指标，能同时检查结果正确性和过程/产出质量。电商推荐
  Agent 评测可以在离线指标之外加入业务专家按 rubric 对推荐方案、实验分析、上线报告进行「可上线性」评分。

  - 任务来源要真实且由领域专家亲自构建，避免公开题泄漏和过拟合。推荐/广告团队可把历史业务难题（比如某次大促 ROI 异常、冷启动策略）改造成 Agent 端到端任务，要求产出方案、实验和复盘文档。

  - 轨迹分析定位 Agent 短板：论文发现失败主要不是知识/执行错误，而是推理不严谨和专家直觉不足。对推荐/广告 Agent 同样不要只堆工具和知识库，应加强推理链、自我校验、领域先验注入；可定期人工审查
  agent 轨迹定位「不严谨」环节。

  - 端到端自主研究 pass rate 最高仅 27.4%，说明全自动科研型 Agent 仍不成熟。业务中更稳妥的是人机协作：Agent 负责文献综述、候选策略生成、实验执行，专家做关键决策与最终审核。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有物理 benchmark 只评估固定问题、隔离子任务或已知解决方案的论文复现，缺乏端到端研究质量评估。

**方法关键点**：FrontierPhysics 由 42 位物理学家基于自身研究构建 56 个任务，覆盖理论、计算、实验等九个领域。每个任务要求 Agent 完成文献综述、研究计划、研究实验、结构化输出和科学手稿。评估组合确定性验证器和专家 rubrics，考察正确性与可发表性。

**关键结果**：评测 22 个模型 26 个配置，每配置 168 次 rollout，最高 pass rate 27.4%（Claude Opus 5.5），无配置超过 46/168。手动审查轨迹发现前沿 Agent 主要短板在于推理不够严谨和专家直觉有限，而非物理知识或执行错误。
