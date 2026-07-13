---
title: 'CtrlVTON: Controllable Virtual Try-On via Visual-Instance-Prompt Segmentation'
title_zh: CtrlVTON：基于视觉实例提示分割的可控虚拟试穿
authors:
- Seungyong Lee
- Hyun Jun Jang
- Sangoh Kim
- Sungjoon Park
affiliations:
- NXN Labs
- KAIST
arxiv_id: '2607.09362'
url: https://arxiv.org/abs/2607.09362
pdf_url: https://arxiv.org/pdf/2607.09362
published: '2026-07-10'
collected: '2026-07-13'
category: Other
direction: 可控虚拟试穿 · 像素级布局控制
tags:
- Virtual Try-On
- Controllable Generation
- Segmentation
- Diffusion Models
- Image Editing
- VIP-SAM
one_liner: 提出VIP-SAM实例分割与CtrlVTON图像编辑框架，首次实现试穿中服装风格、尺寸和位置的像素级控制
practical_value: '- 可控试穿为电商商品详情页生成多样化模特图（不同穿法、松紧度），提升用户购买信心

  - 配合用户偏好掩码可实现个性化虚拟试穿，增强推荐系统的可视化吸引力与解释性

  - VIP-SAM分割能力可用于UGC图片中自动识别同款服装，辅助搭配推荐与社交电商

  - 像素级控制思想可迁移至家居、美妆等场景，为生成式推荐提供更精细的可控生成能力'
score: 6
source: arxiv-cs.CV
depth: abstract
---

**动机**：现有虚拟试穿系统缺乏对穿着方式的控制，如服装松紧、塞入与否、空间位置等，用户无法自定义穿衣效果。

**方法**：论文从两方面解决该问题。① 定义视觉实例提示分割（VIP-SAM）：给定服装平面图，在人物照片中分割出穿着该特定实例的区域，不同于传统类别级分割。② 提出 CtrlVTON 框架，将试穿转化为图像编辑任务，利用分割掩码作为像素级控制信号，实现服装款式、尺寸、空间布局的细粒度调节，并支持多件服装同时试穿。

**结果**：VIP-SAM 与 CtrlVTON 在各自任务上均达到最优。CtrlVTON 能忠实遵循用户绘制的掩码布局，对布局的遵循度远超商业闭源编辑系统，同时保持与领先方法相当的服装保真度。
