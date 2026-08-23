---
title: 'GRACE: Grounded Reasoning via Adapter Composition and Evidence-Aware Calibration
  for Educational Visual Question Answering'
title_zh: GRACE：通过适配器组合与证据感知校准实现教育视觉问答的接地推理
authors:
- Xinjin Li
- Yudi Xia
- Xi Zhao
- Yiliu Xu
- Yining Liu
- Cheng Lu
- Yujian Long
- Yu Ma
- Jinghan Cao
- Liang Fan
affiliations:
- Columbia University
- Carnegie Mellon University
- University of California, Berkeley
- Stevens Institute of Technology
- Georgetown University
arxiv_id: '2608.19355'
url: https://arxiv.org/abs/2608.19355
pdf_url: https://arxiv.org/pdf/2608.19355
published: '2026-08-19'
collected: '2026-08-23'
category: Multimodal
direction: 多模态VQA · 参数高效适配
tags:
- Multimodal VQA
- Adapter Composition
- Parameter-Efficient Fine-Tuning
- Evidence-Aware Calibration
- ScienceQA
- Educational AI
one_liner: GRACE利用题目教学状态路由轻量语言与视觉适配器并做证据感知选项校准，在ScienceQA上将准确率从90.5%提升至93.1%
practical_value: '- 将结构化业务状态（如类目、场景、用户意图、选项/候选结构）作为路由信号，组合不同因子专属的轻量 adapter 或 prompt，可在不微调大模型的前提下实现多场景/多任务适配，类似推荐系统中的多场景专家路由。

  - 证据感知选项校准：在共享上下文中对所有候选联合打分并校准，可借鉴到电商搜索/推荐的精排阶段，尤其适合语义相近的候选（如相似商品标题/广告文案）的去混淆排序。

  - 冻结多模态 LLM，仅训练轻量视觉/语言 adapter，降低多模态业务（商品图+文本描述）接入大模型的训练成本，便于快速迭代。

  - 消融实验说明结构化状态、跨模态证据和选项校准各自贡献约为1-1.5个点，提示在多模态推荐/搜索中应同等重视元数据路由信号与候选间联合校准。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

**动机**：教育视觉问答需要同时利用语言和视觉证据解决课程导向选择题。相比开放域 VQA，教育场景包含结构化评估元数据、图表或图像上下文，以及语义相近的答案选项，容易产生题目-选项捷径，影响模型的真实推理能力。

**方法关键点**：GRACE 在冻结的多模态大模型上引入参数高效适配。它利用每道题的教学状态（学科、分组技能、年级、视觉上下文、问题意图、选项结构）来专门化轻量语言与视觉适配。具体包括：使用因子专属提示（factor-specific prompts）和轻量视觉适配器，然后通过证据感知选项校准在共享多模态上下文中对所有候选打分。

**关键结果**：在 ScienceQA 上，GRACE 将共享适配器基线的整体准确率从 90.5% 提升到 93.1%，图像上下文题目从 88.7% 提升到 91.2%。消融显示，去掉教学组合、选项校准或视觉适配器分别下降 1.4、1.0、1.5 个点，证明结构化教育状态是参数高效多模态适配的有效路由信号。
