---
title: On the Off-Policy Teacher in On-Policy Distillation
title_zh: On-Policy 蒸馏中的 Off-Policy 教师模型问题与 SCOUT 框架
authors:
- Langlin Huang
- Hao Liu
- Mononito Goswami
- Xinyu Li
- Prithwith Jana
- Nikos Kanakaris
- Patrick Blöbaum
- Purak Jain
affiliations:
- Washington University in St. Louis
- AWS AI Labs
- Carnegie Mellon University
- Georgia Institute of Technology
arxiv_id: '2609.38360'
url: https://arxiv.org/abs/2609.38360
pdf_url: https://arxiv.org/pdf/2609.38360
published: '2026-09-28'
collected: '2026-10-01'
category: Training
direction: LLM 蒸馏训练 · 教师自适应
tags:
- On-Policy Distillation
- Teacher Adaptation
- GRPO
- LLM Distillation
- Reinforcement Learning
- Reasoning
one_liner: 提出 SCOUT：周期性地用学生前缀对教师做结果奖励 RL，缓解教师 off-policy 问题，提升蒸馏效果
practical_value: '- 当用强 LLM 蒸馏小模型做生成式推荐/query 改写/Agent 策略时，教师面对学生生成的中间状态（候选商品序列、推理链）可能给出不可靠的
  token 分布。可参考 SCOUT：让学生采样轨迹，取前缀交给教师继续 rollout，用业务可验证奖励（如点击、转化、代码测试结果）做 RL 更新教师，提升教师在这些状态上的监督质量。

  - 工程上教师无需每一步同步：每 10 步学生更新后更新一次教师即可保持大部分收益，降低训练成本；前缀长度可以线性递增，从短前缀开始逐渐暴露长序列，避免早期训练过难。

  - 若教师是黑盒 API 不可更新，SCOUT 不直接适用，但可以考虑 prompt-based 教师适配或改用可训练的小教师；该方法与已有 loss 级监督信号修改（如信任区域、加权）正交，可以叠加使用。

  - 不要把增益简单归因于额外的教师训练：如果没有在学生前缀上条件化教师更新，仅做 same outcome-reward GRPO 提升有限，说明适配学生分布才是关键。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
On-policy distillation (OPD) 让学生从自身策略采样的轨迹中学习，同时由更强教师提供 token 级监督。但教师是在自身策略分布上优化的，面对学生生成的前缀属于 off-policy 状态；随前缀长度增加，教师 continuation 准确率下降、熵升，监督可靠性降低。现有方法冻结教师，通过截断、加权等调节何时相信监督，但未直接优化教师本身。

**方法关键点**  
- SCOUT 保留标准 OPD 的学生更新，每隔 f 步增加一次教师侧 RL 更新。  
- 从学生轨迹中取前缀 p^S，教师从 p^S 继续生成 K 条补全，使用可验证结果奖励通过 GRPO 更新教师，梯度只作用于教师生成的 continuation tokens。  
- 更新后的教师同步回 OPD 为学生提供下一轮监督，形成学生-教师协同训练。  
- 训练中线性增加学生前缀比例，从短前缀开始逐步增加难度。

**关键实验与数字**  
在数学推理（AIME 2024/2025、AMC23、HMMT、OlympiadBench、MATH-500）和代码生成（LiveCodeBench v5、HumanEval+、MBPP）上，使用 Qwen3-4B/8B 和 Skywork-OR1-Math-7B 等多对师生配置。对比 OPD、GRPO、ESR、Prune-OPD、Relay-OPD 等。SCOUT 在所有设置下优于基线：数学平均准确率提升 1.2–2.6 点，代码从 56.6 增至 59.7。消融显示，同样的教师 RL 更新但不以学生前缀为条件（OPD + Teacher GRPO）只带来微弱提升，说明学生状态条件化是关键；教师更新间隔 1/5/10 步效果接近，20 步下降；与 OPTR 组合有互补提升。最值得记住：教师对学生的 off-policy 可通过让其在该分布上进行结果奖励 RL 来缓解，且不需要频繁更新。
