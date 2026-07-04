---
title: 'InstanceControl: Controllable Complex Image Generation without Instance Labeling'
title_zh: InstanceControl：无需实例标注的可控复杂图像生成
authors:
- Xiaoyu Liu
- Huan Wang
- Fan Li
- Zhixin Wang
- Jiaqi Xu
- Ming Liu
- Wangmeng Zuo
affiliations:
- Harbin Institute of Technology
- HUAWEI Noah's Ark Lab
arxiv_id: '2606.31924'
url: https://arxiv.org/abs/2606.31924
pdf_url: https://arxiv.org/pdf/2606.31924
published: '2026-06-29'
collected: '2026-07-04'
category: Other
direction: 多实例可控图像生成 · VLM自动对应
tags:
- Controllable Generation
- Multi-Instance
- Vision-Language Model
- Diffusion Models
- Instance Masks
one_liner: 利用视觉语言模型自动建立文本描述与视觉条件间的实例级对应，消除手动标注，实现高保真多实例控制。
practical_value: '- 在电商商品场景图生成中，可使用类似VLM自动将多个商品文本描述映射到布局或深度图的区域，省去人工标注实例位置。

  - 自适应掩码细化策略可通过迭代校正噪声掩码，提升多实例属性绑定的准确性，可迁移至多模态检索或视频中目标跟踪任务。

  - 该方法展示了如何利用大规模预训练模型（如VLM）的零样本能力进行细粒度对齐，可为电商广告创意生成中的多物品组合控制提供参考。

  - 工程实现上，可将VLM作为插件集成到现有扩散模型生成流程中，无需额外训练数据集，降低部署成本。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有的可控图像生成方法（如ControlNet）在多实例场景中常发生属性混淆，例如将蜘蛛侠的颜色错误地赋予钢铁侠。近期工作尝试通过人工标注实例掩码来解决，但标注成本高。本文旨在消除对实例标注的依赖，实现自动化的多实例可控生成。

**方法**：核心思想是利用视觉-语言模型（VLM）建立文本提示词与视觉条件（如深度图）之间的实例级对应关系。具体来说，VLM首先从文本提示中解析出各个实例的描述，并基于视觉条件预测出对应区域的实例掩码。为了解决掩码可能存在的噪声，引入了一种自适应掩码细化策略，在生成过程中动态调整实例掩码，逐步提升定位精度。该方法无需额外训练实例标注数据，完全依靠预训练VLM的零样本能力。

**结果**：在多个复杂多实例场景上的实验表明，InstanceControl在生成保真度和实例级控制精度上均超越了现有最先进方法，有效缓解了属性混淆问题。
