---
title: Geometry-Preserving Orthonormal Initialization for Low-Rank Adaptation in RLVR
title_zh: RLVR 场景下几何保持正交初始化 LoRA
authors:
- Ruijia Zhang
- Jiacheng Zhu
- Hanqing Zhu
- Laixi Shi
affiliations:
- Johns Hopkins University
- Meta
- University of Texas at Austin
arxiv_id: '2606.31813'
url: https://arxiv.org/abs/2606.31813
pdf_url: https://arxiv.org/pdf/2606.31813
published: '2026-06-30'
collected: '2026-07-01'
category: Training
direction: LoRA 正交初始化提升 RLVR 训练稳定性
tags:
- LoRA
- RLVR
- Orthonormal Initialization
- Mathematical Reasoning
- Fine-tuning
one_liner: 提出正交初始化 LoRA 稳定 RLVR 训练并超越标准 LoRA，解释 SVD 初始化在该场景失败原因
practical_value: '- 在 RLVR 微调 LLM（如推荐理由生成、Agent 策略优化）时，用正交初始化（`torch.nn.init.orthogonal_`）替代默认
  Kaiming 或 SVD-based，可稳定训练并提升性能。

  - 已尝试 PiSSA/MiLoRA 而效果不佳的 RL 微调场景，可直接切换为 RLPO/RLMO，避免训练不稳定与性能倒退。

  - 正交初始化简单易集成，工程代价低，可作为 RL 微调 LoRA 的默认初始化方案，尤其在需要长期稳定收敛的推荐或对话策略学习中。

  - 理论结论“正交初始化使 LoRA 与全参数微调输出差距最小”具有通用性，适用于其他 RL 训练任务（如 RLHF 微调推荐模型）。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：LoRA 在监督微调（SFT）下表现良好，而 PiSSA、MiLoRA 等基于 SVD 初始化的变体在 SFT 中更优。但在强化学习可验证奖励（RLVR）场景，它们出现训练不稳定且性能不如标准 LoRA，表明 RLVR 对初始化敏感。

**方法**：首先构建 LoRA 在 RLVR 下的理论框架，证明正交初始化能最小化 LoRA 与全参数微调的输出差距。据此提出两种几何保持正交初始化变体：RLPO（随机正交矩阵）和 RLMO（部分正交矩阵），分别初始化低秩矩阵 A 和 B。同时从理论角度解释了 PiSSA/MiLoRA 在 RLVR 中失效的原因。

**关键结果**：在数学推理基准（GSM8K、MATH 等）上，RLPO/RLMO 显著稳定训练过程，最终性能超越标准 LoRA，而 PiSSA/MiLoRA 相对标准 LoRA 下降。例如在某实验中，RLPO 相比标准 LoRA 提升约 2% 准确率，且训练曲线更平稳。
