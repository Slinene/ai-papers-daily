---
title: Order-Invariant Answers, Order-Sensitive Representations in Mathematical Reasoning
title_zh: 数学推理中答案不变与表示顺序敏感
authors:
- Zhixu Silvia Tao
affiliations:
- Operations Research and Financial Engineering, Princeton University
arxiv_id: '2609.28442'
url: https://arxiv.org/abs/2609.28442
pdf_url: https://arxiv.org/pdf/2609.28442
published: '2026-09-23'
collected: '2026-09-24'
category: Reasoning
direction: 数学推理 · 表示不变性分析
tags:
- mathematical reasoning
- representation invariance
- permutation SNR
- order sensitivity
- LLM interpretability
one_liner: 16 个 LLM 显示：重排规则下答题越准的模型，对规则顺序的表示区分度越高，Spearman 相关最高 0.86
practical_value: '- **用 permutation SNR 做输入顺序鲁棒性诊断**：在搜索/推荐中，规则、条件、特征或工具说明的顺序经常被重排；可参考论文中的
  probe 思路，在 LLM 推理链路里计算不同顺序下的表示可分性与准确率，定位脆弱的 prompt 模板或排序敏感节点。

  - **评估时不要只看答案正确率**：如果业务需要模型对输入顺序不敏感（如多路召回条件重排、Agent 工具调用顺序无关），建议在离线评估中加入表示层对顺序的区分度指标，防止模型靠表面顺序走捷径，上线后遇到顺序变化掉点。

  - **可做顺序不变的数据增强，但需约束表示**：训练时可对同一规则/条件集合做多种顺序混排增强；但论文提示模型可能仍然学到顺序敏感表示，因此可加对比正则或一致性损失，拉近等价顺序的表示。

  - **整体可移植性**：主要是学术贡献，对推理/可解释性研究更有价值；电商推荐业务可直接复用的结论有限，但表示分析方法可迁移到 LLM 鲁棒性评估。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：重排一组数学规则不改变其正确结论，即任务是答案不变的；但准确推理是否要求模型内部表示也保持顺序不变？此前只关注答案准确性，忽略表示层对顺序的敏感性。

**方法关键点**：构建合成多步函数组合问题，同一问题以多种规则顺序呈现、正确答案一致；用准确率和 permutation SNR 度量顺序模式在不同问题实例中的可区分性；在 16 个 1B–8B 语言模型上评估。

**关键结果**：模型对重排问题回答越准确，对不同规则顺序的表示区分度越高；层平均 permutation SNR 与准确率在所有合成设置中均正秩相关，Spearman 相关系数最高达 0.86。说明答案不变性与表示不变性需要区分：成功的规则组合可伴随等价顺序之间的不同内部表示。
