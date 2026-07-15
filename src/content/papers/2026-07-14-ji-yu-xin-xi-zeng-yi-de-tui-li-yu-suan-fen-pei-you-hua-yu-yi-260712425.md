---
title: 'Where Reasoning Matters: Rethinking Latent Reasoning in Semantic ID-based
  Generative Recommendation'
title_zh: 基于信息增益的推理预算分配优化语义ID生成式推荐
authors:
- Shangxin Yang
- Min Gao
- Zongwei Wang
- Junliang Yu
arxiv_id: '2607.12425'
url: https://arxiv.org/abs/2607.12425
pdf_url: https://arxiv.org/pdf/2607.12425
published: '2026-07-14'
collected: '2026-07-15'
category: GenRec
direction: 生成式推荐 · 语义ID · 推理预算分配
tags:
- Semantic ID
- Generative Recommendation
- Latent Reasoning
- Budget Allocation
- Information Gain
one_liner: 按语义ID位置的信息增益自适应分配推理计算量，实现精度与效率平衡
practical_value: '- 生成式推荐推理时，可按语义ID位置的信息增益分配latent refinement步数：早期token（如类目层级）增益高，多分配计算；后期token增益低，少分配，总体节省计算量。

  - 在实际部署中，可离线统计不同位置token的信息增益，或在线上动态学习分配策略，平衡推理延迟与精度。

  - 方法轻量，不改变模型结构，仅调整推理时的迭代步数，易于在已有生成式推荐框架上实现。

  - 思路可拓展至其他序列生成任务（如搜索query建议），对重要token分配更多计算资源。'
score: 10
source: arxiv-cs.IR
depth: abstract
---

**动机**：基于语义ID的生成式推荐通过自回归生成token序列预测物品，现有方法在每个token决策前执行等量的隐式推理（latent reasoning）步数，未考虑不同位置token对最终预测的信息贡献差异，造成计算浪费。

**方法**：提出IBA（信息增益预算分配）框架。首先定义每个语义ID位置的信息增益（IG），衡量该位置token减少目标物品不确定性的程度。观察发现，序列早期位置（如粗粒度语义ID）信息增益高，后期位置增益低。IBA将隐式推理步数视为有限计算预算，利用一个轻量分配模块根据位置信息增益动态分配步数，对高IG位置给予更多推理迭代，低IG位置减少步数，整体在固定总预算下优化精度-计算效率。

**结果**：在多个公开推荐数据集上，IBA一致优于固定步数分配的强基线，并在保持或提升推荐精度的同时，显著减少总推理计算量，取得更好的精度-计算帕累托前沿。分析表明，对高信息增益位置倾斜预算能带来更大期望增益。
