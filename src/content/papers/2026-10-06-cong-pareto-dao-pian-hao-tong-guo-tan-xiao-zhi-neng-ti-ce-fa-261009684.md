---
title: 'From Pareto to Preference: Personalized Test-Time Scaling via Amortized Agentic
  Policy Discovery'
title_zh: 从 Pareto 到偏好：通过摊销智能体策略发现实现个性化测试时扩展
authors:
- Xinglin Wang
- Zishen Liu
- Tong Zheng
- Shaoxiong Feng
- Peiwen Yuan
- Yiwei Li
- Jiayi Shi
- Yueqi Zhang
- Chuyi Tan
- Ji Zhang
affiliations:
- Beijing Institute of Technology
- Xiaohongshu Inc
arxiv_id: '2610.09684'
url: https://arxiv.org/abs/2610.09684
pdf_url: https://arxiv.org/pdf/2610.09684
published: '2026-10-06'
collected: '2026-10-08'
category: Agent
direction: Agent 策略搜索与测试时计算优化
tags:
- Test-time scaling
- Agentic policy discovery
- Amortized search
- Personalization
- LLM reasoning
one_liner: PersonTTS 用摊销智能体策略发现复用历史搜索经验，按用户多维需求个性化配置测试时计算
practical_value: '- 将用户需求拆成多维约束（准确率、延迟、成本）并学习对应的控制器，可迁移到电商推荐中不同场景/用户对延迟与精度的差异化要求：按
  profile 匹配策略库，而非一套模型打天下。

  - 摊销策略发现思路可解决推荐/广告系统中策略冷启动与重复搜索开销：利用历史搜索经验做 requirement-matched 初始化和程序指导，同时保留目标分布上的重新评估，避免负迁移。

  - 工程上可借鉴固定候选评估预算下的跨用户经验复用机制：在线上策略迭代或 AutoML 场景中，用历史实验经验指导新配置搜索，可显著降低 agent 时间和推理成本。

  - 需求匹配初始化的做法类似于推荐中的 meta-learning / warm-start，可以先构建历史任务库，再按特征相似度初始化优化器，提升新任务收敛速度。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有测试时扩展（TTS）效率优化通常只针对准确率-成本或准确率-延迟的单一 Pareto 前沿，但真实用户会同时指定准确率、延迟和推理成本等多维要求，不同要求可能对应完全不同的控制器。

**方法关键点**：将个性化测试时扩展形式化为发现可执行控制器以最大化用户特定需求的联合满足率。提出 PersonTTS，一个摊销的智能体策略发现框架：对新的用户 profile，通过需求匹配的控制器初始化和源任务蒸馏的程序性指导来复用历史搜索经验，同时每个候选仍保留在目标 profile 上的评估。

**关键结果**：在 AIME 和 HMMT 数据集上，PersonTTS 在未见用户 profile 和 held-out 问题上显著超越强 TTS 基线；在相同候选评估预算下，跨用户经验复用进一步提升策略质量，同时大幅降低发现智能体的时间和成本。
