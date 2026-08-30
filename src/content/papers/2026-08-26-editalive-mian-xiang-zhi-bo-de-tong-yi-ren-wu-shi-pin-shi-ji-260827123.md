---
title: EditaLive! Unified Character Video Editing for Live Streaming
title_zh: EditaLive：面向直播的统一人物视频实时编辑框架
authors:
- Zhiyuan Li
- Chi-Man Pun
- Peng-Tao Jiang
- Bo Li
- Xiaodong Cun
affiliations:
- University of Macau
- vivo BlueImage Lab
- GVC Lab, Great Bay University
arxiv_id: '2608.27123'
url: https://arxiv.org/abs/2608.27123
pdf_url: https://arxiv.org/pdf/2608.27123
published: '2026-08-26'
collected: '2026-08-30'
category: Multimodal
direction: 实时人物视频编辑 · 扩散蒸馏
tags:
- real-time video editing
- diffusion distillation
- appearance-motion decoupling
- live streaming
- character editing
one_liner: 基于外观-运动解耦蒸馏为两步采样器，实现14.47 FPS低延迟直播角色视频编辑
practical_value: '- 直播电商的实时换装/虚拟试穿/人物特效可借鉴外观-运动解耦思路：用预训练图像动画模型作为基底，通过参考帧编辑+视频重建实现指令驱动编辑，同时保留原始动作与面部表情，减少不一致。

  - 低延迟推理工程化：采用 aligned self-rollout distillation 将扩散模型压缩为两步采样器，结合固定 RoPE 与 align
  forcing 缩小训练-推理差距，可大幅降低生成式视频模型的推理成本，适配实时互动场景。

  - 长序列流式生成中引入首帧保留稀疏注意力，过滤冗余历史信息、抑制外观漂移，适合直播等持续流式推理，可迁移到需要长时一致性的视频生成或序列建模。

  - 指令编辑数据构建方法：通过参考帧编辑与视频重建自动生成 CharEdit-50K 数据集，可借鉴到电商商品换背景、模特换装等合成数据生成，降低人工标注成本。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：现有视频编辑方法侧重场景级内容，而直播更关注人物主体。直接应用会导致面部表情不一致，且依赖多步离线推理，无法满足实时交互。

方法关键点：以预训练图像动画模型 Wan-Animate 为基底，利用其外观-运动天然解耦的特性，通过参考帧编辑与视频重建（基于收集的 CharEdit-50K 数据集）实现指令驱动的人物视频编辑。随后将模型从离线双向生成调整为因果流式生成，并设计 aligned self-rollout distillation 策略，将模型压缩为两步采样器：固定 RoPE 和 align forcing 减少训练-推理不一致；首帧保留稀疏注意力过滤冗余历史信息，缓解长序列中的外观漂移。

关键结果：在编辑质量、面部表情保真、长序列一致性上达到 SOTA，实时推理速度 14.47 FPS，支持跨角色编辑。
