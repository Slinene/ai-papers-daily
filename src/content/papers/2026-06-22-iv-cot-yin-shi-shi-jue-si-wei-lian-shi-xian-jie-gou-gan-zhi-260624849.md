---
title: 'IV-CoT: Implicit Visual Chain-of-Thought for Structure-Aware Text-to-Image
  Generation'
title_zh: IV-CoT：隐式视觉思维链实现结构感知的文本到图像生成
authors:
- Zixuan Li
- Haokun Lin
- Yicheng Xiao
- Zhiwei Li
- Xinyang Song
- Zelong Zheng
- Yong He
- Heng Yao
- Ke Ding
- Chao Yu
affiliations:
- NLPR, Institute of Automation, Chinese Academy of Sciences
- Ant Group
- The University of Hong Kong
arxiv_id: '2606.24849'
url: https://arxiv.org/abs/2606.24849
pdf_url: https://arxiv.org/pdf/2606.24849
published: '2026-06-22'
collected: '2026-06-25'
category: Multimodal
direction: 多模态生成 · 隐式视觉链式推理
tags:
- Text-to-Image Generation
- Chain-of-Thought
- MLLM
- Structure-Aware
- Sketch Supervision
one_liner: 提出隐式视觉思维链推理，将条件查询分解为潜层结构规划与语义渲染级联，在单次前向中提升生成图像的结构遵循能力。
practical_value: '- 主要学术贡献，但提供的结构-语义分解式生成框架可启发电商场景下的可控商品图生成：先用隐式查询规划物品属性、数量、空间关系，再渲染纹理细节，提升复杂广告素材的指令遵循度。

  - 训练时仅用草图作为结构监督、推理时完全隐式的设计，可用于业务中需要轻量级中间控制的多模态生成任务，避免增加在线时延。

  - 对于搜索推荐系统中 Agent 驱动的图文混合输出，借鉴这种级联潜空间规划思路，可能改善多约束条件下的生成一致性。

  - 整体而言，方法面向通用 T2I 结构控制，直接迁移到推荐检索场景的路径较窄，更多是提供一种多模态生成质量优化的技术储备。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有统一多模态大模型（MLLM）在文本到图像生成中，常难以遵循结构感知提示，如对象数量、空间关系、属性绑定和粗糙布局。原因之一是结构规划和外观渲染在单一条件流中纠缠，导致生成结果虽有视觉逼真度却违反结构化要求。

**方法关键点**：提出隐式视觉思维链（IV-CoT），将视觉条件查询分解为“结构查询 → 语义查询”的潜层级联。结构查询先生成隐式视觉规划图（不解码为显式草图），语义查询再基于该规划进行外观渲染。训练时引入草图监督信号，驱动结构查询捕获对象的空间与组成信息，但推理时不需任何草图提取或中间解码，保持单次前向的低计算开销。整体框架以 Transformer 的单流形式隐式地完成链式推理。

**关键结果**：在 GenEval 与 T2I-CompBench 基准上，IV-CoT 相较现有 MLLM 生成方法取得更优的结构遵循分数，尤其在多对象计数、空间关系和属性绑定任务上提升显著。可视化分析证实结构查询与语义查询分工明确、互补增强，支撑了结构感知生成。
