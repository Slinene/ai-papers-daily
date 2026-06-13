---
title: 'Phase Transitions in Attention: A Bayesian Theory of Copy Head Emergence'
title_zh: 注意力中的相变：复制头涌现的贝叶斯理论
authors:
- Itay Lavie
- Kirsten Fischer
- Andrey Lekov
- Frederic Van Maele
- Zohar Ringel
- Moritz Helias
affiliations:
- Racah Institute of Physics, Hebrew University of Jerusalem
- John A. Paulson School of Engineering and Applied Sciences, Harvard University
- Institute for Advanced Simulation (IAS-6), Computational and Systems Neuroscience,
  Jülich Research Center
- Institute of AI for Health, Helmholtz Munich
- RWTH Aachen University
arxiv_id: '2606.12058'
url: https://arxiv.org/abs/2606.12058
pdf_url: https://arxiv.org/pdf/2606.12058
published: '2026-06-10'
collected: '2026-06-13'
category: Training
direction: Transformer 注意力机制训练动力学
tags:
- phase transition
- attention mechanism
- Bayesian theory
- in-context learning
- induction head
- training dynamics
one_liner: 用贝叶斯框架证明 softmax 注意力在复制任务上随数据量出现一阶相变，解释了复制头的突然涌现
practical_value: '- 主要是基础理论贡献，对电商/Agent/推荐系统的直接工程迁移有限。

  - 理解 ICL 能力涌现的相变特性，可在训练 Agent 时监控注意力序参量，辅助决定数据投入与 checkpoint 选择。

  - 线性注意力与 softmax 注意力的不同相变行为（二阶 vs 一阶）提示：若需要训练过程更平滑，可考虑线性注意力变体，但需权衡最终性能。'
score: 7
source: arxiv-stat.ML
depth: abstract
---

**动机**：Transformer 的上下文中学习能力常以注意力模式在训练中突然涌现的形式出现，但这一过程缺乏第一性原理的解释。

**方法**：作者提出一个贝叶斯理论来分析单层 softmax 注意力网络在复制任务上的学习。通过将注意力矩阵的后验分布封闭形式简化为低维序参量空间，揭示了训练数据量上的相变。该理论分别用贝叶斯采样和 Adam 标准训练进行了验证。

**关键结果**：Softmax 注意力呈现一阶相变，即复制头在某个数据量阈值处跳跃式出现；而线性注意力先经历二阶相变，随后平滑过渡到结构化的注意力模式（crossover）。这首次从统计力学角度定量解释了 LLM 训练中观察到的复制子电路的突然涌现。
