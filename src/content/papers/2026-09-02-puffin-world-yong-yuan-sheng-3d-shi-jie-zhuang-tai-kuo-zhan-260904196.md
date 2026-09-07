---
title: 'Puffin-World: Scaling a Unified Multimodal Model with Native 3D World States'
title_zh: Puffin-World：用原生 3D 世界状态扩展统一多模态模型
authors:
- Kang Liao
- Yihang Luo
- Xiao-Ming Wu
- Linyi Jin
- Size Wu
- Chunyu Lin
- Yao Zhao
- Fei Wang
- Wei Li
- Chen Change Loy
affiliations:
- S-Lab, Nanyang Technological University
- University of Michigan
- Beijing Jiaotong University
- ACE Robotics
arxiv_id: '2609.04196'
url: https://arxiv.org/abs/2609.04196
pdf_url: https://arxiv.org/pdf/2609.04196
published: '2026-09-02'
collected: '2026-09-07'
category: Multimodal
direction: 多模态世界模型 · 3D 生成重建
tags:
- Multimodal
- World Model
- 3D Generation
- Physics Understanding
- Omni-Camera
- Unified Architecture
one_liner: 统一多模态架构，联合物理/几何/外观三态与 Omni-Camera 实现 3D 世界生成重建
practical_value: '- 可借鉴「原生状态联合建模」：在商品理解/生成中，将视觉、深度/几何、物理属性（如材质、尺寸、重力约束）作为并行状态统一建模，替代只用图文
  embedding，可提升家居、鞋服等品类空间一致性。

  - 用显式 Omni-Camera 参数控制多视角生成：商品视频、虚拟试穿、3D 展示素材可 ground 绝对相机内外参，生成物理稳定、多角度一致内容，减少后期抖动与畸变。

  - 外观-几何耦合生成：同时输出 RGB 和 depth 再用于重建，适合商品 3D 重建/AR 展示/虚拟棚拍，能对齐纹理与几何，降低“贴图漂移”。

  - 闭环自校准探索思路可迁移到 Agent 拍摄/漫游：让模型根据当前状态规划下一视角并在线修正相机与场景参数，但需构建匹配业务场景的轨迹数据。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：现有多模态模型常依赖外部离线模块，难以在一个框架内协同完成物理理解、空间模拟与 3D 世界生成/重建。方法：Puffin-World 联合建模三种原生世界状态——物理（重力场与纬度）、几何（深度）、外观（图像），并采用统一的 Omni-Camera 表示支持多任务和灵活运动；将绝对相机属性 grounding 到真实世界，传播未来帧的物理动态；在单个生成过程中耦合外观与几何，同时合成未来视图并重建深度，支持 mimic 和自校准世界探索等闭环应用。数据：构建 Puffin-16M，包含 1500 万 vision–language–camera 三元组与 100 万条具有多样挑战运动的轨迹。结果：实现物理一致、视觉稳定的世界生成，并公开代码、模型与数据集。
