---
title: Unbundling Multimodal Vision Encoding
title_zh: 解耦多模态视觉编码：视觉先验、专用容量与融合位置
authors:
- Ellis Brown
- Chris Hoang
- Shengyi Qian
- Shang-Wen Li
- Mike Lewis
- Marjan Ghazvininejad
- Luke Zettlemoyer
- Lucas Beyer
- Mengye Ren
- Jakob Verbeek
affiliations:
- Meta FAIR
- New York University
arxiv_id: '2611.17334'
url: https://arxiv.org/abs/2611.17334
pdf_url: https://arxiv.org/pdf/2611.17334
published: '2026-11-11'
collected: '2026-11-14'
category: Multimodal
direction: 多模态视觉编码架构消融研究
tags:
- Multimodal
- Vision Encoding
- Ablation Study
- Architecture
- Training Efficiency
one_liner: 受控实验拆解视觉编码三因素，证明视觉先验可省、专用容量关键且可移入融合层
practical_value: '- 在电商商品图/视频理解等多模态任务中，不必单独预训练视觉编码器，可直接与主干联合从头训练，省去额外预训练阶段和工程链路，前提是算力预算匹配。

  - 保留专用视觉容量比简单扩大 LLM 参数更有效，应给视觉输入分配独立参数模块，而不是直接让 backbone 消化视觉 token。

  - 视觉模块可以放在主干早期层的 in-fusion 位置，性能与 pre-fusion 编码器相当，且能降低 time to first token，适合对首
  token 延迟敏感的在线商品问答或 Agent 实时理解场景。

  - 从 pretrained LLM 初始化时结论仍成立，可在现有语言模型上直接挂载轻量视觉模块联合训练，无需重训视觉塔。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：多模态语言模型的视觉编码方案仍存争议，常见做法混合了三个设计因素：上游预训练视觉先验、专用视觉容量、以及容量放置位置（pre-fusion vs in-fusion）。由于已发布模型在数据、架构和算力上差异大，难以单独归因。

**方法关键点**：搭建受控框架，所有模型从 scratch 在相同数据上训练，匹配 lifetime compute，主要在视觉问答和语言基准上对比。分别测试三组变量：是否使用预训练编码器、是否保留专用视觉容量、容量放在主干前还是主干早期层内。

**关键结果**：视觉先验非必需，联合从头训练的编码器与预训练编码器性能持平；专用视觉容量是关键，encoder-free 模型即使按编码器参数量扩展主干，视觉理解仍落后；容量不必放在融合之前，添加到主干早期层的 in-fusion 视觉模块与 pre-fusion 编码器性能相当，并能降低 time to first token。这些结论在不同主干尺寸、将编码器预训练视为免费、以及从预训练语言模型初始化时均成立。最终建议：专用视觉容量应与主干联合训练，并置于主干早期层内。
