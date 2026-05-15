---
title: Long Context Pre-Training with Lighthouse Attention
title_zh: 灯塔注意力：长上下文预训练的高效对称分层注意力方法
authors:
- Bowen Peng
- Subho Ghosh
- Jeffrey Quesnelle
affiliations:
- Nous Research
arxiv_id: '2605.06554'
url: https://arxiv.org/abs/2605.06554
pdf_url: https://arxiv.org/pdf/2605.06554
published: '2026-05-06'
collected: '2026-05-15'
category: Training
tags:
- Long Context
- Sparse Attention
- Hierarchical Attention
- Pre-training
- FlashAttention
one_liner: 对称池化Q/K/V并解耦选择的层次化注意力，训练长上下文时大幅加速且可无损恢复为密集模型
score: 10
source: huggingface-daily
depth: full_pdf
---

**动机**  
扩展上下文窗口是当前 LLM 的核心趋势，但标准注意力随序列长度 N 呈二次方增长，成为长上下文预训练的最大硬件瓶颈。现有的稀疏注意力多为推理设计，压缩仅面向 KV 侧且嵌入自定义内核，无法直接用于训练；训练中引入的稀疏方法又常需学习额外参数或面临优化不稳定。如何在不牺牲最终密集模型质量的前提下，加速长上下文预训练，是一个急迫问题。  

**方法关键点**  
1. **对称金字塔构建**：对 Q、K、V 同步进行多层平均池化，形成多分辨率表示，每层对应同一文本跨度，保持表示空间一致。  
2. **参数无关打分与 Top‑K 选择**：采用 ℓ2 范数对金字塔条目评分，无需学习参数；通过分块双调排序内核选取跨层 Top‑K 条目，保持因果关系。  
3. **选择与注意力解耦**：选中条目被拼接为稠密连续子序列，直接送入标准 FlashAttention，无需任何自定义稀疏注意力内核，既简化实现又兼容现有优化。  
4. **两阶段训练**：大部分步数使用 Lighthouse 训练，最后短暂切换为密集注意力（SDPA）继续训练，恢复为全注意力模型。选择过程不可导，梯度仅流经被选中的值，避免直通估计器或辅助损失。  

**关键实验**  
在 530M Llama‑3 风格模型上，使用 C4 数据、98K 上下文、16K 步（约 50B tokens）训练。与密集 SDPA 基线相比，Lighthouse 在训练阶段达到 2× 的吞吐提升（84–126k vs 46k tokens/s/GPU），端到端（含恢复阶段）实现 1.4–1.69× 的墙钟加速。最关键的发现是**恢复性**：经过 10k–12k 步 Lighthouse 训练再 4k–6k 步密集恢复后，最终训练损失（0.698–0.710）匹配或低于从头密集训练的基线（0.724），证明层次化训练没有损害模型的全注意力能力。消融进一步显示，较小的 Top‑K 预算（L=3, p=2, k=1536）能带来最低损失和较高吞吐，投影范数打分器与更昂贵的扩展注意力打分器效果相当。  

**核心洞见**  
_“层次化训练不会掏空模型在推理时使用全注意力能力，甚至能通过正则化带来更佳损失。”_ 这一结果使得 Lighthouse 成为长上下文预训练的实用选择，同时也为训练与推理的解耦设计提供了有力论据。
