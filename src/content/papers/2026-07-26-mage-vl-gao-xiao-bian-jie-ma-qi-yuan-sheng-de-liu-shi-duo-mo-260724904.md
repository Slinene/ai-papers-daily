---
title: 'Mage-VL: An Efficient Codec-Native Streaming Multimodal Foundation Model'
title_zh: 'Mage-VL: 高效编解码器原生的流式多模态基础模型'
authors:
- Senqiao Yang
- Kaichen Zhang
- Zhaoyang Jia
- Jinghao Guo
- Yifei Shen
- Xinjie Zhang
- Xiaoyi Zhang
- Haoqing Wang
- Xiao Li
- Peng Zhang
affiliations:
- Microsoft
arxiv_id: '2607.24904'
url: https://arxiv.org/abs/2607.24904
pdf_url: https://arxiv.org/pdf/2607.24904
published: '2026-07-26'
collected: '2026-07-30'
category: Multimodal
direction: 流式视频理解 · 高效视觉编码
tags:
- streaming
- codec
- video understanding
- efficient VLM
- dual-system
- AI4AI
one_liner: 利用类视频编码的 I/P 帧运动向量选择性编码动态区域，减少 75% visual token 并实现 3.5 倍推理加速的流式 VLM
practical_value: '- 借鉴 Mage-ViT 的稀疏编码思路：在电商视频理解或用户行为序列建模中，可设计基于运动/变化量驱动的自适应 token
  剪枝，只保留高熵片段，大幅降低 Transformer 输入长度与成本。

  - 双系统架构（轻量 System1 事件门 + 因果 System2 解码器）适合实时推荐场景：用极低成本的事件门控持续监听流式交互，仅当检测到关键意图或状态变化时才唤醒重型推理模型，实现低延迟主动推荐。

  - AI4AI 数据管线中的 prompt-code 联合优化与性能诊断方法，可迁移到商品文案生成、搜索词推荐的自动评估与迭代优化，用 AI 诊断模型产出调优建议，替代人工
  badcase 分析。

  - 论文发现 VideoQA 中的 SFT 数据存在大量冗余，实际只需少量高质量样本即可饱和；在推荐系统里的对话式推荐或解释生成任务中，可尝试小样本精调，避免全量标注成本。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：标准 VLM 在离线视觉推理上优异，但在连续流式感知（如视频流实时理解）中效率低下，被 Moravec 悖论困扰。需要一种既能保持强语义理解又能高效处理流式视觉输入的方案。

方法关键点：
- 提出 **Mage-ViT** tokenizer，模仿视频编解码器思路，将视频帧分为稀疏锚帧（I 帧）和预测帧（P 帧），仅对运动矢量大、残差能量高的动态区域以 16×16 patch 粒度提取视觉 token，跳过静态背景，token 消耗减少超 75%，同时保留时空上下文。
- 设计**双系统架构**：轻量级 System 1 事件门持续监听流，因果 System 2 解码器在事件触发时才进行深层推理，实现主动流式感知。
- 构建 **AI4AI 数据管线**：通过 prompt-code 联合优化自动生成高质量多模态描述，并用 AI 诊断模型指导训练配方。
- 仅使用约 560M 无标签图像和 100M 无标签视频帧从零训练编码器，未依赖大规模图文对。

关键结果：
- Mage-VL-4B 在静态多模态基准上与 Qwen3-VL-4B 匹配，在视频理解和 2D/3D 空间推理上显著超越，推理 wall-clock 速度提升最高 3.5 倍，且综合表现优于 15B 的 Phi-4-reasoning-vision。
- 七个实证发现：预训练数据高效性、可变分辨率缩放规律、编解码系统加速、VideoQA SFT 冗余、运动-空间协同增益、AI4AI 数据管线有效性、零视觉 SFT 的多模态 RL。
