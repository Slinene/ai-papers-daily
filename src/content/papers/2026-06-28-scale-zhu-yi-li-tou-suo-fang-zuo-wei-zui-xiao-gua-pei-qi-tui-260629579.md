---
title: 'ScAle: Attention Head Scaling as a Minimal Adapter for Spatial Reasoning in
  Vision Language Models'
title_zh: ScAle：注意力头缩放作为最小适配器增强VLM空间推理
authors:
- Rahul Chowdhury
- Timothy A Rupprecht
- Xuan Shen
- Pu Zhao
- Yanzhi Wang
affiliations:
- Northeastern University
- EmbodyX Inc.
- Zhejiang University
arxiv_id: '2606.29579'
url: https://arxiv.org/abs/2606.29579
pdf_url: https://arxiv.org/pdf/2606.29579
published: '2026-06-28'
collected: '2026-07-05'
category: Multimodal
direction: 轻量级激活缩放适配视觉语言模型
tags:
- PEFT
- Spatial Reasoning
- Vision-Language Model
- Activation Scaling
- Adapter
one_liner: 仅用1K可训练标量系数缩放冻结VLM层激活，空间推理准确率相对提升最高134.1%
practical_value: '- **极低资源任务适配**：冻结整个VLM，只训练少量标量系数（~1K参数量）即可注入空间推理能力，适合快速部署到电商多模态场景（如商品图片方位判断、广告布局合理性校验）。

  - **激活重标定策略**：针对最后token的注意力输出和MLP激活做缩放，无需改动模型结构，可直接套用于现有推荐系统中的视觉理解模块（如对商品详情图进行空间关系抽取）。

  - **原始能力无损**：缩放系数被有界约束，避免灾难性遗忘，在非空间VQA上保持原有性能，这对线上多任务系统（如同时做商品质量评估和空间描述）很关键。

  - **架构无关的即插即用**：该方法不依赖特定注意力实现，可作为轻量级适配层嵌入任一Transformer，适合探索在图文匹配、虚拟试穿对齐等推荐链路环节快速实验。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

**动机**：视觉语言模型（VLM）在空间推理上表现不佳，而传统PEFT方法（如LoRA）仍需要百万级参数。观察到在特定层简单地重标定激活值就能显著影响下游性能，提出用极小参数集实现高效适配。

**方法**：提出ScAle，冻结整个预训练骨干，仅学习一组标量系数，分别对选定Transformer层中最后token的注意力输出和MLP激活进行乘法缩放。缩放系数被约束在预设范围内，避免原始能力退化。不同层可独立适配，最终总参数量仅约1K。

**结果**：在空间推理基准SpatialEval及真实VQA数据集（COCOQA、VGQA）上，ScAle用1K参数取得最高134.1%的相对精度提升，并在非空间任务上保持原有准确率，证明了有界激活重加权作为极轻量适配策略的有效性。
