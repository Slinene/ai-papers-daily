---
title: 'Rounding in Preconditioner Space: Redesigning 4-bit AdamW Optimizer-State
  Quantization'
title_zh: 基于预条件空间的舍入：重新设计4-bit AdamW优化器状态量化
authors:
- Hanyang Li
- Shao Tang
- Daniel Thomas Braithwaite
- Gregory Dexter
- Leonardo Neves
- Aman Gupta
- Hiroto Udagawa
- Abhishek Shivanna
- Daniel Silva
- Rohan Ramanath
affiliations:
- University of California, Berkeley
- Nubank
arxiv_id: '2610.12444'
url: https://arxiv.org/abs/2610.12444
pdf_url: https://arxiv.org/pdf/2610.12444
published: '2026-10-08'
collected: '2026-10-10'
category: Training
direction: 4-bit AdamW 优化器状态量化
tags:
- optimizer-state quantization
- 4-bit AdamW
- stochastic rounding
- preconditioner space
- LLM training
one_liner: 提出在预条件空间做随机舍入的4-bit AdamW状态量化方法，显著缩小与32-bit训练的验证损失差距
practical_value: '- 若已经在用 TorchAO 4-bit AdamW 压缩大模型优化器状态，可直接替换第二动量的量化方式：不再做 state-space
  rounding，而是在 preconditioner space 计算随机舍入概率，改动集中在量化器实现层，训练流程无需重构。

  - 第二动量码书可两条路线选择：ZIP-SR 保留零点适合大多数场景；ZE-EDEN 排除零点并 rescale 量化块，可缓解正量化底带来的预条件失真，对推荐/搜索模型中大量稀疏或接近零的梯度更有针对性。

  - 第一动量用 4-bit NF4 已经够稳，但输出层（如推荐系统中的 item embedding 或 LLM 的 LM head）对量化更敏感，最后 10%
  训练步对输出层第一动量做针对性随机舍入，能进一步降低验证损失，适合在微调生成式推荐模型时采用。

  - 对需要大规模预训练或全参数 SFT 的电商/Agent 场景，该方法可降低优化器显存占用，同时把 4-bit 训练与 32-bit 训练之间的验证损失差距最多缩小
  70%，适合作为训练成本优化的默认配置。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：AdamW 的 FP32 一阶和二阶动量每参数需 8 字节，4-bit 状态量化能大幅降低存储，但量化误差会通过动量递推传播并扰动后续自适应更新。现有方法在 state space 选择舍入层级，存在小状态误差被放大为预条件误差的问题。

**方法关键点**：从 rounding space 视角重新设计 4-bit AdamW 状态量化。提出 ZIP-SR：第二动量码书保留零点，并在 preconditioner space 计算随机舍入概率；补充 ZE-EDEN：第二动量码书排除零点，并 rescale 量化后的第二动量块，以缓解正量化底造成的预条件失真。两种方案第一动量均使用 4-bit NormalFloat NF4，并在最后 10% 训练步对 LM-head 第一动量做针对性随机舍入。

**关键结果**：在 130M 到 2.7B 参数的 GPT 与 Llama 预训练中，两种方法在每个模型尺寸均降低 TorchAO 4-bit AdamW 相对 32-bit AdamW 的验证损失差距，最大差距降幅达 70%。全参数 SFT 中验证损失低于 TorchAO，下游任务表现接近 32-bit AdamW。
