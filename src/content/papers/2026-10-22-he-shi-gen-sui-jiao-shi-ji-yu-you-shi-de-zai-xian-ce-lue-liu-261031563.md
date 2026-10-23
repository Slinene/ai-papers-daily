---
title: 'When to Follow the Teacher: Advantage-Based On-Policy Distillation'
title_zh: 何时跟随教师：基于优势的在线策略蒸馏
authors:
- Mahdi Sabbaghi
- George Pappas
- Hamed Hassani
- Adel Javanmard
affiliations:
- University of Pennsylvania
- University of Southern California
arxiv_id: '2610.31563'
url: https://arxiv.org/abs/2610.31563
pdf_url: https://arxiv.org/pdf/2610.31563
published: '2026-10-22'
collected: '2026-10-23'
category: Training
direction: LLM 在线蒸馏 · 优势加权
tags:
- On-Policy Distillation
- Advantage Weighting
- Knowledge Distillation
- LLM Training
- RLHF
one_liner: AOPD 用学生优势加权教师动作，仅靠标准 rollout 和终局奖励即可无偏估计，提升在线蒸馏效率与效果
practical_value: '- 在生成式推荐/搜索场景做 teacher-student 蒸馏时，不要在所有状态都强行跟随教师；可以用 advantage-weighted
  监督，只强化对当前 student 有益的教师动作，减少有害模仿。

  - 工程实现上，AOPD 只需要保存 student rollout 的 logprob 和 terminal reward，再用 teacher/student
  概率比做 importance weighting 即可，无需额外 rollout 或 reward model，轻量且易接入现有 on-policy 训练流程。

  - 若业务中已有用户点击/转化/成交等终局奖励，可把蒸馏目标从 token-level SFT 换成 AOPD 形式，使教师监督与业务回报对齐，尤其适用于 query
  推荐、push 文案、商品描述生成等 LLM 应用。

  - 自蒸馏设置下也能用同一套优势加权逻辑，从历史高质量策略或大模型生成样本中蒸馏，同时避免拖累当前学生已擅长的状态。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：标准在线策略蒸馏（OPD）让学生在采样轨迹的每个状态都模仿教师，默认教师指导总是有益；但教师偏好的动作未必能提升当前学生的实际回报，盲目跟随可能有害。

**方法关键点**：提出 Advantage-Based On-Policy Distillation（AOPD），用学生视角下的反事实优势对教师动作加权：能提高学生期望回报的教师动作被强化，否则被降权。直接计算优势需要逐状态尝试替代教师动作并重新 rollout；AOPD 的关键是只需标准学生 rollout 和终局奖励，通过 teacher importance weights 对学生采样动作做无偏 advantage-weighted 监督，不增加额外 rollout 或 reward 评估。

**关键结果**：在 math、coding、MedQA 任务上，AOPD 在外部教师和自蒸馏两种设置下均优于标准蒸馏和 RL 基线，保持与 OPD 相同的 rollout 效率。
