---
title: 'A Glance Is All You Need: Single-Pass Fine-Grained Image Captioning with SimLoss'
title_zh: SimLoss：嵌入空间监督实现单遍细粒度图像描述
authors:
- Suryaansh Jain
- Rahasya Barkur
- Vishal G
- Ryan Rossi
- Franck Dernoncourt
- Jack Wang
- Koustava Goswami
- Nedim Lipka
- Puneet Mathur
- Samyadeep Basu
affiliations:
- University of Massachusetts Amherst
- Adobe Research
arxiv_id: '2609.00591'
url: https://arxiv.org/abs/2609.00591
pdf_url: https://arxiv.org/pdf/2609.00591
published: '2026-08-31'
collected: '2026-09-05'
category: Multimodal
direction: 多模态图像描述训练 · Embedding-space 对比学习
tags:
- image captioning
- SimLoss
- InfoNCE
- vision-language model
- fine-grained
- single-pass
one_liner: 用冻结图像嵌入的 InfoNCE 对比损失对齐 VLM 隐藏状态，单遍生成细粒度描述，速度提升约20倍
practical_value: '- 在电商商品视觉描述生成中，可用 SimLoss 的嵌入空间对齐：冻结 CLIP 等图像编码器作为教师，用 InfoNCE 让生成模型在解码前对齐视觉特征，无需人工细粒度标注，低成本提升商品属性、材质、计数等描述完整性。

  - 对需要实时性的商品文案、图片 alt 文本自动生成，可把多阶段验证流水线替换为单遍生成 + 嵌入空间约束，保持描述质量的同时降低约20倍推理延迟，适合线上部署。

  - 黑盒变体 SimLoss GRPO 将嵌入模型作为奖励，可复用现有 GRPO/RLHF 训练框架，对生成式推荐或广告文案模型做奖励优化，避免直接依赖人类标注。

  - 注意 InfoNCE 需要较大 batch 或 memory bank 来提供足够负样本；该方法可扩展到商品标题-图像、query-落地页图像等跨模态对齐任务。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现代视觉语言模型（VLM）能生成流畅的高层图像描述，但常遗漏属性、计数、纹理、材质、空间关系等视觉细节。多阶段系统通过生成-分解-验证-重写恢复细节，但推理延迟大幅增加。

**方法关键点**：提出 SimLoss，一种无参考的嵌入空间目标，用于单遍细粒度图像描述。它将 VLM 的投影隐藏状态与冻结的图像嵌入通过 InfoNCE 对比损失对齐，在解码文本前提供密集视觉监督，无需人工细粒度描述或伪标签。提供两种实例：SimLoss FFT 通过可微嵌入模型反向传播；SimLoss GRPO 将嵌入模型作为黑盒奖励进行优化。

**关键结果数字**：SimLoss FFT 在精度上最优，F1 接近多阶段方法，但保持单遍推理，速度约为多阶段管线的20倍；SimLoss GRPO 获得最强召回。整体表明嵌入空间监督能够以单遍延迟恢复多阶段验证的描述质量。
