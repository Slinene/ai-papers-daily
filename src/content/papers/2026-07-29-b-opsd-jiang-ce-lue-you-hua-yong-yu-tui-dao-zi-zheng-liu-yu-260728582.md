---
title: 'β-OPSD: Deriving with Policy Optimization, Training with Self-Distillation'
title_zh: β-OPSD：将策略优化用于推导、自蒸馏用于训练的推理增强框架
authors:
- Jiawei Xu
- Minghui Liu
- Juzheng Zhang
- Tom Goldstein
- Furong Huang
affiliations:
- University of Maryland, College Park
arxiv_id: '2607.28582'
url: https://arxiv.org/abs/2607.28582
pdf_url: https://arxiv.org/pdf/2607.28582
published: '2026-07-29'
collected: '2026-08-01'
category: Training
direction: KL正则化策略优化 · 自蒸馏
tags:
- OPSD
- Self-Distillation
- KL-regularized RL
- Logit Interpolation
- Return-to-go Credit Assignment
- Mathematical Reasoning
one_liner: 将on-policy自蒸馏统一为KL正则化策略优化族，通过可控的logit插值目标与return-to-go信用分配替代直接教师模仿，显著提升推理模型训练稳定性与性能。
practical_value: '- **蒸馏目标调度**：在在线蒸馏中，不直接跳到教师分布，而是用logit插值在参考策略与教师之间构造平滑课程（β从大到小）。这一trick可迁移至推荐系统的生成式模型训练（如LLM生成商品标题或推荐解释），避免训练初期因教师‑学生差距过大导致的崩溃。

  - **return‑to‑go信用分配**：将序列级KL散度梯度分解为token级累积未来误差，替代局部token‑KL损失。在电商对话Agent中，对于多轮对话的回复质量评估，可借鉴这种将最终用户满意度信号反向传播到每个token的方法，提升训练效率。

  - **参考策略的动态/固定选择**：实验表明，使用当前学生（stop‑gradient）作为参考端、固定教师作为教师端的混合插值效果最好。这在搜推场景中可对应为：用当前模型的历史快照作为“保守先验”，用业务强信号（如成交）构造教师，在持续学习或在线更新时保持稳定性。

  - **低成本策略优化近似**：通过闭式解推导出理论最优目标，再用轻量logit混合实现，避免直接RL的方差和成本。在资源受限的推荐Agent微调场景中，可复用这种“推导用RL，训练用蒸馏”的范式，兼顾效果与效率。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
On‑policy self‑distillation (OPSD) 虽能提升语言模型推理能力，但实践中十分脆弱，常需大量工程调优。其本质问题在于：直接以特权教师为唯一模仿目标，缺乏控制学生策略移动幅度的机制。

## 方法
- **将OPSD重铸为KL正则化策略优化**：选择教师‑参考对数比作为奖励，β控制KL惩罚项，当β=1时退化为标准OPSD（反向KL散度）。更一般的β>1给出更保守的更新，β→1更激进。
- **闭式最优策略与logit插值目标**：推导β‑OPSD的最优解为参考策略和教师策略的几何插值（指数加权）。实际训练时，用token级logit加权和（softmax）近似该全局目标，避免序列级归一化常数。
- **β调度课程**：采用线性增长（如从0.5到0.8）的教师权重wk=1/βk，使训练初期目标靠近学生，逐步移向教师。
- **return‑to‑go信用分配**：将token级局部KL误差替换为未来累积误差的折扣和（γ=0.99），提供序列级反向KL的无偏梯度估计，修正短视的局部模仿。

## 关键结果
在Qwen3‑1.7B/4B/8B上用OpenThoughts数学数据训练，评估AIME 2024、2025和HMMT 2025。Qwen3‑1.7B的avg@12在三个基准上分别提升9.16、5.27和2.78个百分点，平均提升5.74点；在大模型上亦有1.66‑1.76点平均提升，一致优于原始OPSD、SFT及GRPO。消融证实：logit插值目标和return‑to‑go信用分配各自独立贡献显著。
