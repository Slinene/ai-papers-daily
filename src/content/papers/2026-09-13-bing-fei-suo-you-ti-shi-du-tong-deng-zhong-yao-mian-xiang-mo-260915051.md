---
title: 'Not All Prompts Are Equal: Exploration-Guided Prompt Scaffolding for Multimodal
  Reinforcement Post-Training'
title_zh: 并非所有提示都同等重要：面向多模态强化后训练的探索引导式提示脚手架
authors:
- Yuanhao Yue
- Qianli Ma
- Chengyu Wang
- Haoting Wang
- Lei Shen
- Jun Huang
affiliations:
- Alibaba Cloud Computing
- Shanghai Jiao Tong University
- Fudan University
- Xi’an Jiaotong University
arxiv_id: '2609.15051'
url: https://arxiv.org/abs/2609.15051
pdf_url: https://arxiv.org/pdf/2609.15051
published: '2026-09-13'
collected: '2026-09-15'
category: Training
direction: 多模态 RL 后训练 · 提示脚手架
tags:
- Prompt Scaffolding
- Reinforcement Learning
- MLLM
- Exploration Potential
- Training Data Refinement
- GRPO
one_liner: 提出基于探索潜力评分的动态提示脚手架框架，自适应调整多模态LLM RL后训练的提示分布，提升域内外性能
practical_value: '- 动态训练采样策略：在 LLM 推荐/Agent 的 RL 后训练中，不要均匀采样 prompt 或 trajectory。可借鉴
  EPS 思想，用在线 rollouts 的 reward 方差、优势差异等轻量统计量估计样本信息量，对低方差高成功率（饱和）或极低成功率（过难）的样本降低采样权重或触发重写，节省算力。

  - 难样本重写而非丢弃：业务中收集到的用户指令/交互轨迹质量参差，直接过滤会损失信息。可以用 teacher LLM 对过难或过易的 prompt 做 scaffolded
  rewriting，保留意图（如商品查询、任务目标）同时调整难度，提升训练数据利用率。

  - KL 约束可转化为数据选择启发式：EPS 从 KL-regularized policy improvement 导出，无需额外模型，只用 rollout
  统计量即可实现，适合集成到现有 PPO/GRPO 训练循环，对多模态 Agent 和生成式推荐模型的 RL 后训练有直接参考价值。

  - 监控 prompt 级效用并动态调整 batch 构成：类似课程学习，在训练过程中周期性评估每个 prompt 的 utility，动态改变训练分布，能在不增加总预算的情况下提升域内和
  OOD 泛化。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：在线 RL 后训练中，训练 prompt 被均匀分配 rollout 预算，但不同 prompt 对当前策略的信息量差异很大：已饱和的 prompt 提供不了梯度信号，过难的 prompt 学不到可靠信号，造成算力浪费。

方法关键点：
- 提出 Exploration Potential Score (EPS)，从 KL-regularized policy improvement 理论推导出的轻量级 prompt 效用代理指标；仅依赖 on-policy rollout 的统计量（如 reward 方差、策略熵等）即可计算，无额外模型或开销。
- 对低 EPS prompt 不直接丢弃，而是用 teacher model 生成 scaffolded rewrites，保持任务意图不变但调整难度或表达，使改写后的 prompt 更 informative；将 teacher 的监督从输出模仿重定位为训练数据精炼。
- 框架与 GRPO 集成，在 Geo3K 和 MMK12 两个多模态基准上训练，动态调整训练 prompt 分布。

关键结果数字：域内相对提升最高 9.7%；OOD 基准 MathVision 提升 11.5%，MMMU-Pro 提升 11.1%，均优于 GRPO 基线。
