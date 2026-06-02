---
title: When Does Multi-Agent RL Improve LLM Workflows? Workflow, Scale, and Policy-Sharing
  Tradeoffs
title_zh: 多智能体强化学习何时提升LLM工作流：工作流、规模与策略共享的权衡
authors:
- Yifan Zeng
- Yiran Wu
- Yaolun Zhang
- Wentian Zhao
- Kun Wan
- Qingyun Wu
- Huazheng Wang
affiliations:
- Oregon State University
- Pennsylvania State University
- Adobe Inc.
- AG2AI, Inc.
arxiv_id: '2605.24202'
url: https://arxiv.org/abs/2605.24202
pdf_url: https://arxiv.org/pdf/2605.24202
published: '2026-05-21'
collected: '2026-06-02'
category: MultiAgent
direction: 多Agent RL训练稳定性与工作流拓扑
tags:
- Multi-Agent RL
- GRPO
- Role Drift
- Policy Sharing
- Workflow Topology
one_liner: 多智能体RL训练通常提高精度，但稳定性由工作流拓扑与策略路由决定，隔离策略峰值高但后期退化，共享策略易被主导角色捕获
practical_value: '- 在设计多Agent工作流时，必须监控每个角色的训练指标（如困惑度、梯度范数），而非仅看整体准确率，防止角色漂移。

  - 对于有相同角色并行实例的拓扑（如投票、Orch-Workers），隔离策略（IP）会导致梯度放大，使该角色过快退化，可考虑共享策略或限制并行度。

  - 在投票工作流中，聚合器输出的长度分布是关键诊断信号：若聚合器从简洁选择变为冗长阐述，表明共享策略已被投票角色捕获。

  - 策略共享不是默认的稳定选择：工作流拓扑和任务决定了共享或隔离哪个更合适，应通过实验验证，而非盲目使用共享。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：多智能体LLM工作流（如Eval-Opt、Voting、Orch-Workers）通过分解生成、评估、聚合等角色来提升端到端准确率，但用强化学习（RL）联合训练这些角色时训练不稳定，且不稳定性的成因不清。本文系统研究何时多智能体RL训练能超越基础模型，并解释不同工作流、模型规模、任务和政策共享策略下的训练动态。

**方法关键点**：
- 工作流拓扑：Eval-Opt（生成器+评估器迭代修订）、Voting（3个生成器+1个聚合器）、Orch-Workers（1个协调者+3个工人+1个合成者）。
- 政策共享策略：Isolated-Policy (IP) 为每个角色类型分配独立LoRA适配器，Shared-Policy (SP) 所有角色共享一个LoRA。
- 训练设置：使用GRPO（无KL惩罚），每步8次工作流展开，组内相对优势；基模型为Qwen3（0.6B/1.7B/4B），LoRA rank=64；数据集DAPO-Math-17K和DeepCoder。
- 控制基线与单智能体RL对照，以分离多智能体训练带来的增益。

**关键实验与结果**：
多智能体RL在大多数配置下优于基模型，但增益依赖工作流、任务和规模。IP通常达到更高峰值准确率，但易出现后期精度“悬崖”退化；SP峰值较低但更保守，却未能消除退化，而是重新分配为角色捕获等模式。例如，Math 1.7B下Eval-Opt IP比单智能体RL高+10.1%，而Voting SP在4B Math上比单智能体RL低-10.3%。梯度分析揭示两种机制：“梯度放大”（IP下并行相同角色梯度相干，加速退化）和“共享策略捕获”（SP下主导角色贡献更多梯度，使共享策略偏向其分布，导致其他角色输出模式转移，如评估器输出代码块、聚合器输出长篇解释）。

**核心结论**：政策共享不应视为默认的稳定性开关，它和工作流拓扑共同决定训练压力通道，需按工作流和任务条件选择。
