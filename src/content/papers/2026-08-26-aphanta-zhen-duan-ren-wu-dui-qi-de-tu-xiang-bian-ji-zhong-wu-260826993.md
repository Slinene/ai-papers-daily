---
title: 'Aphanta: Diagnosing Task-Aligned Image-Edited Intermediates for Multimodal
  Reasoning'
title_zh: Aphanta：诊断任务对齐的图像编辑中间产物在多模态推理中的效用
authors:
- Hengyuan Xu
- Wei Cheng
- Yumeng Ji
- Xuanyang Zhang
- Xianfang Zeng
- Gang Yu
- Xingjun Ma
affiliations:
- Fudan University
- StepFun
- Shanghai Jiaotong University
arxiv_id: '2608.26993'
url: https://arxiv.org/abs/2608.26993
pdf_url: https://arxiv.org/pdf/2608.26993
published: '2026-08-26'
collected: '2026-08-29'
category: Multimodal
direction: 多模态推理 · 图像编辑中间产物诊断
tags:
- MLLM
- Image Editing
- Multimodal Reasoning
- Diagnostic Framework
- Evaluation
one_liner: 提出闭环诊断框架 Aphanta，量化图像编辑中间产物在多模态推理中的任务条件化增益与边界
practical_value: '- 评估生成式中间产物（如 Semantic ID、图像生成、检索文档）时，应加入 idealized reference 条件，分离上游生成器误差与下游模型能力上限，避免把生成器的失败误判为方法无效。

  - 不要假设同一中间表示对所有任务都有帮助；应识别任务条件化增益的边界。在电商场景中，可先诊断哪些商品属性或查询类型适合用图像生成/编辑增强，而不是全量铺开。

  - 闭环诊断协议可复用到 Agent 工具调用：自动发现候选任务，对比直接推理、工具生成中间产物推理、理想化中间产物推理三种条件，量化工具的真实贡献与失效模式。

  - 从结果看，图像编辑作为“专用视觉工作区”更适合视觉线索注入、定位和反事实状态实现；对于需要精确结构外推的任务，应避免依赖当前生成器，或引入校验环节。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：显式视觉中间产物能帮助 MLLM 外化空间证据和更新视觉状态，但其效用取决于图像编辑器能否忠实实现所需变换。现有工作通常默认视觉中间产物有益，缺乏对任务对齐和编辑器实现能力的系统诊断。

**方法关键点**：提出 Aphanta，一个自动化任务发现与闭环诊断框架，针对 MLLM→图像编辑器→MLLM pipeline。框架评估三种条件：直接推理、使用编辑器生成的中间产物推理、使用理想化参考中间产物推理，以分离潜在视觉收益与当前编辑器的实际效用。覆盖 20 个候选任务及多组 editor-MLLM 组合。

**关键结果**：效用呈现强任务条件化。增益集中在视觉线索注入、接地定位和反事实状态实现；需要符号敏感构建或结构外推的中间产物则显著不可靠。在选定的正任务子集上，整合的 Qwen pipeline 将平均任务分数从 0.343 提升至 0.445（+10.2 点，相对提升 29.7%）；完整研究同时保留过滤与失败任务以暴露能力边界。
