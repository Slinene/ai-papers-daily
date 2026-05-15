---
title: 'GPart: End-to-End Isometric Fine-Tuning via Global Parameter Partitioning'
title_zh: GPart：通过全局参数分区的端到端等距微调
authors:
- Paolo Mandica
- Michał Brzozowski
- Zuzanna Dubanowska
- Neo Christopher Chung
affiliations:
- Samsung AI Center, Warsaw
- University of Warsaw
arxiv_id: '2605.14841'
url: https://arxiv.org/abs/2605.14841
pdf_url: https://arxiv.org/pdf/2605.14841
published: '2026-05-14'
collected: '2026-05-15'
category: Training
tags:
- PEFT
- LLM
- Isometry
- Fine-tuning
- Parameter-Efficient
one_liner: 提出 GPart，用单一随机分区矩阵将可训练向量直接映射至全权重空间，消除 LoRA 的低秩瓶颈并实现端到端等距
score: 10
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
LoRA 通过低秩分解实现参数高效微调，但其双线性映射 (A,B)↦BA 不是等距的，优化器看到的欧氏距离在权重空间会被扭曲。Uni-LoRA 虽引入等距投影压缩可训练参数，但后续仍需经过 LoRA 的映射，整体仍非等距，且保留低秩瓶颈。如果直接在全权重空间选取一个低维随机子空间进行优化，既能保持几何一致性，又能完全移除结构约束，这正是 GPart 的出发点。

### 方法关键点
- **全局分区矩阵**：将模型所有 N 个可适应参数打乱并等分为 d 组，构造稀疏嵌入矩阵 P∈R^{N×d}，满足 P^⊤P=I_d ，将 d 维可训练向量 θ_d 等距映射为全量权重更新 Δw=Pθ_d。
- **更新规则**：每个参数 i 的更新为 θ_{g(i)} / √n_{g(i)}，其中 g(i) 为组索引，n_{g(i)} 为组大小。相同组内的参数共享同一个缩放后的值。
- **存储极简**：只需保存 d 个浮点数和一个随机种子（用于复现分组），共 d+1 个值，远少于 LoRA 的 O(D) 参数。
- **单超参数**：仅 d 控制可训练子空间维度，无需选择秩 r。初始化 θ_d=0，无需打破对称性。

### 关键实验结果
- **自然语言理解 (GLUE)**：在 RoBERTa-base 上以 23K 可训练参数取得平均 83.7 分，超过同等预算的 Uni-LoRA (83.0) 及更高参数的 LoRA (83.5)、VeRA (83.4)；RoBERTa-large 上平均 86.3，也高于 Uni-LoRA (85.9)。
- **数学推理**：在 GSM8K 和 MATH 上，多款解码器模型（Qwen2.5、Llama-3.1、Gemma）上平均准确率微胜 Uni-LoRA（GSM8K: 69.66 vs 69.26; MATH: 32.03 vs 31.56）。
- **计算机视觉**：ViT-Base 上以 72K 参数取得平均 86.19%（超过 Uni-LoRA 的 85.15% 和 FourierFT 的 80.29%）；ViT-Large 上 144K 参数平均 88.14%（超过 Uni-LoRA 的 88.00%）。
- **损失地形可视化**：GPart 的损失曲面呈现平滑、对称的盆状，而 Uni-LoRA 出现陡峭方向，验证了等距参数化带来的优化几何优势。

### 一句话记住
**有效微调不需要低秩瓶颈，直接在全权重空间的随机低维子空间内优化，既简单又保持几何一致性。**
