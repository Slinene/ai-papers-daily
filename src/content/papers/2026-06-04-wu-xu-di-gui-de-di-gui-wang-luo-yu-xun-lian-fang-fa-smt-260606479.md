---
title: Pretraining Recurrent Networks without Recurrence
title_zh: 无需递归的递归网络预训练方法 SMT
authors:
- Akarsh Kumar
- Phillip Isola
affiliations:
- MIT
arxiv_id: '2606.06479'
url: https://arxiv.org/abs/2606.06479
pdf_url: https://arxiv.org/pdf/2606.06479
published: '2026-06-04'
collected: '2026-06-07'
category: Training
direction: RNN 预训练 · 长程依赖优化
tags:
- SMT
- RNN
- BPTT
- pretraining
- long-range dependencies
- gradient stability
one_liner: SMT 将 RNN 训练转化为有监督记忆转移学习，实现时间并行且梯度路径 O(1) 稳定训练长程依赖
practical_value: '- 电商用户行为序列（点击、购买）建模可用 SMT 稳定训练长序列 RNN，缓解梯度问题，捕获更长期的兴趣演化。

  - SMT 的时间并行训练特性可大幅加速大规模用户序列的 RNN 预训练，适合百万级序列场景。

  - 解耦“记忆内容”与“更新规则”的设计可借鉴为记忆网络优化：使用一个独立模块（如 Transformer）预先压缩历史为预测性状态，再教 RNN 逐步更新。

  - 若业务中已有 Transformer 模型，可将 SMT 视为一种离线知识蒸馏方案，将 Transformer 的长程能力注入 RNN 以提升在线推理效率。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：RNN 训练依赖于 BPTT，它在时间上顺序展开，难以并行化，且梯度路径长达 O(T)，导致长程依赖学习困难。

**方法**：提出 Supervised Memory Training (SMT)，核心思路是将 RNN 的训练拆为两步：
1. 用一个 Transformer 编码器-解码器，以“预测性状态”为目标进行训练：编码器从过去序列中提取仅对未来预测必要的信息，生成每一步的记忆标签（memory label）$(m_t, x_{t+1})\rightarrow m_{t+1}$。
2. 此后的 RNN 训练完全退化为有监督的一步回归/分类：直接拟合这些记忆转移标签，无需在时间上展开 RNN，因此梯度路径长度为 O(1)，稳定且可并行。

**结果**：在语言建模和像素序列建模任务上，SMT 预训练的多种非线性 RNN 在长程依赖上优于 BPTT，且训练可全并行化，验证了其在大规模序列建模中的潜力。
