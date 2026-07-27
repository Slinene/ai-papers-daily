---
title: 'Unboxing Diffusion Models for the Arts: Interactive Model Bending and Practice-Based
  Explainability'
title_zh: 为艺术拆解扩散模型：交互式模型弯曲与基于实践的可解释性
authors:
- Ahmed M. Abuzuraiq
- Philippe Pasquier
affiliations:
- Simon Fraser University
arxiv_id: '2607.22428'
url: https://arxiv.org/abs/2607.22428
pdf_url: https://arxiv.org/pdf/2607.22428
published: '2026-07-24'
collected: '2026-07-27'
category: Other
direction: 交互式AI解释性 · 扩散模型弯曲
tags:
- Explainable AI
- Diffusion Models
- Interactive Bending
- Stable Diffusion
- Creative Practice
- ComfyUI
one_liner: 通过交互式弯曲与检查界面，让艺术家操控扩散模型内部层以产生可预测的视觉效应
practical_value: '- 主要是学术贡献，面向艺术创作与交互式解释性研究，电商/推荐/Agent 业务可借鉴点有限。若涉及多模态生成工具的内部解释与调控，可参考其将模型层抽象为可干预单元并构建交互界面的思路，但直接迁移至搜索推荐系统的成本较高。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：艺术家需要将扩散模型视为可检查、修改和调试的创意材料，而非黑箱工具。现有 XAI 以技术为中心，忽视艺术实践中的动手介入需求。

**方法**：提出基于实验与干预的可解释性方法，在 ComfyUI 节点工作流中集成模型弯曲与交互式检查界面。界面支持交互式层选择与干预控制，允许艺术家直接操纵 Stable Diffusion 1.5 的内部组件（如注意力层、残差块等）。通过定性与定量分析弯曲干预效果，系统性记录不同层操作产生的视觉效应家族。

**关键结果**：操纵特定扩散管道组件能产出一致、可预测的视觉变化（如色彩偏移、构图调整、纹理变形），艺术家可借此建立对模型各层功能的直觉。该工作为艺术创作提供了新型调试与探索工具，使大型模型具备类似物理材料的可塑性。
