---
title: A Fix for Softmax and Cross-Entropy
title_zh: softmax 与交叉熵的数值修复：消除梯度塌缩与抵消
authors:
- Jonathan T. Barron
- Dan Gnanapragasam
- Michael Tschannen
affiliations:
- Google DeepMind
arxiv_id: '2610.31642'
url: https://arxiv.org/abs/2610.31642
pdf_url: https://arxiv.org/pdf/2610.31642
published: '2026-10-22'
collected: '2026-10-23'
category: Training
direction: 数值稳定训练 · softmax/CE 修复
tags:
- softmax
- cross-entropy
- numerical stability
- knowledge distillation
- grokking
- AdamW
one_liner: 修复 softmax/cross-entropy 的两个数值 bug，消除 Slingshot 尖刺与蒸馏漂移
practical_value: '- 在大规模多分类/生成式推荐训练（含 bf16）中，若出现 loss 精确为 0、梯度不对称或 Slingshot 尖刺，优先检查
  logit margin 是否超过精度悬崖：bf16 约 5.5，fp32 约 16.6。可直接替换 CE 为论文的稳定实现：loss=softplus(-margin)，margin=-logsumexp(非目标
  logits - 目标 logit)，保证 target logit 梯度不归零且梯度严格零和。

  - 做知识蒸馏（如 LLM 教师蒸馏排序模型、语义 ID 蒸馏、ctr 蒸馏）时，学生接近教师时标准 soft-target CE 会因 q-p 相减产生非零噪声梯度，导致学生漂移；应改用
  log-space 直接计算 q-p 的实现（expm1/log1p），保证 zS=zT 时梯度为 0，bf16 下尤其重要。

  - AdamW/Adam 训练时 logit margin 最终会稳定在 log(1/ε)，若 ε=1e-8 则 margin≈18.4，略高于 fp32 悬崖；可通过调整
  ε 避开精度悬崖或使用稳定 CE，避免高置信度下的隐性优化问题。

  - 该修复为 drop-in 替换、无额外计算开销，建议直接用于训练框架的 CE 实现，防止高置信度场景的数值退化。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

## 动机
标准 softmax、log-softmax 和 cross-entropy 实现存在两个数值 bug：Softmax Collapse 在目标 logit 远大于其他 logit 时，把 target 梯度舍入为 0，梯度不再零和；Softmax Cancellation 在学生 logits 接近教师 logits 时，因 q 与 p 分别计算再相减而损失精度，产生非零梯度。这两个问题会导致 grokking 中的 Slingshot 尖刺、蒸馏中学生网络漂移，以及训练不稳定。

## 方法关键点
- 针对 **Softmax Collapse**：不把最大 logit 的 exp(0)=1 加进分母，改用 softplus(-margin)。对于 hard-target CE，令 margin = -logsumexp(非目标 logits - 目标 logit)，loss = softplus(-margin)。这样 target 梯度 = -sum(非目标梯度)，严格零和，且在 fp32/bf16 下不归零。
- 针对 **Softmax Cancellation**：在 soft-target CE 中直接用 log-space 计算 q-p，利用 expm1、log1p 避免相近概率相减。令 δ=zS-zT，d=δ-sum(pδ)，s=d-log1p(sum(p expm1(d)))，u=p expm1(s)，最后校正零和。zS=zT 时梯度精确为 0。
- 所有修复不增加内部精度，不影响速度，可 drop-in 替换。

## 关键结果
- 在 a+b mod 31 上，fixed CE 在所有精度（bf16/fp32/fp64）达到 100% 测试准确率，而 standard CE 在 fp32 ε=1e-8 时仅为 94.3%；ε=1e-16 时甚至 fp64 standard 也失败（97.2% vs fixed 99.0%）。
- 无权重衰减的 a²+b² mod 97 实验中，standard CE 在触及 fp32 悬崖后测试准确率从 61% 掉到 23%，fixed 继续升至 85%。
- 蒸馏实验中，学生初始化为教师权重，standard soft-target CE 在 bf16 下产生 KL 尖峰并降低准确率，fixed 保持 KL=0 和 100% 准确率。
- 理论发现：AdamW 作用下 logit margin 收敛到 log(1/ε)，默认 ε=1e-8 对应 margin≈18.4，略高于 fp32 悬崖 16.6。

最值得记住的一句话：**高置信度下 softmax/cross-entropy 的数值 bug 不是边缘问题，而是会触发优化器失稳的根本原因；用 softplus/log-space 实现即可彻底修复。**
