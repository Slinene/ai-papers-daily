---
title: 'From Answer Generators to Reasoning Facilitators: Designing AI Tutors for
  Mathematical Reasoning in High-Stakes Environments'
title_zh: 从答案生成器到推理促进者：为高压数学教育设计AI导师
authors:
- Yuming Feng
- Yuan Tian
- Erica Zhao
affiliations:
- Stanford University
arxiv_id: '2607.01692'
url: https://arxiv.org/abs/2607.01692
pdf_url: https://arxiv.org/pdf/2607.01692
published: '2026-07-02'
collected: '2026-07-04'
category: Reasoning
direction: AI辅导中的推理促进设计
tags:
- AI tutoring
- mathematical reasoning
- LLM
- cognitive scaffolding
- HCI
- reasoning-centric design
one_liner: 发现学生抗拒纯苏格拉底式对话，将‘答案优先’捷径重新用作诊断检查点，提出推理中心化产品循环
practical_value: '- 对话式推荐/Agent 可借鉴‘答案优先’作为诊断捷径：在推理链中允许用户跳过步骤直接查看结果，系统再反向引导用户反思缺失步骤，降低摩擦。

  - 分层工作示例与步骤链接的可视化锚定，可迁移到推荐解释界面：将多步推理过程展开为可折叠的层次，并高亮当前步骤所依赖的输入，提升透明度。

  - 元认知脚手架（提示用户自我解释推理步骤）可融入 Agent 决策过程，让用户在关键节点确认或修正，增强人与 Agent 的协作信任。

  - 推理中心化产品循环（检查→局部修复→课程验证→延迟检索）可视为一种推理型任务的交互框架，适用于搜索/推荐系统中需要多轮修正的场景，如动态查询细化或探索式推荐。'
score: 6
source: arxiv-cs.HC
depth: abstract
---

**动机**：LLM 在教育中的快速集成正将数学学习降级为答案生成，尤其在高压备考环境下，传统的苏格拉底式引导难以奏效。本文设计并评估了 AITutor，旨在将教学理论转化为支持推理修复的 UI 机制。

**方法关键点**：
- 采用生成性研究、可用性测试和 12 名初中生备战中考的现场部署，通过 7,379 条遥测事件、8 次情境观察和 10 次访谈进行混合方法三角化。
- 系统提供分层工作示例（逐步展示解题过程）、步骤链接的视觉锚定（将文本步骤与图形高亮关联）和元认知脚手架（提示学生解释下一步）。
- 发现学生主动抵制纯苏格拉底对话，将“先看答案”的捷径重新用作诊断检查点，再反向修补推理缺口。

**关键结果**：
- 提出了“推理中心化产品循环”，包含四个设计维度：推理检查、局部修复、课程范围验证和延迟检索。
- 分层示例和视觉锚定有效降低了推理修复的交互成本，使学生在高压下仍能保持解题投入。
- 该循环为 AI 教育产品提供了结构化支持数学推理的界面设计启示。
