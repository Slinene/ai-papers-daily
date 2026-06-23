---
title: Randomized YaRN Improves Length Generalization for Long-Context Reasoning
title_zh: 随机化 YaRN：通过随机位置采样与长度课程提升长上下文推理
authors:
- Manas Mehta
- Fangcong Yin
- Greg Durrett
affiliations:
- New York University
arxiv_id: '2606.23687'
url: https://arxiv.org/abs/2606.23687
pdf_url: https://arxiv.org/pdf/2606.23687
published: '2026-06-22'
collected: '2026-06-23'
category: Training
direction: 位置编码与长度课程训练
tags:
- length generalization
- positional encoding
- YaRN
- randomized positional encoding
- long-context reasoning
- curriculum learning
one_liner: 结合 YaRN 位置编码、随机位置采样与长度课程，仅用短上下文数据微调即大幅提升 OOD 长上下文推理能力
practical_value: '- **不依赖长文本数据的长度扩展**：在电商搜索推荐或 Agent 场景中，若需要模型处理超长对话历史或商品描述，但缺乏长文本微调数据，可借鉴随机化
  YaRN 在标准短上下文数据上训练，就能获得长上下文泛化能力。

  - **长度课程策略**：消融实验表明，逐步增大位置采样范围（例如 8K→16K→32K）对泛化至关重要，业务中微调长上下文模型时可显式设计长度课程，避免直接跳到最大长度导致性能退化。

  - **位置编码的随机化技巧**：训练时对每个 batch 内的 token 随机分配来自更长区间的 YaRN 编码（排序后保持顺序），让模型提前接触 OOD
  位置表征，此 trick 可与现有 RoPE 类模型结合，成本低且无需改变模型结构。

  - **推理时 YaRN 因子可大于训练因子**：论文发现 s'' > s 时可进一步外推至未见的长度，实际部署时可尝试用更大的推理尺度因子来覆盖极端长输入，无需重新训练。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：大语言模型通常在短序列上预训练，之后通过长文本继续预训练扩展上下文窗口，但在远超训练长度的输入上泛化仍然困难，尤其在需要多跳推理的长上下文任务中表现不佳。现有的推理时 YaRN 等方法对简单检索有效，但对复杂推理的长度泛化提升有限。因此，需要一种在短上下文训练数据上就能有效外推至超长上下文的方法。

**方法关键点**
- **随机位置采样（Randomized Positional Encoding, RPE）**：训练时，对每个 token 不在原位置上计算 RoPE/YaRN，而是从区间 [1, L_t] 中随机采样 L 个位置并排序，分配给序列中的 L 个 token。这使得模型即使在 8K 长的输入上也能看到来自 16K、32K 甚至更长位置的编码，从而提前接触 OOD 位置表征。
- **与 YaRN 结合**：所有位置编码均使用 YaRN 计算（带缩放因子 s），将传统 RPE 直接扩展到 YaRN 框架下。YaRN 本身通过 NTK 插值和注意力温度缩放缓解外推问题，随机化则进一步暴露旋转角度的 OOD 组合。
- **长度课程（Length Curriculum）**：最大采样长度 L_t 随着训练 epoch 逐步增加（如 8K→10K→12K→16K→16K），让模型先适应温和的外推，再逐步泛化到更大范围，避免直接跳到大长度带来的训练不稳定。
- **推理时保持标准 YaRN**：推理时不进行随机采样，仅用标准 YaRN 编码，可选 s' ≥ s 以进一步外推。

**关键实验**
- **任务与数据**：BABILong（三跳推理子集，4K 训练样本，0–8K 上下文）和 MRCR（多轮共指消解，60 条训练样本，4–8K 上下文），评估长度从 8K 到 128K。
- **基线**：零样本+推理时 YaRN、普通 LoRA、仅用 YaRN 训练的 LoRA、仅用 RPE 训练的 LoRA（不结合 YaRN）。模型为 Qwen2.5-7B-Instruct 和 Olmo3-7B-Instruct。
- **核心结果**：在 BABILong 上，Qwen2.5 的 OOD 平均准确率从 Trained YaRN 的 81.3% 提升至 90.3%，Olmo3 从 83.2% 提升至 88.0%；在 MRCR 上，Qwen2.5 的 OOD 平均准确率从 59.3% 提升至 72.7%，Olmo3 从 38.1% 提升至 43.8%。尤为突出的是在最远 OOD 长度 (128K 或 64–128K) 上的优势。
- **消融**：去掉长度课程后，RPE 和随机化 YaRN 在 MRCR 上的 OOD 平均性能分别下降 18.3% 和 7.9%，证明课程是关键设计。

**一句话记住**：“在短上下文上通过随机位置采样 + 长度课程训练 YaRN，能让模型像‘见过’长上下文一样进行推理泛化。”
