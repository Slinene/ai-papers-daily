---
title: 'Rethinking Heterogeneous LLM Merging: A Weighted Model Averaging Perspective'
title_zh: 重新审视异构大模型合并：加权平均视角
authors:
- Jiahe Fan
- Yinghao Hou
- Si Chen
- Aiyuan Zhang
- Hong Xie
- Defu Lian
affiliations:
- University of Science and Technology of China
arxiv_id: '2607.18026'
url: https://arxiv.org/abs/2607.18026
pdf_url: https://arxiv.org/pdf/2607.18026
published: '2026-07-20'
collected: '2026-07-21'
category: Training
direction: 模型合并 · 异构参数空间加权平均
tags:
- Model Merging
- Heterogeneous LLM
- Weighted Averaging
- Dimensional Adaptation
- Training-free
- Parameter Interpolation
one_liner: 证明通过维度适配和比率控制，无需训练直接加权平均即可有效合并参数量不同的LLM
practical_value: '- 工程上可直接合并不同尺寸的微调模型，无需重新训练，特别适合电商推荐系统中多任务模型的快速融合。

  - 使用小比率插值（如0.1）将辅助模型能力注入主模型，例如将对话能力迁移到商品描述生成模型。

  - Union-style 扩展或 Intersection-style 截断均为免训练操作，可作为轻量级模型更新方案，部署成本低。

  - 注意避免平衡插值，否则性能崩溃；该跷跷板效应提示业务中合并比例需精细 A/B 测试。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：现有异构 LLM 合并方法依赖蒸馏、适配器、路由等复杂机制，本文探索能否通过最简单的加权平均实现有效融合。

**方法**：提出两种免训练策略——Union-style 将小模型参数空间扩展到大模型维度，Intersection-style 将大模型截断到小模型维度，然后按比例加权插值合并。实验用 Qwen 家族模型对，覆盖数学推理、代码生成、语言理解、常识推理、知识问答和指令遵循等任务。

**关键结果**：
- 确定性扩展几乎无损保留源模型功能；
- 小比率插值（5%–15%）可超过强源模型，成功迁移互补能力；
- 接近 1:1 的平衡插值严重退化；
- 任务表现呈现“跷跷板效应”，某些能力提升伴随其他能力下降。

结论：简单加权平均配合维度适配和谨慎比率控制是异构 LLM 合并的强大基线，其性能上限可能也约束了更复杂方法。
