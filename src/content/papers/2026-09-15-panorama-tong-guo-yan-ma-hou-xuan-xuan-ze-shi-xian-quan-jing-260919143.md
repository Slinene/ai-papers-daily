---
title: 'PANORAMA: Panoptic Grounded Captioning via Mask Proposal Selection'
title_zh: PANORAMA：通过掩码候选选择实现全景接地图像描述
authors:
- Sara Pieri
- Evangelos Kazakos
- Shizhe Chen
- Josef Sivic
- Cordelia Schmid
affiliations:
- Inria, École normale supérieure, CNRS, PSL Research University
- Czech Institute of Informatics, Robotics and Cybernetics, Czech Technical University
  in Prague
arxiv_id: '2609.19143'
url: https://arxiv.org/abs/2609.19143
pdf_url: https://arxiv.org/pdf/2609.19143
published: '2026-09-15'
collected: '2026-09-18'
category: Other
direction: 视觉-语言 grounding 与稠密 caption
tags:
- Panoptic Grounded Captioning
- Mask Proposal Selection
- Vision-Language Model
- Dense Captioning
- Pixel-level Grounding
- Benchmark
one_liner: 提出 PanoCaps 基准与 PANORAMA 模型，将短语 grounding 形式化为掩码候选选择，联合生成稠密 caption 与像素级掩码
practical_value: '- 把需要精细化对齐的任务从“直接生成”改为“从候选池中选择”：推荐/搜索中生成 item 描述、解释或文案时，可先用用户/query
  表征条件化候选池，再训练选择器，降低生成难度并提升一致性。

  - 联合优化生成与对齐目标：PANORAMA 同时训练 caption 生成和 mask 选择，保证文本与实体一致；推荐系统做生成式推荐或解释生成时，可把 item
  embedding/属性对齐作为辅助 loss，避免生成内容与实体脱节。

  - 评价指标设计可借鉴 gPQ：同时量化文本与实体匹配，而不只看单一维度；多模态推荐、商品描述生成评估时可设计类似联合指标，避免只评文本流畅度忽略 grounding
  准确性。

  - 高效利用预训练模型：条件化冻结/预训练 segmenter 输出候选，而非端到端重训，适合业务中快速接入现有多模态编码器或分割模型，降低训练成本。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：现有 VLM 能生成流畅详细的图像 caption，但难以可靠地将短语关联到像素；结合 dense captioning 与像素级 grounding 的方法常出现描述不完整或分割 mask 不准。为此定义 panoptic grounded captioning 任务：VLM 需同时描述前景物体与背景区域，并为每个指代短语生成像素级 mask。

方法关键点：
- 构建 PanoCaps 基准：基于 panoptic segmentation 数据集人工标注，提供近完全像素覆盖的稠密 caption 与实体级图像-文本对齐，并设计 phrase-mask matching 协议及广义 Panoptic Quality (gPQ) 指标，联合评估文本与 mask 一致性。
- 提出 PANORAMA：将 phrase grounding 形式化为从 phrase-conditioned mask proposal pool 中选择；用 contextualized phrase 表示条件化预训练 segmenter 获得候选 mask，再学习为每个短语选择对应 mask；与 caption 生成联合训练，允许一个短语指代单个区域或多个实例。

关键结果：PANORAMA 在 PanoCaps 上取得最佳 overall grounding，并在多个 pixel-level grounding 任务上匹配或超过专用模型，同时保持详细且 mask 一致的 caption。代码、数据与模型已开源。
