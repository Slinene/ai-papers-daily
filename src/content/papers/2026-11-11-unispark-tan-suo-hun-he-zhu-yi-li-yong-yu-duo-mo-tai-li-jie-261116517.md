---
title: 'UniSpark: Exploring Hybrid Attention for Multimodal Understanding and Generation'
title_zh: UniSpark：探索混合注意力用于多模态理解与生成
authors:
- Jiancheng Pan
- Yuzheng Liu
- Hengyuan Cao
- Qiyuan Zhang
- Yangyan Li
- Biao Gong
- Zheng Zhang
- Ka Long Cheng
- Xinyang Wang
- Yujun Shen
arxiv_id: '2611.16517'
url: https://arxiv.org/abs/2611.16517
pdf_url: https://arxiv.org/pdf/2611.16517
published: '2026-11-11'
collected: '2026-11-14'
category: Multimodal
direction: 统一多模态理解与生成的混合注意力骨干
tags:
- Multimodal
- Hybrid Attention
- Visual Generation
- Flow Matching
- Linear Attention
- Mixture of Experts
one_liner: 提出9B混合注意力多模态模型UniSpark，统一视觉理解与生成，在MME-S和GenEval上取得领先
practical_value: '- 混合注意力架构可借鉴：在长序列多模态生成中，用全注意力处理关键token交互，用GatedDeltaNet线性注意力压缩历史上下文，能显著降低显存和计算，适合生成商品详情页长图文或广告创意。

  - 交错生成中的噪声隔离机制：将待生成的噪声视觉token与后续预测隔离，通过块级注意力掩码和循环状态保留实现，可迁移到多步生成或Agent工具调用中，避免中间生成结果污染后续推理。

  - 四阶段课程训练策略：先分别训练理解和生成，再联合微调，逐步扩展图像分辨率到2K，能稳定训练统一多任务模型，电商可参考训练统一的商品理解与创意生成模型，减少多模型维护成本。

  - 统一模型同时支持VQA、文生图、指令编辑和交错生成，适合需要快速迭代的广告素材生成场景，一个模型覆盖多种内容生产需求。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：多模态理解和生成通常由独立模型处理，统一模型面临全注意力计算昂贵、线性注意力表达受限的权衡。UniSpark探索混合注意力作为统一骨干，在MoE架构下每分支约9B参数，结合全注意力（显式token交互）和GatedDeltaNet线性注意力（紧凑上下文传播）。

方法关键点：自回归文本预测与视觉流匹配联合训练，支持VQA、文生图、指令编辑、交错文本图像预测。交错生成中，噪声视觉目标与后续预测隔离，干净视觉表示提供上下文。通过块级协议在全注意力层施加注意力掩码，在线性注意力层用循环状态保留规则实现区分。训练数据包含159.7M生成样本、213.4M理解样本、624.8K交错序列，采用四阶段课程训练，逐步提升答案精度、指令跟随和图像分辨率至2K。

关键结果：UniSpark在MME-S得2470.3，GenEval得0.83，MMBench 86.7，MMMU-Val 56.7，均优于对比模型。定性结果还展示交错图像生成、视频合成和编辑能力，验证混合注意力作为统一多模态骨干的有效性。
