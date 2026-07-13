---
title: Evolution of Accuracy and Visual-Cognitive Errors in a Decade of Vision-Language
  AI Models
title_zh: 十年间视觉语言模型准确度与视觉认知错误的演进
authors:
- Shravan Murlidaran
- Miguel P. Eckstein
affiliations:
- University of California, Santa Barbara
arxiv_id: '2607.09654'
url: https://arxiv.org/abs/2607.09654
pdf_url: https://arxiv.org/pdf/2607.09654
published: '2026-07-10'
collected: '2026-07-13'
category: Eval
direction: 多模态视觉语言模型评估与错误分析
tags:
- VLM
- Scene Description
- Error Analysis
- Multimodal Evaluation
- CSB Dataset
one_liner: 引入复杂社会行为数据集，评估十年间VLM场景描述准确度提升，并分析五类错误演变
practical_value: '- 电商商品图描述、用户行为理解等场景可借鉴 CSB 数据集思路，自建包含复杂交互的测试集，系统性评估多模态模型在业务场景下的描述准确度。

  - 五种错误类型（目标检测、识别、幻觉、场景理解、空间依赖）可直接作为诊断维度，监控线上多模态模型的输出质量，重点排查高影响的检测/识别/幻觉错误。

  - MLLM 在复杂场景已接近人类但仍有空间依赖误差，提示在商品详情理解、直播画面解析等应用中需关注模型是否关注了关键区域，可引入注意力可视化辅助校验。

  - 论文揭示了预训练与指令微调阶段模型的性能鸿沟，为业务选型提供依据：复杂视觉理解任务应优先选用 MLLM，并围绕空间依赖等残余误差做针对性优化。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：过去十年 VLM 评估多基于简单场景（MS-COCO），缺乏对人类复杂社交行为的覆盖，且未系统分析模型错误类型。为此构建包含 100 张复杂社交行为图片的 CSB 数据集，并设计五种视觉认知错误类型（目标检测、识别、幻觉、场景理解、空间依赖），旨在全面刻画 VLM 场景描述能力的演进。

**方法关键点**：收集 2017 至 2025 年间 9 款模型（4 款 pre-MLLM、5 款 MLLM）及 20 名人类对 CSB 和 MS-COCO 子集的场景描述，以专家金标准为参照，计算准确率并标注错误类型。

**关键结果**：1) CSB 上的准确率提升比 MS-COCO 更显著，pre-MLLM 远逊于最差人类描述，MLLM 已达最优人类水平；2) MLLM 消除了简单与复杂场景间的准确率差距；3) 除偶尔的空间依赖错误，其余错误类型几乎被消除；4) 检测、识别、幻觉错误对准确率影响最大。
