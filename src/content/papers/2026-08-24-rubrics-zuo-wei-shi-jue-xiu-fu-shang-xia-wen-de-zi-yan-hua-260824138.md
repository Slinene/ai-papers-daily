---
title: Rubrics as Visual-Repair Context for Self-Evolving UI-to-Code Generation
title_zh: Rubrics 作为视觉修复上下文的自演化 UI-to-Code 生成
authors:
- Tianyi Xiong
- Zhengyuan Yang
- Xiaofei Wang
- Chung-Ching Lin
- Ruichun Ma
- Kevin Lin
- Zhendong Wang
- Linjie Li
- Chenxi Liu
- Ruibo Chen
affiliations:
- University of Maryland, College Park
- Microsoft
arxiv_id: '2608.24138'
url: https://arxiv.org/abs/2608.24138
pdf_url: https://arxiv.org/pdf/2608.24138
published: '2026-08-24'
collected: '2026-08-27'
category: Multimodal
direction: VLM 自演化 · 视觉修复上下文
tags:
- UI-to-Code
- VLM
- Self-Evolution
- Rubric
- Visual Repair
- Multimodal
one_liner: 提出 RubSE，用结构化 rubric 引导视觉修复，解决 UI-to-code 自演化中局部修复相互耦合导致轨迹不稳定的问题
practical_value: '- 在迭代优化 Agent（如落地页、商品详情页、广告创意自动生成）中，引入结构化“修复指令/评分标准”作为上下文，而不是反复给模型完整截图让其自由修改，能明显约束修改范围，避免模型过度重写导致原本正确区域被破坏。

  - “每轮只选一个最高优先级修复目标”并维护已选目标历史，这种机制可以迁移到多轮自优化流程（如搜索推荐文案、UI 布局、推送消息的自动迭代），提升轨迹稳定性，减少回归。

  - 强 rubric 生成器 + 弱代码执行器的组合：业务上若代码生成模型能力有限，可以用更强的模型生成视觉修复 rubric，再交给轻量模型执行修改，推理成本更低且效果可迁移，类似推理时蒸馏。

  - 将视觉差异表示为 typed rubrics（layout_geometry、style、component 等），把修复问题分解为可执行子目标，对多模态
  Agent 设计有直接参考价值，可用于电商多模态内容生成的闭环优化。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：UI-to-code 生成模型在测试时的自演化（self-evolution）严重不稳定。作者将根本障碍归纳为“视觉修复耦合”：一次局部代码编辑会通过布局、样式、组件依赖向外传播，可能修正了一个视觉不匹配，却同时破坏了之前已经正确的区域。

**方法关键点**：提出 RubSE（Rubric-guided Self-Evolution）框架，把视觉反馈表示为结构化的视觉修复上下文，即 rubrics。每轮 refinement 分三步：① 生成多个 typed candidate rubrics；② 选择一个优先级最高的修复目标；③ 将历史选中的 rubrics 存入记忆。这种机制迫使每次修订只针对一个 well-scoped 修复目标，抑制重复或过于宽泛的改动。

**关键结果**：在 6 个 VLM 和 3 个 UI-to-code 基准上，RubSE 在 final-round 和 best-round 设置下均大幅优于朴素自演化，达到更稳定的 refinement 轨迹和更高的轨迹级性能上限。进一步分析表明，RubSE 通过改善严重视觉退化的恢复能力来缓解轨迹坍缩，且较强的 rubric 生成器可将有效的视觉修复指导迁移给较弱的 code improver。
