---
title: Enhancing In-context Panoramic Generation via Geometric-aware Pretraining
title_zh: 面向上下文全景生成的几何感知预训练框架
authors:
- Haoran Feng
- Ruiyang Zhang
- Longyi Zhang
- Dizhe Zhang
- Lu Qi
affiliations:
- Insta360 Research
- Tsinghua University
- Beihang University
- Wuhan University
arxiv_id: '2607.08765'
url: https://arxiv.org/abs/2607.08765
pdf_url: https://arxiv.org/pdf/2607.08765
published: '2026-07-08'
collected: '2026-07-11'
category: Other
direction: 全景图像生成 · 几何感知预训练
tags:
- Panoramic Generation
- In-context Learning
- Depth Generation
- Circular Padding
- Similarity Loss
one_liner: 通过几何感知预训练和 token 级任务统一，提升全景图像生成的几何一致性与任务覆盖度
practical_value: '- 全景生成与电商/Agent 直接关联弱，但几何一致性设计可迁移到需保持结构约束的生成任务（如商品多视角合成、虚拟试穿），用深度预估辅助纹理生成。

  - 统一任务框架思路值得借鉴：通过 token 级条件拼接，将风格迁移、修复、外扩等多个任务融入单一模型，降低工程维护成本。

  - 针对领域特性设计辅助损失（如这里的相似度正则与圆形填充）可推广到其他对称性或循环结构生成问题（如系列 Banner 设计）。

  - 主要仍是学术贡献，业务可借鉴点较有限。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：全景图像生成通常缺乏大规模、高质量配对数据，且现有模型难以处理全景特有的几何畸变和全局一致性，任务之间也相互割裂。

**方法关键点**：
- 构建 1M 高质量全景配对数据集 Canvas360Dataset，覆盖风格迁移、修补、外扩、编辑四类任务。
- 提出两阶段框架：几何感知预训练 + 下游任务微调。预训练阶段通过并行深度生成、速度圆形填充（velocity circular padding）和相似度损失正则化，迫使模型学习几何感知表示，缓解边缘畸变并提升跨边界一致性。
- 下游任务统一为 token 级条件拼接范式，一个模型支持多种全景生成任务。

**结果**：在全景专用指标 FAED 上大幅领先，其他定量评估中也取得竞争或最优性能，视觉保真度和几何连贯性均有显著提升。
