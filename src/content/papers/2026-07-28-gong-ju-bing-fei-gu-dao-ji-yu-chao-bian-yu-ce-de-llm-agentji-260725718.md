---
title: 'Tools Are Not Islands: Set-Level Tool Retrieval for LLM Agents via Query-Conditioned
  Hyperedge Prediction'
title_zh: 工具并非孤岛：基于超边预测的LLM Agent集合级工具检索
authors:
- Xinyi Hong
- Pinjun Dong
- Xinyang Yu
- Binyan Jiang
affiliations:
- Shanghai Jiao Tong University
- The Hong Kong Polytechnic University
arxiv_id: '2607.25718'
url: https://arxiv.org/abs/2607.25718
pdf_url: https://arxiv.org/pdf/2607.25718
published: '2026-07-28'
collected: '2026-07-29'
category: Agent
direction: Agent工具检索的集合级重定义与超图建模
tags:
- Tool Retrieval
- Hypergraph
- LLM Agent
- Set-level Scoring
- Cardinality-specific Interaction
one_liner: 将工具检索重构为查询条件超边预测，以工具集合整体为单位评分，并捕捉基数依赖的工具交互
practical_value: '- **把工具集当作整体来打分**：在电商 Agent 场景（如比价+下单+物流查询）中，不要只按单个 API 相关性召回，可参考
  HYSET 的超边预测思想，对候选工具子集做联合评分，直接优化「工具集合是否完整覆盖任务」指标。

  - **用基数特异性交互矩阵捕捉工具间依赖**：多工具任务中，工具之间的互补性随集合规模变化。可以用一组按集合大小索引的交互矩阵（即 M2, M3, M4 …）来建模这种动态依赖，参数开销远小于显式高阶张量。

  - **执行反馈可作为弱监督信号**：即使只有部分标注数据，也可以在线采集工具调用链的最终任务成功与否作为奖励，通过 reward-weighted self-training
  持续优化检索模块，尤其适合随时新增 API 的电商工具库。

  - **两阶段推理兼顾效率与集合评分**：先用轻量双编码器做 top-K 初筛，再用集合重排序在缩减后的空间里显式对比不同大小、不同组合的候选工具集，推理延迟可控（12
  ms/query），可直接嵌入生产级 Agent 管线。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：LLM Agent 调用外部工具时，需从数千个 API 中选出一个小而全的工具集。现有方法或独立评分每个工具（语义匹配），或经图增强但仍是单工具评分，或自回归顺序生成，均未以工具集合整体为单位评估联合效用，导致选出的工具集覆盖不全（Top‑3 召回虽高，但完整覆盖所需工具集的比例仅约 40%）。此外，工具间的互补模式随集合大小变化明显（如「汇率转换」与「天气查询」在 4 工具任务中的共现率远高于 2 工具任务），孤立评分无法捕捉这一依赖。

**方法关键点**：
- **问题重定义**：将工具检索形式化为工具共调用超图上的查询条件超边预测，候选工具集即为超边，评分对象变为整个集合。
- **评分函数分解**：F(x, E) = F_set(E) + F_align(x, E)。F_set 建模工具间的内部交互，使用基数特异性矩阵 M_m，同一对工具在不同集合大小下得分不同，以捕捉高阶依赖；F_align 通过查询与集合的交叉注意力实现查询级集合对齐。
- **训练与推理**：负采样构造对比池，用检索损失（拉大标注集与其他集的分差）加执行反馈的自训练损失（奖励成功执行的选择）联合优化。推理时先按单工具评分构建短列表，再用集合重排序从短列表的所有子集中选出最优工具集。

**关键实验**：在 ToolBench 上，HYSET (BERT) 的 COMP@5 达 77.55%，相对最强基线 ToolGen 提升 10.8%；GPT‑4 Pass Rate 达 69.69%，相对提升 12.8%。消融实验：去掉 F_set 项导致 COMP@5 下降 13.1%，用共享矩阵替代基数特异性矩阵则 COMP@5 下降 9.9%，验证了集合级打分和基数依赖建模的核心作用。在零样本跨域迁移和每类仅 5 个样本的小样本适应中，仍保持有竞争力的完整性。
