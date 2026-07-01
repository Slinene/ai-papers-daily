---
title: 'CoMet: Context and Multiplicity Decomposition for Multimodal Uncertainty Estimation'
title_zh: CoMet：上下文与多重性分解的多模态不确定性估计
authors:
- Sanghyuk Chun
- William Yang
- Amaya Dharmasiri
- Olga Russakovsky
affiliations:
- Princeton University
arxiv_id: '2606.32012'
url: https://arxiv.org/abs/2606.32012
pdf_url: https://arxiv.org/pdf/2606.32012
published: '2026-06-30'
collected: '2026-07-01'
category: Eval
direction: 多模态大模型不确定性估计
tags:
- Uncertainty Estimation
- MLLM
- Post-hoc
- Context Decomposition
- Multiplicity
- Hallucination Detection
one_liner: 将多模态不确定性分解为上下文相关项与多重性相关项，用轻量级后置模块高效估计，无需重复生成
practical_value: '- 电商推荐场景下的多模态模型（如图文推荐、短视频描述）可采用不确定性分解思路，区分任务固有歧义和多种可能答案的模糊性，辅助在线决策。

  - 轻量级后置模块直接复用已有隐藏表征，无需多次采样或完整生成，适合推荐系统对低延迟的要求。

  - 可用于多模态生成内容的幻觉检测，例如自动过滤不可信的图文推荐理由或评论，提升用户体验。

  - Agent 在调用 MLLM 时可使用 CoMet 估计置信度，实现自适应动作执行或请求人工确认，增强系统鲁棒性。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：多模态大语言模型(MLLM)在开放域中面临不确定性的多源性和答案空间无限性的挑战，传统基于采样或自回归生成的方法计算开销大，且难以区分来自任务/提示的歧义与来自输入本身的多种可能。

**方法**：CoMet 将不确定性分解为**上下文特定项**（context-specific，刻画任务或提示带来的模糊性）和**多重性特定项**（multiplicity-specific，衡量与该输入兼容的合理答案数量）。通过一个轻量的后置模块，直接基于 MLLM 的隐藏状态预测这两个量，无需生成答案或多次采样，实现高效估计。训练时利用监督标签，可端到端优化。

**结果**：在多个开放式多模态基准、幻觉检测任务和多选视觉问答上，CoMet 一致优于现有不确定性估计基线（如 entropy、mutual information 等），同时保持了低计算开销，验证了分解策略的有效性和效率。
