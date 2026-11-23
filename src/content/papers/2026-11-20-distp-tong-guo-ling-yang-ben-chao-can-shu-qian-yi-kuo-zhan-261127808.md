---
title: '$\mathtt{DistP}$: Scaling Local-Update Training with Zero-Shot Hyperparameter
  Transfer'
title_zh: DistP：通过零样本超参数迁移扩展本地更新训练
authors:
- Andrej Jovanović
- Alex Iacob
- Philipp Wiesner
- Christophe Roux
- Max Zimmer
- Lorenzo Sani
- Sebastian Pokutta
- Nicholas D. Lane
affiliations:
- University of Cambridge
- Science of Fundamental AI Research Lab (SOFAIR)
- Zuse Institute Berlin (ZIB)
- CNRS - ENS, PSL Research University, INRIA
- Flower Labs
arxiv_id: '2611.27808'
url: https://arxiv.org/abs/2611.27808
pdf_url: https://arxiv.org/pdf/2611.27808
published: '2026-11-20'
collected: '2026-11-23'
category: Training
direction: 大规模分布式训练 · 超参数迁移
tags:
- local-update training
- hyperparameter transfer
- zero-shot
- distributed training
- learning rate scaling
- communication-efficient training
one_liner: 提出 DistP 理论框架，为本地更新训练提供零样本超参数迁移规则，实现跨尺度稳定的学习率缩放
practical_value: '- 在电商广告推荐的大规模模型训练中，若采用 local-update（多步本地训练后同步）降低通信开销，可直接复用 DistP
  的学习率迁移规则：小模型上调好的内部学习率可迁移到更大宽度/深度模型，避免在目标规模上重新扫描超参。

  - 全局 batch size 增加时，区分两种情况：增加每个 worker 的 local batch 使用平方根学习率缩放；增加 worker 数量则保持参考学习率不变。这一
  trick 可指导工程上的分布式扩展，避免盲目线性缩放。

  - 外部优化器选择影响调参成本：使用 averaging 或 Adam 作为外部优化器时，宽度/深度迁移更稳定；若使用带 momentum 的优化器，改变 batch
  size 或 local steps 可能需要联合调整内外学习率，建议优先选 averaging/Adam 以减少调参负担。

  - 同步间隔（local steps）改变时，内部学习率可直接迁移，无需重新调整；在通信受限的跨机房/联邦学习场景中，可据此快速调整同步频率而不牺牲性能。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

## 动机
DDP 每个优化步前同步梯度，在低带宽网络中成为瓶颈。本地更新方法让 worker 本地多步训练后再通信，减少同步开销，但引入额外超参数，调参成本高。零样本超参数迁移在 DDP 中有效，能否用于本地更新训练并不明确。

## 方法关键点
提出 DistP 理论框架，将 DDP 的迁移规则扩展到本地更新训练，覆盖 worker 数量、local steps 和外部优化器三个维度。核心发现：以 averaging 为外部优化器时，学习率可跨模型宽度和深度迁移，同时提升模型质量；调优的内部学习率可直接跨同步间隔迁移；全局 batch size 增大时，若来自更大 local batch 则内部学习率按平方根缩放，若来自更多 workers 则保持固定参考速率。进一步将宽度/深度迁移推广到 Adam 等其他外部优化器，实现稳定扩展。但外部优化器含 momentum 时，改变 batch size 或 local steps 可能需要内外学习率联合调参。

## 关键结果数字
在 823M 参数语言模型实验中，相对未在更大规模重新调参的 baseline，DistP 将验证损失降低 8.1%，平均下游准确率提升 10%。拟合的扩展律显示，该优势随计算预算增长而扩大，验证了 DistP 对通信高效训练的可扩展性价值。
