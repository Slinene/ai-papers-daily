---
title: 'CODE: Cross-Modal Calibration and Dynamic Suppression for Open World Object
  Detection'
title_zh: CODE：面向开放世界目标检测的跨模态校准与动态抑制
authors:
- Hao Xu
- Zhaoning Shi
- Hehe Jin
- Bo Ma
affiliations:
- Beijing Institute of Technology
arxiv_id: '2608.27214'
url: https://arxiv.org/abs/2608.27214
pdf_url: https://arxiv.org/pdf/2608.27214
published: '2026-08-27'
collected: '2026-08-30'
category: Multimodal
direction: 多模态基础模型的开放世界检测
tags:
- Open World Object Detection
- Cross-Modal Calibration
- Multimodal Foundation Models
- OOD Detection
- Inference-Time
one_liner: 提出推理时跨模态校准与动态抑制框架，在 OWOD 基准上 U-mAP/K-mAP 分别提升 2.6/2.3 点
practical_value: '- 多模态检索/推荐中常见的单向 text-to-vision 匹配可用全局视觉原型校准文本驱动分数，缓解文字描述与商品图像之间的语义歧义，适合商品搜索、广告创意匹配等场景。

  - 对冷启动或未入库新品，可借鉴「从局部视觉响应测量分类犹豫度」的思路，检测模型不确定的区域并将其强化为潜在未知商品，辅助发现新类目或 UGC 中的未标商品。

  - 在 query/商品类目分类中，用 margin-aware 动态离群点抑制替代刚性阈值，能保留决策边界附近的模糊样例，减少对长尾 query 的误杀，提升召回。

  - 整套方法是推理时框架，不重新训练基础模型，可作为插件层覆盖现有 VLM/多模态 API，适合快速验证跨模态校准与 OOD 检测策略。'
score: 6
source: arxiv-cs.CV
depth: abstract
---

动机：开放世界目标检测（OWOD）使用多模态基础模型时，文本到视觉的单向匹配带来语义歧义；同时刚性离群点惩罚会过度抑制已知类边界附近的未知物体。

方法关键点：CODE 是统一推理时框架，包含三个互补模块：1）跨模态联合置信度校准：注入全局视觉原型，校准文本驱动的已知类预测；2）不确定性引导的通用目标性增强：从局部视觉响应测量分类犹豫，强化潜在未知物体；3）基于置信度边界的动态离群点抑制：用边界感知调整替代刚性抑制，保留模糊 OOD 实例。无需重训。

关键结果：在 Real-World Detection 基准上，使用 OWL-ViT L/14 骨干，Task 1 达到 21.7 U-mAP、40.8 K-mAP，分别超过先前 SOTA 2.6 和 2.3 点。
