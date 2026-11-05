---
title: 'When Fine-Grained Credit Assignment Helps and Hurts: Multimodal Agentic Reinforcement
  Learning through Video Editing'
title_zh: 细粒度信用分配何时有益与有害：基于视频编辑的多模态智能体强化学习
authors:
- Lei Zhao
- Zongheng Cao
- Xinyu Hu
affiliations:
- University of Pennsylvania
- Philo Labs
arxiv_id: '2610.35497'
url: https://arxiv.org/abs/2610.35497
pdf_url: https://arxiv.org/pdf/2610.35497
published: '2026-10-25'
collected: '2026-11-05'
category: Agent
direction: 多模态 Agent RL 信用分配机制
tags:
- Credit Assignment
- Process Reward
- GRPO
- Multimodal Agent
- Video Editing
- Reward Hacking
one_liner: 在视频编辑长程任务中揭示过程奖励需衰减权重以避免奖励黑客，短程任务仅结果奖励即可
practical_value: '- 长 horizon 的 Agent 任务（如多步购物助手、广告创意生成）中使用过程奖励时，建议给 PRM 权重设置随训练衰减的调度，后期趋近于
  0，以保留早期工具调用引导、同时避免过度推理与冗余工具调用。

  - 短 horizon 任务（30-40 步以内）仅用结果奖励的 GRPO 已足够，不必引入复杂的过程奖励，可降低训练与推理开销。

  - 若尝试 OPSD/自蒸馏为 Agent 提供密集 token 监督，需谨慎选择特权信息，并监控 teacher-student 分歧和梯度幅度，否则可能出现明显退化——长轨迹中信号被稀释是关键风险。

  - 视频编辑的四个子任务（内容选择、叙事排序、粗剪、精剪）可作为多媒体/广告 Agent 的任务分解模板，便于课程训练和分段评估。'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
RL 训练多模态 Agent 执行长程任务时，何时使用细粒度信用分配（如过程奖励）能提升效果，何时反而有害，缺乏系统结论。视频编辑是理想测试平台：同时涉及多模态感知、长程规划、工具调用和延迟结果反馈。

### 方法关键点
构建四种电影预告片编辑任务：Content Selection、Narrative Sequencing、Rough Cut、Fine Cut，覆盖不同复杂度和交互长度。比较：仅结果奖励 GRPO、GRPO+固定权重 PRM、衰减过程奖励权重，以及 OPSD（密集 token 监督）。监控过程奖励、工具调用次数、任务完成率和结果分数。

### 关键结果
- 在 Fine Cut（平均 >60 轮）上，衰减过程奖励相对仅结果奖励 GRPO 提升 45.4%；在较短任务（30-40 轮）上仅结果奖励 GRPO 已具竞争力，衰减过程奖励最多提升 10.4%。
- 固定权重的 GRPO+PRM 训练后期出现奖励黑客：过程奖励继续上升，但任务完成率和结果分数下降，表现为过度推理和冗余工具调用；将过程奖励权重衰减至零可缓解该问题。
- OPSD 即使有密集 token 监督，也几乎无提升或大幅退化，且对特权信息选择高度敏感；分析表明长轨迹中信息信号可能被稀释。
