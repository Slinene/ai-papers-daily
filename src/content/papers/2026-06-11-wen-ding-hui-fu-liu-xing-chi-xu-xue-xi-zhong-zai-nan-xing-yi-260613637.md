---
title: 'The Stable Recovery Manifold: Geometric Principles Governing Recoverability
  in Continual Learning'
title_zh: 稳定恢复流形：持续学习中灾难性遗忘的几何原理
authors:
- Ayushman Trivedi
- Bhavika Melwani
arxiv_id: '2606.13637'
url: https://arxiv.org/abs/2606.13637
pdf_url: https://arxiv.org/pdf/2606.13637
published: '2026-06-11'
collected: '2026-06-14'
category: Training
direction: 持续学习灾难性遗忘的几何分析
tags:
- Continual Learning
- Catastrophic Forgetting
- Representational Geometry
- Subspace Analysis
- Accessibility Collapse
one_liner: 发现遗忘的知识保存在约 8 维低秩子空间，遗忘是几何可及性问题而非信息损毁。
practical_value: '- 对电商推荐模型持续更新：旧知识未真正消失，可以通过低秩子空间访问，不必全量重训，可设计轻量适配器恢复旧任务性能，降低频繁全量更新的成本。

  - 对 Agent 多任务学习：遗忘后通过主角度对齐就能大幅恢复性能，提示我们在微调 Agent 策略时保留旧策略的低维流形方向，可构建更稳健的持续学习系统。

  - 对生成式推荐（如 Semantic ID 生成）：模型更新后旧 item ID 生成能力仍存于低维子空间，可恢复旧码本映射，避免冷启动和遗忘。

  - 主要学术贡献，业务可借鉴点在于遗忘可逆性的认知转变，具体工程落地仍需进一步验证。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：传统观点认为灾难性遗忘是知识的永久破坏，但前作提出“可及性崩塌”假说，认为遗忘的知识仍可通过探测恢复。本文进一步探究该可恢复知识的几何结构与时间动态。

**方法**：使用 ResNet-18 在 Split CIFAR-100 上顺序训练十个任务，定义恢复子空间维度 k_t（保留 90% 探测性能所需最小奇异方向数），测量可恢复性、表示漂移、恢复复杂度等指标；提出稳定恢复流形（SRM）假说，并构建几何模型解释可恢复性方差。

**关键结果**：恢复子空间维度非常稳定（均值 8.0，标准差 0.82），并未随任务增多而增长，推翻作者自己的“可恢复性扩散”假说。主角度漂移与可恢复性高度负相关（r = -0.862）；一个仅含三个几何变量的简单模型解释了 82.2% 的可恢复性方差。深度分层结果显示网络各层参与比例不同，解释了层次保留机制。最终结论：遗忘主要是可及性和流形对齐问题，而非信息丢失。
