---
title: 'SpatialBlock: Enhancing Spatial Intelligence in LVLMs via Synthetic Block-Stacking
  Problem'
title_zh: SpatialBlock：通过合成积木堆叠问题增强 LVLM 空间智能
authors:
- Soohyun Ryu
- Sohee Kim
- Eunho Yang
affiliations:
- KAIST
- AITRICS
arxiv_id: '2609.07064'
url: https://arxiv.org/abs/2609.07064
pdf_url: https://arxiv.org/pdf/2609.07064
published: '2026-09-06'
collected: '2026-09-13'
category: Multimodal
direction: LVLM 空间智能 · 合成数据训练
tags:
- LVLM
- Spatial Intelligence
- Synthetic Data
- Block-Stacking
- Spatial Reasoning
- 3D-to-2D
one_liner: 用 15k 合成积木堆叠数据训练 LVLM，显著提升 3D 空间推理并泛化到真实场景
practical_value: '- 借鉴合成数据思路：当真实标注昂贵且有噪声时，用结构化合成任务训练模型专项能力。在电商场景可生成产品摆放/货架布局/包装堆叠等合成图像，低成本提升
  LVLM 对商品空间关系的理解。

  - 锚点式推理：通过 controlled color modulation 注入视觉线索，引导模型在复杂图像中关注关键区域。可用于商品图属性标注、广告创意布局评估等任务，降低对密集几何标注的依赖。

  - 小规模高针对性数据集即可带来泛化：15k 合成数据就能提升真实空间任务，说明针对核心认知子任务的合成数据比大规模弱标注更高效，适合业务中快速验证新能力。

  - 多目标训练：直接回答与 reasoning-based prediction 两种方式均可提升，可在业务 LLM 中同时保留直接输出和 CoT 解释输出，提升鲁棒性。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：LVLMs 在 2D 图像理解上表现强，但从 2D 图像重建 3D 结构并进行空间推理的能力仍有限。现有方法依赖真实场景空间问答数据集，需要密集几何标注，成本高、噪声大。受人类认知发展启发，提出通过积木堆叠等结构化操作任务学习基础空间技能。

**方法关键点**：构建 SpatialBlock-15k 合成数据集，包含 15,000 个积木堆叠问题，覆盖 3D-to-2D 投影、视角变换、结构组合三类任务；进一步加入受控颜色调制作为视觉线索，鼓励模型在复杂视觉条件下进行锚点式推理。训练时支持直接回答和带推理的预测两种范式。

**关键结果**：在 SpatialBlock-15k 上训练的 LVLMs 显著优于基线，并且尽管数据是合成且规模紧凑，仍能泛化到真实世界空间任务，证明通过合成积木任务注入空间归纳偏置的有效性。
