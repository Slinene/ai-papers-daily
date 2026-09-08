---
title: 'TruthInsightBench: An Evidence-Grounded Benchmark for Automated Evaluation
  of Open-Ended Scientific Discovery Agents'
title_zh: TruthInsightBench：面向开放式科学发现智能体的证据基准评估
authors:
- Zhibo Yang
- Chen Zhang
- Yuewei Zhang
- Hao Wang
affiliations:
- TruthInsight-AI
arxiv_id: '2609.05079'
url: https://arxiv.org/abs/2609.05079
pdf_url: https://arxiv.org/pdf/2609.05079
published: '2026-09-04'
collected: '2026-09-08'
category: Eval
direction: Agent 科学发现评估基准
tags:
- Agent
- Benchmark
- Scientific Discovery
- LLM-as-Judge
- Evidence Grounding
- Automated Evaluation
one_liner: 提出区分复现与发现的基准，用固定 LLM 裁判评估智能体声明的证据成熟度，揭示瓶颈在科学判断而非编码
practical_value: '- 在评估推荐/广告 Agent 时，引入“盲任务”设计：只给中性业务目标（如“提升点击率”）和冻结历史数据，隐藏已知最优策略，考察
  Agent 能否自主提出可验证的假设和实验方案，而不是复现预设的优化流程。

  - 借鉴其“声明-证据成熟度”的 6 维度/29 项检查表，为推荐 Agent 输出建立证据审计清单：是否包含对照组设计、鲁棒性检查（不同时间段/人群分片）、可证伪性（明确什么结果会否定假设）、跨数据集/场景泛化验证等，量化决策质量。

  - 采用固定 LLM judge + 确定性聚合实现自动化评估，降低人工标注成本，支持 Agent 自我迭代。具体实现：将 Agent 产出拆解为可核验 artifact（图表、统计结果、实验设计），让
  LLM 对每个证据项打分，再用规则聚合，避免 LLM 主观偏差。

  - 结论“瓶颈在科学判断而非编码”提示：在推荐系统中引入 Agent 时，应优先加强推理、实验设计和因果推断模块，而非只提升代码生成能力，可接入因果推断工具或
  A/B 测试模拟器。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有 AI 科研 Agent 基准大多围绕“复现”设计：隐藏目标研究，奖励恢复源结论，无法区分执行预设分析与真正做出科学发现。

### 方法关键点
TruthInsightBench 包含 40 个盲任务，来自 10 个科学领域的 40 篇同行评审论文。每个任务只提供中性科学目标和冻结数据，隐藏源结论、期望值和分析路径，让 Agent 自行判断数据支持什么声明。评估采用固定 LLM 裁判，从六个维度（如证据可审计性、新颖性、对照、鲁棒性、可证伪性、跨数据集泛化）对 Agent 自己的声明进行打分，操作化为 29 个基于 artifact 的检查项。聚合过程自动且确定，无需逐实例人工评分，可重复评估。

### 关键结果
在冻结基座模型上，四个编码 Agent 总分集中在 58.4–60.3（满分 100），两两之间无统计显著差异，处于“执行”水平而非“发现”水平。证据可审计性和新颖性相对较强，但建立可信声明所需的对照、鲁棒性、可证伪性和跨数据集泛化等判别性行为基本缺失。瓶颈是科学判断而非编码能力，真正的科学发现仍不可及。
