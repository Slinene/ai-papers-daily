---
title: 'Reasoning as Pattern Matching: Shared Mechanisms in Human and LLM Everyday
  Reasoning'
title_zh: 模式匹配即推理：人类与 LLM 日常推理的共享机制
authors:
- Zach Studdiford
- Gary Lupyan
affiliations:
- University of Wisconsin–Madison
arxiv_id: '2606.13607'
url: https://arxiv.org/abs/2606.13607
pdf_url: https://arxiv.org/pdf/2606.13607
published: '2026-06-11'
collected: '2026-06-14'
category: Reasoning
direction: 人类与 LLM 推理机制比较
tags:
- reasoning
- pattern matching
- attention heads
- common sense
- human evaluation
one_liner: 人类与 LLM 在常识推理中犯类似的错误，且 LLM 的注意力头实现了一种模式匹配，可预测人类看似不合理的错误。
practical_value: '- 借鉴注意头分析技术，诊断 LLM 在推荐、Agent 规划等下游任务时的决策归因，识别依赖拼凑式模式匹配的场景。

  - 在构建 prompt 时警惕无关细节干扰，可参考该文发现的“不相关提示信息导致错误”的现象，通过对抗性提示去除诱偏因素。

  - 若业务需要 LLM 执行严格因果推理（如多步 Agent 任务），应避免单纯依赖模型内部模式匹配，可结合结构化世界模型、知识图谱或符号推理模块。

  - 论文对常识推理难点的分类可作为构建评估集或进行数据增强的依据，帮助 Agent 在物理、社会等常见场景中减少相似错误。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：人们常认为 LLM 的推理失败源于其仅进行模式匹配，而人类拥有抽象世界模型。本文探究人类与 LLM 在日常因果推理中是否表现出相似的错误，以及 LLM 内部机制是否确为模式匹配。

**方法**：作者设计了一系列日常常识推理题目（如物理、空间变换等），同时测试人类参与者和 25 个 LLM。通过分析 LLM 的注意力头，定位驱动回答的关键头，并发现这些头实现的就是一种模式匹配。更进一步，这些注意力头能预测人类在看似无关的提示细节干扰下产生的非理性错误。

**关键结果**：人类与 LLM 的推理错误模式高度相似；LLM 中负责推理的核心注意力头本质上进行的是模式匹配，而非抽象因果计算；利用这些头可以准确预测人类被试易犯错的条件。整体表明，人类和 LLM 的日常推理可能都更贴近模式匹配，而非基于结构化的世界模型。
