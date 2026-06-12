---
title: 'Operadic consistency: a label-free signal for compositional reasoning failures
  in LLMs'
title_zh: 操作子一致性：一种用于LLM组合推理故障的无标签信号
authors:
- Nathaniel Bottman
- Yinhong Liu
- Kyle Richardson
affiliations:
- Incubilate
- University of Cambridge
- Allen Institute for Artificial Intelligence
arxiv_id: '2606.13649'
url: https://arxiv.org/abs/2606.13649
pdf_url: https://arxiv.org/pdf/2606.13649
published: '2026-06-11'
collected: '2026-06-12'
category: Eval
direction: LLM组合推理一致性评估
tags:
- operadic consistency
- compositional reasoning
- selective prediction
- chain-of-thought
- uncertainty quantification
- multi-hop QA
one_liner: 提出操作子一致性(OC)作为无标签信号，检测LLM直接回答与分解重组回答的不一致，跨模型准确率高度相关且互补于采样基线的选择性预测
practical_value: '- 在Agent多步推理中，增加操作子一致性检查：若模型对同一问题的直接回答与按自身分解步骤组合后的回答不一致，则标记为不可信，用于选择性预测或触发人工复核

  - 对于电商场景中需要组合多个子查询的任务（如“查找符合条件A且B的商品”），可将复杂查询分解为子查询，分别获取结果后重组，对比直接查询结果，利用OC分数作为置信度特征输入到重排序或路由模块

  - 该信号本身无需标签，只需3次推理调用，可与现有的采样多样性信号（如自洽性、语义熵）简单融合，通过逻辑回归等轻量校准器提升整体信心估计，适合生产环境中低成本实施

  - 在生成式推荐中，可以利用操作子一致性验证多跳推理的中间步骤，例如验证推荐解释链的逻辑连贯性，作为事实一致性检查的补充'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**：现有LLM推理不确定性评估（自洽性、语义熵、P(True)）只关注答案分布的方差或自我评估，未检验推理过程的内部组合一致性——即直接回答与按自身分解步骤组合后的回答是否一致。然而，LLM在多跳推理中常出现“组合性缺口”：即使子问题正确，最终组合也可能错误。操作子理论（operad）为这种组合结构提供了严格的语言，据此可定义操作子一致性（OC）作为一个新的无标签信号。

**方法关键点**：
- 将问题模板视作操作子Q的元素，LLM为Q上代数；若模型对复合问题的直接回答与按分解树从叶子到根逐步替换子答案所得的回答一致，则称满足操作子一致性。
- 实证上简化为深度2的链：将多跳问题分解为两个子问题Q1、Q2，先回答Q1，将其答案填入Q2得到分解答案，然后用数据集特定的语义等价评分（SQuAD-F1、yes/no匹配等）计算OC分数（0~1）。成本：3次模型调用。
- 与CoT自洽性、语义熵、P(True)等基线比较，并在选择性预测中融合OC与自洽性信号。

**关键结果**：
- 在12个指令微调模型（4B–671B）和四个多跳QA数据集上，OC与准确率的跨模型Pearson r在0.86–0.94，是唯一在所有数据集上r≥0.85的方法；CoT-SC(K=10)在HotpotQA和DROP上r=0.93/0.87，但在MuSiQue和StrategyQA上骤降至≈0.45。
- 逐问题逻辑回归中，OC的系数在所有数据集上显著（p≤10⁻¹⁶），表明其带来超越自洽性与语义熵的额外信息。
- 同等成本（K=3）下，将OC加入CoT-SC选择性预测器后，AUARC提升0.086–0.096，AUROC提升0.092–0.164，95% CI全部不含零。
- 对思维模型，从模型思维链中自动提取子问题也得到类似互补提升，16个测试cell中12个CI不含零。

**最值得记住的一句话**：操作子一致性通过比较直接回答与按模型自身分解重组后的答案是否一致，提供了一项与采样方差完全正交、无需标签就能跨模型准确率高度相关的推理正确性信号。
