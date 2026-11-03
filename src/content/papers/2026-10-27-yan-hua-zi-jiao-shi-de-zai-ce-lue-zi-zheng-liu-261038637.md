---
title: On-Policy Self-Distillation with Teacher Evolution
title_zh: 演化自教师的在策略自蒸馏
authors:
- Shufan Shen
- Zhongni Hou
- Chao Bi
- Yufei Zhang
- Guojun Yin
- Shuhui Wang
affiliations:
- State Key Lab. of AI Safety, Institute of Computing Technology, Chinese Academy
  of Sciences
- University of Chinese Academy of Sciences
- Meituan
arxiv_id: '2610.38637'
url: https://arxiv.org/abs/2610.38637
pdf_url: https://arxiv.org/pdf/2610.38637
published: '2026-10-27'
collected: '2026-11-03'
category: Training
direction: LLM 训练 · 自蒸馏教师进化
tags:
- Self-Distillation
- RLVR
- LLM Post-training
- Teacher Evolution
- Reward Sparsity
one_liner: 提出 Teacher-Evolution Self-Distillation，通过环境奖励优化自教师并自适应加权学生蒸馏，缓解 OPSD 训练停滞
practical_value: '- 在生成式推荐/Agent 的 RLVR 训练中，可将固定 self-teacher 的蒸馏改为带环境反馈的教师进化：teacher
  先 rollout，用任务正确性和上下文独立性构造 reward，再对 teacher 做优化，避免指导质量停滞。

  - 利用 teacher reward 估计指导可靠性，作为样本级权重：在 student 蒸馏损失中降低不可靠样本的权重，防止错误 token 分布被放大，适合落地到电商文案生成、query
  改写等 token 级 RL 训练。

  - 把“是否命中上下文无关的正确答案/动作”作为附加奖励信号，与序列级奖励结合，可缓解稀疏奖励与训练波动；尤其在在线学习或持续 post-training 的
  LLM 推荐/对话策略中值得尝试。

  - 若内部已有 on-policy 蒸馏或 LLM 推理训练流程，可引入 teacher-student 联合更新，但需注意用 adaptive weighting
  防止模型因可靠性估计偏差而 collapse。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：OPSD 通过对齐 student 与 self-teacher 的 token 级分布来缓解序列级 RL 的奖励稀疏，但训练中性能常停滞。原因在于模型自我教学能力有限，对部分样本生成不可靠指导。

**方法关键点**：TESD 让 self-teacher 生成 rollouts，并从环境获得基于任务正确性和上下文独立性的 reward。首先，以这些 reward 为训练目标执行 teacher-oriented optimization，持续增强教师的自我教学能力；其次，根据 reward 估计教师指导可靠性，在 student-oriented optimization 中自适应下调不可靠样本的权重。

**关键结果**：在多个数据集和模型规模上，TESD 一致优于代表性的 token 级和序列级方法，表明提升 OPSD 中监督质量对训练稳定性与最终性能至关重要。
