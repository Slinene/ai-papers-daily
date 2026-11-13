---
title: Actor, Judge, or Teacher? Understanding Decision Models in Long-Horizon Agents
title_zh: 演员、裁判还是老师？理解长程智能体中的决策模型
authors:
- Haochen Liu
- Qianhao Zhu
- Zixuan Wang
- Dingming Li
- Tongbo Chen
- Peng Qiu
- Yingqi Qu
- Weiming Lu
- Jun Xiao
- Yongliang Shen
affiliations:
- Zhejiang University
- Baidu Inc.
arxiv_id: '2611.17167'
url: https://arxiv.org/abs/2611.17167
pdf_url: https://arxiv.org/pdf/2611.17167
published: '2026-11-11'
collected: '2026-11-13'
category: Agent
direction: 长程智能体决策模型的多角色分析
tags:
- Decision Models
- Long-Horizon Agents
- Reinforcement Learning
- GRPO
- Judge
- Teacher
one_liner: 决策模型即使行动表现差，也能作为事后裁判和教师显著提升长程策略成功率
practical_value: '- 使用轻量级决策模型（如 JEV）作为 step-level judge 为动作打分，替代昂贵的 LLM judge 或人工标注，可大幅降低长程
  RL 训练成本，同时提升梯度信号质量

  - 训练时的提问方式很重要：问“这个动作是否对任务有帮助”比问“这个动作能否让任务成功”更能区分有用与无用动作，可直接用于奖励模型或 critic 的设计

  - 在长程任务中，actor 容易被较简单的子目标带偏，但事后 judge 能看到完整轨迹并正确归功；可以把 judge 的判断作为附加奖励信号来纠正策略的短视行为

  - 即使决策模型本身作为策略表现一般，仍可将其作为教师模型来蒸馏或引导小参数策略，在电商搜索/推荐场景中可复用该思路，例如用决策模型评估用户轨迹中的关键节点，辅助策略优化'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：决策模型输出类型化结果（如选项及概率）而非生成文本，速度快、成本低，可充当智能体的 actor（选择动作）或 judge（评估动作），进而作为 teacher 指导强化学习。但此前研究主要把决策模型当作 actor 评估，不清楚一个行动表现差的决策模型是否仍能教得好。

**方法关键点**：作者在 ALFWorld 上比较了三个决策模型与三个通用 LLM 作为 actor 和 judge；随后用 JEV 作为 teacher，在 ALFWorld 和 WebShop 上用 GRPO 训练 Qwen2.5-1.5B 策略。关键实验对比了不同提问方式对 judge 质量的影响。

**关键结果**：作为 actor，所有六个模型都被较容易的子目标从必须先完成的子目标引开；但作为能看到完整轨迹的 judge，相同模型会认可朝向该子目标的步骤。此外，询问“每个动作是否对任务有帮助”而非“任务是否会成功”能更有效地分离有用与无用动作。作为 teacher，JEV 将 Qwen2.5-1.5B 策略在 ALFWorld 的成功率从 72.8% 提升到 82.9%，在 WebShop 从 56.8% 提升到 71.4%。结果表明，表现差的 actor 仍能成为好老师，因为事后判断能揭示动作的长期后果，而行动本身需要提前预测这些后果。
