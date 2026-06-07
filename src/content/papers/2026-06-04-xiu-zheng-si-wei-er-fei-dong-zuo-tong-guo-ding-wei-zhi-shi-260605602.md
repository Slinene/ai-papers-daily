---
title: 'Fix the Mind, Not the Move: Interpretable AI Assistance via Knowledge-Gap
  Localization'
title_zh: 修正思维而非动作：通过定位知识鸿沟实现可解释的AI辅助
authors:
- Ayano Hiranaka
- Ya-Chuan Hsu
- Stefanos Nikolaidis
- Erdem Bıyık
- Daniel Seita
affiliations:
- University of Southern California
arxiv_id: '2606.05602'
url: https://arxiv.org/abs/2606.05602
pdf_url: https://arxiv.org/pdf/2606.05602
published: '2026-06-04'
collected: '2026-06-07'
category: Other
direction: 可解释AI辅助 · 知识误解诊断
tags:
- misconception diagnosis
- knowledge-gap localization
- human-AI collaboration
- interpretable AI
- compositional generalization
one_liner: 从行为反推认知误解，以最小干预修正内在知识缺陷，而非纠正单个错误动作
practical_value: '- 可借鉴其“从行为序列反推认知偏差”的思路，在推荐系统中针对用户频繁点击低质内容的行为，诊断其对商品关键属性的误解，并生成解释性提示（如“您可能忽略了XX参数”）。

  - 结构化知识表示（如属性-关系图）与组合泛化能力，可启发构建模块化的用户兴趣模型，即使只见过单一偏好偏差，也能在推理时解耦并处理用户多因素混合的误解。

  - 在智能客服或对话Agent中，可模仿SENSEI框架，通过用户提问序列定位其知识鸿沟，提供最少量但关键的信息纠正，提升问题解决效率。

  - 多智体协作场景中，可将该框架用于Agent间信念对齐：当检测到其他Agent执行了次优动作时，主动推断其策略中的误解，并定向沟通修正，替代简单的动作级干预。'
score: 7
source: arxiv-cs.HC
depth: abstract
---

**动机**：传统AI辅助通过行为反馈纠正用户即时错误，但难以根除重复犯错的根源——内在知识误解。要实现长期改进，必须定位并修正这些误解。

**方法**：提出SENSEI框架，利用结构化知识表示（如任务相关知识图谱），从用户交互行为推断其误解。框架将错误归因于知识节点的错误连接，并通过概率推理定位最可能的误解组合，然后提供针对性的最小纠正建议，而非直接修正动作。训练仅使用单一误解数据，但通过组合泛化，在测试时能解耦多个重叠的误解。

**结果**：在三个长期决策任务（数学题、物理模拟等）上，SENSEI展现了零样本组合泛化能力，有效分离多重误解。用户研究中，该方法成功识别并纠正了90%的学生误解，显著提升了长期任务表现。
