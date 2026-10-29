---
title: 'MuonGS: Pretraining LLMs with Relaxed Weight-Norm Control'
title_zh: MuonGS：放宽权重范数控制的LLM预训练优化器
authors:
- Athanasios Glentis
- Dawei Li
- Mingyi Hong
affiliations:
- University of Minnesota
arxiv_id: '2610.37647'
url: https://arxiv.org/abs/2610.37647
pdf_url: https://arxiv.org/pdf/2610.37647
published: '2026-10-27'
collected: '2026-10-29'
category: Training
direction: 优化器训练 · 权重范数控制
tags:
- Muon
- weight-norm control
- LLM pretraining
- Gram-Schmidt
- optimizer
one_liner: 用Gram-Schmidt移除Muon更新径向分量，权重范数最多√t增长，长期困惑度更低并加速LLM预训练约15%
practical_value: '- 训练电商/广告域的大模型（CTR、NLP、多模态等）时，可尝试用 MuonGS 替代 AdamW 或 MuonH，尤其在长训练
  horizon 下：MuonGS 不固定权重范数，省去严格范数约束的超参调优，同时保持后期有效学习率，可能降低最终损失。

  - 把累积有效学习率 C_T = Ση_t/||W_t||_F 作为监控指标：如果训练后期 C_T 增长明显放缓（对数增长），说明有效学习率相对权重范数过小，可考虑放松范数控制、调整学习率或改用
  MuonGS 类方法。

  - 对推荐模型中的矩阵参数，Muon 类优化器可直接作用于 2D 权重；但 embedding 表通常是高维稀疏结构，需先验证 Gram-Schmidt 投影在混合参数上的工程开销，建议小规模预训练对比后再推广。

  - 结论上，权重范数不必严格固定，允许其以 √t 增长可维持长期有效学习率，这一原则可用于指导自定义优化器或学习率调度。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：权重衰减和显式权重范数约束在 LLM 预训练中有效，但为什么需要控制范数、控制到什么程度缺乏统一理解。Muon 优化器表现良好，但 vanilla Muon 的后期进展偏慢，可能与其权重范数控制过紧、有效学习率积累不足有关。

**方法关键点**：定义累积有效学习率 C_T = Ση_t/||W_t||_F，用于刻画整个训练轨迹上有效学习率的积累。分析表明 vanilla Muon 只能对数级积累，限制探索；MuonW/MuonH 可保证线性积累但约束较强。进一步证明，若权重范数增长足够慢，就能获得比对数最坏情况更快的积累，从而松开范数约束。基于此提出 MuonGS：用 Gram-Schmidt 投影移除每次 Muon 更新的径向分量，但不固定权重范数。在更新方向有界、学习率恒定的条件下，证明权重范数最多以 √t 增长，因此 C_T = Ω(√T)；对光滑尺度不变目标，给出 O(T^{-1/2}) 稳定性保证。

**关键结果**：在 160M/400M 稠密模型和 135M active/1B total MoE 模型上，长训练 horizon 下 MuonGS 验证困惑度低于 MuonH；稠密模型在匹配验证损失时 token 等效加速约 15%。
