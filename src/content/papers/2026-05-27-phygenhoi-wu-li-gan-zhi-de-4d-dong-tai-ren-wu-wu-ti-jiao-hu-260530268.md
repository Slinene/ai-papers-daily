---
title: 'PhyGenHOI: Physically-Aware 4D Generation of Dynamic Human-Object Interactions'
title_zh: PhyGenHOI：物理感知的 4D 动态人物-物体交互生成
authors:
- Omer Benishu
- Gal Fiebelman
- Sagie Benaim
affiliations:
- Hebrew University of Jerusalem
arxiv_id: '2605.30268'
url: https://arxiv.org/abs/2605.30268
pdf_url: https://arxiv.org/pdf/2605.30268
published: '2026-05-27'
collected: '2026-05-31'
category: Other
direction: 4D 生成 · 人物物体交互 · 物理仿真
tags:
- 4D Generation
- Human-Object Interaction
- Physical Simulation
- Motion Diffusion
- 3D Gaussian Splatting
one_liner: 结合运动扩散模型与材料点法，通过窗口吸引损失、接触驱动重模拟和掩码视频 SDS 实现物理一致的 4D HOI 生成
practical_value: '- 主要面向动画、游戏、VR 等视觉内容生产，与电商 / 推荐 / Agent 业务直接关联较弱，但可借鉴生成式 AI 融入物理仿真的思路，用于商品
  3D 交互展示或虚拟试穿场景的物理真实感提升。

  - 窗口吸引损失和接触驱动重模拟的机制设计，可启发在对生成序列施加时序约束和物理反馈的工程实现，比如在虚拟主播带货动作合成中，让人物与道具的接触更自然。

  - 利用 3D Gaussian Splatting 作为统一可微表示，兼顾渲染效率与物理仿真，该表示可复用到需要快速渲染的商品 3D 场景中，例如大规模商品
  AR 展示。

  - 整体属于计算机视觉 / 图形学前沿，业务直接可迁移的技术组件有限，但其中运动扩散模型 + 物理仿真耦合的范式可能启发对 Agent 行为生成的结果进行物理合理性校验。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：现有 4D HOI 生成常忽视物理规律，导致视觉失真或碰撞不真实。PhyGenHOI 旨在从静态 3DGS 人类与物体出发，根据文本描述生成物理准确且视觉逼真的动态交互（如踢球、推柜子）。

方法关键点：
- 将人类建模为语义智能体，由运动扩散模型（MDM）驱动；物体作为物理智能体，通过材料点法（MPM）仿真。
- 通过三个耦合机制监督交互：
  1. Windowed Attraction Loss：在时间窗口内对齐人与物的运动，确保接触时机。
  2. Contact-Driven Re-simulation：在接触瞬间触发动量传递的物理重模拟，保证碰撞后运动合理。
  3. Masked Video-SDS：用视频先验增强接触部位的外观细节。
- 统一使用 3D Gaussian 表示，支持可微渲染与物理仿真耦合。

关键结果：在多种动作、人体和物体类型上均能生成物理一致的 4D HOI，相较于基线方法在物理合理性和视觉质量上均有显著提升。
