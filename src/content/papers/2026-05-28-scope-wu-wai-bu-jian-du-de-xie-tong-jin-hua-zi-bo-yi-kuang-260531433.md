---
title: 'SCOPE: Self-Play via Co-Evolving Policies for Open-Ended Tasks'
title_zh: SCOPE：无外部监督的协同进化自博弈框架
authors:
- Wai-Chung Kwan
- Aryo Pradipta Gema
- Joshua Ong Jun Leang
- Pasquale Minervini
affiliations:
- University of Edinburgh
- Imperial College London
- Miniml.AI
arxiv_id: '2605.31433'
url: https://arxiv.org/abs/2605.31433
pdf_url: https://arxiv.org/pdf/2605.31433
published: '2026-05-28'
collected: '2026-06-01'
category: Training
direction: Self-Play协同进化 · 开放式任务训练
tags:
- Self-Play
- Reinforcement Learning
- Open-Ended Tasks
- Co-Evolving Policies
- Retrieval-Augmented Generation
- Rubric-based Judging
one_liner: 通过挑战者与求解器协同进化和自我评分机制，无需外部监督即可提升LLM在开放式任务上的表现
practical_value: '- **自博弈对抗生成训练数据**：在电商推荐中，可让一个模型生成“用户需求描述”（挑战者），另一个模型给出推荐结果（求解者），通过自我评判打分，无需人工标注即可持续提升推荐质量。

  - **基于源文档的自动评分标准生成**：self-judge 从文档自动生成评估准则的机制，可直接用于商品搜索、文案生成等场景的自动化评估，替代人工或大模型评判。

  - **协同进化的课程学习**：挑战者根据求解者表现动态调整任务难度，这一思想可用于推荐模型的训练数据采样，从简单到困难逐步提升模型能力，避免训练饱和。

  - **多轮检索与合成优化**：Solver 的多轮检索回答模式类似 Agent 的多次信息获取，其训练方法可迁移到电商 Agent 的检索策略优化，提升信息收集与综合能力。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有语言模型自博弈方法只能处理有标准答案的任务，导致开放式任务（如深度研究、复杂问答）仍依赖人工提示或更强模型裁判，限制性能上限。

**方法**：提出 SCOPE，一个无外部数据的自博弈框架，通过协同进化两个策略突破限制。挑战者基于源文档生成开放式任务（如写作、分析），求解者通过多轮检索综合信息生成答案。初始模型的冻结副本充当自我裁判，自动从源文档中提取任务特定评分标准（rubric），并对求解者响应评分。奖励信号通过 PPO 同时优化两个策略，挑战者被鼓励生成难度适中的任务，求解者被要求给出符合评分标准的高质量回答。

**关键结果**：在 Qwen2.5-7B、Qwen3-8B 和 OLMo-3-8B 三个模型上，SCOPE 在 8 个开放式基准上平均提升最高 +10.4 分，与使用约 9K 人工提示训练的 GRPO 效果持平或更优。仅在开放式任务上训练，却在 7 个短问答基准上迁移提升最高 +13.8 分，全面超过 GRPO。消融实验表明，挑战者协同进化对维持任务难度至关重要；性能增益来自检索与综合能力的双重提升；评分标准生成质量是自我评判的当前瓶颈。
