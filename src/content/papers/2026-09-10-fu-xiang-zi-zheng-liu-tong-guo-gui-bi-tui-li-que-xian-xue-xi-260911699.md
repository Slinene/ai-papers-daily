---
title: 'Negative Self-Distillation: Learning to Reason by Avoiding Flaws'
title_zh: 负向自蒸馏：通过规避推理缺陷学习推理
authors:
- Rongcan Pei
- Zhepei Wei
- Shuyao Xu
- Xinyu Zhu
- Wei-Lin Chen
- Yu Meng
affiliations:
- University of Virginia
- Stanford University
arxiv_id: '2609.11699'
url: https://arxiv.org/abs/2609.11699
pdf_url: https://arxiv.org/pdf/2609.11699
published: '2026-09-10'
collected: '2026-09-11'
category: Training
direction: LLM 负向自蒸馏与推理增强
tags:
- Negative Self-Distillation
- Unlikelihood Training
- Reasoning
- Token-Level Gating
- Label-Free Training
one_liner: 用模型自生成负向条件并做门控 unlikelihood，无需标签即可稳定提升 LLM 数学推理，同时保留反思能力
practical_value: '- 负向条件生成替代稀缺正反馈：在搜索 query 补全、广告文案、商品标题生成中，很难获得 ground-truth。可以让同一个
  LLM 扮演“低转化/不相关/粗心生成器”作为 negative teacher，对真实生成做对比训练，在无标注预算下避开坏模式。

  - 动态 token 门控值得复用：对比负向 condition 与中性 reference 在每个生成 token 上的概率，只惩罚对负向注入敏感的关键 token（如
  query 中的类目词、价格带、促销词），避免对停用词和语法 token 施加损失导致文案流畅性崩塌。工程上只需要额外一次并行前向，标量实现。

  - Sigmoid bounded unlikelihood 可作为稳定化 trick：替换原始 -log(1-p) unlikelihood，能自动抑制高置信语法
  token 的梯度，防止推荐解释/文案生成模型在微调后期崩溃；可低成本加到 DPO/GRPO 式损失中。

  - 效率经验：单 rollout + 共享权重的 reference/negative teacher 并行 prefill + 标量 token 损失，比 GRPO(n=8)
  和 OPSD(top-k logit 对齐) 更省时；如果采样是瓶颈，可以先用离线噪声负条件（如 wiki-irr）把每步训练从 68s 降到 54s，性能基本不降。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**

OPSD 依赖 privileged teacher 模仿正确答案，会压制不确定性和自我修正，导致复杂推理退化；RLVR 有稀疏奖励和采样开销，外部 teacher 又难以获取。需要一种无标签、更稳定的自举训练方式，让模型主动避开缺陷而不是模仿正确答案。

**方法关键点**

- 对每个问题 x，先从学生采样 y_init，再在线生成负向条件 n（如“请粗心推理，错误计算质因数分解…”），把同一模型的 π_ref 与带 n 的 π_neg 构造为 reference/negative teacher。
- 动态 token 门控 G_t = max(0, π_neg(yt)−π_ref(yt))，只惩罚负向条件概率提升的 token，过滤标点、语法等语言先验 token。
- 用 Sigmoid 有界 unlikelihood：L_GU = G_t/(2−π_θ(yt))，让高置信 token 梯度趋零，低中置信 reasoning-critical token 获得更强信号。
- 加 token 级 KL 正则 π_ref log(π_ref/π_θ) 防训练崩溃；最终 L_NSD = L_GU + α L_KL。

**关键结果**

在 MATH 上做 2 epoch 无标签训练，Qwen3-1.7B/4B/8B 上 7 个数学基准平均提升 2.3%/7.5%/6.0%；4B 的 AIME 2024 从 23.8 到 35.8，8B 从 28.8 到 39.6。反思 token 频率 NSD 7.5 vs OPSD 2.2 vs Intuitor 0.8（base 3.6）。训练每步 68s，比 OPSD 105s、Intuitor 187s 更省；离线 question-only/wiki-irr 负条件仍可 +7.3%/+6.6%。

**最值得记住的一句话**：与其模仿有正确答案的老师，不如让模型主动离开自生成的缺陷轨迹，并用 token 级门控保护语言先验。
