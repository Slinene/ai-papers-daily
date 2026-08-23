---
title: 'ArmorOCR: Grounded Adversarial Visual Perception via Observation-Transferred
  Self-Distillation'
title_zh: ArmorOCR：基于观察迁移自蒸馏的对抗视觉文本感知
authors:
- Linhan Cao
- Siyuan Li
- Jun Lan
- Liangbo He
- Guannan Li
- Xiaolei Huang
- Jun Jia
- Shuheng Zhou
- Huijia Zhu
- Weiqiang Wang
affiliations:
- Ant Group
- Shanghai Jiao Tong University
- East China Normal University
arxiv_id: '2608.20122'
url: https://arxiv.org/abs/2608.20122
pdf_url: https://arxiv.org/pdf/2608.20122
published: '2026-08-20'
collected: '2026-08-23'
category: Training
direction: 多模态对抗 OCR 鲁棒训练
tags:
- Adversarial OCR
- Self-Distillation
- GRPO
- Multimodal
- Benchmark
- LMM
one_liner: 提出首个对抗性 OCR 基准 AdvSpot，并以观察迁移自蒸馏与 GRPO 提升 LMM 对抗文本定位识别鲁棒性
practical_value: '- 电商图像中常见变形、遮挡、水印等对抗性文字，可借鉴 AdvSpot 的 13 类模式与区域级标注构造内部鲁棒 OCR 测试集，评估商品标题、标签、资质文本识别。

  - OPSD 用 privileged transformed observations 做自蒸馏：先让模型在易读观察上生成定位/识别伪标签，再迁移到对抗观察，可迁移到用户上传图、广告素材等难例训练。

  - GRPO 奖励拆分为 localization、recognition、full spotting、VQA 四类并动态加权，可作为多任务强化微调的 reward
  设计模板，适用于需要同时优化定位与理解的多模态 Agent 任务。

  - 保持通用 OCR 能力不掉的训练策略（两阶段、混合数据）可借鉴到已有 LMM 的鲁棒性增强，避免只提升对抗场景而伤害线上自然文本识别。'
score: 6
source: arxiv-cs.CV
depth: abstract
---

**动机**：LMM 在自然 OCR 上表现强，但对人类可读但模型难以定位/识别的对抗性视觉文本脆弱；现有 OCR 基准缺少对抗文本的规模化、区域级评估。

**方法关键点**：
- 将对抗 OCR 形式化为 grounded OCR perception 任务，并提出首个基准 AdvSpot：390 张图像、区域级标注，覆盖 5 大类 13 种细粒度对抗 OCR 类型。
- 提出 ArmorOCR 两阶段训练框架：第一阶段 On-Policy Self-Distillation (OPSD)，从 privileged transformed observations 中蒸馏缺失的对抗 OCR 感知能力；第二阶段用 Group Relative Policy Optimization (GRPO) 结合任务条件奖励，对定位、识别、全 spotting 和 VQA 四项子任务分别设计 reward 进行细化。

**关键结果**：在 AdvSpot、其他对抗 OCR 基准与通用 OCR 基准上，ArmorOCR 一致提升对抗 OCR 感知，同时保持通用 OCR 能力不退化。
