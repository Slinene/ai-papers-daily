---
title: 'ENTRAP-VL: A Taxonomic Probe for Dual Contextual Entrainment in Vision-Language
  Models'
title_zh: ENTRAP-VL：视觉语言模型双重上下文夹带分类探测工具
authors:
- Karan Goyal
- Afreen Hossain
- Debojyoti Das
- Vishal Bhutani
affiliations:
- IIIT Delhi, India
- Dr. Ambedkar Institute of Technology, India
- Heritage Institute of Technology, India
- PwC, India
arxiv_id: '2607.20092'
url: https://arxiv.org/abs/2607.20092
pdf_url: https://arxiv.org/pdf/2607.20092
published: '2026-07-21'
collected: '2026-07-25'
category: Eval
direction: 多模态评估工具 · 上下文忠诚度探测
tags:
- contextual entrainment
- VLM
- probing
- dataset
- taxonomy
- multimodal
one_liner: 提出首个用于多模态上下文夹带探测的双模分类基准 ENTAP-VL，以文本和视觉独立诱发夹带现象。
practical_value: '- 电商多模态搜索/推荐中，产品图片和描述常被无关上下文干扰，可借鉴双流探测思想，设计文本和视觉独立的鲁棒性测试集，检验模型是否被不相关但合理的上下文带偏。

  - 评估多模态商品理解模型时，可构建类似“真实性-关联度”2×2 分类探针，检测模型是否轻信虚假但可能的上下文（如 PS 背景、误导性配文），提升可信度。

  - 在 Agent 调用 VLM 进行多模态决策（如图文问答、商品审核）时，可将该探针作为安全检测环节，避免上下文注入攻击导致错误输出。

  - 该工作的分类夹带条件设计（无上下文、随机上下文、矛盾上下文等）可直接复用，用于自制多模态评测集，量化模型对干扰的敏感度。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：语言模型的上下文夹带（entrainment）指无关、错误甚至无意义的上下文仍会牵引模型输出。该现象在纯文本模型中已有机械学解释，但在视觉语言模型（VLM）中几乎未被研究，且缺乏专用测评工具。将现有文本基准简单移植到多模态不够，需要一种围绕具体项（图中物体、文本查询）构建的双模分类工具。

**方法关键点**：提出 ENTRAP-VL，一个手工标注的 1500 样本数据集，覆盖 8 个类别。分类轴有两个：上下文与项的关联度（相关联 vs. 不关联）、与事实的关系（真 vs. 假）。分为两个流：文本诱发流（8 种上下文条件，如无上下文、随机真/假上下文、错误关联上下文等）和视觉诱发流（3 种条件，如图像内添加无关物体、修改属性等）。双模设计使夹带可独立由文本或视觉驱动，并引入“可能为假但世界合理”的真实性区分，这是纯文本设定中不存在的。

**关键结果**：数据集未测量具体模型表现，而是提供研究工具、分类动机和评估协议，以推动社区对 VLM 夹带现象的严谨研究。数据与文档将公开。
