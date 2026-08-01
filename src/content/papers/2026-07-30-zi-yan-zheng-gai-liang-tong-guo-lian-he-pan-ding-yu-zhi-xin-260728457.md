---
title: 'SVR: Self-Verifying Refinement via Joint Verdict-Confidence Reinforcement
  Learning for Adaptive Test-Time Compute'
title_zh: 自验证改良：通过联合判定与置信度强化学习实现自适应测试时计算
authors:
- Hongyu Chen
- Liang Lin
- Guangrun Wang
affiliations:
- Sun Yat-sen University
- Guangdong Key Laboratory of Big Data Analysis and Processing
- X-Era AI Lab
arxiv_id: '2607.28457'
url: https://arxiv.org/abs/2607.28457
pdf_url: https://arxiv.org/pdf/2607.28457
published: '2026-07-30'
collected: '2026-08-01'
category: Reasoning
direction: 自适应推理 · 自验证强化学习
tags:
- Self-Verification
- Adaptive Compute
- GRPO
- Confidence Calibration
- Test-Time Compute
- Reasoning
one_liner: 学习自验证与置信度作为内部控制信号，在推理时自适应分配计算预算，无需外部验证器
practical_value: '- **多轮决策的自适应终止**：在推荐Agent或对话系统中，可以借鉴SVR让模型在对每轮输出（如推荐列表、搜索建议）同时生成质量判定和置信度，达到阈值则提前终止交互，节省LLM调用成本。

  - **无需外部监督的自我验证训练**：通过奖励校准自验证正确性，模型能内生判断能力，适用于电商场景中缺乏及时反馈的推荐解释、文案生成等任务，训练时只用最终答案正确性，推理时自我把关。

  - **联合输出校准与决策**：将离散判定与连续置信度联合输出，并通过校准奖励使其对齐真实准确性，该思路可迁移到CTR预估中的不确定性建模或排序模型的置信度输出。

  - **自适应计算分配**：对简单样本自动减少推理步数，复杂样本多步迭代，类似思想可用于动态召回、重排序的算力分配，例如对低候选集质量的请求执行更多召回或精排步骤。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：测试时计算规模提升语言模型推理，但统一预算浪费资源，现有验证器引导的改良依赖外部反馈。需要一种自适应的、无需预言机的计算分配策略。

**方法**：提出自验证改良（SVR），一个多轮强化学习框架。模型每轮生成解、离散正确性判定（Correct/Incorrect）和置信度分数；只当判定为Correct且置信度超过阈值时才保留答案，否则继续改良。训练使用GRPO，固定最大轮次，奖励由三部分组成：解的正确性、校准感知的自验证奖励（鼓励判定与真实正误一致且置信度反映实际概率）、以及奖励处于“可停止的正确状态”。推理时激活自适应停止，阈值可通过目标校准误差确定。整个过程不向模型暴露真实标签，仅训练奖励使用。

**结果**：在7个数学推理基准上，基于Qwen3.5-2B，SVR获得宏观平均准确率0.563，平均仅2.99轮推理。相比固定10轮GRPO和其他多轮基线，增益显著，且大幅节省推理计算。消融表明联合训练判定和置信度、以及自适应停止均关键。
