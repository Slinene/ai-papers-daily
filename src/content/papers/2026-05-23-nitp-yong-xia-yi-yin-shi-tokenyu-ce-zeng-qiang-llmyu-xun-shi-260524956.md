---
title: 'NITP: Next Implicit Token Prediction for LLM Pre-training'
title_zh: NITP：用下一隐式Token预测增强LLM预训练表示
authors:
- Xiangdong Zhang
- Debing Zhang
- Shaofeng Zhang
- Xiaohan Qin
- Yu Cheng
- Junchi Yan
affiliations:
- School of AI, Shanghai Jiao Tong University
- Xiaohongshu Inc.
- University of Science and Technology of China
- The Chinese University of Hong Kong
arxiv_id: '2605.24956'
url: https://arxiv.org/abs/2605.24956
pdf_url: https://arxiv.org/pdf/2605.24956
published: '2026-05-23'
collected: '2026-06-02'
category: Training
direction: LLM预训练 · 表示级监督
tags:
- Next Implicit Token Prediction
- representation degeneration
- self-supervised target
- pre-training objective
- MoE
one_liner: 用模型浅层表示作为连续自监督目标，显式约束隐藏状态几何，有效缓解NTP的表示退化
practical_value: '- **低成本的表示质量提升手段**：仅增加约2%的训练FLOPs，无需额外推理开销，可移植到任何基于Transformer的推荐模型预训练中，改善物品/用户表示的各向异性与退化。

  - **浅层作为语义锚点**：利用模型自身浅层输出作为连续监督目标，无需外部编码器，这一自蒸馏思路可直接用于序列推荐中的状态表示学习，例如用中间层表示约束最终隐藏状态。

  - **余弦相似度作为稳定辅助损失**：相比MSE或KL散度，余弦损失在跨层表示对齐中更稳定，可避免梯度尖峰，适合在工业级大模型训练中作为正则项。

  - **几何正则化的显式设计**：论文揭示了NTP目标在表示空间的零空间问题，并通过理论证明NITP在该零空间引入正曲率，这对于理解并缓解推荐模型中常见的嵌入维度坍缩有直接启发，可尝试为召回/排序模型添加类似隐式预测目标。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
标准下一token预测（NTP）仅通过离散标签监督模型，隐藏状态的表示空间缺乏显式几何约束。实证发现，随着训练进行，隐藏状态的有效秩迅速下降、余弦相似度急剧上升，即出现表示退化现象，限制了模型的泛化能力。根本原因在于NTP目标在正确token方向之外的大量自由度上几乎不变，允许表示坍缩为低维各向异性锥体。  

**方法关键点**  
- 提出**下一隐式Token预测（NITP）**，在NTP之外增加一个连续表示级辅助损失：要求最后一个隐藏状态预测**下一个token的浅层表示**（称为隐式token）。  
- **隐式token构建**：取自模型前k层（约总深度20%）的输出，经过梯度截断，利用浅层富含词汇及局部语义且训练更早收敛的特性，作为稳定自监督目标。  
- **损失函数**：通过一个投影头（MLP）将深层状态映射到与目标相同的空间，使用余弦相似度损失（1 – cos），保持尺度不变性，避免MSE等带来的训练不稳定。  
- **联合训练**：总损失 = NTP损失 + λ * NITP损失（λ≈1.0）。  
- **理论分析**：推导了NITP的Hessian，证明其在NTP语义零空间的方向上引入正曲率，从而有效正则化表示几何。  

**关键实验**  
- 在MoE（1.9B/3B/9B）和Dense（0.5B/2B/3B）模型上从零预训练，训练token量从数百亿到330B。  
- 相比NTP基线，NITP在所有规模上均取得一致提升：9B MoE在MMLU-Pro上绝对提升5.7%（15.29%→21.00%），C3提升6.4%，CommonsenseQA提升4.3%；2B Dense平均得分提升1.79个点。  
- 训练额外FLOPs仅约2%，且不影响推理。  
- 消融实验证实：①时间偏移（预测t+1而非对齐当前位置）至关重要，无偏移会导致损失极低但性能大幅下降；②浅层目标显著优于中层或深层；③余弦损失优于MSE、Smooth L1和KL散度。  

**一句话记忆点**  
“NTP只定义预测什么，不约束如何表示；NITP用模型自己的浅层语义作为连续锚点，以可忽略的计算成本显式地正则化了隐藏空间几何。”
