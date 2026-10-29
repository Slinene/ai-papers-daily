---
title: 'AlphaBet: Reinforcement Learning for LLM Event Forecasting Agents'
title_zh: AlphaBet：面向 LLM 事件预测智能体的强化学习框架
authors:
- Liqin Ye
- Rongzhi Zhang
- Xin Liu
- Zheng Li
- Yuan He
- Qingyu Yin
- Priyanka Nigam
- Chao Zhang
affiliations:
- Georgia Institute of Technology
- Amazon
arxiv_id: '2610.22684'
url: https://arxiv.org/abs/2610.22684
pdf_url: https://arxiv.org/pdf/2610.22684
published: '2026-10-14'
collected: '2026-10-29'
category: Agent
direction: Agent 强化学习 · 事件预测
tags:
- Reinforcement Learning
- LLM Agent
- Event Forecasting
- GRPO
- Brier Score
- Evidence Acquisition
one_liner: 用多日期事件结果联合监督证据搜索与概率报告，显著降低 Brier 分数并提升准确率
practical_value: '- **多信息状态监督**：利用同一事件在不同预测日期提供不同信息状态，让单个已解决事件监督多个决策点。可迁移到用户行为序列建模：对同一用户，在不同交互时刻构造不同上下文，用最终转化/成交结果监督每个时刻的决策，提升样本效率。

  - **GRPO 归一化陷阱**：在需要概率校准的任务（如 CTR/CVR 预估、排序打分）中，如果采用 GRPO 做 RL 训练，注意其 std 归一化可能扭曲
  proper scoring rule 下的概率报告，导致校准恶化但 top-1 准确率不变。建议在奖励设计时避免对概率型输出做过度的组内标准化，或分离校准与排序目标。

  - **Regret 分解诊断**：将预测误差分解为证据获取 gap 和概率报告 gap，分别评估信息检索质量和概率校准能力。类似地，在推荐/搜索系统中可把整体损失拆成召回（信息获取）和排序（概率报告）两部分，定位瓶颈后再针对性优化。

  - **Agentic 三段式结构**：search → reason → report 的固定流程可复用于需要动态获取外部信息的交互式推荐或对话搜索场景，让
  policy 自主决定何时、如何获取证据再输出概率。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有 LLM 事件预测器通常在单一日期使用预收集证据做有监督训练，证据获取环节不参与学习，导致信息检索和概率校准脱节。

**方法关键点**：AlphaBet 用强化学习训练单个 LLM policy，在多个预测日期执行 search（搜索证据）、reason（推理）、report（输出概率）。每个日期的预测由 proper scoring rule 根据最终事件结果打分，使得同一已解决事件能监督不同信息状态下的决策。作者将预测 regret 分解为 evidence-acquisition gap（证据获取差距）和 probability-reporting gap（概率报告差距），并指出 GRPO 的标准差归一化在多分类 proper scores 下会扭曲概率报告目标。

**关键结果**：在 GLM-4.5-Air 上，AlphaBet 将 Brier score 从 0.731 降至 0.626（Forecast-Dojo），从 0.612 降至 0.528（FutureX）；准确率分别提升 8.9 pp 和 6.6 pp。消融实验将收益归因于多日期训练，并验证其同时改善了信息获取与概率报告。此外，实验确认 GRPO 的 std 归一化会损害 proper scoring rule 性能，但对 top-outcome accuracy 基本无影响。
