---
title: Learning Dynamics of On-Policy Distillation
title_zh: On-Policy 蒸馏的学习动力学分析
authors:
- Guan Zhe Hong
- Sumeet Ramesh Motwani
- Liang Chen
- Yangchen Pan
- Junchi Yu
- Jialin Yu
- Philip Torr
- Yi Ren
affiliations:
- University of Oxford
- EPFL
- City University of Hong Kong
arxiv_id: '2611.08016'
url: https://arxiv.org/abs/2611.08016
pdf_url: https://arxiv.org/pdf/2611.08016
published: '2026-11-05'
collected: '2026-11-06'
category: Training
direction: On-policy 蒸馏学习动力学与后训练
tags:
- On-policy Distillation
- Learning Dynamics
- Knowledge Distillation
- LLM Post-training
- Feedback Loop
one_liner: 拆解 OPD 的“参数更新”与“rollout 分布广播”两阶段，揭示离线预热可避免退化并带来准确率提升
practical_value: '- 在生成式推荐或对话式 Agent 的策略蒸馏中，直接采用 on-policy 蒸馏会导致学生 rollout 分布随更新漂移，可能使生成质量下降；建议先用离线蒸馏预训练学生策略，再少量
  OPD 微调，兼顾分布稳定与最终准确率。

  - 监控 OPD 过程中“局部 teacher 一致率”与“成功续写概率”的背离：若更新提升了对 teacher 分布的匹配，却增大了无效轨迹概率，后续 rollout
  会暴露于低质量监督，需通过 reward/过滤机制或 trust region 限制此类更新。

  - 将蒸馏信号的影响拆成 conversion（梯度更新对当前前缀的响应）和 broadcast（跨前缀泛化与状态分布重塑），用于诊断学生响应不足或二次退化；在业务中可类似地分阶段分析训练动态，而不仅看
  loss 下降。

  - 离线蒸馏即使不能立刻提升 held-out 指标，也可作为 OPD 的预热步骤，这提示业务中不要因为离线蒸馏即时收益小就跳过它，它可能为在线阶段提供必要的参数几何条件。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：On-policy distillation（OPD）在 LLM 后训练中愈发重要，它结合稠密 teacher 监督与学生生成轨迹上的训练，但学生每次更新都会改变自身行为并重塑后续 rollout 分布，这个反馈回路如何影响学习和泛化仍不清楚。

**方法关键点**：将 OPD 学习动态拆为两个阶段：conversion——蒸馏信号如何转化为参数更新；broadcast——更新如何跨前缀改变预测并重塑 rollout 分布。基于该框架分析两类现象：一是尽管 teacher-student 分歧很大，学生响应仍然有限；二是某些更新虽提升局部 teacher 一致性，却也增加失败续写概率，使后续 rollout 暴露于不可靠监督，导致退化。

**关键结果**：离线蒸馏可以在不显著提升即时 held-out 准确率的情况下，为后续 OPD 做好准备；单独 OPD 可能降低生成质量，但经过足够离线准备后能带来显著的准确率提升。因果链条将 teacher 监督、学生几何与演化 rollout 分布连接起来，解释了 OPD 何时有效、何时退化。
