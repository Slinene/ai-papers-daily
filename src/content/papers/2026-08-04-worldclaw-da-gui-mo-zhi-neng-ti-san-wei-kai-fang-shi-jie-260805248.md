---
title: 'WorldClaw: Agentic 3D Open-World Generation at Scale'
title_zh: WorldClaw：大规模智能体三维开放世界生成
authors:
- Chunchao Guo
- Jinpeng Li
- Yang Li
- Zilong Huang
affiliations:
- Tencent Hunyuan
arxiv_id: '2608.05248'
url: https://arxiv.org/abs/2608.05248
pdf_url: https://arxiv.org/pdf/2608.05248
published: '2026-08-04'
collected: '2026-08-08'
category: Agent
direction: Agent 驱动的 3D 开放世界生成
tags:
- 3D Generation
- Open-World
- Agentic Framework
- Coarse-to-fine
- Text-to-3D
- Editable Assets
one_liner: 利用规划代理和渲染代理从文本生成全局一致、可编辑的大规模 3D 开放世界，实现粗到细的生成
practical_value: '- 借鉴其“意图分析-全局规划-区域细化”的分层 Agent 架构，在设计搜索/推荐助手 Agent 时，对复杂用户需求进行结构化分解与分步执行。

  - 利用渲染反馈循环（render-based agents）进行自改进的思路，可用于电商推荐文案/图片生成的自我优化，通过生成后的评测反馈迭代提升质量。

  - 将生成过程建模为可编辑资产（可复用、可调整）的理念，可以迁移到推荐解释生成或广告素材生成，确保生成的元素可独立调整和组合。

  - 虽然主要是3D生成，但其coarse-to-fine流程可启发推荐系统中的多阶段生成（如先规划品类再细分子项）。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有文本驱动的3D世界生成难以兼顾全局空间一致性、丰富局部内容和可编辑资产重用。

**方法**：WorldClaw采用全智能体、粗到细的框架。Planning agents将文本提示转化为区域、地形、资产、材质和空间关系的结构化规范。然后分两步生成：
- **全局地形生成**：基于语义布局、可重用资产、生成或程序化材质，构建一致的地形基础和高程场。
- **区域细化**：对细节区域，生成地形条件组合，重建可编辑的纹理网格，并通过渲染代理（render-based agents）迭代优化地形、物体、外观和接触。

**结果**：在多样化开放世界提示下，WorldClaw能生成大规模场景，具有空间组织连贯、局部视觉生动、资产实例可独立编辑的特点，同时保持全局地形结构一致。
