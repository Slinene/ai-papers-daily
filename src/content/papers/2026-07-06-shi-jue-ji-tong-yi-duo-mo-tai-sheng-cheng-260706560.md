---
title: Vision as Unified Multimodal Generation
title_zh: 视觉即统一多模态生成
authors:
- Xiaoyang Han
- Jianhua Li
- Kewang Deng
- Zukai Chen
- Xuanke Shi
- Sihan Wang
- Boxuan Li
- Linyan Wang
- Siyi Xie
- Xin You
affiliations:
- SenseTime Research
- Nanyang Technological University
- The Chinese University of Hong Kong
- Peking University
- Shanghai Jiao Tong University
arxiv_id: '2607.06560'
url: https://arxiv.org/abs/2607.06560
pdf_url: https://arxiv.org/pdf/2607.06560
published: '2026-07-06'
collected: '2026-07-08'
category: Multimodal
direction: 视觉任务统一为多模态指令生成
tags:
- Unified Multimodal Generation
- Instruction Tuning
- Vision Foundation Model
- Task Unification
- Text-Image Generation
one_liner: 将异构视觉任务统一为多模态生成，单一模型通过指令输出文本或图像，匹配专家系统
practical_value: '- 统一生成范式可迁移至电商推荐：将召回、排序、解释等任务统一为自然语言指令驱动的多模态生成，降低多任务工程开销。

  - 指令与视觉提示机制可直接用于多模态搜索Agent：允许用户通过自然语言和区域/属性提示灵活指定需求，模型输出文本或结构化推荐结果。

  - 异构标注转指令数据集的方法可复制到推荐场景：将点击、购买、评论等行为数据转化为指令-回答对，支持推荐模型的指令微调。

  - 从预训练多模态模型出发，混合任务数据保持能力的训练策略，适合构建兼具通用知识与业务专长的推荐Agent。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：将计算机视觉集成为通用基础模型的统一能力，消除任务特定预测头与架构修改。

**方法**：定义范式为“多模态生成”——输入自然语言指令和可选视觉提示（指定区域、视角、解码约定），输出文本（符号化结果）或图像（密集预测）。构建 **SenseNova-Vision Corpus**：将检测、OCR、关键点、分割、深度、法线、点图、相机姿态等异构标注转化为指令-回答样本，覆盖文本、图像和混合目标。从一个现成预训练统一多模态模型出发，在该语料上主训练，辅以通用多模态数据保持能力，无需任务专用修改。

**结果**：统一模型在结构化视觉理解、密集几何预测、分割及多视图几何等多项基准上达到领先专用系统水平。例如，Common Det F1@mIoU 达 56.6，其他密集预测任务上同样匹配专家模型，证明统一生成范式可扩展地将CV集成到通用基础模型中。
