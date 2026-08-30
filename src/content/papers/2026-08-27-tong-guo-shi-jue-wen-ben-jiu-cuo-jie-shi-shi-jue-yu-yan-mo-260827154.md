---
title: 'ReViCo: Unveiling the Limitations of VLMs in Visual Text Understanding via
  Error Correction'
title_zh: 通过视觉文本纠错揭示视觉语言模型在图像文本理解上的局限
authors:
- Bojun Zhang
- Junhong Liang
- Feifei Zhai
- Fengxian Ji
- Yu Zhou
affiliations:
- State Key Laboratory of Multimodal Artificial Intelligence Systems, Institute of
  Automation, CAS, Beijing, China
- School of Artificial Intelligence, University of Chinese Academy of Sciences, Beijing,
  China
- Fanyu AI Laboratory, Zhongke Fanyu Technology Co., Ltd, Beijing, China
- Mohamed bin Zayed University of Artificial Intelligence
arxiv_id: '2608.27154'
url: https://arxiv.org/abs/2608.27154
pdf_url: https://arxiv.org/pdf/2608.27154
published: '2026-08-27'
collected: '2026-08-30'
category: Eval
direction: 多模态评估 · 视觉文本纠错
tags:
- VLM
- Benchmark
- Visual Text Understanding
- Error Correction
- OCR
- Multimodal
one_liner: 提出 ReViCo 基准，以视觉文本纠错任务评估 VLM 对图像内文字及其视觉上下文的理解能力
practical_value: '- 电商/广告图像中大量文字（价格、促销、成分、资质）是决策关键。可借鉴 ReViCo 的视觉文本纠错任务，构建内部“商品图文字纠错”评测集，重点考察模型对价格数字、折扣文案、生产日期等易错文本的识别与修正能力。

  - 业务用 VLM 做图文理解或信息抽取时，不要只依赖 OCR 指标；应增加“给出错误位置+修正结果”的输出要求，暴露模型在视觉上下文中误读文本的问题，降低后续
  Agent 或推荐链路中的错误传播。

  - 若需要快速提升，可参考其 targeted training 范式：用少量带标注的视觉文本纠错数据微调多模态模型，尤其针对业务中高频图像模板（banner、主图、详情页）提升鲁棒性；同时保留
  prompt-based 基线做对比。

  - 评估结果提示，即使 SOTA VLM 也可能误解图像内文字，设计 Agent 工作流时应增加校验环节，比如让模型输出原文与修正后文本，再由规则或 OCR 引擎交叉验证。'
score: 6
source: arxiv-cs.CV
depth: abstract
---

**动机**：VLM 在通用视觉任务表现好，但图像内文本理解不足，现有评估缺乏对“视觉文本+上下文”深层理解的要求。
**方法**：提出 ReViCo 基准，定义视觉文本纠错（VTEC）任务——模型需识别并修正真实世界图像中的文本错误，需理解文字与周围视觉情境的关系。用两种范式评估：prompt-based 直接询问和 targeted model training 微调，测试多类 VLM。
**结果**：最好 VLM 与人类仍有显著差距；多数模型难以准确感知视觉文本，常出现纠错错误。ReViCo 为更鲁棒、文本感知的 VLM 提供新基准。
