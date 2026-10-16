---
title: 'TimeRSI: Towards Self-Improved Agentic Deployment for Time-Series Foundation
  Models'
title_zh: TimeRSI：面向时间序列基础模型的自改进智能体部署
authors:
- Haoxin Liu
- Deqing Fu
- Lucheng Fu
- Yiqiao Jin
- Rushi Qiang
- Harshavardhan Kamarthi
- B. Aditya Prakash
affiliations:
- Georgia Institute of Technology
- University of Southern California
- Samay AI
arxiv_id: '2610.19725'
url: https://arxiv.org/abs/2610.19725
pdf_url: https://arxiv.org/pdf/2610.19725
published: '2026-10-14'
collected: '2026-10-16'
category: Agent
direction: Agent 自动编排预测部署流程
tags:
- Agentic Deployment
- Time-series Forecasting
- Coding Agent
- Self-improving
- Foundation Models
- AutoML
one_liner: 用 LLM coding agent 在冻结预测模型外围自动生成与迭代 pipeline，并通过自适应选择器提升时间序列预测部署效果
practical_value: '- 把“冻结模型 + 外围 pipeline 自动迭代”迁移到电商预估/推荐：不改模型权重，由 coding agent 生成和修改特征注入、日历/活动信号、后处理或重排代码，在滚动历史回放窗口上评估，可显著降低人工
  pipeline 调试成本。

  - 借鉴错误反馈闭环：将回测中的分场景误差（如大促、时段、类目偏差）写成自然语言反馈给 agent 进行下一轮修改，比一次性搜索更有效；推荐系统可用“场景化 error
  report”驱动规则/校准代码生成。

  - 在线集成 adaptive selector：按当前上下文和近期相似条件下的实际表现，从多个候选 pipeline/策略中动态选择，而不是固定单一版本；适合推荐场景中多召回/多后处理策略的在线组合选择。

  - 工程落地时限定 agent 可修改空间（输入特征、输出校准、后处理逻辑）并做沙箱执行与回测成本控制，避免开放式搜索失控。'
score: 7
source: huggingface-daily
depth: abstract
---

时间序列基础模型（TSFM）零样本预测能力强，但实际部署仍需针对具体任务设计模型输入输出，否则领域知识（如节假日闭店、潮汐周期）和重复出现的预测误差无法被利用。传统定制 pipeline 需要大量人工。TimeRSI 在冻结的预测模型外围部署一个 LLM coding agent：它根据任务描述生成可执行的 pipeline 修改代码，并在历史预测窗口上回测，用观测到的误差作为反馈引导后续修改，形成自改进闭环。部署时，adaptive selector 基于已完成预测在相似条件下的表现，从生成的多个 pipeline 中选择最合适版本。在 TIME 和 fev-bench 共 198 个任务上，TimeRSI 在六项点预测和概率预测指标上优于所有提交。对照实验表明，反馈驱动的迭代修改优于非迭代式 pipeline 搜索；在不同 coding agent 和预测模型上的实验验证了泛化性。代码已开源。
