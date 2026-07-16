---
title: 'MonkeyOCRv2: A Visual-Text Foundation Model for Document AI'
title_zh: MonkeyOCRv2：面向文档AI的视觉-文本基础模型
authors:
- Yuliang Liu
- Zhang Li
- Ziyang Zhang
- Shuo Zhang
- Qiang Liu
- Jiajun Song
- Zidun Guo
- Xinhan Wang
- Handong Zheng
- Yang Liu
affiliations:
- Huazhong University of Science and Technology
- Kingsoft Office
arxiv_id: '2607.11562'
url: https://arxiv.org/abs/2607.11562
pdf_url: https://arxiv.org/pdf/2607.11562
published: '2026-07-13'
collected: '2026-07-16'
category: Multimodal
direction: 文档视觉预训练 · 多模态基础模型
tags:
- Document AI
- Visual Pretraining
- OCR
- Multimodal
- Foundation Model
- Pretraining Strategy
one_liner: 面向文档图像的视觉-文本预训练模型，通过联合生成与重建策略提升多任务性能，冻结后可作为高效的多模态LLM视觉编码器
practical_value: '- **商品图像文本增强**：联合生成与像素重建的预训练策略对字符笔画和布局高度敏感，可直接用于提升电商商品图、广告素材的OCR准确率，特别是小字、艺术字、复杂背景下的关键信息提取。

  - **高效商品文档解析**：冻结MonkeyOCRv2+轻量LM（0.7B）即可获得SOTA文档解析效果，推理开销远低于通用大模型，适合大规模商品描述、质检报告、报关单据的结构化信息抽取。

  - **多语言支持**：预训练涵盖17种语言，对国际化电商平台处理多语言商品标题、评论图片、广告文案有直接帮助，无需额外语言适配。

  - **篡改检测与内容审核**：模型在文档篡改检测上的强大能力可迁移至商品图片真伪鉴定、用户评论截图真实性审核等风控场景。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：通用视觉编码器预训练于自然图像，缺乏对密集文本与字符笔画的细粒度感知，难以有效应用于文档图像。

**方法**：构建目前最大的文档图像预训练语料库MonkeyDoc v2（1.13亿张图像，覆盖17种语言），并提出联合学习策略——同时进行图像到文本生成（对齐视觉与文本语义）和像素级文档重构（保留字符笔画与布局细节）。

**结果**：在文本识别、公式识别、文本检测、文档篡改检测和重叠文本分割五项任务上，替换编码器后性能全面提升（如CRNN准确率从58.7%提升至67.3%）。作为多模态LLM视觉编码器，冻结后与0.7B语言模型组合，在文档解析基准MDPBench上超越此前最佳开源3B模型2.8个百分点（视觉编码器仅为其1/11）；在文档理解八项基准上优于基于CLIP、DINO、SAM的模型。证明文档导向的视觉预训练可独立作为文档智能的基础底座。
