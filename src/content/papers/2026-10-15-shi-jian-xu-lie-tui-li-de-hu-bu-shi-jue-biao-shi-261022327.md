---
title: 'Twice Upon a Time: Complementary Representations for Time-Series Reasoning'
title_zh: 时间序列推理的互补视觉表示
authors:
- Hedi Zisling
- Liran Nochumsohn
- Ilan Naiman
- Mihir Parmar
- Omri Azencot
affiliations:
- Ben-Gurion University
- Google
arxiv_id: '2610.22327'
url: https://arxiv.org/abs/2610.22327
pdf_url: https://arxiv.org/pdf/2610.22327
published: '2026-10-15'
collected: '2026-10-17'
category: Multimodal
direction: 多模态时序表示 · 互补视图融合
tags:
- Time Series
- Complementary Representations
- Vision-Language Model
- TSLM
- Multimodal Reasoning
one_liner: 用线图与归一化延迟嵌入两种互补视觉视图训练视觉-语言时序模型，显著提升推理精度
practical_value: '- 在电商销量预测、广告投放趋势分析等场景，若用 VLM/LLM 做时序问答或归因，避免只给单一线图或数值序列；同时输入原始线图（保留绝对量纲）与归一化延迟嵌入图（突出形态、去量纲偏移），让模型兼顾绝对峰值和形状相似性。

  - 借鉴多级特征融合：时序视觉编码时，不只把最终 patch token 接入 LLM，可把中间层特征也作为 visual token 融合，保留更细粒度时间模式，适合流量、GMV
  曲线等复杂信号。

  - 对跨商品/类目趋势比较，先做幅度/偏移不变表示（如归一化延迟嵌入），可降低不同 scale 带来的过拟合，提升 cross-domain 泛化。

  - 工程上可直接复用 Qwen-VL 系列：把原始 line plot 和 normalized delay embedding 渲染成两张图输入，无需重新设计数值
  tokenizer，改造成本低但可能带来明显提升。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

动机：TSLM 要让 LLM 理解时间序列，但现有方案通常给单一表示，强加固定归纳偏置，例如只给数值序列或只给线图，难以兼顾绝对坐标与形态结构。

方法：提出互补表示原则，将时间序列渲染为两种互补视觉视图：线图保留绝对测量值和原坐标框架；归一化延迟嵌入通过去除正幅度缩放和偏移，显式暴露时序结构。用两个专用视觉编码器分别编码，再通过 visual tokens 和多级特征融合接入共享 LLM（Qwen3-VL-8B），实现统一推理。

结果：在 TSRBench 上整体准确率从单线图的 44.5% 提升到 53.2%，显著超过最强专用 TSLM baseline 的 36.7%；TSExam 准确率 89.9%，多变量 ChatTS 数值对齐准确率 86.8%。评估期干预验证两种视图具有不同不变性，单视图消融显示互补组合在预测和推理上的收益超过基本感知。
