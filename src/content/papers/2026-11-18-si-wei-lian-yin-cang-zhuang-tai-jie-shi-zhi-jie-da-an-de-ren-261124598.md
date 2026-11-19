---
title: Chain-of-Thought Hidden States Reveal Task-Solving Directions for Direct Answers
title_zh: 思维链隐藏状态揭示直接答案的任务解决方向
authors:
- Houman Mehrafarin
- Ioannis Konstas
affiliations:
- Heriot-Watt University
- University of Edinburgh
arxiv_id: '2611.24598'
url: https://arxiv.org/abs/2611.24598
pdf_url: https://arxiv.org/pdf/2611.24598
published: '2026-11-18'
collected: '2026-11-19'
category: Reasoning
direction: LLM推理·隐藏状态方向
tags:
- Chain-of-Thought
- Hidden States
- Activation Patching
- Linear Probe
- Inference Efficiency
one_liner: 旋转直接提示的隐藏状态朝向任务解决方向，以十分之一的token超越CoT准确率
practical_value: '- 在需要多步推理的生成任务（如推荐解释、对话策略规划）中，可以尝试通过激活修补定位包含正确答案信息的隐藏状态，并学习一个低秩方向，在推理时对表示进行旋转，替代长CoT生成，显著降低推理token和延迟。

  - 该方法使用线性探针区分recovering和failed状态，说明模型内部存在可线性分离的任务解决信号；在电商推荐中，可对用户意图建模、商品属性推理等中间状态做类似诊断，判断模型是否已编码关键信息，从而决定是否需要额外推理步骤。

  - 方向构建仅需单次旋转，与Prefix Tuning或控制向量方法兼容，可嵌入线上模型作为轻量级推理加速组件，尤其适合Agent中频繁调用LLM做小规模推理的场景。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：CoT虽提升推理准确率，但代价是数百token的生成，且在某些任务上反而低于直接回答。作者基于前人因果证据（错误CoT的隐藏状态仍含解题信息）希望挖掘直接回答的隐藏状态中是否存在可被利用的解题方向，从而以更短生成达到或超过CoT准确率。

**方法关键点**：1) 对每个问题，将CoT各步隐藏状态逐一切片修补到直接提示的forward中，若修补后直接回答正确，则标记该状态为recovering，否则failed；2) 线性探针显示模型对这两类状态有不同编码，说明信息存在且可分离；3) 对直接提示的最后隐藏状态，利用该问题自身的recovering和failed状态构建一个任务解决方向（通过对比两类状态均值或类似方法），在生成前对隐藏状态做一次旋转，然后进行短生成。

**关键结果**：在25个任务上，LLaMA 3.1 8B直接回答平均准确率从46%提升到85%（CoT为69%），Qwen 2.5 7B从52%提升到86%（CoT为77%），且生成token仅为CoT的十分之一。表明直接回答的隐藏状态中存在可激活的解题方向，CoT并非达到该准确率的最短路径。
