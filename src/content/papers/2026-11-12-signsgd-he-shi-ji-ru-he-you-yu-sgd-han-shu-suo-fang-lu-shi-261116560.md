---
title: 'When and How SignSGD Outperforms SGD: A Functional Scaling Law Perspective'
title_zh: SignSGD 何时及如何优于 SGD：函数缩放律视角
authors:
- Zilin Wang
- Binghui Li
- Jia-Nan Wang
- Lean Wang
- Jinbo Wang
- Lei Wu
affiliations:
- Peking University
- AI for Science Institute, Beijing
arxiv_id: '2611.16560'
url: https://arxiv.org/abs/2611.16560
pdf_url: https://arxiv.org/pdf/2611.16560
published: '2026-11-12'
collected: '2026-11-15'
category: Training
direction: 优化算法 · 函数缩放律
tags:
- SignSGD
- Functional Scaling Law
- Optimization
- LLM Pre-training
- Noise-Induced Preconditioning
one_liner: 用函数缩放律揭示 SignSGD 通过噪声诱导预条件将有效 Hessian 变为 H^{1/2} 的权衡与优势
practical_value: '- 优化器选型：在训练广告/推荐场景的大模型骨干（如 LLM 编码器、多模态表征）时，可尝试 Lion/Muon 等 sign-based
  优化器；尤其在难任务、长尾 item 学习或高梯度噪声场景下，可能获得更好数据效率。建议先在小规模 scaling 实验上验证。

  - 大 batch 训练：业务上为利用 GPU 常被迫加大 batch size；SignSGD 在更大 batch 下仍能保持数据效率，固定数据预算时所需训练步数更少，适合加速召回/粗排大
  embedding 模型的迭代。

  - 缩放律指导：FSL 把学习过程分解为信号学习与噪声遗忘，可用小样本拟合 scaling law 的方式预判不同 batch size 和优化器下的 loss
  曲线，低成本选择训练配置；可建立内部优化器-缩放曲线库。

  - 保留梯度噪声：sign 操作依赖梯度噪声实现平滑和预条件，实际训练中不要过度追求 small batch/full-batch 去噪，应保留适当随机噪声，并配合合理的
  weight decay 与学习率调度。'
score: 6
source: arxiv-stat.ML
depth: abstract
---

动机：SignSGD、Lion、Muon 等 sign-based 优化器在大规模训练中越来越受重视，但何时以及为何相对 SGD 更优缺少理论解释。

方法：在具有对角特征的幂律核回归框架下，建立 SignSGD 的函数缩放律（FSL），将学习动态拆分为信号学习和噪声遗忘两个过程。核心机制是噪声诱导预条件：梯度噪声平滑 sign 算子，使优化等价于一个预条件 SGD，且有效 Hessian 从 H 被变换为 H^{1/2}。

结果：该机制带来更快的信号学习，但更慢的噪声遗忘，从而形成与任务难度和 batch size 相关的比较：在难任务 regime，SignSGD 数据效率优于 SGD；在容易任务 regime，两者数据效率相同，但 SignSGD 在更大 batch size 下保持该效率，固定数据预算时所需优化步数更少。

实验：幂律核回归实验支持该机制及预测的缩放行为；LLM 预训练实验进一步表明，SignSGD FSL 比原始 SGD FSL 能更好地捕捉 sign-based 优化器的 batch size 依赖损失动态。
