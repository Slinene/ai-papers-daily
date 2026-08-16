---
title: 'Beyond Final Scores: A Systematic Evaluation of Agents for Long-Horizon AI
  Research and Development'
title_zh: 超越最终分数：面向长时域 AI 研究与开发的智能体系统性评估
authors:
- Yiwei Li
- Wanli Yang
- Hexiang Tan
- Xiangzhou Huang
- Zhengyu Chen
- Ziran Li
- Borun Chen
- Shanglin Lei
- Huaisheng Zhu
- Hao Tian
affiliations:
- Meituan
- University of Chinese Academy of Sciences
arxiv_id: '2608.13417'
url: https://arxiv.org/abs/2608.13417
pdf_url: https://arxiv.org/pdf/2608.13417
published: '2026-08-13'
collected: '2026-08-16'
category: Eval
direction: Agent 长时域任务过程评估与经验复用
tags:
- Agent Evaluation
- Long-Horizon
- Experience Reuse
- Frontier Models
- Process Metrics
- AI R&D
one_liner: 通过过程化指标与受控对比，评估 7 个前沿模型在 36 个长时域任务上的行为，发现当前智能体更像工程优化器而非自主研究者
practical_value: '- 评估 Agent 不能只看最终指标，应监控 Solution Framing、Execution、Feedback Control
  三个过程环节，定位瓶颈是方案设计、代码执行还是反馈调整，再针对性优化。

  - 经验复用是把双刃剑：成功经验可能误导后续决策，建议在 Agent 记忆模块中加入相似性门控或置信度过滤，避免盲目复用历史方案。

  - Harness 设计（提示模板、工具接口、实验环境）会显著影响表现稳定性，在业务中上线 Agent 前需隔离变量做 A/B 测试，避免将平台差异误判为模型能力。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：面向长时域 AI 研究的 Agent 评估往往只看最终得分，无法揭示进展从何而来、经验是否被有效复用。

**方法**：提出新评估框架，在 36 个长时域任务上对 7 个前沿模型进行系统评估。框架使用规则化指标刻画单次运行内的 Solution Framing、Execution、Feedback Control 三个过程维度，并通过受控对比任务内与跨任务的经验复用效果。

**关键结果**：当前 Agent 更接近工程优化器而非自主研究者：能提出并实现可行方案，但跨运行表现差异显著；最强方案主要是对既有技术的适配或组合，真正的方法创新很少。相似最终结果背后存在不同过程瓶颈，经验复用有时帮助、有时误导后续决策，harness 设计直接影响稳定性。

**结论**：评估必须深入过程与经验机制，论文给出了模型训练、推理策略、经验管理、harness 设计的具体改进方向。
