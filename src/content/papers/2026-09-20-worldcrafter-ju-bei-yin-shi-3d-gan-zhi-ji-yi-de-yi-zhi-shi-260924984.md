---
title: 'WorldCrafter: Consistent Video World Model with Implicit 3D-aware Memory'
title_zh: WorldCrafter：具备隐式 3D 感知记忆的一致视频世界模型
authors:
- Wangbo Yu
- Kunhao Liu
- Wenbo Hu
- Shenghai Yuan
- Chaoran Feng
- Haiyang Zhou
- Yukun Huang
- Yiran Wang
- Wang Zhao
- Yingmin Luo
affiliations:
- ARC Lab, Tencent IEG
- Peking University
arxiv_id: '2609.24984'
url: https://arxiv.org/abs/2609.24984
pdf_url: https://arxiv.org/pdf/2609.24984
published: '2026-09-20'
collected: '2026-09-22'
category: Multimodal
direction: 视频世界模型 · 3D 记忆
tags:
- video world model
- 3D-aware memory
- camera control
- long-horizon consistency
- distillation
one_liner: 用相机可查询的隐式 3D 记忆压缩多视角证据，实现长时域一致的视频世界探索
practical_value: '- 固定 token budget 的记忆压缩思想可直接借鉴到用户长期行为建模：将多源行为序列压缩成固定数量的 target-conditioned
  tokens，避免长序列直接进模型带来的 KV cache 和计算压力。

  - pose-conditioned readout 可类比为“场景/意图条件下的记忆读取”，在推荐或 Agent 中可按当前上下文动态选择历史信息，提升长期依赖建模。

  - few-step distillation 用于加速生成过程，对生成式推荐或文案生成模型的推理加速有参考价值。

  - 整体仍是视频世界模型方向，与电商/推荐业务直接关联较弱，主要是工程方法上的通用借鉴。'
score: 6
source: huggingface-daily
depth: abstract
---

## 动机
视频世界模型在交互探索中难以保持长时间跨度和多视角下的一致性。现有方法在历史观察的利用上受限，无法在相机移动后可靠重建或重现场景细节。

## 方法关键点
WorldCrafter 的核心是让请求的视角决定多视角证据如何被压缩进视频生成器的有限 token 预算。具体通过一个与视频生成器联合训练的 memory encoder 和 pose-conditioned readout module，将历史观察整合为固定数量的目标视角 tokens，再进入去噪过程。该方法不需要显式的深度对应关系。结合近期时间上下文和 few-step distillation，实现从单张图像或文本 prompt 开始的流式场景探索。

## 关键结果
在静态和动态场景实验中，WorldCrafter 显著提升长时域一致性与相机控制精度，同时保持视觉质量，支持分钟级探索；在重访视角和物体重新出现时仍能保持外观与结构一致。
