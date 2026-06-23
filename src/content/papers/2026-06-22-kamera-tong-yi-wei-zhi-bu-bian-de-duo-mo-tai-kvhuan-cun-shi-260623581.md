---
title: 'Kamera: Unified Position-Invariant Multimodal KV Cache for Training-Free Reuse'
title_zh: Kamera：统一位置不变的多模态KV缓存实现训练免费复用
authors:
- Bole Ma
- Jan Eitzinger
- Harald Koestler
- Gerhard Wellein
affiliations:
- Erlangen National High Performance Computing Center (NHR@FAU)
arxiv_id: '2606.23581'
url: https://arxiv.org/abs/2606.23581
pdf_url: https://arxiv.org/pdf/2606.23581
published: '2026-06-22'
collected: '2026-06-23'
category: Multimodal
direction: 多模态Agent的KV缓存位置不变复用
tags:
- KV cache
- multimodal agents
- training-free
- position-invariant
- low-rank patch
- RoPE
one_liner: 通过低秩条件补丁恢复跨块绑定，使多模态KV缓存可任意位置复用，消除重复编码
practical_value: '- 在多轮Agent对话或滑动窗口推理中，可缓存商品图片、UI截图等视觉块的KV，随位置变化通过旋转和补丁恢复，避免重编码，显著降低电商直播、视频推荐场景的推理成本。

  - 低秩条件补丁训练免费、即插即用，能以极小存储代价恢复被丢弃的跨块上下文，保持多跳推理准确率，适合需要长程记忆的推荐Agent。

  - 支持重排、滑动窗口生存和回忆三种操作，工程实现简单，可直接集成到现有推理框架，利用RoPE重旋转和单一补丁即实现任意位置复用。

  - 在视觉冗余严重的视频流中效果最突出，正对多模态商品介绍、广告片反复分析等高计算场景，可大幅减少重计算预算。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：多模态Agent反复查看同一视频帧、UI截图，滑动窗口每次移动都从零编码KV缓存，传统前缀缓存只能在固定前导位置复用，导致大量重计算。直接复用内存块会丢失块间条件信号，多跳推理准确率减半。

**方法**：提出训练免费的低秩条件补丁，与位置无关的KV块一起存储。复用只需一次操作：精确RoPE重旋转到任意目标位置，加上补丁恢复跨块绑定。这使得三个窗口操作变得廉价：重排序（一个补丁服务所有排序）、滑动窗口存活（存活块仅通过旋转重定位，零重编码）、回忆（被逐出的块通过补丁补水，永不重编码）。

**结果**：在跨块绑定基准MM-NIAH跨两种注意力家族和双页文档QA上，秩-m补丁以极小KV足迹恢复完整任务准确率；在六个模型上的生产级SGLang内核中，重建的预填充KV与bf16舍入误差内一致。视觉/视频流中条件信号最强，多模态Agent重计算预算最高的场景收益最大。
