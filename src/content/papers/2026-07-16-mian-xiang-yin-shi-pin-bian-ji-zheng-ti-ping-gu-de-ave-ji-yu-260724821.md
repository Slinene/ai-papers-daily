---
title: 'AVE-Compass: Towards Holistic Evaluation for Audio-Video Editing Abilities'
title_zh: 面向音视频编辑整体评估的 AVE-Compass 基准与 AVE-Agent 框架
authors:
- Yuqing Wen
- Yukai Huang
- Qianqian Xie
- Jiangtao Wu
- Yibin Lin
- Yikai Gu
- Jialu Chen
- Yuanxing Zhang
- Jiaheng Liu
affiliations:
- Nanjing University
- Kuaishou Technology
- National University of Singapore
- Beijing University of Posts and Telecommunications
- University of Illinois Urbana-Champaign
arxiv_id: '2607.24821'
url: https://arxiv.org/abs/2607.24821
pdf_url: https://arxiv.org/pdf/2607.24821
published: '2026-07-16'
collected: '2026-08-08'
category: Eval
direction: 多模态音视频编辑评估
tags:
- audio-video editing
- benchmark
- multi-modal agent
- cross-modal consistency
- instruction following
- self-reflection
one_liner: 提出首个音视频耦合编辑评估基准 AVE-Compass，并设计模块化 Agent 框架提升跨模态编辑一致性与指令遵循度
practical_value: '- 清单式 MLLM 评估方法可迁移至电商短视频广告的多模态生成质量校验，例如自动检查视频中商品外观与背景音乐的协调性。

  - AVE-Agent 的模块化任务分解与自反思循环，为构建自动化多模态内容编辑流水线提供了模板，可用于批量优化商品展示视频。

  - 跨模态对齐评估指标（如音画一致性）可能启发推荐系统中视频与音频协同特征的质量监控。

  - 整体偏学术，业务直接落地难度较大，但 Agent 设计中的“分解→执行→评估→修正”闭环对多步骤推理任务（如动态创意生成）有参考意义。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有视频编辑基准只评估无声视觉编辑，忽略现实视频中音频与视觉紧密耦合，编辑一方需要另一方协同变化。音视频联合编辑的跨模态一致性缺乏系统评估。

**方法**：构建 AVE-Compass 基准，包含 145 个源视频、196 条音视频耦合编辑指令、2688 条细粒度检查项。从指令遵循、保真度保持、真实性和编辑意图四个维度，采用基于清单的 MLLM 评判与人工设计真实感评分标准，结合跨模态、视频、音频自动指标进行综合评估。进一步提出 AVE-Agent，将复杂编辑指令分解为依赖的子任务，通过自反思和评估器反馈迭代优化结果。

**关键结果**：主流模型在跨模态指令上表现挣扎，难以同时保持非目标内容。AVE-Agent 在指令执行、保真度保持和音视频对齐方面显著提升，同时保持有竞争力的感知质量。
