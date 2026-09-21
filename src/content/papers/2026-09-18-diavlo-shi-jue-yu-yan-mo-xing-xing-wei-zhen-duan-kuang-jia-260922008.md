---
title: 'DiaVLo: Diagnosing Behaviours of Vision-Language Models'
title_zh: DiaVLo：视觉语言模型行为诊断框架
authors:
- Lorenzo Corti
- Jie Yang
affiliations:
- Delft University of Technology
arxiv_id: '2609.22008'
url: https://arxiv.org/abs/2609.22008
pdf_url: https://arxiv.org/pdf/2609.22008
published: '2026-09-18'
collected: '2026-09-21'
category: Eval
direction: 多模态模型行为诊断与因果分析
tags:
- Vision-Language Models
- Behavior Diagnosis
- Causal Analysis
- Model Evaluation
- Multimodal
one_liner: 提出 DiaVLo 框架，结合人类标注与模型生成构建行为规范，因果定位关键概念以诊断 VLM 行为错位
practical_value: '- 行为规范对比思路可迁移：在电商多模态模型（商品图理解、图文审核）上线前，用人工标注期望行为 + 模型实际行为生成规范，系统审计
  alignment/misalignment，而不是只看准确率。

  - 因果估计方法可用于定位影响模型预测的关键 visual/textual concept，帮助识别模型是否过度依赖文本而忽略图像，适用于排查多模态商品标签模型、图片搜索模型的
  bias。

  - 行为标签与性能指标关联的结果可以作为模型选型的辅助信号，特别是在不同业务场景下评测模型是否真的“看到”了关键视觉信息。

  - 局限：论文面向通用 VLM 诊断，与推荐系统直接关联较弱；若要落地，需要构建电商领域的概念集和期望行为库，成本较高。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：VLM 由视觉编码器、投影层和大语言模型组成，模块间信息存储与传递必须符合预期，但现有识别 VLM 行为的方法稀缺，可靠部署需要验证其行为是否对齐人类期望。

**方法关键点**：DiaVLo 利用人类 curation 和 VLM 自身生成能力，分别构建期望行为规范和观察行为规范，通过对比发现潜在错位；同时提供因果估计，定位对行为影响最大的 concept（如视觉对象、关系、属性），从而解释模型为何产生某种行为。流程包括场景图生成、人工精炼、行为标注与诊断，适用于分类和生成两种条件。

**关键结果**：在多个开源 VLM 上实验显示，DiaVLo 生成的行为标签与模型性能相关，能为性能指标提供上下文解释；框架成功识别出 aligned 和 misaligned 行为，并揭示 VLM 感知、组织和优先处理 concept 的模式。摘要未给出具体数值，但强调行为标签与性能的关联性。
