---
title: 'PhyWorld: Physics-Faithful World Model for Video Generation'
title_zh: PhyWorld：通过流匹配与DPO后训练提升视频生成物理忠实度
authors:
- Pu Zhao
- Juyi Lin
- Timothy Rupprecht
- Arash Akbari
- Chence Yang
- Rahul Chowdhury
- Elaheh Motamedi
- Arman Akbari
- Yumei He
- Chen Wang
affiliations:
- Northeastern University
- University of Georgia
- Tulane University
- EmbodyX
arxiv_id: '2605.19242'
url: https://arxiv.org/abs/2605.19242
pdf_url: https://arxiv.org/pdf/2605.19242
published: '2026-05-19'
collected: '2026-05-23'
category: Other
direction: 视频生成世界模型后训练
tags:
- Video Generation
- World Model
- Direct Preference Optimization
- Flow Matching
- Physics Faithfulness
one_liner: 二阶段后训练（流匹配微调 + DPO）让视频生成模型产出物理更合理的时序延续
practical_value: '- **两阶段后训练流程可复用**：先流匹配微调保时序一致性，再用DPO对齐偏好，这种组合可迁移到推荐系统的商品视频生成，例如改善动态展示的连贯性和物理合理性。

  - **偏好对构建思路**：通过仿真引擎生成物理正确/违背的视频对，可为其他领域提供人工标注之外的偏好数据构造方法，例如用商品3D模型渲染符合物理规律的交互视频。

  - **细粒度评估基准设计**：分物理定律打分的评估方案可用于生成式推荐中检验生成内容的属性控制，如光照、运动是否符合预期。

  - **业务可借鉴点有限**：整体面向物理AI仿真，与电商/Agent直接关联较弱，主要学术贡献在于世界模型后训练。'
score: 7
source: arxiv-cs.MM
depth: abstract
---

**动机**：大型视频生成模型可作为世界模拟器训练Physical AI，但现有模型生成的视频常违背物理规律（如物体穿透、运动不连贯），无法提供安全可靠的仿真环境。需提升视频延续的物理忠实性。

**方法**：PhyWorld在基模型上做两阶段后训练。第一阶段，用流匹配（Flow Matching）对video-to-video continuation任务微调，让模型稳定保持输入场景的视觉属性并生成连贯运动；第二阶段，构建物理偏好对（同一条件下符合物理规律的视频 vs 违背规律的视频），通过Direct Preference Optimization (DPO) 引导模型倾向生成物理合理的动态。

**结果**：在VBench视频质量基准上，PhyWorld平均分0.769，优于最强基线0.756；在自建物理忠实度基准上平均分3.09（基线2.99），各项物理定律（如重力、碰撞）得分均有提升，证明后训练能增强世界模拟器的物理一致性。
