---
title: Which Way Did It Move? Diagnosing and Overcoming Directional Motion Blindness
  in Video-LLMs
title_zh: Video-LLMs 方向运动盲的诊断与克服
authors:
- Jongseo Lee
- Hyuntak Lee
- Sunghun Kim
- Sooa Kim
- Jihoon Chung
- Jinwoo Choi
affiliations:
- Kyung Hee University
- Princeton University
arxiv_id: '2605.22823'
url: https://arxiv.org/abs/2605.22823
pdf_url: https://arxiv.org/pdf/2605.22823
published: '2026-05-21'
collected: '2026-05-24'
category: Multimodal
direction: 视频理解 · 运动方向感知增强
tags:
- Video-LLM
- motion-direction-blindness
- diagnosis
- instruction-tuning
- projector-loss
- concept-vector
one_liner: 揭示 Video-LLMs 存在方向运动盲，提出投影器级辅助损失 DeltaDirect 显著提升运动方向理解
practical_value: '- **能力缺陷诊断范式**：通过线性探测各层隐状态可定位信息是否保留但未能绑定到输出，这套诊断流程可迁移到电商视频理解模型的动作、属性等基本感知能力的排查。

  - **低成本辅助任务注入先验**：DeltaDirect 仅在投影器上预测相邻帧特征差的运动向量，参数量极小，可作为一种轻量级插件提升视频模型的基础运动敏感性，适合在商品摆拍、物流监控等简单运动场景中快速部署。

  - **合成数据与真实泛化平衡**：文中发现视觉复杂性会削弱运动方向信号，提示在生成训练数据时需控制背景复杂度，否则域外泛化受限；在制作合成训练样本时可采用渐进式复杂度策略。

  - **概念向量分析指导特征工程**：运动方向概念向量的分析方法，可用于检测模型内部其他关键概念（如物体朝向、交互姿态）的信号强度，指导数据增强或特征正则化。'
score: 6
source: arxiv-cs.CV
depth: abstract
---

**动机**：当前 Video-LLMs 在时序理解任务上进步显著，却在最基础的运动方向判断（左/右/上/下）上接近随机水平，这种“方向运动盲”此前未被系统诊断。

**方法**：通过线性探测追踪运动方向信息在视觉编码器、投影器、LLM 隐状态中的线性可分性，发现信号始终存在，但最终输出无法正确绑定到词汇选项，即存在“方向绑定间隙”。进一步用运动方向概念向量分析表明，视觉复杂性会削弱该信号。为解决此问题，提出 MoDirect 数据集（合成与真实）和 DeltaDirect 辅助损失：在投影器层输入相邻帧特征差，预测归一化 2D 运动向量，作为指令微调的额外目标。

**结果**：在合成基准 MoDirect-SynBench 上，DeltaDirect 使运动方向准确率从 25.9% 飙升至 85.4%；在真实基准 MoDirect-RealBench 上，无需任何真实微调数据，即提升 21.9 个百分点，且不损害标准视频理解指标。诊断揭示的方向绑定间隙及投影器级修复方案，为提升 Video-LLM 基本感知能力提供了低成本路径。
