---
title: Distilling Routed 3D Privilege for Spatial Reasoning in Vision-Language Models
title_zh: 路由化 3D 特权蒸馏提升视觉语言模型空间推理
authors:
- Hongxing Li
- Yixin Li
- Dingming Li
- Zixuan Wang
- Yuchen Yan
- Wenqi Zhang
- Weiming Lu
- Yongliang Shen
affiliations:
- 浙江大学
arxiv_id: '2610.12355'
url: https://arxiv.org/abs/2610.12355
pdf_url: https://arxiv.org/pdf/2610.12355
published: '2026-10-07'
collected: '2026-10-11'
category: Reasoning
direction: VLM 空间推理 · 特权蒸馏
tags:
- Spatial Reasoning
- VLM
- Distillation
- GRPO
- 3D Privilege
- On-Policy Self-Distillation
one_liner: 将深度、语义、BEV 等 3D 几何线索作为特权，在 GRPO 中对错误轨迹做路由化蒸馏，提升 VLM 空间推理且部署保持仅 RGB
practical_value: '- 借鉴「特权信息蒸馏」思路：训练时引入部署时不可用的 3D 几何、商品属性、用户行为后验等特权信号作为教师，通过 KL 蒸馏到仅
  RGB/文本输入的在线模型，在不增加推理延迟的前提下提升空间推理或多模态判断能力，尤其适合电商图像中的家具尺寸、商品摆放、场景布局理解。

  - 借鉴「仅对错误轨迹施加特权 KL」的稀疏监督：在 RLVR/GRPO 流程中，只对模型出错的样本做特权蒸馏，能更高效利用稀疏错误信号，降低训练开销并改善收敛稳定性；推荐/Agent
  系统中也可以只对失败案例蒸馏专家/特权信息。

  - 借鉴「问题条件路由」：按问题内容只注入相关几何线索（如当前问的是距离则只给深度，问的是方向则给 BEV），而非全量上下文，避免冗余信息稀释注意力；可迁移到
  Agent 或推荐模型中对多源特征的按需路由与融合。

  - 多种特权可以互补：答案特权和几何特权叠加优于单一特权，业务上可同时蒸馏商品属性、用户反馈、场景 3D 等多类特权，进一步压缩模型与真实环境的信息差。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：空间推理仍是 VLM 的短板，因为 RGB 输入不直接提供几何证据，模型只能从表观推断深度与布局。现有方案要么在推理时注入 3D 模块，带来架构与延迟成本；要么只用结果奖励训练，无法纠正感知层面的空间错误。

**方法关键点**：GPD（Geometry-Privileged Distillation）在 on-policy self-distillation 框架下，把几何证据作为特权。对每个问题，将深度、语义、鸟瞰图（BEV）线索渲染为紧凑文本，按问题条件路由给教师模型，同时提供参考答案；特权 KL 只在模型生成错误轨迹时施加，并与 GRPO 结合。部署模型保持仅 RGB，不增加推理成本。

**关键结果**：在 4B 骨干上，GPD 在 VSI-Bench 达 57.1，在 MindCube、SPARBench、MMSI-Bench、ViewSpatial 四个基准平均 37.6，均优于 GRPO 和 answer-privileged OPSD。消融证实 3D 特权与答案特权互补、问题条件路由优于全上下文注入、只对错误轨迹蒸馏效果更佳。
