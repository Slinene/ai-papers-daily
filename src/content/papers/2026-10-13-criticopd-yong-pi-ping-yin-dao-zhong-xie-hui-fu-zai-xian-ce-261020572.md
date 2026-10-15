---
title: Recovering Reliable Supervision via Critique-Guided On-Policy Distillation
title_zh: CriticOPD：用批评引导重写恢复在线策略蒸馏的可靠监督
authors:
- Kaixiang Zhao
- Tianrun Yu
- Shangzhe Li
- Yuxiao Yang
- Amanda Hughes
- Weitong Zhang
- Taylor W. Killian
affiliations:
- Brigham Young University
- University of North Carolina at Chapel Hill
arxiv_id: '2610.20572'
url: https://arxiv.org/abs/2610.20572
pdf_url: https://arxiv.org/pdf/2610.20572
published: '2026-10-13'
collected: '2026-10-15'
category: Training
direction: On-policy distillation 可靠监督恢复
tags:
- On-policy Distillation
- Critique-Guided Rewriting
- Teacher Recoverability
- Privileged Information
- Mathematical Reasoning
- LLM Distillation
one_liner: 教师先批判错误，学生从最后错误处重写；教师带批判评分、学生无批判训练，显著提升数学推理蒸馏效果。
practical_value: '- 在电商/Agent 的生成式策略蒸馏中，不要直接对错误的学生轨迹做 token 级教师监督；先让强模型批判错误，截断到最后一个错误后重写，只蒸馏重写
  suffix，可避免教师跟错，并保持学生轨迹覆盖。

  - 把 critique/reference answer 当 privileged context：教师评分时可见，学生训练和上线都不可见，因此能利用更强反馈而不增加推理时延或
  prompt 长度；适合有可验证结果的任务，如 query 改写是否召回商品、结构化生成是否符合 schema、生成代码单测。

  - 若业务没有 reference answer，可用 reward model、人工反馈或转化标签替代，但批判质量决定收益；论文显示 73–81% 的 valid
  error flags 即可带来显著提升。

  - 选择“只监督重写后缀、保留错误前缀”的做法，比提前截断或教师接管更接近推理分布；在在线学习或 agent 轨迹蒸馏时可作为降低 occupancy mismatch
  的工程原则。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
On-policy distillation (OPD) 假设教师能从学生任意前缀恢复正确解，但该假设在错误 rollout 上失效：教师虽能识别错误，却常跟着学生错误走。测量显示 Qwen3-4B 教师在学生错误前缀上的 recoverability 从 0.82 降至 0.29，而其 error-flag 精度稳定在 73–81%。因此需要在不引入更大 occupancy mismatch 的前提下恢复教师监督可靠性。

**方法关键点**
- 定义 recoverability Λ_T(h) 为教师从学生前缀 h 继续时的期望正确率，作为监督可靠性指标。
- CriticOPD：错误或超长 rollout 触发；教师带 reference answer 批判学生分段中的错误，定位最后错误段落；保留前缀到该段结束，学生带批判重写 suffix。
- 训练时教师带批判对 rewrite 评分；学生不带批判计算 log-prob，只对 suffix 做 reverse KL / sampled-token advantage。批判是 privileged information。
- 相比 truncation/takeover，所有被监督 token 仍由学生生成，occupancy mismatch 仅 0.16。

**关键结果**
- Qwen3-1.7B：OPD 50.08 → CriticOPD 54.65（+4.57）；Qwen3-0.6B：34.80 → 38.86（+4.06）。
- 竞赛题增益最大：AIME24/25、AMC23 分别 +6.01/+7.36/+6.94（1.7B）。
- 消融：去掉 critique 掉 5.90，教师无 critique 评分掉 1.19，教师写 suffix 掉 0.66。
- 批判将 correction vs continue 的 per-token advantage 从 +0.24 提升到 +1.47。

**最值得记住的一句话**
教师继续能力随错误前缀下降，但识错能力仍在；把 critique 作为 privileged info 让学生从最后错误处重写，是恢复 OPD 可靠监督而几乎不加 occupancy mismatch 的关键。
