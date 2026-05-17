---
title: 'SANA-WM: Efficient Minute-Scale World Modeling with Hybrid Linear Diffusion
  Transformer'
title_zh: SANA-WM：基于混合线性扩散Transformer的高效分钟级世界模型
authors:
- Haoyi Zhu
- Haozhe Liu
- Yuyang Zhao
- Tian Ye
- Junsong Chen
- Jincheng Yu
- Tong He
- Song Han
- Enze Xie
affiliations:
- NVIDIA
arxiv_id: '2605.15178'
url: https://arxiv.org/abs/2605.15178
pdf_url: https://arxiv.org/pdf/2605.15178
published: '2026-05-13'
collected: '2026-05-17'
category: Other
direction: 高效长视频世界建模 · 混合线性注意力
tags:
- World Model
- Diffusion Transformer
- Linear Attention
- Gated DeltaNet
- Camera Control
- Long Video Generation
one_liner: 用2.6B参数、单GPU在34秒内生成长达60秒的720p控制视频，效率比工业基线高36倍
practical_value: '- **长序列建模的线性注意力可复用到用户行为序列**：帧间Gated DeltaNet（GDN）的线性化记忆更新机制，与softmax高低频分工的思路，可直接用于电商用户长期兴趣建模，在保持精度的同时将显存和延迟从
  $O(L^2)$ 降至 $O(L)$。

  - **双分支控制可作为多模态条件生成的范式**：将相机6-DoF分解为低频姿态与高频视角的双分支控制，对生成式推荐中融合多种条件（如时间、场景、个性化）的设计有参考意义。

  - **两阶段生成（粗-精）是通用的效率优化**：先用小模型快速生成粗稿，再用精炼器提升局部一致性，可迁移到生成式推荐的item生成链路，降低全尺寸模型的一次推理成本。

  - **从弱标注视频中提取精确动作的流水线**：可借鉴其从公开视频估算 metric-scale 相机姿态的方法，用于电商场景下的用户行为模拟数据构建，例如从店内视频中提取移动轨迹作为世界模型的训练监督。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有世界模型难以在普通GPU上生成长时间、高保真、可控的视频，阻碍其在具身仿真与交互环境中的规模化应用。SANA-WM 旨在用较少的计算和数据实现分钟级720p的相机控制世界建模。

**方法**：提出四个核心设计：
1. **Hybrid Linear Attention**：对帧内局部依赖使用标准softmax注意力，帧间全局依赖改用Gated DeltaNet线性注意力，大幅降低长序列的显存和计算量；
2. **Dual-Branch Camera Control**：将6-DoF轨迹分解为低频姿态路径和高频视角微调两个分支，以精确控制相机运动；
3. **Two-Stage Generation Pipeline**：首先生成粗略的长视频，再利用轻量精炼器提升时空一致性；
4. **Robust Annotation Pipeline**：从公开视频自动提取 metric-scale 相机姿态，获得时空一致的动作标签。

**结果**：仅用约213K公开视频片段训练，64张H100训练15天；单张H100可生成60秒720p视频；经蒸馏和FP4量化后，一张RTX 5090只需34秒。在分钟级世界模型基准上，行动跟随准确率超过开源基线，视觉质量与工业级方法可比，且吞吐量高36倍。
