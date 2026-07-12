---
title: 'LOPA: Enhancing Spoken Language Assessment via Latent Ordinal Prototype Alignment'
title_zh: 通过隐式有序原型对齐增强口语评估
authors:
- Hong-Yun Lin
- Fu-An Chao
- Bi-Cheng Yan
- Berlin Chen
affiliations:
- National Taiwan Normal University
arxiv_id: '2606.31310'
url: https://arxiv.org/abs/2606.31310
pdf_url: https://arxiv.org/pdf/2606.31310
published: '2026-06-30'
collected: '2026-07-12'
category: Other
direction: 口语评估 · 有序回归
tags:
- spoken language assessment
- ordinal regression
- prototype alignment
- layer routing
- Whisper
one_liner: 用原型对齐正则化和语义锚定层路由在冻结Whisper上实现0.36 RMSE，媲美十亿参数大模型
practical_value: '- 评分场景（如店铺评分、用户满意度预测）可利用有序原型对齐，在隐空间强制序关系，提升回归精度和可解释性

  - 语义锚定层路由（SALR）可启发多深度特征融合：对冻结大模型不同层输出做自适应加权，相当于低成本提取多粒度特征

  - 不微调大模型、仅加轻量正则器即达高性能，适合资源受限的线上服务；可尝试对BERT/Whisper等冻结编码器加原型损失微调下游任务

  - 原型作为可学习的序数锚点，可类比推荐中的用户/物品层级原型（如消费力分层），辅助冷启动和排序校准'
score: 6
source: arxiv-cs.MM
depth: abstract
---

**动机**：当前口语评估多采用超大MLLM做有监督微调，计算成本高，且忽视语言习得的序数本质。本文旨在无需LLM微调的前提下，实现与数十亿参数模型相当的性能，并注入序数先验。

**方法关键点**：
- 提出隐式有序原型对齐（LOPA），在隐空间学习一组有序原型（可学习的序数锚点），强制样本表示靠近对应级别原型，并施加序数距离约束，使潜空间具备明确的序数几何结构。
- 设计语义锚定层路由（SALR）：以Whisper编码器的中间某层输出作为语义锚，通过注意力计算其他各层与该锚的相似度，生成软权重，自适应地融合多层特征，避免手工选择层数。
- 整体框架：冻结Whisper提取多深度特征，经SALR融合后送入轻量评分头，并添加LOPA正则项联合训练。

**关键结果**：在Speechocean762等基准上，RMSE低至0.361，与百亿参数MLLM微调方案持平，且参数量极小。分析显示SALR对不同评分标准自动呈现不同层偏好，与LOPA协同提升了可解释性和序数感知。
