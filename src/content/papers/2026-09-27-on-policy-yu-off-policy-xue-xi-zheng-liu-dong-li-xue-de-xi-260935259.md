---
title: On-Policy or Off-Policy Learning? A Systematic Study of Distillation Dynamics
title_zh: On-Policy 与 Off-Policy 学习：蒸馏动力学的系统研究
authors:
- Julianna Piskorz
- Antonin Berthon
- Mihaela van der Schaar
affiliations:
- University of Cambridge
arxiv_id: '2609.35259'
url: https://arxiv.org/abs/2609.35259
pdf_url: https://arxiv.org/pdf/2609.35259
published: '2026-09-27'
collected: '2026-10-03'
category: Training
direction: 蒸馏训练策略对比
tags:
- on-policy distillation
- off-policy distillation
- forward KL
- reverse KL
- catastrophic forgetting
- strong-to-weak distillation
one_liner: 在强到弱蒸馏中解耦 rollout 策略、KL 方向和 learning rate，发现 on-policy 无一致优势，forward KL
  更鲁棒，learning rate 主导遗忘与稀疏性
practical_value: '- 在构建领域 LLM 蒸馏流水线（如将大模型蒸馏到线上小模型用于 query 理解或文案生成）时，优先使用 forward KL
  + off-policy 数据：成本低且对 rollout 策略鲁棒，不必频繁生成 on-policy 样本。

  - 控制 learning rate 是平衡效果与灾难性遗忘的关键旋钮；如果微调后通用能力下降，先调低 learning rate，而不是转向 on-policy
  采样。

  - 如果需要提升模型对更难任务（如从简单商品描述生成到复杂营销文案）的泛化，可适量引入 on-policy 数据，但注意后续若接 RLVR，该优势可能消失。

  - 若要抑制教师模型的风格/偏见迁移（如避免推荐文案出现不符合品牌调性的表达），可考虑 on-policy rollouts + reverse KL 组合。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
过去普遍认为 on-policy 学习可以减少灾难性遗忘、产生更稀疏的参数更新并提升泛化，但大量证据来自 SFT 与 RLVR 的对比，混淆了目标函数、监督密度、优化器等变量。因此需要控制实验来隔离 rollout policy 的真实作用。

**方法关键点**  
- 在 strong-to-weak distillation 框架下，固定教师模型，仅改变学生训练数据生成策略：OffPD 用教师 rollout，OnPD 用学生 rollout。
- 独立变化 token-level KL 方向：forward KL（mode-covering）和 reverse KL（mode-seeking），并控制 learning rate（1e-5 与 5e-5）。
- 使用 Llama-3.1-8B 教师蒸馏到 Llama-3.2-1B 学生，Qwen2.5-7B 到 1.5B；任务包括 MedReason、Science、Countdown。
- 额外引入 rollout-policy spectrum 参数 λ，从教师偏好到学生偏好连续插值，以研究渐变影响。

**关键结果数字**  
- 最终 ID 准确率：OnPD 最高 72%，OffPD 73%；forward KL 稳定在 71-73%，reverse KL 波动 35%-72%。
- 灾难性遗忘：低学习率下 OOD 变化不超过 1.3 个百分点；高学习率下降 11.2-14.0 个百分点；rollout policy 差异远小于 learning rate。
- 更新稀疏度：低学习率 85.3-89.6%，高学习率 51.9-60.0%；OffPD 在所有匹配比较中至少与 OnPD 一样稀疏。
- 在 rollout-policy spectrum 上，forward KL 保持 80% 以上准确率，仅波动 5.2 个百分点；reverse KL 显著敏感并偏好学生 rollout。
- 泛化到更难 Countdown 变体时，on-policy 在两种 KL 方向上均带来 10-15% 的 pass@k 提升，但后续 RLVR 后优势不持久。
- 鲁棒性：移除梯度裁剪、改用 sampled KL、更长推理链任务，结论基本不变。

**最值得记住的一句话**  
在蒸馏中选择 KL 方向和 learning rate 比 rollout policy 更重要；on-policy 的价值高度依赖于目标、评估设置和优化超参数。
