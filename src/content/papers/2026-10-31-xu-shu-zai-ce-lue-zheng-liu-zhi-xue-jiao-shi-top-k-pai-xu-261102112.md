---
title: Order-Only On-Policy Distillation
title_zh: 序数在策略蒸馏：只学教师 Top-K 排序
authors:
- Guangzeng Han
- Yu Wu
- Xiaolei Huang
affiliations:
- University of Memphis
- University of Missouri
arxiv_id: '2611.02112'
url: https://arxiv.org/abs/2611.02112
pdf_url: https://arxiv.org/pdf/2611.02112
published: '2026-10-31'
collected: '2026-11-04'
category: Training
direction: LLM 知识蒸馏 · 序数监督
tags:
- Knowledge Distillation
- On-Policy Distillation
- Ranking Loss
- LLM
- Temperature Invariant
one_liner: O3PD 在策略蒸馏中只复现教师 top-K token 排序，不拟合概率值，对温度不变并在数学推理上全面优于 OPD
practical_value: '- 在蒸馏 LLM 到线上小模型时，不要强制小模型拟合教师 soft probabilities 的绝对数值，尤其当教师温度需要搜索时；改用
  top-K 排序监督（如 ListMLE、RankNet）可省去温度调参，训练更稳定。

  - 生成式推荐/query 生成的 on-policy 蒸馏中，教师概率值混杂其自身校准与置信度，小容量学生难以复现；只保留序数信息能降低容量要求，让模型专注学习候选
  token 的相对好坏，适合电商 query 推荐、广告文案生成、推荐理由生成等场景。

  - 若已有 OPD 流水线，可将 loss 替换为对 teacher top-K logits 的 ranking loss，保留 on-policy 生成模式；数学推理任务上的
  +2.9 平均分提升说明该 trick 在复杂生成任务上可能有效。

  - 对 Agent 策略蒸馏的启示：当学生策略模型容量有限时，教师动作分布的序数偏好可能比概率值更重要，可以在策略优化中借鉴序数监督。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：On-policy distillation (OPD) 让学生在自己生成的 prefix 上匹配教师 token 概率。但概率值同时编码教师偏好和置信度，后者依赖教师容量与校准，小模型难以复现；且温度改变概率值而不改变排序，OPD 对温度选择敏感。作者质疑：是否只需要教师的候选 token 排序？

**方法关键点**：提出 O3PD，在每个学生生成的 prefix 处，训练学生复现教师 top-K token 的序关系（p(v1)>p(v2)>...>p(vK)），不拟合概率数值。目标对教师温度保持不变，无需温度调参。其他 ranking loss（如 ListMLE、RankNet）也适用，核心是序数监督。

**关键结果**：跨六个教师-学生对，O3PD 在 HMMT25、AIME24、AIME25 的平均分上每对都优于 OPD，最高提升 2.9 分；AIME25 上最大提升 5.6 分。替换为其他 ranking loss 仍有一致增益，表明收益来自序数监督本身。分析显示 O3PD 偏离教师概率分布更远，但更忠实地复现排序，学生更强——说明迁移知识在于 ranking 而非概率值。
