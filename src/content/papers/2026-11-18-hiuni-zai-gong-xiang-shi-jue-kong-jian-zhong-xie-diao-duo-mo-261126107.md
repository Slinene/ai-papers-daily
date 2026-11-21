---
title: 'HiUni: Harmonizing Understanding and Generation in Shared Visual Space'
title_zh: HiUni：在共享视觉空间中协调多模态理解与生成
authors:
- Jiahao Hu
- Jingdong Du
- Yichen Zhang
- Yi Song
- Zhenyu Zhang
- Jiaxin Niu
- Ruihang Li
- Xiangzhao Hao
- Yiqian Zhang
- Yong Huang
affiliations:
- ERNIE Team, Baidu Inc.
arxiv_id: '2611.26107'
url: https://arxiv.org/abs/2611.26107
pdf_url: https://arxiv.org/pdf/2611.26107
published: '2026-11-18'
collected: '2026-11-21'
category: Multimodal
direction: 统一多模态理解与生成
tags:
- multimodal
- unified model
- image generation
- vision-language
- parameter sharing
one_liner: 通过复用语言对齐 ViT 与 dense Transformer 骨干，将任务特定计算限制在输出端，实现统一多模态理解与生成
practical_value: '- 架构上可将商品/广告素材的理解与生成任务共享同一骨干网络，降低线上模型部署与维护成本；任务特定计算仅放在输出侧，避免双塔分离带来的特征不一致。

  - Pixel Diffusion Head 直接优化像素空间生成，适合电商场景下商品图合成、背景替换、营销海报生成等对图像质量敏感的任务，可参照其绕过 VAE
  潜空间损失的思路。

  - HiGate 轻量通路在接近输出阶段注入细粒度空间细节，可借鉴到商品视觉表征中：对预训练 ViT 的图像特征增加低成本细节增强分支，在不破坏语义对齐的同时提升生成或编辑效果。

  - Controlled comparisons 显示单一 dense backbone 足以支撑双任务，表明业务中可优先尝试参数共享方案，而非直接引入 MoE
  或双编码器；若任务干扰严重再考虑轻度解耦。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有多模态统一模型普遍将视觉表示或骨干计算按理解/生成任务分离，限制了统一程度。HiUni 探索能否将预训练 VLM 直接扩展为参数高度共享的统一模型，复用同一套语言对齐 ViT 与 dense Transformer 主干，仅把任务特定计算放在输出侧。

**方法关键点**：该设计面临两个挑战——像素空间生成难以优化，以及预训练 ViT 的语义抽象会丢失生成所需的细粒度空间细节。HiUni 引入两个组件：① Pixel Diffusion Head，专为直接像素空间优化设计，避免 VAE 潜空间瓶颈；② 轻量 HiGate pathway，在接近输出阶段注入来自 ViT 中间层的细粒度空间信息，弥补语义特征的细节缺失。整个主干网络不增加任何任务特定计算。

**关键结果**：HiUni 在理解任务上取得与预训练 VLM 相近的平均分数，同时在图像生成与编辑上达到有竞争力的性能。控制实验进一步证明，单一 dense backbone 无需任务特定骨干计算即可同时有效支持理解与生成，为统一多模态建模提供了更简单的路径。
