---
title: 'The Illusion of Visual Tool-Use: A Causal Audit of Thinking with Images'
title_zh: 视觉工具使用的幻觉：对“用图像思考”的因果审计
authors:
- Zhiheng Wang
- Bo Peng
- Lai Wei
- Chaochao Lu
affiliations:
- Shanghai Artificial Intelligence Laboratory
- Shanghai Jiao Tong University
- Shanghai Innovation Institute
arxiv_id: '2608.06270'
url: https://arxiv.org/abs/2608.06270
pdf_url: https://arxiv.org/pdf/2608.06270
published: '2026-08-06'
collected: '2026-08-08'
category: Eval
direction: 多模态LLM视觉工具使用的因果评估方法
tags:
- visual tool-use
- causal audit
- multimodal LLMs
- evaluation
- counterfactual
one_liner: 用因果干预审计多模态LLM视觉工具调用，发现总体增益微小且大部分轨迹中视觉证据无因果效应
practical_value: '- **Agent工具调用的因果有效性审计**：在电商搜索或推荐Agent中，若引入类似截图、缩放等视觉操作，可直接套用论文的`Visual
  Evidence Gain`来量化每次工具调用是否对最终决策有真实因果贡献，避免高代价无效调用。

  - **识别Agent策略的校准错误**：论文发现的“Calling Without Looking”（调用了但观察被忽略）和“Looking Without
  Planning”（观察有用但调用计划混乱）两种失败模式，适用于诊断任何多步交互Agent（如搜索筛选、商品对比Agent）的工具使用幻觉。

  - **轨迹级增益分解**：将整体准确率增益分解到单条轨迹，定位增益仅来自少数“校准样本”，可帮助过滤掉无效工具使用，降低线上推理成本，提升Agent吞吐。

  - **工程实现指引**：通过随机扰动/替换观察结果的介入方法，无需额外标注即可在线下评估工具策略，为迭代优化提供诊断信号。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：多模态LLM（如GPT-4V）新增的视觉操作（crop-and-zoom）旨在让模型“用图像思考”，但实际实验显示，相比直接推理，整体准确率增益极小甚至为负，且token成本大增，同时存在反复裁剪无关区域、正确问题反而答错等现象。作者怀疑返回的视觉证据是否真正被模型用来改变答案，还是仅作为无关动作。

**方法关键点**：将视觉工具使用过程建模为因果图，分离**观察中介路径**（observation→answer）和**动作引发捷径**（action→answer）。设计三级干预审计：
1. **策略层**：比较视觉工具使用策略与直接推理策略的整体准确率差异。
2. **轨迹层**：在完整 rollout 中随机打乱所有观察结果，观察答案是否变化。
3. **步骤层**：固定前缀，用反事实替换单个工具返回的观察（如空白图），定义**Visual Evidence Gain (VEG)** 量化该观察对最终答案的因果贡献。

**关键结果**：在6个代表性MLLM（GPT-4o、Gemini等）和5个细粒度感知基准上发现：
- 策略校准错误普遍存在，有两种失败模式：**Calling Without Looking**（VEG≈0，观察无因果影响）和**Looking Without Planning**（观察有信息但调用计划混乱）。
- 轨迹级诊断显示准确率增益主要由少数**校准样本**驱动，其余大量轨迹中工具使用无效甚至有害，形成“视觉工具使用的幻觉”。整体增益掩盖了因果失效的广泛性。
