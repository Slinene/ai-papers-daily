---
title: VGGT-$Ω$
title_zh: VGGT-Ω：可扩展的前馈三维重建模型
authors:
- Jianyuan Wang
- Minghao Chen
- Shangzhan Zhang
- Nikita Karaev
- Johannes Schönberger
- Patrick Labatut
- Piotr Bojanowski
- David Novotny
- Andrea Vedaldi
- Christian Rupprecht
affiliations:
- Meta
arxiv_id: '2605.15195'
url: https://arxiv.org/abs/2605.15195
pdf_url: https://arxiv.org/pdf/2605.15195
published: '2026-05-14'
collected: '2026-05-17'
category: Training
direction: 可扩展多视角重建与空间理解
tags:
- 3D Reconstruction
- Feed-forward
- Self-supervised
- Register Attention
- Multi-task
- Scalability
one_liner: 通过架构精简、寄存器注意力与大规模自监督训练，前馈重建模型在精度与效率上大幅超越先前工作
practical_value: '- **寄存器注意力可用于多模态特征压缩**：将场景信息压缩到少量寄存器 token，仅在这些寄存器间做全局交互，类似操作可迁移到电商多模态商品表示中，用少量可学习
  token 对图文特征进行汇聚与交叉注意力，降低计算量。

  - **自监督从视频中学习通用表示**：利用海量无标注视频，通过重建代理任务预训练模型，该思路可直接用于用户行为序列建模——将行为序列视为时间帧，通过预测下一行为或重建序列结构获得更强序列表示。

  - **单头多任务密集预测**：用一个密集预测头同时监督深度、相机参数等多个任务，这种多目标共享表示的设计可借鉴到推荐模型的多目标学习中，减少参数冗余并提升泛化。

  - **重建是空间理解的强代理任务**：学习到的寄存器可直接改善视觉-语言-动作模型，表明三维重建能训练出对视觉-语言对齐有益的空间特征，电商视觉搜索或布局生成任务中可尝试引入重建预训练来增强空间敏感度。'
score: 6
source: arxiv-cs.CV
depth: abstract
---

**动机**：前馈重建模型 VGGT 已可比肩传统优化方法，但模型与数据规模的扩展规律尚不清晰。为此目标，需要大幅提升训练效率以支持更大规模数据。

**方法**：提出 VGGT-Ω，从三方面突破。架构上：用单一密集预测头替代多任务分支，移除高分辨率卷积层以减少计算；引入“寄存器”（registers），将多帧信息压缩到少量可学习 token 中，并设计寄存器注意力（register attention）仅在这些 token 间进行跨帧交互，替代昂贵的全局注意力，训练 GPU 内存降至前代的 30%。数据上：开发动态场景的标注管线，获得高质量监督数据。学习策略：构造自监督协议，首次利用海量无标注视频进行训练。

**结果**：监督数据量扩展至前代 15 倍，同时结合海量无标签视频。在 Sintel 等基准上，相机估计精度提升 77%，动态场景重建质量显著提高。寄存器表示可直接提升视觉-语言-动作模型性能，并与语言对齐，表明三维重建是空间理解的高效可扩展代理任务。
