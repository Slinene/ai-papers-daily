---
title: 'Encore: Infinite Audio-Video Generation with Adaptive Signal Routing'
title_zh: Encore：利用自适应信号路由实现无限音视频生成
authors:
- Shaohua Pan
- Junbao Chen
- Shengyi He
- Jingfeng Xue
- Wen Tao
- Haocheng Feng
- Siming Fan
- Dongwei Pan
- Yi Yang
- Wei He
affiliations:
- Baidu
- Beijing Institute of Technology
arxiv_id: '2609.04249'
url: https://arxiv.org/abs/2609.04249
pdf_url: https://arxiv.org/pdf/2609.04249
published: '2026-08-28'
collected: '2026-09-08'
category: Multimodal
direction: 长音频视频生成与跨模态合成
tags:
- Audio-Video Generation
- Long-form Generation
- Adaptive Signal Routing
- Cross-modal Synthesis
- Diffusion
one_liner: 提出长音频视频联合生成框架Encore，通过自适应信号路由解决跨模态长时一致性
practical_value: '- 长序列多模态生成可借鉴双通路设计：局部连续性用 chunk 迭代加显式跨 chunk 上下文传递，全局一致性用参考信号加 shifted
  position embedding，电商短视频、直播切片自动配音等场景可复用。

  - Adaptive Signal Routing 的 learnable attention biases 与 residual scales 是通用插件，可控制多模态生成中不同
  conditioning 信号（文案、画面、背景音乐）的权重，适合商品视频生成中的模态协调。

  - 推理阶段持续对 ground-truth modality 做 conditioning，实现无限长度 audio-to-video / video-to-audio，能迁移到为已有商品图生成配音、或为音频补全视频帧等交互式素材生成。

  - 注意：该工作属于多模态生成模型，非推荐系统本身，但可作为内容供给侧自动生成工具，提升电商内容生态丰富度。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

动机：现有音视频生成只能输出短视频，长视频生成方法又缺乏音频。联合生成长音频视频更难，每个 chunk 需同时维持视频时间连贯、音频时间连贯和跨模态同步，且不同条件信号进入模型的路径不同。

方法关键点：Encore 将挑战拆成两部分：局部连续性通过迭代生成和显式跨 chunk 上下文传播处理；全局一致性通过参考音视频信号与 shifted position embedding 强制。核心提出 Adaptive Signal Routing (ASR)，在 self-attention 中引入可学习 attention biases，在 cross-attention 输出上加入可学习 residual scales，让模型自适应调节各条件信号的影响。端到端训练联合音视频生成，推理时对 ground-truth 模态持续 conditioning，支持无限长度 audio-to-video 和 video-to-audio 合成。

结果：在扩展的 VerseBench 长音视频评测上，生成质量和时间连贯性显著优于现有方法，可生成超过 500 秒的一致身份与音频。
