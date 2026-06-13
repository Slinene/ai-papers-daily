---
title: Operads for compositional reasoning in LLMs
title_zh: LLM组合推理的Operad数学框架
authors:
- Nathaniel Bottman
- Kyle Richardson
affiliations:
- Incubilate
- Allen Institute for Artificial Intelligence
arxiv_id: '2606.13634'
url: https://arxiv.org/abs/2606.13634
pdf_url: https://arxiv.org/pdf/2606.13634
published: '2026-06-11'
collected: '2026-06-13'
category: Reasoning
direction: LLM多步推理的形式化数学框架
tags:
- Operads
- Question Decomposition
- Compositional Reasoning
- Consistency
- Multi-hop QA
- LLM Evaluation
one_liner: 用Operad代数形式化问题分解，提出Operadic一致性度量，可预测多步推理准确性
practical_value: '- 在电商问答、多跳查询中，可计算Operadic一致性来监控推理链路可靠性，替代单纯依赖输出概率或自洽性。

  - 一致性得分与准确率强相关，可作为无监督信号筛选更优的分解模板或中间答案，降低人工标注成本。

  - 将推理步骤抽象为操作数，便于设计模块化、可复用的推理流水线，适配不同业务逻辑的组合。

  - 该框架不限于QA，可用于任何需要组合子任务的多Agent协作或推荐解释生成，提供统一的数学语义。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

动机：LLM常通过问题分解提升多步推理能力，但缺乏严格的数学基础来描述组合过程。

方法：引入Operad理论，定义questions operad Q，其中操作对应问题模板，组合对应子答案替换。QA模型可视为Q上的代数。基于此提出Operadic一致性：度量分解树在部分坍塌后模型答案的自洽程度。

结果：伴随论文在12个LLM和4个多跳QA数据集上验证，Operadic一致性与准确率强相关，且优于基于温度的多次采样自洽基线，表明该数学不变量能有效衡量推理可靠性。
