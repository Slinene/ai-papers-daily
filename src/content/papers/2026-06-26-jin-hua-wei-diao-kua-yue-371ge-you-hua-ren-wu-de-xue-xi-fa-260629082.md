---
title: 'Evolution Fine-Tuning: Learning to Discover Across 371 Optimization Tasks'
title_zh: 进化微调：跨越371个优化任务的学习发现
authors:
- Young-Jun Lee
- Seungone Kim
- Minki Kang
- Alistair Cheong Liang Chuen
- Zerui Chen
- Seungho Han
- Taehee Jung
- Dongyeop Kang
affiliations:
- University of Minnesota
- Carnegie Mellon University
- KAIST
- University of Cambridge
- Hanyang University
arxiv_id: '2606.29082'
url: https://arxiv.org/abs/2606.29082
pdf_url: https://arxiv.org/pdf/2606.29082
published: '2026-06-26'
collected: '2026-07-01'
category: Agent
direction: 进化搜索LLM Agent · 跨任务迁移
tags:
- Evolutionary Search
- Fine-Tuning
- LLM Agent
- Optimization
- Cross-task Generalization
- Trajectory Supervision
one_liner: 将进化搜索轨迹转为训练数据，让LLM学会跨任务的迭代进化改进能力
practical_value: '- 搜索/推荐场景中的超参调优、召回策略组合优化可借鉴：将历史自动调参轨迹作为训练数据，让 LLM 预测下一步变异方向，减少试错成本。

  - Agent 设计可学习“如何改进解决方案”的元能力，而非依赖外部脚手架：将搜索中的成功/失败经验注入模型，使 Agent 在新场景下快速适应。

  - 多目标优化（如点击率 vs 多样性）可将帕累托搜索过程构造为轨迹数据集，微调出能直接生成改进策略的模型。

  - 工程上，轨迹数据的构造需包含候选解、评分、变异操作、结果反馈，可仿照 Finch Collection 设计领域特定的搜索轨迹格式。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有LLM集成进化搜索虽在数学猜想、GPU内核设计等优化任务上取得SOTA，但每次针对单一任务从零开始搜索，搜索经验随任务结束而丢弃，“如何进化”（如哪部分变异、何时回溯）完全依赖外部脚手架，模型自身未习得进化能力。能否让模型学会这种跨任务的进化策略？

**方法关键**：提出进化微调（EFT），一种中期训练范式。将进化搜索轨迹转化为监督信号：每个轨迹包含一系列变异步骤及其评分变化，模型学习根据当前解和历史预测下一变异。构建Finch Collection，含10个领域（数学、代码、科学等）371个优化任务的156K条轨迹。微调2B-9B的开源LLM。

**关键结果**：在22个留出任务上，EFT模型相比基座平均提升10.22%，展现跨任务泛化。结合测试时强化学习后，在两个圆填充任务上匹配SOTA性能，在Erdős最小重叠问题上超越基座模型。EFT成为通用发现智能体的“练习阶段”，使其不再从零开始搜索。
