---
title: 'Video DeltaNet: A Video-Native Hybrid Attention for Livestream Video Generation'
title_zh: Video DeltaNet：面向直播视频生成的视频原生混合注意力
authors:
- Haocheng Xi
- Yiming Xie
- Hexu Zhao
- Yiwen Zhang
- Michael Liu
- Thomas Creavin
- Kurt Keutzer
- Xiuyu Li
- Zhaoyang Lv
- Chenfeng Xu
affiliations:
- University of California, Berkeley
- Impossible, Inc.
- University of Texas at Austin
arxiv_id: '2609.20744'
url: https://arxiv.org/abs/2609.20744
pdf_url: https://arxiv.org/pdf/2609.20744
published: '2026-09-16'
collected: '2026-09-18'
category: Multimodal
direction: 视频生成 · 混合线性注意力加速
tags:
- Linear Attention
- Video Generation
- Diffusion Models
- Hybrid Attention
- Inference Acceleration
one_liner: 提出 Video DeltaNet，用局部 Softmax 注意力+双向线性记忆加速视频扩散，在 MiniMax H3 上实现 14.5 倍去噪加速
practical_value: '- 混合注意力可用于用户长期行为序列建模：对最近行为用局部 Softmax 精确捕捉，对远期行为用线性 memory 压缩，控制长序列推理成本；推荐/广告的
  user sequence transformer 可以尝试。

  - 分阶段 teacher-alignment 是向预训练模型注入新模块的低风险方法：先固定原主干，单独训练新分支对齐教师输出，再逐步解冻联合微调；适合在已有排序/召回模型上实验新型注意力。

  - 按语义单元（session/帧/事件）更新 memory 而非逐 token：直播、短视频等场景中，用户在一个 session 内的行为可以聚合更新，减少状态更新频率，同时保持序列语义完整。

  - few-step distillation + 分布式 serving 可大幅压缩生成式模型推理延迟：业务上如创意文案生成、商品视频摘要等可借鉴 8 步蒸馏和
  SGLang 优化栈。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：视频扩散模型在去噪时反复处理长时空 token 序列，注意力成为计算瓶颈；线性注意力虽在 LLM 中成熟，但直接迁移到视频会损失细粒度空间交互，影响生成质量。

方法关键点：论文提出 Video DeltaNet（VDN），采用混合注意力：局部 Softmax 注意力保留精细 token 交互，新增双向线性 memory 分支建模长程视频上下文。线性分支的 Video Delta Attention（VDA）以帧为单位更新 memory，每帧联合其全部空间 token 一次性写入，而非逐 token 更新；两个分支拥有独立输出投影，并通过可学习门控融合。为将新通路平稳注入预训练视频模型，设计了分阶段 teacher-alignment 训练策略：逐步引入 VDA 并让新分支对齐原模型分布。VDN 在 MiniMax H3 上实例化，混合注意力只用在 video-to-video 交互，text/audio 交互保持 Softmax，避免跨模态语义损失。

关键结果：配合 8 步蒸馏与优化 SGLang serving，VDN-H3 在 8 张 NVIDIA B200 GPU 上完成 14.3 秒、768p 视频的 DiT 去噪仅需 6.70 秒；相比同 GPU 数下 50 步 dense H3 基线加速 14.5 倍。单 GPU 上累计约 16.2 倍，8 GPU 达 119.3 倍，且速度优势随视频时长增加而扩大。
